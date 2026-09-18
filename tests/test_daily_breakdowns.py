"""Daily live P&L by product and by strategy (report sections added 2026-09-18).

product_daily_pnl rolls the executor's per-symbol rows up to product root;
the report tables must foot to the per-symbol total.
"""
from __future__ import annotations

import os
import sys

import pandas as pd

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, ROOT)
os.environ.setdefault("TRACKER_CNEXEC", os.path.join(ROOT, "tests", "_no_cnexec"))

import config as C  # noqa: E402
from tracker import io_live, report  # noqa: E402

PNL = {
    "2026-09-16": pd.DataFrame({
        "symbol": ["cu2610", "cu2611", "IF2612", "CF701"],
        "holding_pnl": [-100.0, 50.0, 300.0, -40.0],
        "trading_pnl": [10.0, 0.0, -20.0, 0.0],
        "total_pnl": [-90.0, 50.0, 280.0, -40.0]}),
    "2026-09-17": pd.DataFrame({
        "symbol": ["cu2610", "CF701"],
        "holding_pnl": [5.0, -500.0], "trading_pnl": [0.0, 0.0],
        "total_pnl": [5.0, -500.0]}),
}


def test_product_rollup_sums_symbols_and_skips_missing_days(monkeypatch):
    monkeypatch.setattr(io_live, "daily_pnl", lambda d: PNL.get(d))
    out = io_live.product_daily_pnl(["2026-09-15", "2026-09-16", "2026-09-17"])
    v = out.set_index(["day", "product"])["total_pnl"]
    assert v[("2026-09-16", "cu")] == -40.0
    assert v[("2026-09-16", "IF")] == 280.0
    assert v[("2026-09-17", "CF")] == -500.0
    assert "2026-09-15" not in set(out["day"])


def test_product_section_ranks_worst_first_and_foots(monkeypatch, tmp_path):
    monkeypatch.setattr(io_live, "daily_pnl", lambda d: PNL.get(d))
    monkeypatch.setattr(C, "DATA", tmp_path)
    lines: list[str] = []
    report._product_section(lines.append, list(PNL))
    body = [l for l in lines if l.startswith("| ") and not l.startswith("| product")]
    assert body[0].startswith("| CF |")          # -540, the worst
    assert body[-1].startswith("| all products |")
    assert body[-1].split("|")[-3].strip() == "-295"   # window total: +200 - 495
    assert (tmp_path / "product_daily.csv").exists()


def test_day_table_row_total_and_sum_row():
    lines: list[str] = []
    wide = pd.DataFrame({"a": [1.0, -3.0], "b": [2.0, 0.0]},
                        index=["2026-09-16", "2026-09-17"])
    report._day_table(lines.append, wide, ["a", "b"])
    assert lines[2] == "| 2026-09-16 | +1 | +2 | +3 |"
    assert lines[-1] == "| sum | -2 | +2 | +0 |"


# -- settlement-to-settlement accounting (F134 follow-up, 2026-09-18) --------

def test_account_pnl_final_uses_settle_implied_and_excludes_deposits():
    row = pd.Series({"gross": -63945.0, "fees": 952.57, "aggregate": 935102.43,
                     "deposit": 1000000.0, "withdraw": 0.0,
                     "final_pnl": -35042.25, "settle_implied": 29845.0,
                     "final_status": "final"})
    a = io_live.account_pnl(row)
    assert a["final"] and a["live_gross"] == -34100.0
    assert a["live_net"] == -35042.25
    assert round(a["broker_resid"], 2) == 10.32      # settle_residual


def test_account_pnl_provisional_is_close_marked_net_of_cash():
    row = pd.Series({"gross": -160285.0, "fees": 1433.98, "aggregate": -161718.98,
                     "deposit": 0.0, "withdraw": 0.0, "final_pnl": float("nan"),
                     "settle_implied": float("nan"), "final_status": "provisional"})
    a = io_live.account_pnl(row)
    assert not a["final"] and a["live_gross"] == -160285.0
    assert round(a["broker_resid"], 2) == 0.0


def test_daily_pnl_adds_close_to_settlement_move(monkeypatch, tmp_path):
    (tmp_path / "daily_pnl_20260917.csv").write_text(
        "symbol,net_prev,net_now,settle_prev,settle_now,holding_pnl,trading_pnl,total_pnl\n"
        "p2705,28,28,10509,10417,-25760,0,-25760\n"
        "cu2610,-7,0,108000,108500,-3500,0,-3500\n"
        "_GROSS,,,,,,,-29260\n")
    import json
    (tmp_path / "state_20260917.json").write_text(json.dumps(
        {"positions": {"p2705": {"net": 28, "multiplier": 10, "settle": 10417}}}))
    (tmp_path / "state_20260918.json").write_text(json.dumps(
        {"positions": {"p2705": {"net": 28, "multiplier": 10, "pre_settle": 10511}}}))
    monkeypatch.setattr(C, "PNL_DIR", tmp_path)
    df = io_live.daily_pnl("2026-09-17").set_index("symbol")
    assert df.loc["p2705", "settle_adj"] == 28 * (10511 - 10417) * 10
    assert df.loc["p2705", "total_pnl"] == -25760 + 26320
    assert df.loc["cu2610", "settle_adj"] == 0.0          # flat at the close
    assert io_live.day_settles("2026-09-17")["p2705"] == 10511.0
    assert io_live.day_settles("2026-09-18") == {}         # no marks in fixture
    assert io_live.final_settles("2026-09-18") == {}       # latest: provisional
