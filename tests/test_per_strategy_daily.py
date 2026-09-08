"""per_strategy_daily(): per-day, per-strategy expected vs live-attributed.

Added 2026-09-09 so a sleeve's shortfall can be judged on its trailing
distribution instead of one window sum. Pure function: the report already
had every input in scope; this only lays them side by side per day.
"""
from __future__ import annotations

import os
import sys

import pandas as pd

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, ROOT)
os.environ.setdefault("TRACKER_CNEXEC", os.path.join(ROOT, "tests", "_no_cnexec"))

import config as C  # noqa: E402
from tracker.report import per_strategy_daily  # noqa: E402

DAYS = ["2026-09-01", "2026-09-02", "2026-09-03"]


def _live(scale=0.5):
    return pd.DataFrame({"scale": [scale] * len(DAYS),
                         "live_gross": [1.0, 2.0, 3.0]}, index=DAYS)


def test_expected_is_bridge_times_scale_and_gap_is_attributed_minus_expected():
    bridge = pd.DataFrame({"ks_branch": [100.0, 200.0, -50.0],
                           "fund_v3": [10.0, 0.0, 30.0]}, index=DAYS)
    attr = pd.DataFrame({"ks_branch": [40.0, 110.0, -30.0],
                         "fund_v3": [5.0, 1.0, 2.0],
                         "shared": [0.0, 0.0, 0.0],
                         "neither": [0.0, 0.0, 0.0]}, index=DAYS)
    out = per_strategy_daily(_live(0.5), bridge, attr)
    ks = out[out.strategy == "ks_branch"].set_index("day")
    assert ks.loc["2026-09-02", "expected"] == 100.0        # 200 x 0.5
    assert ks.loc["2026-09-02", "attributed"] == 110.0
    assert ks.loc["2026-09-02", "gap"] == 10.0
    assert ks.loc["2026-09-03", "gap"] == -30.0 - (-25.0)
    # every registered strategy appears on every day, absent ones as zeros
    assert set(out.strategy) == set(C.STRATEGIES)
    assert len(out) == len(DAYS) * len(C.STRATEGIES)
    chem = out[out.strategy == "chem_fund"]
    assert (chem[["expected", "attributed", "gap"]] == 0).all().all()


def test_window_sum_foots_to_the_per_strategy_table():
    """The sum over days per strategy equals what the 'Per strategy' table
    prints (bridge x scale summed, attribution summed) -- same inputs."""
    bridge = pd.DataFrame({"china_pairs": [8.0, -4.0, 6.0]}, index=DAYS)
    attr = pd.DataFrame({"china_pairs": [1.0, 1.0, 1.0]}, index=DAYS)
    live = _live(0.5)
    out = per_strategy_daily(live, bridge, attr)
    p = out[out.strategy == "china_pairs"]
    assert p.expected.sum() == (bridge["china_pairs"] * live["scale"]).sum()
    assert p.attributed.sum() == attr["china_pairs"].sum()


def test_alignment_ignores_days_outside_the_live_window_and_handles_missing():
    bridge = pd.DataFrame({"ks_branch": [1.0, 2.0, 3.0, 99.0]},
                          index=DAYS + ["2026-09-04"])          # extra bt day
    attr = pd.DataFrame({"ks_branch": [5.0, 6.0]}, index=DAYS[:2])  # missing day 3
    out = per_strategy_daily(_live(1.0), bridge, attr)
    ks = out[out.strategy == "ks_branch"].set_index("day")
    assert list(ks.index) == DAYS
    assert ks.loc["2026-09-03", "attributed"] == 0.0
    assert ks.loc["2026-09-03", "gap"] == -3.0
    # no bridge at all -> expected 0, gap == attributed
    out2 = per_strategy_daily(_live(1.0), None, attr)
    ks2 = out2[out2.strategy == "ks_branch"].set_index("day")
    assert (ks2.expected == 0).all() and ks2.loc["2026-09-01", "gap"] == 5.0
    # empty live -> empty frame with the schema
    empty = per_strategy_daily(pd.DataFrame(), bridge, attr)
    assert list(empty.columns) == ["day", "strategy", "expected", "attributed", "gap"]
    assert len(empty) == 0
