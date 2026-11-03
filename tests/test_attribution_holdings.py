"""Forward-day holdings attribution (replaced the lot pro-rata 2026-11-03).

A strategy's share of day D is its own D-1 book at the scale it was executed
at, marked to the settlement move of D; the account's remainder (fills vs
settlement, lot rounding) is ``trading``.  The pro-rata it replaced split
each contract's whole P&L by END-of-D lot shares and sent offsetting
contracts to ``shared``: over 2026-09-01..11-02 it read ks_branch +344,546
against holdings of +66,085 and china_pairs -110,072 against -14,224.

These tests pin the rule, the cases that used to go wrong (a roll-out leg, a
book changed during the day, an offset-to-zero contract the account never
carries), the regime boundary, a bookless day, and the footing identity.
"""
from __future__ import annotations

import os
import sys

import pandas as pd
import pytest

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, ROOT)
os.environ.setdefault("TRACKER_CNEXEC", os.path.join(ROOT, "tests", "_no_cnexec"))

import config as C  # noqa: E402
from tracker import attribution as AT  # noqa: E402
from tracker import io_backtest, io_live  # noqa: E402

DAYS = ["2026-09-15", "2026-09-16"]
WEIGHTS = {"ks_branch": 0.8, "stat_arb": 1.0, "china_pairs": 1.0}
SCALES = {"2026-09-15": 0.5, "2026-09-16": 1.0, "2026-09-17": 1.0}

#: 09-15 holds ni2610; 09-16 has rolled it to ni2611 and no longer names it.
BOOKS = {
    "2026-09-15": {"ks_branch": {"ni2610": 9.0, "ni2611": 9.0},
                   "stat_arb": {"ni2610": 1.0}},
    "2026-09-16": {"ks_branch": {"ni2611": 28.0}},
}

#: CNY per lot held through the day
MOVE = {"2026-09-16": {"ni2610": -1000.0, "ni2611": 200.0}}

#: the roll day's live P&L: the exit of ni2610 plus the leg that is still on book
PNL = pd.DataFrame({"symbol": ["ni2610", "ni2611"],
                    "total_pnl": [-28720.0, 4000.0]})


def _fake(monkeypatch, books=None, pnl=None, move=None):
    books = BOOKS if books is None else books
    move = MOVE if move is None else move
    monkeypatch.setattr(io_backtest, "component_books", lambda d: books.get(d, {}))
    monkeypatch.setattr(io_backtest, "weights_for_day", lambda d, h: (WEIGHTS, None))
    monkeypatch.setattr(io_live, "daily_pnl",
                        lambda d: (PNL if pnl is None else pnl).copy())
    monkeypatch.setattr(io_live, "product_multipliers", lambda: {})
    monkeypatch.setattr(io_live, "settle_move", lambda d, m: move.get(d, {}))


def _run(days=None, flags=None, scales=None):
    days = days or DAYS
    flags = flags if flags is not None else {d: True for d in days}
    return AT.attribute_all(days, flags, {}, SCALES if scales is None else scales)


def test_each_strategy_gets_its_previous_day_book_at_its_executed_scale(monkeypatch):
    _fake(monkeypatch)
    day = _run().loc["2026-09-16"]
    # 09-15 book at 09-15's scale 0.5: ks 0.8*9 lots of each, stat_arb 1.0*1 of ni2610
    ks = 0.5 * 0.8 * 9 * (-1000.0) + 0.5 * 0.8 * 9 * 200.0
    sa = 0.5 * 1.0 * 1 * (-1000.0)
    assert day["ks_branch"] == pytest.approx(ks)
    assert day["stat_arb"] == pytest.approx(sa)
    # the roll's exit fill and the new lots' fill-to-settle are the account's
    assert day["trading"] == pytest.approx(-28720.0 + 4000.0 - ks - sa)
    assert day["neither"] == 0.0 and day["shared"] == 0.0


def test_a_contract_only_the_days_own_books_name_is_trading():
    """Opened during D: no strategy carried it in, so its first day -- fill
    to settlement -- is the account's."""
    split = AT.split_day(pd.DataFrame({"symbol": ["ni2612"], "total_pnl": [-300.0]}),
                         who={"ni2612": {"ks_branch": 4.0}}, prev_who={},
                         forward=True, move={"ni2612": 50.0}, scale_prev=1.0)
    assert split == [("ni2612", "trading", -300.0)]


def test_a_contract_no_recent_book_names_stays_in_neither(monkeypatch):
    _fake(monkeypatch, pnl=pd.DataFrame({"symbol": ["lh2701"], "total_pnl": [-8640.0]}))
    assert _run().loc["2026-09-16", "neither"] == -8640.0


def test_an_offset_contract_the_account_never_carries_still_pays_each_holder(monkeypatch):
    """china_pairs short rb against ks_branch long: the merge nets them to
    zero, the account has no row, and each book still earns its own leg --
    the case pro-rata sent to ``shared``."""
    books = {"2026-09-15": {"ks_branch": {"rb2701": 10.0}, "china_pairs": {"rb2701": -8.0}},
             "2026-09-16": {}}
    _fake(monkeypatch, books=books, pnl=pd.DataFrame({"symbol": [], "total_pnl": []}),
          move={"2026-09-16": {"rb2701": 100.0}})
    day = _run().loc["2026-09-16"]
    assert day["ks_branch"] == pytest.approx(0.5 * 0.8 * 10 * 100.0)
    assert day["china_pairs"] == pytest.approx(0.5 * 1.0 * -8 * 100.0)
    # the account held round(0.5 * (8 - 8)) = 0 lots: rounding is trading's
    assert day[AT.BUCKETS].sum() == pytest.approx(0.0)


def test_book_ticker_matches_the_live_czce_spelling(monkeypatch):
    books = {"2026-09-15": {"chem_fund": {"SA2701": 4.0}}, "2026-09-16": {}}
    monkeypatch.setitem(WEIGHTS, "chem_fund", 1.5)
    _fake(monkeypatch, books=books, pnl=pd.DataFrame({"symbol": ["SA701"], "total_pnl": [70.0]}),
          move={"2026-09-16": {"SA701": 20.0}})
    day = _run().loc["2026-09-16"]
    assert day["chem_fund"] == pytest.approx(0.5 * 1.5 * 4 * 20.0)
    assert day["trading"] == pytest.approx(70.0 - 60.0)


def test_an_unpriced_or_unscaled_holding_goes_to_trading_not_to_a_strategy(monkeypatch):
    _fake(monkeypatch, move={"2026-09-16": {"ni2611": 200.0}})      # ni2610 unmarked
    day = _run().loc["2026-09-16"]
    assert day["stat_arb"] == 0.0
    assert day["trading"] == pytest.approx(-28720.0 + 4000.0 - 0.5 * 0.8 * 9 * 200.0)
    _fake(monkeypatch)
    day = _run(scales={}).loc["2026-09-16"]
    assert day["ks_branch"] == 0.0 and day["trading"] == pytest.approx(-24720.0)


def test_the_first_forward_day_has_no_holdings(monkeypatch):
    """A legacy day's holder map means something else, so the regimes are
    not crossed: the first forward day is trading (its own books name the
    contract) or neither."""
    _fake(monkeypatch)
    monkeypatch.setattr(AT, "_classify_legacy",
                        lambda d: {"ni2610": "ks_branch", "ni2611": "ks_branch"})
    day = _run(flags={"2026-09-15": False, "2026-09-16": True}).loc["2026-09-16"]
    assert day["neither"] == -28720.0
    assert day["trading"] == 4000.0
    assert day[list(C.STRATEGIES)].abs().sum() == 0.0


def test_a_day_whose_books_never_shipped_keeps_the_last_book_and_its_scale(monkeypatch):
    books = dict(BOOKS)
    books["2026-09-16"] = {}                      # nothing shipped that day
    books["2026-09-17"] = {"ks_branch": {"ni2612": 5.0}}
    move = {"2026-09-16": MOVE["2026-09-16"], "2026-09-17": {"ni2611": 100.0}}
    _fake(monkeypatch, books=books, move=move,
          pnl=pd.DataFrame({"symbol": ["ni2611"], "total_pnl": [0.0]}))
    out = _run(days=DAYS + ["2026-09-17"])
    # 09-17 is still marked off 09-15's book, at 09-15's scale (0.5)
    assert out.loc["2026-09-17", "ks_branch"] == pytest.approx(0.5 * 0.8 * 9 * 100.0)


def test_every_day_foots_to_the_days_live_pnl(monkeypatch):
    _fake(monkeypatch)
    out = _run()
    for day in DAYS:
        assert out.loc[day, AT.BUCKETS].sum() == pytest.approx(PNL["total_pnl"].sum())
    assert set(AT.BUCKETS) == set(C.STRATEGIES) | {"shared", "neither", "trading"}
