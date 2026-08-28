"""Performance statistics on daily CNY P&L series (additive, no compounding)."""

from __future__ import annotations

import math

import pandas as pd

import config as C


def perf(series: pd.Series) -> dict:
    s = series.dropna()
    n = len(s)
    if n < 2:
        return {"n_days": n, "total": float(s.sum()) if n else 0.0,
                "sharpe": None, "mdd": None, "hit": None, "small_sample": True}
    mu, sd = float(s.mean()), float(s.std())
    cum = s.cumsum()
    dd = float((cum - cum.cummax()).min())
    return {
        "n_days": n,
        "total": float(s.sum()),
        "ann_pnl": mu * C.ANN_DAYS,
        "sharpe": (mu / sd * math.sqrt(C.ANN_DAYS)) if sd > 0 else None,
        "mdd": dd,
        "hit": float((s > 0).mean()),
        "small_sample": n < C.SMALL_SAMPLE_DAYS,
    }


def windows(series: pd.Series, oos_start: str = C.OOS_START,
            live_start: str = C.LIVE_START) -> dict[str, dict]:
    s = series.dropna().sort_index()
    return {
        "live-to-date": perf(s[s.index >= live_start]),
        "last-20d": perf(s.tail(20)),
        "2026-YTD": perf(s[s.index >= oos_start]),
    }
