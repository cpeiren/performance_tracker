"""Window alignment of the bridge (fixed 2026-09-08, FAIL 4 of the daily
health check).

A backtest row D is the 09:00(D) -> 09:00(D+1) window; a live day is
settle(D-1) -> settle(D).  With the marking benchmark at each contract's
FIRST decision of the day, ``live - marking`` equals the 09:00(D-1) ->
09:00(D) window, which is backtest row D-1 -- so for a held book the
residual is zero by construction.  Before the fix (bench = last decision,
row = D) the whole overnight leg sat in the residual: 2026-09-04 printed
-85,775 on a -18,290 live day, all of it the Friday-13:30 -> Monday-09:00
leg that the backtest booked on Friday and the account earned on Monday.

Everything live is faked through io_live / intraday so nothing reads the box.
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
from tracker import intraday as intr  # noqa: E402
from tracker import io_live  # noqa: E402
from tracker import reconcile as R  # noqa: E402

D1, D2, D3 = "2026-09-03", "2026-09-04", "2026-09-07"
T = "rb2701"
LOTS, MULT = 10.0, 10.0
# first decision (09:00) and settle per day; D3 opens far from D2's settle
OPEN = {D1: 100.0, D2: 105.0, D3: 120.0}
SETTLE = {D1: 103.0, D2: 101.0, D3: 118.0}


def _full(_day, _forward):
    return {T: LOTS}


def _state(day):
    return {"positions": {T: {"net": LOTS, "multiplier": MULT, "settle": SETTLE[day]}},
            "marks": {T: {"settle": SETTLE[day]}}}


def _live_gross(day, prev):
    return LOTS * MULT * (SETTLE[day] - SETTLE[prev])


@pytest.fixture
def fake_live(monkeypatch):
    monkeypatch.setattr(io_live, "state", _state)
    monkeypatch.setattr(io_live, "bench_prices", lambda day: {T: OPEN[day]})
    monkeypatch.setattr(io_live, "fullsize_book_for_bridge", _full)
    summ = pd.DataFrame({"gross": [_live_gross(D2, D1), _live_gross(D3, D2)],
                         "fees": [0.0, 0.0], "aggregate": [0.0, 0.0]},
                        index=[D2, D3])
    monkeypatch.setattr(io_live, "daily_summary", lambda: summ)
    monkeypatch.setattr(io_live, "exec_summary", lambda: pd.DataFrame())
    monkeypatch.setattr(intr, "unfilled_between_snaps",
                        lambda *a, **k: (0.0, {"n_runs_used": 0, "n_unpriced": 0}))


def _bt_window_row(day, nxt):
    """Backtest row for `day`: the shipped book from 09:00(day) to 09:00(next)."""
    return LOTS * MULT * (OPEN[nxt] - OPEN[day])


def test_held_book_has_zero_residual_with_previous_row(fake_live):
    """Live day D3 (settle D2 -> settle D3) is explained by backtest row D2
    (09:00 D2 -> 09:00 D3) once live is re-marked to first decision."""
    rec = R.bridge_day(D3, D2, 1.0, _bt_window_row(D2, D3), forward=True, prev_forward=True)
    assert rec["marking"] == pytest.approx(
        LOTS * MULT * ((SETTLE[D3] - OPEN[D3]) - (SETTLE[D2] - OPEN[D2])))
    assert rec["resid"] == pytest.approx(0.0)


def test_same_day_row_leaves_the_overnight_leg_in_resid(fake_live):
    """The pre-fix pairing (row D explains live D) is off by exactly the
    difference of the two overnight legs -- the 2026-09-04 signature."""
    # emulate a next-day open for the D3 row: any value != the D2 row shows up 1:1
    fake_next_open = 130.0
    row_d3 = LOTS * MULT * (fake_next_open - OPEN[D3])
    rec = R.bridge_day(D3, D2, 1.0, row_d3, forward=True, prev_forward=True)
    assert rec["resid"] == pytest.approx(_bt_window_row(D2, D3) - row_d3)


def test_weighted_bt_lags_all_but_stat_arb(monkeypatch):
    days = ["2026-09-01", "2026-09-02", "2026-09-03"]
    bt = pd.DataFrame({"ks_branch": [10.0, 20.0, 30.0], "stat_arb": [1.0, 2.0, 3.0]},
                      index=days)
    bt.index.name = "date"
    monkeypatch.setattr(C, "LIVE_START", "2026-09-01")
    w = {d: {"ks_branch": 0.8, "stat_arb": 1.0} for d in days}
    fwd = {d: True for d in days}
    out, problems, incomplete = R.weighted_bt(bt, fwd, w)
    assert problems == []
    # day 2 explained by ks_branch row 1 (lag 1) and stat_arb row 2 (lag 0)
    assert out.at["2026-09-02", "ks_branch"] == pytest.approx(0.8 * 10.0)
    assert out.at["2026-09-02", "stat_arb"] == pytest.approx(2.0)
    assert out.at["2026-09-03", "ks_branch"] == pytest.approx(0.8 * 20.0)
    # the first live day has no previous ks_branch row: held out, not zeroed
    assert incomplete == {"2026-09-01": ["ks_branch"]}
    assert out.at["2026-09-01", "ks_branch"] == 0.0


def test_bench_prices_take_the_earliest_snap_per_ticker(monkeypatch):
    sets = {"0900": {"rb2701": 100.0}, "0930": {"rb2701": 101.0, "IF2609": 4500.0},
            "1330": {"rb2701": 103.0, "IF2609": 4510.0, "MA701": 2900.0}}

    def fake_snap(day, snap, source="ks"):
        return sets.get(snap) if source == C.FORWARD_SOURCE else None
    monkeypatch.setattr(io_live, "snap_prices", fake_snap)
    monkeypatch.setattr(io_live, "fund_prices", lambda day: {"MA701": 2890.0, "CF701": 16800.0})
    b = io_live.bench_prices("2026-09-04")
    assert b == {"rb2701": 100.0, "IF2609": 4500.0, "MA701": 2900.0, "CF701": 16800.0}
