"""Per-source live attribution -- honest v1.

The live account merges every source's fills, so per-strategy live P&L can
only be attributed exactly where a contract is held by exactly one source's
shipped book that day.  Contracts in both books go to an explicit ``shared``
bucket; live positions with no shipped target go to ``neither`` (inherited or
manual).  Nothing is pro-rated.
"""

from __future__ import annotations

import pandas as pd

import config as C
from . import io_live
from .dates import normalize_date


def classify_day(day: str) -> dict[str, str]:
    """{ticker: 'ks' | 'fundamental' | 'shared'} from the dated books."""
    _, per = io_live.combined_fullsize_book(day)
    holders: dict[str, set] = {}
    for src, bookd in per.items():
        for t, lots in bookd.items():
            if lots:
                holders.setdefault(t, set()).add(src)
    out = {}
    for t, srcs in holders.items():
        out[t] = next(iter(srcs)) if len(srcs) == 1 else "shared"
    return out


def attribute_day(day: str) -> dict[str, float] | None:
    """Bucketed live total_pnl for one day, or None without live data."""
    pnl = io_live.daily_pnl(day)
    if pnl is None:
        return None
    who = classify_day(day)
    buckets = {"ks": 0.0, "fundamental": 0.0, "shared": 0.0, "neither": 0.0}
    for _, row in pnl.iterrows():
        t = row["symbol"]
        bucket = io_live.lookup(who, t) or "neither"
        buckets[bucket] += float(row["total_pnl"] or 0.0)
    return buckets


def attribute_all(days: list[str]) -> pd.DataFrame:
    rows = []
    for d in days:
        b = attribute_day(d)
        if b is not None:
            b["date"] = normalize_date(d)
            rows.append(b)
    df = pd.DataFrame(rows)
    return df.set_index("date").sort_index() if len(df) else df


def live_flags(days: list[str]) -> dict[str, bool]:
    """strategy -> has this strategy's source fed an executed run recently."""
    seen: set[str] = set()
    for d in days[-10:]:
        seen |= io_live.executed_sources(d)
    return {k: (v[1] in seen) if v[1] else False for k, v in C.STRATEGIES.items()}
