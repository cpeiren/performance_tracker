"""Per-source live attribution.

LEGACY days (per-source books traded unweighted): a contract's live P&L is
attributed exactly where it is held by exactly one source's shipped book;
contracts in both books go to ``shared``, live positions with no shipped
target to ``neither``.  Nothing is pro-rated.

FORWARD days (one merged weighted book of all 7 signals): most contracts are
held by several signals, so exclusive-holder degenerates -- P&L is instead
PRO-RATED by each signal's weighted full-size lots.  Per contract c the
signal contribution is w_i * lots_i(c); signal i receives
pnl_c * w_i*lots_i / sum_j w_j*lots_j.  The ratio is scale-invariant, and
signed: a signal short a contract the book is net long correctly receives
negative P&L when the contract makes money.  When the weighted lots offset
to (near) zero the split is undefined and the contract's P&L goes to
``shared``; live positions with no component-book holder go to ``neither``
(rounding residue, inherited or manual lots).  Owner decision 2026-08-31.
"""

from __future__ import annotations

import pandas as pd

import config as C
from . import io_backtest, io_live
from .dates import normalize_date

#: below half a weighted lot net, a pro-rata split is noise -> shared bucket
NET_LOTS_FLOOR = 0.5
#: and when the net is under this fraction of the GROSS weighted lots, the
#: split amplifies each holder's share past ~4x the contract's P&L -- the
#: non-position part of total_pnl (fills) makes that ill-conditioned, so it
#: goes to shared as well.  Measured 2026-08-31: median |gross/net| 1.17,
#: this floor moves only ~7 of 76 contracts.
NET_GROSS_FLOOR = 0.25

BUCKETS = list(C.STRATEGIES) + ["shared", "neither"]


def _classify_legacy(day: str) -> dict[str, str]:
    """{ticker: strategy_key | 'shared'} from the legacy per-source books."""
    _, per = io_live.combined_fullsize_book(day)
    holders: dict[str, set] = {}
    for src, bookd in per.items():
        for t, lots in bookd.items():
            if lots:
                holders.setdefault(t, set()).add(src)
    out = {}
    for t, srcs in holders.items():
        if len(srcs) == 1:
            out[t] = C.SOURCE_TO_STRATEGY.get(next(iter(srcs)), "shared")
        else:
            out[t] = "shared"
    return out


def _attribute_legacy(day: str, pnl: pd.DataFrame) -> dict[str, float]:
    who = _classify_legacy(day)
    buckets = {b: 0.0 for b in BUCKETS}
    for _, row in pnl.iterrows():
        bucket = io_live.lookup(who, row["symbol"]) or "neither"
        buckets[bucket] += float(row["total_pnl"] or 0.0)
    return buckets


def _attribute_forward(day: str, pnl: pd.DataFrame,
                       weights: dict[str, float] | None) -> dict[str, float]:
    buckets = {b: 0.0 for b in BUCKETS}
    books = io_backtest.component_books(day)
    if not books or not weights:
        # component books or weights not shipped (yet): nothing attributable
        for _, row in pnl.iterrows():
            buckets["neither"] += float(row["total_pnl"] or 0.0)
        return buckets
    # {ticker: {strategy: weighted full-size lots}}
    contrib: dict[str, dict[str, float]] = {}
    for key, bookd in books.items():
        w = float(weights.get(key, 0.0))
        if not w:
            continue
        for t, lots in bookd.items():
            if lots:
                contrib.setdefault(t, {})[key] = w * lots
    for _, row in pnl.iterrows():
        v = float(row["total_pnl"] or 0.0)
        c = io_live.lookup(contrib, row["symbol"])
        if not c:
            buckets["neither"] += v
            continue
        net = sum(c.values())
        gross = sum(abs(x) for x in c.values())
        if abs(net) < max(NET_LOTS_FLOOR, NET_GROSS_FLOOR * gross):
            buckets["shared"] += v
            continue
        for key, ci in c.items():
            buckets[key] += v * ci / net
    return buckets


def attribute_day(day: str, forward: bool,
                  weights: dict[str, float] | None) -> dict[str, float] | None:
    """Bucketed live total_pnl for one day, or None without live data."""
    pnl = io_live.daily_pnl(day)
    if pnl is None:
        return None
    if forward:
        return _attribute_forward(day, pnl, weights)
    return _attribute_legacy(day, pnl)


def attribute_all(days: list[str], forward_flags: dict[str, bool],
                  weights_hist: dict[str, dict[str, float]]) -> pd.DataFrame:
    rows = []
    for d in days:
        fwd = bool(forward_flags.get(d))
        w = io_backtest.weights_for_day(d, weights_hist)[0] if fwd else None
        b = attribute_day(d, fwd, w)
        if b is not None:
            b["date"] = normalize_date(d)
            rows.append(b)
    df = pd.DataFrame(rows)
    return df.set_index("date").sort_index() if len(df) else df


def live_flags(days: list[str], forward_flags: dict[str, bool],
               weights_hist: dict[str, dict[str, float]]) -> dict[str, bool]:
    """strategy -> is it live: its legacy source fed a recent executed run,
    or the forward book executes and the strategy's merge weight is > 0.

    ``days`` should include the report day: the weights that decide "live"
    are those of the LAST DAY A FORWARD RUN EXECUTED, which is usually today
    and not yet reconciled (its backtest row is still pending).  Until
    2026-09-03 this read the last reconciled day, so a strategy parked for one
    day and re-enabled the next showed as not live for a day.
    """
    recent = days[-10:]
    seen: set[str] = set()
    last_fwd = None
    for d in recent:
        src = io_live.executed_sources(d)
        seen |= src
        if C.FORWARD_SOURCE in src:
            last_fwd = d
    flags = {k: (v[1] in seen) if v[1] else False for k, v in C.STRATEGIES.items()}
    if last_fwd is None:
        last_fwd = max((d for d in recent if forward_flags.get(d)), default=None)
    if last_fwd:
        w = io_backtest.weights_for_day(last_fwd, weights_hist)[0] or {}
        for key in C.STRATEGIES:
            if w.get(key):
                flags[key] = True
    return flags
