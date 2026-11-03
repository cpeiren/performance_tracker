"""Paper tracking for strategies held at weight 0 in the forward book.

A strategy paused by weight (2026-11-02: agri_event 1.0 -> 0.0) still runs its
pipeline and still ships its book and backtest every day; only the merge
multiplies its lots by zero.  It is tracked, not traded: the report shows its
own full-size backtest over the pause, its drawdown against its history, its
rolling Sharpe, and a PAPER-LIVE series -- its own pinned full-size book of
D-1 times the settlement-to-settlement move of D -- the holdings method, priced
by the same io_live.settle_move as the forward attribution, so a paper number
and a live one are the same measurement.  Only contracts the day's state
capture marks can be priced; the coverage column says how much of the book
that was.  Re-entry stays the owner's call.
"""

from __future__ import annotations

import math

import pandas as pd

import config as C
from . import io_backtest, io_live


def paused(weights_hist: dict[str, dict[str, float]]) -> dict[str, str]:
    """{strategy: first day of its current zero-weight run} on the latest
    shipped weights; strategies never at nonzero weight are not "paused"."""
    days = sorted(weights_hist)
    if not days:
        return {}
    out = {}
    for key, w in weights_hist[days[-1]].items():
        if w:
            continue
        since = None
        for d in reversed(days):
            if weights_hist[d].get(key, 0.0):
                break
            since = d
        if since is not None and since != days[0]:
            out[key] = since
    return out


def paper_live(key: str, days: list[str]) -> pd.DataFrame:
    """Per live day: (pnl, coverage) of ``key``'s own full-size book of the
    previous day x the settlement-to-settlement move of the day."""
    rows, books_prev, mult = [], None, None
    for d in days:
        book = io_backtest.component_books(d).get(key)
        if books_prev and io_live.state(d):
            if mult is None:
                mult = io_live.product_multipliers()
            move = io_live.settle_move(d, mult)     # the attribution's pricing
            tot = gross = priced = 0.0
            for t, lots in books_prev.items():
                gross += abs(lots)
                per_lot = io_live.lookup(move, t)
                if per_lot is None:
                    continue
                tot += lots * per_lot
                priced += abs(lots)
            rows.append({"date": d, "pnl": tot,
                         "coverage": priced / gross if gross else float("nan")})
        if book:
            books_prev = book
    return pd.DataFrame(rows, columns=["date", "pnl", "coverage"]).set_index("date")


def summary(key: str, since: str, bt: pd.DataFrame | None, days: list[str]) -> dict:
    """The paper row for one paused strategy (full size, CNY)."""
    s = (bt["gross_pnl"].astype(float).sort_index()       # io_backtest.load_series: date index
         if bt is not None and len(bt) else pd.Series(dtype=float))
    cum = s.cumsum()
    dd = cum - cum.cummax()
    worst_before = float(dd[dd.index < since].min()) if (dd.index < since).any() else float("nan")
    r60 = s.tail(60)
    paper = paper_live(key, [d for d in days if d >= since])
    return {
        "since": since,
        "bt_since": float(s[s.index >= since].sum()),
        "bt_20d": float(s.tail(20).sum()),
        "dd_now": float(dd.iloc[-1]) if len(dd) else float("nan"),
        "dd_worst_before": worst_before,
        "sharpe_60d": (float(r60.mean() / r60.std() * math.sqrt(C.ANN_DAYS))
                       if len(r60) > 1 and r60.std() > 0 else float("nan")),
        "paper_since": float(paper["pnl"].sum()) if len(paper) else 0.0,
        "paper_days": int(len(paper)),
        "paper_coverage": float(paper["coverage"].mean()) if len(paper) else float("nan"),
    }
