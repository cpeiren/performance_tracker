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
``shared``.  Owner decision 2026-08-31.

PRIOR-DAY FALLBACK (2026-09-21).  Day D's P&L is earned on the positions
held since D-1's settlement, but the books pinned for D are the END-of-D
inbox snapshot -- the targets the executor moved TO during D.  Every
contract rolled out or dropped during D is therefore absent from D's books,
so its final day of P&L (the overnight gap plus the exit fill) had no
holder and fell into ``neither``.  That was the bucket's dominant
population, not the "rounding residue, inherited or manual lots" this
module originally assumed: over the 15 forward days to 2026-09-18 it was
-41,000 CNY across 38 contract-days, of which 34 (-38,480) are named by the
previous day's books -- one roll of ``ni2610`` on 2026-09-16 alone was
-28,720, owed ~88% to ks_branch and ~12% to stat_arb.  A contract the day's
own books do not name is now resolved against the last preceding day of the
SAME regime, which leaves ``neither`` for what the name claims.  Depth 1 is
enough: a deeper walk recovered one further contract-day worth 0 CNY.  The
regimes are not crossed (their holder maps mean different things), so the
first forward day keeps its -2,520 of unresolvable exits.

``neither`` now means: held live, named by no book on the day or the day
before it -- inherited, manual, or a position the books abandoned more than
a day before the executor flattened it.
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
#:
#: REJECTED ALTERNATIVE (measured 2026-09-21).  Splitting these contracts by
#: each holder's own price move -- w_i * lots_i * (settle_now - settle_prev)
#: * multiplier -- was tried to stop ``shared`` swallowing realised P&L.  It
#: does not work.  Over the 15 forward days to 2026-09-18 the 140 offsetting
#: contract-days carry -39,120 CNY of realised P&L between them, but the
#: holders' own notional moves on those same contracts total 546,654 in
#: magnitude (ks_branch -199,056 against fund_v3 +119,700): the offset that
#: makes the split ill-conditioned is exactly what makes each leg's notional
#: huge next to the P&L the account actually earned.  It also drains only 8%
#: of the bucket (-39,120 -> -35,911 left over) and puts gross-notional
#: numbers in the same column as every other contract's share of realised
#: P&L, which are not the same unit.  ``shared`` stays: it is the price of
#: refusing to split what the books deliberately offset, it is zero-mean
#: (mean -276 per contract-day, median -55, positive on 8 of 15 days), and
#: it is honest about being unattributed.
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


def _classify_forward(day: str,
                      weights: dict[str, float] | None) -> dict[str, dict[str, float]]:
    """{ticker: {strategy_key: weighted full-size lots}} for one forward day.

    Empty when the component books or the weights have not shipped yet.
    """
    contrib: dict[str, dict[str, float]] = {}
    if not weights:
        return contrib
    for key, bookd in io_backtest.component_books(day).items():
        w = float(weights.get(key, 0.0))
        if not w:
            continue
        for t, lots in bookd.items():
            if lots:
                contrib.setdefault(t, {})[key] = w * lots
    return contrib


def holder_map(day: str, forward: bool,
               weights: dict[str, float] | None) -> dict:
    """Who held what on ``day``, in the shape that regime attributes with."""
    return _classify_forward(day, weights) if forward else _classify_legacy(day)


def _holders_for(row, who: dict, prev_who: dict | None):
    """The day's holders of a contract, else the preceding day's (see module
    docstring: a contract rolled out during the day is gone from the day's
    own books, but its P&L that day is the exit of a position the previous
    day's books do name)."""
    return io_live.lookup(who, row["symbol"]) or (
        io_live.lookup(prev_who, row["symbol"]) if prev_who else None)


def _attribute_legacy(pnl: pd.DataFrame, who: dict[str, str],
                      prev_who: dict[str, str] | None) -> dict[str, float]:
    buckets = {b: 0.0 for b in BUCKETS}
    for _, row in pnl.iterrows():
        bucket = _holders_for(row, who, prev_who) or "neither"
        buckets[bucket] += float(row["total_pnl"] or 0.0)
    return buckets


def _attribute_forward(pnl: pd.DataFrame, who: dict[str, dict[str, float]],
                       prev_who: dict[str, dict[str, float]] | None,
                       ) -> dict[str, float]:
    buckets = {b: 0.0 for b in BUCKETS}
    for _, row in pnl.iterrows():
        v = float(row["total_pnl"] or 0.0)
        c = _holders_for(row, who, prev_who)
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


def attribute_day(day: str, forward: bool, weights: dict[str, float] | None,
                  who: dict | None = None,
                  prev_who: dict | None = None) -> dict[str, float] | None:
    """Bucketed live total_pnl for one day, or None without live data.

    ``who`` / ``prev_who`` are this day's and the preceding same-regime day's
    holder maps; ``attribute_all`` passes them so each is built once.
    """
    pnl = io_live.daily_pnl(day)
    if pnl is None:
        return None
    if who is None:
        who = holder_map(day, forward, weights)
    if forward:
        return _attribute_forward(pnl, who, prev_who)
    return _attribute_legacy(pnl, who, prev_who)


def attribute_all(days: list[str], forward_flags: dict[str, bool],
                  weights_hist: dict[str, dict[str, float]]) -> pd.DataFrame:
    rows = []
    #: last non-empty holder map seen, per regime -- a day whose books never
    #: shipped must not erase the fallback for the day after it
    prev_who: dict[bool, dict | None] = {True: None, False: None}
    for d in days:
        fwd = bool(forward_flags.get(d))
        w = io_backtest.weights_for_day(d, weights_hist)[0] if fwd else None
        who = holder_map(d, fwd, w)
        b = attribute_day(d, fwd, w, who=who, prev_who=prev_who[fwd])
        if who:
            prev_who[fwd] = who
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
