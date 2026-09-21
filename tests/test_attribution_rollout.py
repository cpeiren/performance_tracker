"""The prior-day fallback in attribution (added 2026-09-21).

Day D's live P&L is earned on positions held since D-1's settlement, but the
component books pinned for D are the END-of-D inbox snapshot.  A contract
rolled out during D is therefore absent from D's books, and its last day of
P&L -- the overnight gap plus the exit fill -- used to land in ``neither``.
That was the bucket's dominant population: -41,000 CNY over the 15 forward
days to 2026-09-18, of which -38,480 is named by the previous day's books
(one ``ni2610`` roll on 2026-09-16 was -28,720 of it, owed ~88% to ks_branch
and ~12% to stat_arb).

These tests pin the fallback itself, the fact that it does not reach across
the regime boundary or past a bookless day, and the footing identity the
report depends on.
"""
from __future__ import annotations

import os
import sys

import pandas as pd

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, ROOT)
os.environ.setdefault("TRACKER_CNEXEC", os.path.join(ROOT, "tests", "_no_cnexec"))

import config as C  # noqa: E402
from tracker import attribution as AT  # noqa: E402
from tracker import io_backtest, io_live  # noqa: E402

DAYS = ["2026-09-15", "2026-09-16"]
WEIGHTS = {"ks_branch": 0.8, "stat_arb": 1.0}

#: 09-15 holds ni2610; 09-16 has rolled it to ni2611 and no longer names it.
BOOKS = {
    "2026-09-15": {"ks_branch": {"ni2610": 9.0, "ni2611": 9.0},
                   "stat_arb": {"ni2610": 1.0}},
    "2026-09-16": {"ks_branch": {"ni2611": 28.0}},
}

#: the roll day's P&L: the exit of ni2610 plus the leg that is still on book
PNL = pd.DataFrame({"symbol": ["ni2610", "ni2611"],
                    "total_pnl": [-28720.0, 4000.0]})


def _fake(monkeypatch, books=None, pnl=None):
    books = BOOKS if books is None else books
    monkeypatch.setattr(io_backtest, "component_books",
                        lambda d: books.get(d, {}))
    monkeypatch.setattr(io_backtest, "weights_for_day",
                        lambda d, h: (WEIGHTS, None))
    monkeypatch.setattr(io_live, "daily_pnl",
                        lambda d: (PNL if pnl is None else pnl).copy())


def _run(days=None, flags=None):
    days = days or DAYS
    flags = flags if flags is not None else {d: True for d in days}
    return AT.attribute_all(days, flags, {})


def test_rolled_out_leg_is_attributed_to_the_previous_day_holders(monkeypatch):
    _fake(monkeypatch)
    out = _run()
    roll = out.loc["2026-09-16"]
    # ni2610 was 0.8*9 = 7.2 ks_branch and 1.0*1 = 1.0 stat_arb on 09-15
    assert roll["neither"] == 0.0
    assert round(roll["ks_branch"], 2) == round(-28720.0 * 7.2 / 8.2 + 4000.0, 2)
    assert round(roll["stat_arb"], 2) == round(-28720.0 * 1.0 / 8.2, 2)


def test_a_contract_no_recent_book_names_stays_in_neither(monkeypatch):
    _fake(monkeypatch, pnl=pd.DataFrame({"symbol": ["lh2701"],
                                         "total_pnl": [-8640.0]}))
    out = _run()
    assert out.loc["2026-09-16", "neither"] == -8640.0


def test_the_fallback_does_not_cross_the_regime_boundary(monkeypatch):
    """A legacy day's holder map means something else, so the first forward
    day keeps its unresolvable exits rather than reading it."""
    _fake(monkeypatch)
    monkeypatch.setattr(AT, "_classify_legacy",
                        lambda d: {"ni2610": "ks_branch", "ni2611": "ks_branch"})
    out = _run(flags={"2026-09-15": False, "2026-09-16": True})
    assert out.loc["2026-09-16", "neither"] == -28720.0
    assert round(out.loc["2026-09-16", "ks_branch"], 6) == 4000.0


def test_a_day_whose_books_never_shipped_keeps_the_fallback_alive(monkeypatch):
    books = dict(BOOKS)
    books["2026-09-16"] = {}                      # nothing shipped that day
    books["2026-09-17"] = {"ks_branch": {"ni2612": 5.0}}
    _fake(monkeypatch, books=books)
    out = _run(days=DAYS + ["2026-09-17"])
    # 09-16 resolves off 09-15; 09-17 must still see 09-15, not the empty day
    assert out.loc["2026-09-16", "neither"] == 0.0
    assert out.loc["2026-09-17", "neither"] == 0.0


def test_every_day_still_foots_to_the_days_live_pnl(monkeypatch):
    _fake(monkeypatch)
    out = _run()
    for day in DAYS:
        assert round(out.loc[day, AT.BUCKETS].sum(), 6) == PNL["total_pnl"].sum()
    assert set(AT.BUCKETS) == set(C.STRATEGIES) | {"shared", "neither"}
