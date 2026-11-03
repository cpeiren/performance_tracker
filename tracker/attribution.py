"""Per-source live attribution.

LEGACY days (per-source books traded unweighted): a contract's live P&L is
attributed exactly where it is held by exactly one source's shipped book;
contracts in both books go to ``shared``, live positions with no shipped
target to ``neither``.  Nothing is pro-rated.

FORWARD days (one merged weighted book of all 7 signals): HOLDINGS.  The
books pinned for D are the END-of-D inbox snapshot, so the positions carried
into D are D-1's.  Signal i receives its own D-1 book at the scale it was
executed at:

    scale(D-1) * sum_c w_i * lots_i(c) * (settle_D(c) - settle_D-1(c)) * mult(c)

including contracts the merge offsets to zero, which the account never
carries (their legs cancel across signals).  Everything else the account
earned on the day -- fills against settlement on the day's rebalances and
rolls, lot rounding, a scale change -- goes to ``trading``, so every day
still foots to live gross.  A live contract only D's books name (opened
during D) is all ``trading``; one named by neither day's books is
``neither`` (inherited, manual, or abandoned more than a day before the
executor flattened it).  The regimes are not crossed, so the first forward
day has no holdings.  The per-strategy number is therefore the shipped book
marked to live settlements; execution is an account-level quantity.  A
contract the day's capture does not mark cannot be priced and stays out of
every row (2026-11-02: sub-lot ks_ext lg / IM / si legs never traded live).

WHY NOT PRO-RATA (used 2026-08-31 .. 2026-11-02).  Each contract's live P&L
was split by the day's weighted-lot shares w_i*lots_i / net, with
near-offsetting contracts (net < 0.25 x gross) sent to ``shared``.  Over the
forward days 2026-09-01..11-02 it read ks_branch +344,546 / fund_v3 +132,876
/ china_pairs -110,072 / chem_fund -41,012 / stat_arb -43,480 against
holdings of +66,085 / +257,330 / -14,224 / +39,423 / +44,678.  Two causes:
(1) on contract-days where a book changed during D (snap rebalances,
rolls), the contract's whole P&L -- the day's fills included -- went by
END-of-D shares, amplified up to 4x when the net was small; that is
+244,000 of ks_branch's +278,000 excess; (2) ``shared`` dropped whole
holdings -- china_pairs' hedge legs offsetting other books were worth about
+95,000 to it.  The 2026-09-21 rejection of own-price-move splits (gross
notional next to shares of realised P&L in one column) was about using them
for the offsetting contracts only; applied to every contract the column is
one unit and the remainder is named.
"""

from __future__ import annotations

import pandas as pd

import config as C
from . import io_backtest, io_live, names
from .dates import normalize_date

#: ``shared`` is legacy-only now; ``trading`` is forward-only
BUCKETS = list(C.STRATEGIES) + ["shared", "neither", "trading"]


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


def _holders_for(symbol: str, who: dict, prev_who: dict | None):
    """Legacy days: the day's holder of a contract, else the preceding day's
    (a contract rolled out during the day is gone from the day's own books,
    but its P&L that day is the exit of a position the previous day's books
    do name -- 2026-09-21, -38,480 of -41,000 in ``neither`` was that)."""
    return io_live.lookup(who, symbol) or (
        io_live.lookup(prev_who, symbol) if prev_who else None)


def _live_spelling(ticker: str, live: dict) -> str:
    """The live P&L's spelling of a book ticker (the CZCE year-digit forms
    differ between producers), or the ticker itself when the account does
    not carry the contract."""
    if ticker in live:
        return ticker
    alt = names.alt_ticker(ticker)
    return alt if alt is not None and alt in live else ticker


def _split_forward(live: dict[str, float], who: dict, prev_who: dict | None,
                   move: dict[str, float], scale_prev: float | None
                   ) -> list[tuple[str, str, float]]:
    """Holdings split of one forward day (module docstring)."""
    held: dict[str, dict[str, float]] = {}
    for t, c in (prev_who or {}).items():
        dst = held.setdefault(_live_spelling(t, live), {})
        for key, wl in c.items():
            dst[key] = dst.get(key, 0.0) + wl
    opened = {_live_spelling(t, live) for t in (who or {})}
    scaled = scale_prev is not None and not pd.isna(scale_prev)
    out = []
    for sym in sorted(set(live) | set(held)):
        v = live.get(sym, 0.0)
        c = held.get(sym)
        per_lot = io_live.lookup(move, sym)
        if not c or per_lot is None or not scaled:
            if v:
                out.append((sym, "trading" if c or sym in opened else "neither", v))
            continue
        shares = [(key, float(scale_prev) * wl * per_lot) for key, wl in c.items()]
        out.extend((sym, key, h) for key, h in shares)
        out.append((sym, "trading", v - sum(h for _, h in shares)))
    return out


def split_day(pnl: pd.DataFrame, who: dict, prev_who: dict | None, forward: bool,
              move: dict[str, float] | None = None,
              scale_prev: float | None = None) -> list[tuple[str, str, float]]:
    """``[(symbol, bucket, pnl)]`` for one day under its regime.

    The single place the split rule lives.  Both the day's bucket totals and
    the per-product cross below consume it, so the two can never disagree
    about who held what.  ``move`` (io_live.settle_move) and ``scale_prev``
    (the execution scale of ``prev_who``'s day) are used on forward days only.
    """
    live: dict[str, float] = {}
    for s, v in zip(pnl["symbol"].astype(str), pnl["total_pnl"]):
        live[s] = live.get(s, 0.0) + float(v or 0.0)
    if forward:
        return _split_forward(live, who, prev_who, move or {}, scale_prev)
    return [(s, _holders_for(s, who, prev_who) or "neither", v)
            for s, v in live.items()]


def _attribute(split: list[tuple[str, str, float]]) -> dict[str, float]:
    buckets = {b: 0.0 for b in BUCKETS}
    for _, bucket, share in split:
        buckets[bucket] += share
    return buckets


def _walk(days: list[str], forward_flags: dict[str, bool],
          weights_hist: dict[str, dict[str, float]], scales):
    """Yield ``(day, split)`` once per day with live data.

    Holder maps are the expensive part (they read the shipped books), so the
    bucket totals and the per-product cross share one pass.  ``scales`` maps
    day -> execution scale (the bridge's ``scale`` column).
    """
    #: last non-empty holder map seen per regime, and its day -- a day whose
    #: books never shipped must not erase the holdings for the day after it
    prev_who: dict[bool, dict | None] = {True: None, False: None}
    prev_day: dict[bool, str | None] = {True: None, False: None}
    mult = None
    for d in days:
        fwd = bool(forward_flags.get(d))
        w = io_backtest.weights_for_day(d, weights_hist)[0] if fwd else None
        who = holder_map(d, fwd, w)
        pnl = io_live.daily_pnl(d)
        prev, pday = prev_who[fwd], prev_day[fwd]
        if who:
            prev_who[fwd], prev_day[fwd] = who, d
        if pnl is None:
            continue
        move, scale_prev = None, None
        if fwd and prev:
            if mult is None:
                mult = io_live.product_multipliers()
            move = io_live.settle_move(d, mult)
            scale_prev = scales.get(pday)
        yield normalize_date(d), split_day(pnl, who, prev, fwd, move, scale_prev)


def attribute_all(days: list[str], forward_flags: dict[str, bool],
                  weights_hist: dict[str, dict[str, float]], scales) -> pd.DataFrame:
    rows = []
    for day, split in _walk(days, forward_flags, weights_hist, scales):
        b = _attribute(split)
        b["date"] = day
        rows.append(b)
    df = pd.DataFrame(rows)
    return df.set_index("date").sort_index() if len(df) else df


def attribute_products(days: list[str], forward_flags: dict[str, bool],
                       weights_hist: dict[str, dict[str, float]], scales) -> pd.DataFrame:
    """``day, strategy, product, pnl`` -- the strategy x product cross.

    The report already says which strategy lost and, separately, which
    product lost.  Neither answers "which product did THIS strategy lose it
    in", which is the question a bleeding sleeve actually raises.  Same split
    rule as ``attribute_all`` (``split_day``), so summing this over products
    reproduces that table exactly, ``shared``, ``neither`` and ``trading``
    included.
    """
    acc: dict[tuple, float] = {}
    for day, split in _walk(days, forward_flags, weights_hist, scales):
        for sym, bucket, share in split:
            key = (day, bucket, names.product_root(sym))
            acc[key] = acc.get(key, 0.0) + share
    if not acc:
        return pd.DataFrame(columns=["day", "strategy", "product", "pnl"])
    out = pd.DataFrame([{"day": d, "strategy": s, "product": p, "pnl": v}
                        for (d, s, p), v in acc.items()])
    return out.sort_values(["day", "strategy", "pnl"]).reset_index(drop=True)


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
