"""Unit tests for the two alert paths fixed on 2026-09-02 (FAIL 3 of the daily
health check):

  * BACKTEST REVISED used to hash the whole stable region of each series; the
    region grows by one row per day, so the hash never matched and the alert
    fired for all seven books every run regardless of content.  It now
    compares mature rows value by value against the previous run's baseline.
  * RESIDUAL used to alert on single days; the backtest day (09:00 -> 09:00)
    and the live day (settle -> settle) share only 09:00-15:00, so one
    overnight move prints a large residual of one sign on D and its mirror
    on D+1.  It now alerts on the two-day sum.

Pure functions only: nothing here reads the box or data/.
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
from tracker import alerts as A  # noqa: E402
from tracker import io_backtest as ib  # noqa: E402


def _series(values: dict[str, float]) -> pd.DataFrame:
    df = pd.DataFrame({"gross_pnl": pd.Series(values)})
    df.index.name = "date"
    return df.sort_index()


YESTERDAY = {"2026-08-24": 100.0, "2026-08-25": -50.0, "2026-08-26": 30.0,
             "2026-08-27": 7.5, "2026-08-28": 12.0}
# same values, one more day appended (the normal daily growth)
TODAY_GROWTH_ONLY = dict(YESTERDAY, **{"2026-08-31": 41.0})


# ----------------------------------------------------------------- mature rows
def test_mature_rows_excludes_last_provisional_row():
    rows = ib.mature_rows(_series(YESTERDAY))
    assert "2026-08-28" not in rows
    assert rows == {"2026-08-24": 100.0, "2026-08-25": -50.0,
                    "2026-08-26": 30.0, "2026-08-27": 7.5}


def test_mature_rows_empty_series():
    assert ib.mature_rows(_series({})) == {}


# ------------------------------------------------------------------ revisions
def test_growth_only_is_not_a_revision():
    base = ib.mature_rows(_series(YESTERDAY))
    assert ib.series_revisions(base, _series(TODAY_GROWTH_ONLY)) == []


def test_provisional_row_finalising_is_not_a_revision():
    # yesterday's last row (provisional) takes its final value today
    base = ib.mature_rows(_series(YESTERDAY))
    today = dict(TODAY_GROWTH_ONLY, **{"2026-08-28": -20_000.0})
    assert ib.series_revisions(base, _series(today)) == []


def test_changed_mature_row_is_a_revision():
    base = ib.mature_rows(_series(YESTERDAY))
    today = dict(TODAY_GROWTH_ONLY, **{"2026-08-25": -25.0})
    assert ib.series_revisions(base, _series(today)) == [("2026-08-25", -50.0, -25.0)]


def test_sub_tolerance_move_is_ignored():
    base = ib.mature_rows(_series(YESTERDAY))
    today = dict(TODAY_GROWTH_ONLY, **{"2026-08-25": -50.0 + 0.5 * ib.REVISION_TOL})
    assert ib.series_revisions(base, _series(today)) == []


def test_pinned_dates_are_left_to_the_pin_alert():
    base = ib.mature_rows(_series(YESTERDAY))
    today = dict(TODAY_GROWTH_ONLY, **{"2026-08-25": -25.0, "2026-08-26": 999.0})
    rev = ib.series_revisions(base, _series(today), skip_dates=["2026-08-25"])
    assert rev == [("2026-08-26", 30.0, 999.0)]


def test_revision_alerts_first_run_creates_baseline_silently():
    state = {"backtest_fingerprints": {"x": {"sha256": "dead"}}}
    out = A.revision_alerts({"x": _series(YESTERDAY)}, state)
    assert out == []
    assert "backtest_fingerprints" not in state          # legacy sha baseline dropped
    assert state["backtest_mature_rows"]["x"] == ib.mature_rows(_series(YESTERDAY))


def test_revision_alerts_daily_growth_stays_silent_then_reports_once():
    state: dict = {}
    A.revision_alerts({"x": _series(YESTERDAY)}, state)
    assert A.revision_alerts({"x": _series(TODAY_GROWTH_ONLY)}, state) == []
    revised = dict(TODAY_GROWTH_ONLY, **{"2026-08-24": 125.0, "2026-08-26": 0.0})
    out = A.revision_alerts({"x": _series(revised)}, state)
    assert len(out) == 1
    msg = out[0]
    assert msg.startswith("BACKTEST REVISED: x -- 2 mature row(s)")
    assert "net -5 CNY" in msg                          # +25 - 30
    assert "largest 2026-08-26 +30 -> +0" in msg
    # baseline re-set: the same series is silent next run
    assert A.revision_alerts({"x": _series(revised)}, state) == []


def test_revision_alerts_skips_dates_the_pins_carry():
    state = {"bt_pinned": {"2026-08-25": {"x": -50.0, "y": 1.0}}}
    A.revision_alerts({"x": _series(YESTERDAY)}, state)
    revised = dict(TODAY_GROWTH_ONLY, **{"2026-08-25": 0.0})
    assert A.revision_alerts({"x": _series(revised)}, state) == []


# ------------------------------------------------------------------- residual
def _recon(resids: list[float]) -> pd.DataFrame:
    dates = pd.bdate_range("2026-08-03", periods=len(resids)).strftime("%Y-%m-%d")
    return pd.DataFrame({"resid": resids}, index=dates)


QUIET = [300.0, -200.0, 150.0, -100.0, 250.0, -300.0, 100.0, 200.0, -150.0, 50.0]


def test_window_straddle_pair_does_not_alert():
    # ten quiet days, then one overnight move: -40k on D, +40k on D+1, quiet after
    assert A.residual_alerts(_recon(QUIET + [-40_000.0, 40_000.0, 120.0])) == []


def test_straddle_onset_on_latest_day_waits_for_its_successor():
    # D is the latest reconciled day: nothing to judge it against yet
    assert A.residual_alerts(_recon(QUIET + [-40_000.0])) == []
    # ...and once the mirror arrives it is excused
    assert A.residual_alerts(_recon(QUIET + [-40_000.0, 39_500.0])) == []


def test_genuine_breakout_alerts_once_naming_both_neighbours():
    recon = _recon(QUIET + [-40_000.0, -100.0, 200.0])
    out = A.residual_alerts(recon)
    assert len(out) == 1
    d_prev, d, d_next = recon.index[-4], recon.index[-3], recon.index[-2]
    assert out[0].startswith(f"RESIDUAL {d}: -40000 CNY")
    assert f"({d_prev} +50, {d_next} -100)" in out[0]
    assert "straddle" in out[0]


# the actual bridge as reconciled on 2026-09-02 (data/reconciliation.csv)
REAL_RESID = [3637.0, -2499.0, 5766.0, -2281.0, 1926.0, 5210.0,
              -7068.0, -6192.0, 6173.0, -42842.0]


def test_real_2026_09_01_pattern_is_not_judged_until_next_day():
    # 09-01 -42,842 is the latest day: no successor yet, nothing alerts
    assert A.residual_alerts(_recon(REAL_RESID)) == []


def test_real_2026_09_01_excused_when_09_02_mirrors_it():
    assert A.residual_alerts(_recon(REAL_RESID + [41_000.0])) == []


def test_real_2026_09_01_alerts_when_09_02_does_not_mirror_it():
    out = A.residual_alerts(_recon(REAL_RESID + [1_500.0]))
    assert len(out) == 1 and out[0].startswith("RESIDUAL 2026-08-14: -42842 CNY")


def test_residual_floor_suppresses_tiny_pairs():
    small = [1.0, -1.0, 2.0, -2.0, 1.5, -1.5, 1.0, 1.0, 2.0, 3.0, 5.0, 6.0]
    assert max(abs(sum(small[i:i + 2])) for i in range(len(small) - 1)) < C.RESID_ABS_FLOOR
    assert A.residual_alerts(_recon(small)) == []


def test_residual_needs_history():
    assert A.residual_alerts(_recon([10.0, -10.0, 5.0])) == []
    assert A.residual_alerts(pd.DataFrame()) == []


if __name__ == "__main__":
    sys.exit(pytest.main([__file__, "-q"]))
