"""Promote ship-script payloads from incoming/ into the canonical store.

A payload is a directory ``incoming/payload_<ts>/`` containing per-strategy
CSVs (``<strategy>.csv`` with columns strategy,date,gross_pnl,traded_notional)
and a ``manifest.json`` with per-file sha256 and row counts.  Payloads may
also carry a ``forward`` section: the merge weights file plus the per-source
full-size component books for one book date; those promote first-write-wins
into data/forward/ (as-shipped pins on disk -- a re-ship that differs is a
problem message, never an overwrite).  Validation failures reject the WHOLE
payload (moved to incoming/rejected_<ts>) -- no partial promotion.
Promotion is atomic per file (tmp + rename).

Backtest VINTAGES (2026-10-30).  The canonical <strategy>.csv is the latest
series and is overwritten on every ship; the per-day pins keep only the
as-shipped value of each live day.  So whenever a ship RESTATES history (a
date both series have moved by more than io_backtest.REVISION_TOL) the new
full series is also kept, immutable, under data/backtest/vintages/ with an
index row naming the strategy repo commit that produced it (manifest
``source_commit``, from the ship script): cause ``code`` when the commit
moved, ``data`` when it did not.  The first time a strategy is seen its
current series is kept as the ``baseline`` vintage, so the pre-restatement
history is never lost.  Plain appends of new days are not vintages.
"""

from __future__ import annotations

import hashlib
import json
import re
import shutil

import pandas as pd

import config as C
from .dates import normalize_date

VINTAGE_INDEX = C.VINTAGE_DIR / "index.csv"
VINTAGE_COLS = ["strategy", "vintage", "shipped_at", "source_commit", "n_rows",
                "n_restated", "net_change", "cause"]


def _sha256(path) -> str:
    h = hashlib.sha256()
    with open(path, "rb") as fh:
        for chunk in iter(lambda: fh.read(65536), b""):
            h.update(chunk)
    return h.hexdigest()


def _pin_file(src_path, dest, label: str) -> list[str]:
    """First write wins; a differing re-ship is reported, never applied."""
    if dest.exists():
        if _sha256(dest) != _sha256(src_path):
            return [f"{label}: re-shipped with different content than the "
                    f"pinned copy -- kept the pin ({dest.name})"]
        return []
    tmp = dest.with_suffix(dest.suffix + ".tmp")
    shutil.copyfile(src_path, tmp)
    tmp.replace(dest)
    return []


def _promote_forward(pay, fwd: dict) -> list[str]:
    """Store a payload's forward weights + component books, first-write-wins."""
    problems: list[str] = []
    date = fwd.get("book_date")
    if not date:
        return problems
    date = normalize_date(date)
    wname = fwd.get("weights")
    if wname and (pay / wname).exists():
        problems += _pin_file(pay / wname, C.FORWARD_WEIGHTS_DIR / f"{date}.json",
                              f"{pay.name}/weights {date}")
    for src, fname in (fwd.get("books") or {}).items():
        if src not in C.FORWARD_SRC_TO_STRATEGY:
            problems.append(f"{pay.name}/{fname}: unknown forward source "
                            f"'{src}' -- skipped")
            continue
        if not (pay / fname).exists():
            continue  # manifest validation already flagged it
        problems += _pin_file(pay / fname,
                              C.FORWARD_BOOKS_DIR / f"{date}__{src}.json",
                              f"{pay.name}/book {src} {date}")
    return problems


def vintages() -> pd.DataFrame:
    """The vintage index (empty frame with the columns when none yet)."""
    if not VINTAGE_INDEX.exists():
        return pd.DataFrame(columns=VINTAGE_COLS)
    return pd.read_csv(VINTAGE_INDEX, dtype={"source_commit": str})


def _restated(old: pd.DataFrame, new: pd.DataFrame) -> tuple[int, float]:
    """(dates moved by more than REVISION_TOL, their net change) of new vs old."""
    from .io_backtest import REVISION_TOL
    j = (old.set_index("date")["gross_pnl"].rename("old").to_frame()
         .join(new.set_index("date")["gross_pnl"].rename("new"), how="inner").dropna())
    moved = (j["new"] - j["old"])[(j["new"] - j["old"]).abs() > REVISION_TOL]
    return len(moved), float(moved.sum())


def _keep_vintage(strategy: str, df: pd.DataFrame, shipped_at: str,
                  commit: str | None, n_restated: int, net: float, cause: str) -> str:
    (C.VINTAGE_DIR / strategy).mkdir(parents=True, exist_ok=True)
    stamp = re.sub(r"\D", "", str(shipped_at))[:14] or "unknown"
    name = f"{stamp}_{(commit or 'nocommit')[:12]}.csv"
    df[["date", "gross_pnl", "traded_notional"]].to_csv(C.VINTAGE_DIR / strategy / name,
                                                        index=False)
    row = pd.DataFrame([{"strategy": strategy, "vintage": name, "shipped_at": shipped_at,
                         "source_commit": commit or "", "n_rows": len(df),
                         "n_restated": n_restated, "net_change": round(net, 2),
                         "cause": cause}], columns=VINTAGE_COLS)
    row.to_csv(VINTAGE_INDEX, mode="a", header=not VINTAGE_INDEX.exists(), index=False)
    return name


def record_vintage(strategy: str, new: pd.DataFrame, shipped_at: str,
                   commit: str | None) -> str | None:
    """Keep ``new`` as a vintage when it restates the current series; returns
    a message for the run log, or None (no restatement)."""
    dest = C.BACKTEST_DIR / f"{strategy}.csv"
    if not dest.exists():
        _keep_vintage(strategy, new, shipped_at, commit, 0, 0.0, "first")
        return None
    old = pd.read_csv(dest)
    old["date"] = old["date"].map(normalize_date)
    idx = vintages()
    mine = idx[idx["strategy"] == strategy]
    if mine.empty:
        last_ship = str(old["shipped_at"].iloc[-1]) if "shipped_at" in old and len(old) else ""
        _keep_vintage(strategy, old, last_ship, None, 0, 0.0, "baseline")
        prev_commit = ""
    else:
        prev_commit = "" if pd.isna(mine["source_commit"].iloc[-1]) else str(mine["source_commit"].iloc[-1])
    n, net = _restated(old, new)
    if not n:
        return None
    cause = ("unknown" if not (commit and prev_commit)
             else "code" if commit != prev_commit else "data")
    name = _keep_vintage(strategy, new, shipped_at, commit, n, net, cause)
    return (f"VINTAGE {strategy}: {n} historical row(s) restated (net {net:+,.0f} CNY, "
            f"cause {cause}{', commit ' + commit[:7] if commit else ''}) -- kept as "
            f"vintages/{strategy}/{name}; the bridge keeps the as-shipped pins")


def promote_incoming() -> tuple[list[str], list[str]]:
    """Returns (promoted strategy keys, problem messages)."""
    promoted: list[str] = []
    problems: list[str] = []
    payloads = sorted(p for p in C.INCOMING.iterdir()
                      if p.is_dir() and p.name.startswith("payload_"))
    for pay in payloads:
        manifest = pay / "manifest.json"
        if not manifest.exists():
            problems.append(f"{pay.name}: no manifest.json -- rejected")
            pay.rename(C.INCOMING / f"rejected_{pay.name}")
            continue
        with open(manifest) as fh:
            man = json.load(fh)
        ok = True
        for fname, meta in man.get("files", {}).items():
            f = pay / fname
            if not f.exists():
                problems.append(f"{pay.name}/{fname}: listed but missing")
                ok = False
                continue
            if _sha256(f) != meta.get("sha256"):
                problems.append(f"{pay.name}/{fname}: sha256 mismatch")
                ok = False
        if not ok:
            pay.rename(C.INCOMING / f"rejected_{pay.name}")
            continue
        shipped_at = man.get("generated_at", "")
        fwd = man.get("forward") or {}
        fwd_files = set(fwd.get("books", {}).values()) | (
            {fwd["weights"]} if fwd.get("weights") else set())
        problems += _promote_forward(pay, fwd)
        for fname in man.get("files", {}):
            if fname in fwd_files:
                continue
            strategy = fname.rsplit(".", 1)[0]
            if strategy not in C.STRATEGIES:
                problems.append(f"{pay.name}/{fname}: unknown strategy -- skipped")
                continue
            df = pd.read_csv(pay / fname)
            df["date"] = df["date"].map(normalize_date)
            df = df[["date", "gross_pnl", "traded_notional"]].copy()
            df["shipped_at"] = shipped_at
            df = df.drop_duplicates("date", keep="last").sort_values("date")
            msg = record_vintage(strategy, df, shipped_at,
                                 man["files"][fname].get("source_commit"))
            if msg:
                problems.append(msg)
            dest = C.BACKTEST_DIR / f"{strategy}.csv"
            tmp = dest.with_suffix(".csv.tmp")
            df.to_csv(tmp, index=False)
            tmp.replace(dest)
            promoted.append(strategy)
        shutil.rmtree(pay)
    return promoted, problems
