"""Canonical backtest series: what the ship script delivers, plus the ks
series that already arrives in the inbox.

Canonical per-strategy file ``data/backtest/<strategy>.csv``:
    date,gross_pnl,traded_notional,shipped_at
Full-size CNY, ISO dates, 2026 onward.  ``fund_v3`` and ``ks_branch`` are the
two series the account-level bridge consumes (scaled by the day's execution
scale); the other five are report-only until they ship.
"""

from __future__ import annotations

import hashlib
import json

import pandas as pd

import config as C
from .dates import normalize_date
from . import io_live


def load_series(strategy: str) -> pd.DataFrame:
    """Canonical series for one strategy, or empty frame."""
    p = C.BACKTEST_DIR / f"{strategy}.csv"
    if not p.exists():
        return pd.DataFrame(columns=["gross_pnl", "traded_notional", "shipped_at"])
    df = pd.read_csv(p)
    df["date"] = df["date"].map(normalize_date)
    return df.drop_duplicates("date", keep="last").set_index("date").sort_index()


def all_series() -> dict[str, pd.DataFrame]:
    return {k: load_series(k) for k in C.STRATEGIES}


def bt_gross_for_bridge() -> pd.DataFrame:
    """date x {ks, fundamental} full-size backtest gross P&L for the bridge.

    ks comes from the INBOX series (arrives with no workstation in the loop);
    the ship-script ks_branch series is only a cross-check.  fundamental comes
    from the shipped fund_v3 series -- it does not arrive any other way.
    """
    ks = io_live.inbox_ks_summary()
    fund = load_series("fund_v3")
    out = pd.DataFrame(index=sorted(set(ks.index) | set(fund.index)))
    out.index.name = "date"
    if len(ks):
        out["ks"] = ks["gross_pnl_shipped"]
    if len(fund):
        out["fundamental"] = fund["gross_pnl"]
    return out


def pin_divergence(bt_raw: pd.DataFrame, state: dict) -> dict:
    """Where the CURRENT series disagrees with pinned as-shipped values.

    Returns {source: {"dates": [...], "max_abs": float}} for diffs > 1 CNY.
    A full model regeneration upstream shows up here permanently; the bridge
    keeps the pins, and alerts announce each newly-divergent date once.
    """
    out: dict = {}
    pins = state.get("bt_pinned", {})
    for d, vals in pins.items():
        for src, pinned in vals.items():
            if src not in bt_raw.columns or d not in bt_raw.index:
                continue
            cur = bt_raw.loc[d, src]
            if pd.isna(cur):
                continue
            diff = abs(float(cur) - float(pinned))
            if diff > 1.0:
                e = out.setdefault(src, {"dates": [], "max_abs": 0.0})
                e["dates"].append(d)
                e["max_abs"] = max(e["max_abs"], diff)
    for e in out.values():
        e["dates"].sort()
    return out


def overlay_and_update_pins(bt: pd.DataFrame, state: dict) -> tuple[pd.DataFrame, int]:
    """As-shipped basis for the bridge: pin each live-window day's backtest
    value the first run after it matures, and never follow later revisions.

    A day is mature once the series extends past it (date < series max) --
    the provisional same-day row regenerates next morning, so the value seen
    then is the final one from the model that actually shipped that day's
    targets.  Pinned values overlay the current series; upstream history
    regenerations (model changes) therefore cannot rewrite already-reconciled
    days.  Returns (bt with pins applied, n newly pinned).
    """
    pins = state.setdefault("bt_pinned", {})
    new = 0
    for src in ("ks", "fundamental"):
        if src not in bt.columns:
            continue
        ser = bt[src].dropna()
        if not len(ser):
            continue
        mx = ser.index.max()
        for d, v in ser.items():
            if d < C.LIVE_START or d >= mx:
                continue
            if src not in pins.setdefault(d, {}):
                pins[d][src] = float(v)
                new += 1
    for d, vals in pins.items():
        for src, v in vals.items():
            bt.loc[d, src] = v
    return bt.sort_index(), new


def series_fingerprint(df: pd.DataFrame, exclude_last_n: int = 5) -> dict:
    """Revision detector: hash of all rows except the trailing few.

    The trailing rows are provisional (day-D backtest rows regenerate on
    D+1); everything before them must be bit-stable run over run.
    """
    if not len(df):
        return {"sha256": None, "n_rows": 0, "last_date": None}
    stable = df.iloc[:-exclude_last_n] if len(df) > exclude_last_n else df.iloc[:0]
    payload = stable[["gross_pnl"]].round(2).to_csv().encode()
    return {
        "sha256": hashlib.sha256(payload).hexdigest(),
        "n_rows": int(len(stable)),
        "last_date": str(df.index.max()),
    }


def load_state() -> dict:
    if C.STATE_JSON.exists():
        with open(C.STATE_JSON) as fh:
            return json.load(fh)
    return {"backtest_fingerprints": {}, "scale_history": [],
            "missing_live_days": [], "last_run": {}}


def save_state(state: dict) -> None:
    tmp = C.STATE_JSON.with_suffix(".json.tmp")
    with open(tmp, "w") as fh:
        json.dump(state, fh, indent=2, sort_keys=True)
    tmp.replace(C.STATE_JSON)
