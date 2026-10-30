"""Paper tracking for strategies held at weight 0 in the forward book.

A strategy paused by weight (2026-11-02: agri_event 1.0 -> 0.0) still runs its
pipeline and still ships its book and backtest every day; only the merge
multiplies its lots by zero.  It is tracked, not traded: the report shows its
own full-size backtest over the pause, its drawdown against its history, its
rolling Sharpe, and a PAPER-LIVE series -- its own pinned full-size book of
D-1 times the settlement-to-settlement move of D (the holdings method, which
reproduced the account's position P&L within 2% on 10-27..10-29).  Only
contracts the live account also prices that day can be marked; the coverage
column says how much of the book that was.  Re-entry stays the owner's call.
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
    rows, books_prev = [], None
    for d in days:
        book = io_backtest.component_books(d).get(key)
        pnl = io_live.daily_pnl(d)
        st = io_live.state(d) or {}
        if books_prev and pnl is not None:
            fin = io_live.final_settles(d)
            mult = {s: float(p.get("multiplier") or 0.0)
                    for s, p in (st.get("positions") or {}).items()}
            prev = dict(zip(pnl["symbol"].astype(str), pnl["settle_prev"]))
            close = dict(zip(pnl["symbol"].astype(str), pnl["settle_now"]))
            tot = gross = priced = 0.0
            for t, lots in books_prev.items():
                gross += abs(lots)
                s0 = io_live.lookup(prev, t)
                s1 = io_live.lookup(fin, t)
                s1 = io_live.lookup(close, t) if s1 is None else s1
                m = io_live.lookup(mult, t)
                if s0 is None or s1 is None or not m or any(map(pd.isna, (s0, s1))):
                    continue
                tot += lots * (float(s1) - float(s0)) * m
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
