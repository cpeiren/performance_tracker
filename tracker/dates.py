"""Date-key discipline.

Trading-day labels come from the broker counter (CST calendar) on the live
side and from the backtest CSVs on the other; the only real hazard is the two
key formats (``YYYYMMDD`` in cnexec, ``YYYY-MM-DD`` in the shipped series).
Every reader converts through here; wall clocks are never consulted for day
attribution.
"""

from __future__ import annotations

import datetime as _dt


def normalize_date(d) -> str:
    """Anything date-like -> 'YYYY-MM-DD'."""
    if isinstance(d, (_dt.date, _dt.datetime)):
        return d.strftime("%Y-%m-%d")
    s = str(d).strip()
    if len(s) == 8 and s.isdigit():
        return f"{s[:4]}-{s[4:6]}-{s[6:]}"
    if len(s) == 10 and s[4] == "-" and s[7] == "-":
        return s
    raise ValueError(f"unrecognised date key: {d!r}")


def compact(d) -> str:
    """Anything date-like -> 'YYYYMMDD'."""
    return normalize_date(d).replace("-", "")


def as_date(d) -> _dt.date:
    return _dt.date.fromisoformat(normalize_date(d))


def is_weekday(d) -> bool:
    return as_date(d).weekday() < 5


def business_days_between(a, b) -> int:
    """Weekdays strictly after a, up to and including b."""
    da, db = as_date(a), as_date(b)
    if db <= da:
        return 0
    n, cur = 0, da
    while cur < db:
        cur += _dt.timedelta(days=1)
        if cur.weekday() < 5:
            n += 1
    return n
