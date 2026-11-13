"""weekly.summarize / render: the Saturday read of the daily outputs.

Pure: synthetic daily CSV frames in, tables out.  Checks the periods, that
every table foots to live gross, that a pending sleeve-day stays out of
expected/gap, and that a product with no sector is named, not hidden.
"""
from __future__ import annotations

import os
import sys

import pandas as pd

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, ROOT)
os.environ.setdefault("TRACKER_CNEXEC", os.path.join(ROOT, "tests", "_no_cnexec"))

from tracker import weekly as W  # noqa: E402

# prior week Thu/Fri, this week Mon/Tue/Thu (Wed missing)
DAYS = ["2026-11-05", "2026-11-06", "2026-11-09", "2026-11-10", "2026-11-12"]


def _frames(pending_day=None):
    gross = [10.0, -20.0, 100.0, 50.0, -30.0]
    recon = pd.DataFrame({
        "live_gross": gross, "expected": [5.0, -10.0, 80.0, 40.0, -20.0],
        "exec_cost": [1.0] * 5, "fees": [2.0] * 5,
        "live_net": [g - 2.0 for g in gross], "pnl_final": [True] * 4 + [False],
        "bt_pending": [None] * 5}, index=DAYS)
    psd, prod, sp = [], [], []
    for d, g in zip(DAYS, gross):
        # ks_branch 60%, fund_v3 30%, trading 10% of each day
        for k, f in (("ks_branch", 0.6), ("fund_v3", 0.3)):
            e = g * f * 0.8
            if d == pending_day and k == "fund_v3":
                psd.append({"day": d, "strategy": k, "expected": None,
                            "attributed": g * f, "gap": None})
            else:
                psd.append({"day": d, "strategy": k, "expected": e,
                            "attributed": g * f, "gap": g * f - e})
        prod += [{"day": d, "product": "rb", "total_pnl": g * 0.5},
                 {"day": d, "product": "al", "total_pnl": g * 0.3},
                 {"day": d, "product": "ZZ", "total_pnl": g * 0.2}]
        sp += [{"day": d, "strategy": "ks_branch", "product": "rb", "pnl": g * 0.5},
               {"day": d, "strategy": "ks_branch", "product": "al", "pnl": g * 0.1},
               {"day": d, "strategy": "fund_v3", "product": "al", "pnl": g * 0.2},
               {"day": d, "strategy": "fund_v3", "product": "ZZ", "pnl": g * 0.1},
               {"day": d, "strategy": "trading", "product": "ZZ", "pnl": g * 0.1}]
    if pending_day:
        recon.loc[pending_day, "bt_pending"] = "fund_v3"
    return recon, pd.DataFrame(psd), pd.DataFrame(prod), pd.DataFrame(sp)


def test_periods_split_on_monday_and_respect_asof():
    per = W.period_days(DAYS)
    assert per["week"] == ["2026-11-09", "2026-11-10", "2026-11-12"]
    assert per["prior week"] == ["2026-11-05", "2026-11-06"]
    assert per["live-to-date"] == DAYS
    s = W.summarize(*_frames(), asof="2026-11-08")
    assert s["periods"]["week"] == ["2026-11-05", "2026-11-06"]


def test_strategies_and_sectors_foot_to_live_gross():
    s = W.summarize(*_frames(), asof="2026-11-14")
    week_gross = 100.0 + 50.0 - 30.0
    assert abs(s["headline"].loc["live_gross", "week"] - week_gross) < 1e-9
    assert abs(s["strategies"]["week"].sum() - week_gross) < 1e-9
    assert abs(s["strategies"].loc[W.TRADING_ROW, "week"] - 0.1 * week_gross) < 1e-9
    assert abs(s["sectors"]["week"].sum() - week_gross) < 1e-9
    assert abs(s["cross"].values.sum() - week_gross) < 1e-9
    assert s["no_row"] == ["2026-11-11", "2026-11-13"]
    assert s["provisional"] == "2026-11-12"
    assert s["unmapped"] == ["ZZ"]


def test_pending_sleeve_day_left_out_of_expected_and_gap():
    s = W.summarize(*_frames(pending_day="2026-11-12"), asof="2026-11-14")
    f = s["strategies"].loc["fund_v3"]
    # only 11-09 and 11-10 carry fund_v3 expected: 0.3 x 0.8 x (100 + 50)
    assert abs(f["week expected"] - 36.0) < 1e-9
    assert abs(f["week gap"] - (0.3 * 150 - 36.0)) < 1e-9
    assert s["pending"] == ["2026-11-12"]


def test_render_is_ascii_and_names_drivers():
    s = W.summarize(*_frames(), asof="2026-11-14")
    text = W.render(s, {"ks_branch": 0.8, "fund_v3": 2.0})
    text.encode("ascii")
    assert "| al | +36 |" in text and "fund_v3 (+24)" in text
    assert "products with no sector in config.SECTORS: ZZ" in text
