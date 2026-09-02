"""Canonical backtest series: what the ship script delivers, plus the ks
series that already arrives in the inbox.

Canonical per-strategy file ``data/backtest/<strategy>.csv``:
    date,gross_pnl,traded_notional,shipped_at
Full-size CNY, ISO dates, 2026 onward.  The bridge consumes ALL seven series
(weighted per day on forward days, ks+fund unweighted on legacy days).  The
ship script also delivers the forward merge's per-day weights and per-source
component books; both are stored first-write-wins (as-shipped pins on disk).
"""

from __future__ import annotations

import json

import pandas as pd

import config as C
from .dates import normalize_date
from . import io_live, names


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
    """date x strategy-key full-size backtest gross P&L for the bridge.

    One column per strategy.  ks_branch prefers the INBOX series (arrives
    with no workstation in the loop, and same-day) with the shipped series
    filling dates the inbox lacks -- e.g. after the legacy per-source ships
    stop at Phase 5.  Every other strategy comes from its shipped series.
    """
    cols: dict[str, pd.Series] = {}
    for key in C.STRATEGIES:
        df = load_series(key)
        if len(df):
            cols[key] = df["gross_pnl"]
    ks = io_live.inbox_ks_summary()
    if len(ks):
        inbox_ser = ks["gross_pnl_shipped"]
        shipped = cols.get("ks_branch")
        cols["ks_branch"] = (inbox_ser if shipped is None
                             else inbox_ser.combine_first(shipped))
    out = pd.DataFrame(cols)
    out.index.name = "date"
    return out.sort_index()


# --------------------------------------------------------------------------
# Forward merge weights and component books (shipped, first-write-wins)
# --------------------------------------------------------------------------

def weights_history() -> dict[str, dict[str, float]]:
    """{date: {strategy_key: weight}} from data/forward/weights/<date>.json."""
    out: dict[str, dict[str, float]] = {}
    for p in sorted(C.FORWARD_WEIGHTS_DIR.glob("*.json")):
        with open(p) as fh:
            raw = json.load(fh)
        w = {C.FORWARD_SRC_TO_STRATEGY[src]: float(v)
             for src, v in raw.items()
             if src in C.FORWARD_SRC_TO_STRATEGY and isinstance(v, (int, float))}
        if w:
            out[p.stem] = w
    return out


def weights_for_day(day: str, hist: dict[str, dict[str, float]]
                    ) -> tuple[dict[str, float] | None, bool]:
    """(weights, exact) for a forward day: the day's own shipped weights, or
    the latest earlier day's carried forward (exact=False), or None."""
    if day in hist:
        return hist[day], True
    earlier = [d for d in hist if d < day]
    if earlier:
        return hist[max(earlier)], False
    return None, False


def component_books(day: str) -> dict[str, dict[str, float]]:
    """{strategy_key: {ticker: full-size lots}} shipped for one forward day."""
    out: dict[str, dict[str, float]] = {}
    for p in C.FORWARD_BOOKS_DIR.glob(f"{day}__*.json"):
        src = p.stem.split("__", 1)[1]
        key = C.FORWARD_SRC_TO_STRATEGY.get(src)
        if key is None:
            continue
        with open(p) as fh:
            raw = json.load(fh)
        b: dict[str, float] = {}
        for human, lots in raw.items():
            try:
                t = names.preferred_ticker(human)
            except ValueError:
                continue
            b[t] = b.get(t, 0.0) + float(lots)
        out[key] = b
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
    for src in bt.columns:
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


#: A backtest row is a revision only if it moved by more than this (CNY);
#: the same tolerance pin_divergence uses.
REVISION_TOL = 1.0


def mature_rows(df: pd.DataFrame) -> dict[str, float]:
    """{date: gross_pnl} for every row that is final: everything before the
    series' last date.  The last row is provisional (day-D rows regenerate on
    D+1), so it is excluded -- the same maturity rule the pins use.

    This is the revision baseline kept in state.  It replaces the old whole-
    series sha256, which could never match run over run because the stable
    region gains one row every day (BACKTEST REVISED fired for all seven books
    daily, whether or not any value had changed).
    """
    if not len(df):
        return {}
    mx = df.index.max()
    ser = df["gross_pnl"].dropna()
    return {str(d): round(float(v), 2) for d, v in ser.items() if d < mx}


def series_revisions(baseline: dict[str, float], df: pd.DataFrame,
                     skip_dates=()) -> list[tuple[str, float, float]]:
    """Rows present in both the stored baseline and the current series whose
    value moved by more than REVISION_TOL: [(date, old, new)], date-sorted.

    Growth (new mature rows) is not a revision.  `skip_dates` are dates
    covered by another detector (the as-shipped pins) so a revised live-window
    day is reported once, not twice.
    """
    if not baseline or not len(df):
        return []
    cur = mature_rows(df)
    skip = set(skip_dates)
    out = []
    for d, old in baseline.items():
        if d in skip or d not in cur:
            continue
        new = cur[d]
        if abs(new - float(old)) > REVISION_TOL:
            out.append((d, float(old), new))
    return sorted(out)


_LEGACY_PIN_KEYS = {"ks": "ks_branch", "fundamental": "fund_v3"}


def load_state() -> dict:
    if C.STATE_JSON.exists():
        with open(C.STATE_JSON) as fh:
            state = json.load(fh)
    else:
        return {"backtest_mature_rows": {}, "scale_history": [],
                "missing_live_days": [], "last_run": {}}
    # migrate pre-forward pin keys (bridge columns were ks/fundamental) to
    # strategy keys; idempotent, values untouched
    for d, vals in state.get("bt_pinned", {}).items():
        for old, new in _LEGACY_PIN_KEYS.items():
            if old in vals:
                vals.setdefault(new, vals.pop(old))
    ann = state.get("bt_pin_divergence_announced", {})
    for old, new in _LEGACY_PIN_KEYS.items():
        if old in ann:
            ann.setdefault(new, ann.pop(old))
    return state


def save_state(state: dict) -> None:
    tmp = C.STATE_JSON.with_suffix(".json.tmp")
    with open(tmp, "w") as fh:
        json.dump(state, fh, indent=2, sort_keys=True)
    tmp.replace(C.STATE_JSON)
