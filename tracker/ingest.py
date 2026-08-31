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
"""

from __future__ import annotations

import hashlib
import json
import shutil

import pandas as pd

import config as C
from .dates import normalize_date


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
            dest = C.BACKTEST_DIR / f"{strategy}.csv"
            tmp = dest.with_suffix(".csv.tmp")
            df.to_csv(tmp, index=False)
            tmp.replace(dest)
            promoted.append(strategy)
        shutil.rmtree(pay)
    return promoted, problems
