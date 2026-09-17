"""Name resolution and the off-book term (both added 2026-09-17).

Root cause of that day's -150,644 residual: tracker/names.py was a stale
mirror of cnexec/pyexec/names.py, taken before F118 added the CFFEX casing
rule.  "if Dec26" resolved to "if2612" while the counter says "IF2612", so
the merged book's four index-futures legs joined nothing -- ideal 0 (the
whole on-target position booked as a deviation), no bench (marking, creation
and the intraday term all zeroed), and every lot traded in them straight into
the residual.  Nothing alerted, because each reader degraded an unresolvable
or unmatched name to a skip.

These tests pin the three things that changed: the casing itself, the fact
that an unresolvable name is now recorded rather than swallowed, and the
off-book term that keeps contracts no book names out of the residual.

Everything live is faked through io_live / intraday so nothing reads the box.
"""
from __future__ import annotations

import importlib.util
import os
import sys

import pandas as pd
import pytest

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, ROOT)
os.environ.setdefault("TRACKER_CNEXEC", os.path.join(ROOT, "tests", "_no_cnexec"))

import config as C  # noqa: E402
from tracker import alerts as A  # noqa: E402
from tracker import intraday as intr  # noqa: E402
from tracker import io_live  # noqa: E402
from tracker import names  # noqa: E402
from tracker import reconcile as R  # noqa: E402

#: the production module this one mirrors; only present on CME-Server2
PYEXEC_NAMES = os.path.expanduser("~/cnexec/pyexec/names.py")


# ---------------------------------------------------------------- names ----

@pytest.mark.parametrize("human,ticker", [
    ("if Dec26", "IF2612"),     # CFFEX: book says lowercase, counter uppercase
    ("ih Mar27", "IH2703"),
    ("im Dec26", "IM2612"),
    ("IF Dec26", "IF2612"),     # already uppercase: unchanged
    ("SA Jan27", "SA701"),      # CZCE: uppercase AND one year digit
    ("PL Jan27", "PL701"),      # added upstream 2026-09-09
    ("rb Oct26", "rb2610"),     # everything else: lowercase, two year digits
    ("cs Jan27", "cs2701"),
])
def test_ticker_is_the_id_the_counter_carries(human, ticker):
    assert names.preferred_ticker(human) == ticker


def test_cffex_leg_joins_the_live_position_key():
    """The regression itself: book name -> the key state_<D>.json uses."""
    live_positions = {"IF2612": 8, "IH2612": 3, "rb2701": -127}
    assert names.preferred_ticker("if Dec26") in live_positions
    assert io_live.lookup(live_positions, names.preferred_ticker("ih Dec26")) == 3


def test_resolve_records_what_it_cannot_map_instead_of_skipping():
    names.UNRESOLVED.clear()
    assert names.resolve("rb Oct26") == "rb2610"
    assert names.resolve("not a contract") is None
    assert names.resolve("not a contract") is None
    assert names.UNRESOLVED == {"not a contract": 2}
    names.UNRESOLVED.clear()


@pytest.mark.skipif(not os.path.exists(PYEXEC_NAMES),
                    reason="production names.py only exists on the box")
def test_mirror_has_not_drifted_from_pyexec():
    """This module is a copy of pyexec's.  Drift is what caused the bug, so
    compare BEHAVIOUR (not bytes) over every product family we ship."""
    spec = importlib.util.spec_from_file_location("_pyexec_names", PYEXEC_NAMES)
    prod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(prod)
    fixture = [f"{sym} {mon}26" for sym in
               ("if", "ih", "im", "ic", "rb", "cs", "SA", "CF", "PL", "MA", "zn")
               for mon in ("Jan", "Jun", "Dec")]
    for human in fixture:
        assert (names.contract_ticker_candidates(human)
                == prod.contract_ticker_candidates(human)), human
    assert names.CZCE_SYMBOLS == prod.CZCE_SYMBOLS
    assert names.CFFEX_SYMBOLS == prod.CFFEX_SYMBOLS


# ------------------------------------------------------------- off-book ----

D1, D2 = "2026-09-14", "2026-09-15"
T, X = "rb2701", "cs2703"          # T is in the book, X is not
LOTS, MULT = 10.0, 10.0
XLOTS, XMULT = 5.0, 10.0
OPEN = {D1: 100.0, D2: 105.0}       # T's first decision of the day
SETTLE = {D1: 103.0, D2: 101.0}
XSETTLE = {D1: 200.0, D2: 210.0}
#: X is locked: the executor holds it, no book names it, it never trades
XPNL = XLOTS * XMULT * (XSETTLE[D2] - XSETTLE[D1])
BT_ROW = LOTS * MULT * (OPEN[D2] - OPEN[D1])          # 09:00(D1) -> 09:00(D2)
LIVE_GROSS = LOTS * MULT * (SETTLE[D2] - SETTLE[D1]) + XPNL


def _state(day):
    return {"positions": {
        T: {"net": LOTS, "multiplier": MULT, "settle": SETTLE[day]},
        X: {"net": XLOTS, "multiplier": XMULT, "settle": XSETTLE[day]}}}


@pytest.fixture
def fake_live(monkeypatch):
    monkeypatch.setattr(io_live, "state", _state)
    monkeypatch.setattr(io_live, "bench_prices", lambda day: {T: OPEN[day]})
    monkeypatch.setattr(io_live, "bench_prices_with_snap",
                        lambda day: {T: (OPEN[day], "0900")})
    monkeypatch.setattr(io_live, "fullsize_book_for_bridge",
                        lambda day, forward: {T: LOTS})
    monkeypatch.setattr(io_live, "fills_by_run", lambda day: {})
    monkeypatch.setattr(io_live, "daily_pnl", lambda day: pd.DataFrame(
        {"symbol": [T, X],
         "total_pnl": [LOTS * MULT * (SETTLE[D2] - SETTLE[D1]), XPNL]}))
    summ = pd.DataFrame({"gross": [LIVE_GROSS], "fees": [0.0], "aggregate": [0.0]},
                        index=[D2])
    monkeypatch.setattr(io_live, "daily_summary", lambda: summ)
    monkeypatch.setattr(io_live, "exec_summary", lambda: pd.DataFrame())
    monkeypatch.setattr(intr, "unfilled_between_snaps",
                        lambda *a, **k: (0.0, {"n_runs_used": 0, "n_unpriced": 0}))


def _bridge():
    return R.bridge_day(D2, D1, 1.0, BT_ROW, forward=True, prev_forward=True)


def test_contract_no_book_names_is_priced_verbatim_not_left_in_resid(fake_live):
    rec = _bridge()
    assert rec["n_offbook"] == 1
    assert rec["offbook_tickers"] == X
    assert rec["offbook_pnl"] == pytest.approx(XPNL)
    # the book contract is fully explained, so nothing is left over
    assert rec["resid"] == pytest.approx(0.0)


def test_offbook_contract_is_kept_out_of_the_priced_terms(fake_live):
    """X has no bench and is not in the ideal book: left in, it would show up
    as a full-size deviation in bookdiff and as an unbenchmarked leg."""
    rec = _bridge()
    assert rec["bookdiff_carry"] == pytest.approx(0.0)
    assert rec["bookdiff_creation"] == pytest.approx(0.0)
    assert rec["n_nobench"] == 0


def test_bridge_identity_still_closes_exactly(fake_live):
    rec = _bridge()
    rebuilt = (rec["expected"] - rec["exec_cost"] + rec["marking"]
               + rec["bookdiff_carry"] + rec["bookdiff_creation"]
               + rec["intraday_unfilled"] + rec["offbook_pnl"] + rec["resid"])
    assert rebuilt == pytest.approx(rec["live_gross"])


def test_unbenchmarked_held_notional_is_measured(fake_live, monkeypatch):
    """A contract IN the book with no decision price is the case the coverage
    alert exists for -- it must be counted, with its notional."""
    monkeypatch.setattr(io_live, "bench_prices", lambda day: {})
    monkeypatch.setattr(io_live, "bench_prices_with_snap", lambda day: {})
    rec = _bridge()
    assert rec["n_nobench"] == 1
    assert rec["nobench_notional"] == pytest.approx(LOTS * SETTLE[D2] * MULT)


def test_bench_after_0900_is_counted_as_a_straddle(fake_live, monkeypatch):
    monkeypatch.setattr(io_live, "bench_prices_with_snap",
                        lambda day: {T: (OPEN[day], "0930")})
    rec = _bridge()
    assert rec["n_bench_late"] == 1
    assert rec["bench_late_notional"] == pytest.approx(LOTS * SETTLE[D2] * MULT)


# --------------------------------------------------------------- alerts ----

def _recon(**over):
    row = {"live_gross_notional": 100e6, "nobench_notional": 0.0,
           "n_nobench": 0, "n_offbook": 0, "offbook_pnl": 0.0,
           "n_offbook_traded": 0, "offbook_tickers": ""}
    row.update(over)
    return pd.DataFrame([row], index=[D2])


def test_no_join_alerts_when_everything_resolves_and_is_benchmarked():
    names.UNRESOLVED.clear()
    assert A.join_integrity_alerts(_recon()) == []


def test_unbenchmarked_notional_share_alerts():
    names.UNRESOLVED.clear()
    out = A.join_integrity_alerts(
        _recon(nobench_notional=18e6, n_nobench=4))
    assert len(out) == 1 and out[0].startswith("BENCH COVERAGE")
    assert "18%" in out[0]


def test_offbook_pnl_alerts_once_material_and_names_the_contracts():
    names.UNRESOLVED.clear()
    out = A.join_integrity_alerts(
        _recon(n_offbook=1, offbook_pnl=-90000.0, offbook_tickers="cs2703"))
    assert len(out) == 1 and out[0].startswith("OFF-BOOK ")
    assert "cs2703" in out[0]


def test_immaterial_offbook_pnl_stays_quiet():
    names.UNRESOLVED.clear()
    assert A.join_integrity_alerts(
        _recon(n_offbook=1, offbook_pnl=12.0, offbook_tickers="cs2703")) == []


def test_trading_an_offbook_contract_always_alerts():
    names.UNRESOLVED.clear()
    out = A.join_integrity_alerts(_recon(n_offbook=1, n_offbook_traded=1))
    assert len(out) == 1 and out[0].startswith("OFF-BOOK TRADED")


def test_unresolvable_shipped_name_alerts():
    names.UNRESOLVED.clear()
    names.resolve("if Dec26x")
    out = A.join_integrity_alerts(_recon())
    names.UNRESOLVED.clear()
    assert len(out) == 1 and out[0].startswith("NAMES UNRESOLVED")
    assert "if Dec26x" in out[0]
