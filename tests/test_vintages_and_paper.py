"""Unit tests for the 2026-10-30 additions:

  * backtest vintages (ingest.record_vintage): a ship that RESTATES history
    keeps the new full series as an immutable vintage, cause-tagged by the
    strategy repo commit; the first sighting keeps the current series as the
    baseline; a plain append of new days is not a vintage.
  * paper tracking (paper.paused / paper.paper_live): a strategy at weight 0
    on the latest weights is tracked from the first day of its zero run, its
    own book of D-1 marked to the settlement move of D.

Pure functions on tmp dirs: nothing here reads the box or data/.
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
from tracker import ingest  # noqa: E402
from tracker import paper as P  # noqa: E402


def _ship(values: dict[str, float], at: str) -> pd.DataFrame:
    return pd.DataFrame({"date": list(values), "gross_pnl": list(values.values()),
                         "traded_notional": 0.0, "shipped_at": at})


@pytest.fixture()
def store(monkeypatch, tmp_path):
    monkeypatch.setattr(C, "BACKTEST_DIR", tmp_path)
    monkeypatch.setattr(C, "VINTAGE_DIR", tmp_path / "vintages")
    monkeypatch.setattr(ingest, "VINTAGE_INDEX", tmp_path / "vintages" / "index.csv")
    (tmp_path / "vintages").mkdir()
    return tmp_path


def _current(store, df):
    df.to_csv(store / "agri_event.csv", index=False)


def test_append_only_is_not_a_vintage_but_seeds_the_baseline(store):
    _current(store, _ship({"2026-10-27": 10.0, "2026-10-28": -5.0}, "2026-10-28T08:00:00+00:00"))
    msg = ingest.record_vintage("agri_event",
                                _ship({"2026-10-27": 10.0, "2026-10-28": -5.0, "2026-10-29": 3.0},
                                      "2026-10-29T08:00:00+00:00"), "2026-10-29T08:00:00+00:00", "aaa111")
    assert msg is None
    idx = ingest.vintages()
    assert list(idx["cause"]) == ["baseline"]                  # pre-existing history kept once
    assert (store / "vintages" / "agri_event" / idx["vintage"].iloc[0]).exists()


def test_restatement_keeps_the_new_series_and_names_the_cause(store):
    _current(store, _ship({"2026-10-27": 10.0, "2026-10-28": -5.0}, "2026-10-28T08:00:00+00:00"))
    new = _ship({"2026-10-27": 10.0, "2026-10-28": 75.0, "2026-10-29": 3.0}, "2026-10-29T08:00:00+00:00")
    msg = ingest.record_vintage("agri_event", new, "2026-10-29T08:00:00+00:00", "bbb222")
    assert msg and "1 historical row(s) restated" in msg and "+80" in msg
    idx = ingest.vintages()
    assert list(idx["cause"]) == ["baseline", "unknown"]       # baseline had no commit on record
    kept = pd.read_csv(store / "vintages" / "agri_event" / idx["vintage"].iloc[-1])
    assert kept["gross_pnl"].tolist() == [10.0, 75.0, 3.0]
    # next restatement under the SAME commit is data, under a new one code
    _current(store, new)
    again = _ship({"2026-10-27": 11.5, "2026-10-28": 75.0, "2026-10-29": 3.0}, "2026-10-30T08:00:00+00:00")
    ingest.record_vintage("agri_event", again, "2026-10-30T08:00:00+00:00", "bbb222")
    _current(store, again)
    ingest.record_vintage("agri_event", _ship({"2026-10-27": 20.0, "2026-10-28": 75.0, "2026-10-29": 3.0},
                                              "2026-10-31T08:00:00+00:00"), "2026-10-31T08:00:00+00:00", "ccc333")
    assert list(ingest.vintages()["cause"]) == ["baseline", "unknown", "data", "code"]


def test_moves_within_tolerance_are_not_restatements(store):
    _current(store, _ship({"2026-10-27": 10.0}, "2026-10-28T08:00:00+00:00"))
    assert ingest.record_vintage("agri_event", _ship({"2026-10-27": 10.6}, "x"), "x", "a") is None


def test_paused_reports_the_first_day_of_the_current_zero_run():
    hist = {"2026-10-29": {"agri_event": 1.0, "ks_branch": 0.8},
            "2026-10-30": {"agri_event": 1.0, "ks_branch": 0.8},
            "2026-11-02": {"agri_event": 0.0, "ks_branch": 0.8},
            "2026-11-03": {"agri_event": 0.0, "ks_branch": 0.8}}
    assert P.paused(hist) == {"agri_event": "2026-11-02"}
    # a strategy that has been at 0 since the first shipped day was never live: not "paused"
    assert P.paused({"2026-08-31": {"ks_ext": 0.0}, "2026-09-01": {"ks_ext": 0.0}}) == {}


def test_paper_live_marks_the_previous_book_to_the_settlement_move(monkeypatch):
    books = {"2026-11-02": {"agri_event": {"p2701": 9, "y2701": -10}},
             "2026-11-03": {"agri_event": {"p2701": 9, "y2701": -10}}}
    pnl = {"2026-11-03": pd.DataFrame({"symbol": ["p2701"], "settle_prev": [9000.0], "settle_now": [9050.0]})}
    monkeypatch.setattr(P.io_backtest, "component_books", lambda d: books.get(d, {}))
    monkeypatch.setattr(P.io_live, "daily_pnl", lambda d: pnl.get(d))
    monkeypatch.setattr(P.io_live, "state", lambda d: {"positions": {"p2701": {"multiplier": 10}}})
    monkeypatch.setattr(P.io_live, "final_settles", lambda d: {"p2701": 9060.0})
    out = P.paper_live("agri_event", ["2026-11-02", "2026-11-03"])
    assert out.loc["2026-11-03", "pnl"] == pytest.approx(9 * (9060.0 - 9000.0) * 10)   # settlement, not close
    assert out.loc["2026-11-03", "coverage"] == pytest.approx(9 / 19)                 # y2701 not priced live
