"""attribute_products(): the strategy x product cross.

The claim the report makes is that summing a strategy's products reproduces
its row in the bucket table.  These tests pin exactly that, in both regimes,
and pin that the shared/neither escape hatches are carried through unchanged.
"""

import sys
from pathlib import Path

import pandas as pd
import pytest

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))

from tracker import attribution as AT  # noqa: E402
from tracker import io_backtest, io_live  # noqa: E402

DAYS = ["2026-09-01", "2026-09-02"]


def _pnl(rows):
    return pd.DataFrame(rows, columns=["symbol", "total_pnl"])


@pytest.fixture
def wired(monkeypatch):
    """Two forward days, three contracts over two products, two holders."""
    live = {
        "2026-09-01": _pnl([("rb2701", 100.0), ("rb2705", -40.0), ("bu2612", -60.0)]),
        "2026-09-02": _pnl([("rb2701", -10.0), ("bu2612", 30.0), ("zz2701", 7.0)]),
    }
    books = {
        "2026-09-01": {"ks_branch": {"rb2701": 4.0, "rb2705": -2.0},
                       "fund_v3": {"rb2701": 1.0, "bu2612": 3.0}},
        "2026-09-02": {"ks_branch": {"rb2701": 4.0},
                       "fund_v3": {"bu2612": 3.0}},
    }
    monkeypatch.setattr(io_live, "daily_pnl", lambda d: live.get(d))
    monkeypatch.setattr(io_backtest, "component_books", lambda d: books.get(d, {}))
    monkeypatch.setattr(io_backtest, "weights_for_day",
                        lambda d, h: ({"ks_branch": 1.0, "fund_v3": 1.0}, None))
    return {d: True for d in DAYS}


def test_products_sum_back_to_the_bucket_table(wired):
    buckets = AT.attribute_all(DAYS, wired, {})
    cross = AT.attribute_products(DAYS, wired, {})
    rolled = cross.groupby(["day", "strategy"])["pnl"].sum().unstack(fill_value=0.0)
    for day in buckets.index:
        for key in rolled.columns:
            assert rolled.loc[day, key] == pytest.approx(buckets.loc[day, key]), (day, key)


def test_total_foots_to_live_gross(wired):
    cross = AT.attribute_products(DAYS, wired, {})
    assert cross["pnl"].sum() == pytest.approx(100.0 - 40.0 - 60.0 - 10.0 + 30.0 + 7.0)


def test_product_root_not_contract(wired):
    cross = AT.attribute_products(DAYS, wired, {})
    assert set(cross["product"]) == {"rb", "bu", "zz"}
    # rb2701 and rb2705 collapse into one rb cell for ks_branch on day 1
    rb = cross[(cross["day"] == "2026-09-01") & (cross["strategy"] == "ks_branch")
               & (cross["product"] == "rb")]
    assert len(rb) == 1


def test_unheld_contract_lands_in_neither_under_its_own_product(wired):
    cross = AT.attribute_products(DAYS, wired, {})
    row = cross[(cross["strategy"] == "neither") & (cross["product"] == "zz")]
    assert len(row) == 1
    assert row["pnl"].iloc[0] == pytest.approx(7.0)


def test_empty_input_returns_the_declared_schema(monkeypatch):
    monkeypatch.setattr(io_live, "daily_pnl", lambda d: None)
    monkeypatch.setattr(io_backtest, "component_books", lambda d: {})
    monkeypatch.setattr(io_backtest, "weights_for_day", lambda d, h: ({}, None))
    out = AT.attribute_products(DAYS, {d: True for d in DAYS}, {})
    assert list(out.columns) == ["day", "strategy", "product", "pnl"]
    assert len(out) == 0
