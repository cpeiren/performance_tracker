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
