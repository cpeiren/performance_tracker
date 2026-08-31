"""Per-snap desired-position term: price the book the account held BETWEEN
snap decisions against the book each run actually wanted.

The bridge's bookdiff terms see one book per day (the last run's), so a
deviation that arises at an early snap and is gone by the close -- an
unfilled leg later caught up, a BLOCKED run's whole delta, an intraday
round trip executed short -- earned or lost real money that landed
unattributed in ``resid``.  This term prices exactly that path:

    for runs r = 1..N with scaled target T_r, achieved position A_r
    (previous close + cumulative fills), and decision prices P_r:

        intraday_unfilled = sum_{r=1}^{N-1} sum_c
            [ (A_r[c] - T_r[c]) - dbook_prev[c] ] * (P_{r+1}[c] - P_r[c]) * m_c

    (+ = the deviation HELPED; it enters the bridge with sign +, so a
    positive value means lots-not-held-as-desired made money.)

Subtracting ``dbook_prev`` (yesterday's end-of-day deviation) keeps the
decomposition disjoint: a deviation carried from yesterday is priced
settle-to-settle by ``bookdiff_carry``, and the deviation still standing at
the LAST run is priced last-bench-to-settle by ``bookdiff_creation`` --
this term prices only the intraday leg (first bench to last bench) of
deviations that arose today, so no price interval is counted twice.

Every input is best-effort: a run without recorded targets, a contract
without a decision price at either end of a leg, or a day with no run
records at all degrades that piece to zero with a diagnostic count --
exactly the pre-existing behaviour, where all of this sat in ``resid``.
"""

from __future__ import annotations

import datetime as dt

from . import io_live

#: Decision stamped moments after the run began is still that run's decision
#: (advisor generated_at vs executor run stamp; measured skew is seconds).
BENCH_SKEW_SEC = 120.0


def _run_ts(run_id: str) -> dt.datetime | None:
    try:
        return dt.datetime.strptime(run_id, "%Y%m%d_%H%M%S")
    except (ValueError, TypeError):
        return None


def _bench_at(price_sets: list[tuple[dt.datetime, dict]],
              run_ts: dt.datetime) -> dict[str, float]:
    """Latest decision price per ticker at (or skew-close to) the run."""
    out: dict[str, float] = {}
    limit = run_ts + dt.timedelta(seconds=BENCH_SKEW_SEC)
    for ts, prices in price_sets:  # sets are time-sorted; later overwrites
        if ts <= limit:
            out.update(prices)
    return out


def unfilled_between_snaps(day: str, prev_positions: dict, dbook_prev: dict,
                           mult_map: dict[str, float]) -> tuple[float, dict]:
    """(intraday_unfilled, diagnostics) for one day.  Never raises."""
    diag = {"n_runs": 0, "n_runs_used": 0, "runs_without_targets": 0,
            "n_unpriced": 0, "n_dev_contracts": 0}
    try:
        runs = io_live.run_records(day)
        diag["n_runs"] = len(runs)
        usable = []
        for rec in runs:
            targets = rec.get("targets_final")
            ts = _run_ts(rec.get("run_id", ""))
            if not isinstance(targets, dict) or not targets or ts is None:
                diag["runs_without_targets"] += 1
                continue
            usable.append((ts, targets))
        if len(usable) < 2:
            return 0.0, diag  # one decision -> no between-snap interval
        diag["n_runs_used"] = len(usable)

        price_sets = io_live.snap_price_sets(day)
        if not price_sets:
            return 0.0, diag

        fills = io_live.fills_by_run(day)

        # walk the achieved position forward from yesterday's close
        pos: dict[str, float] = {t: float(v[0])
                                 for t, v in (prev_positions or {}).items() if v[0]}
        total = 0.0
        prev_dev: dict[str, float] | None = None
        prev_bench: dict[str, float] | None = None
        for ts, targets in usable:
            rec_fills = fills.get(ts.strftime("%Y%m%d_%H%M%S"), {})
            for sym, filled in rec_fills.items():
                pos[sym] = pos.get(sym, 0.0) + filled
            bench = _bench_at(price_sets, ts)
            if prev_dev is not None and prev_bench is not None:
                for c, d in prev_dev.items():
                    p0 = io_live.lookup(prev_bench, c)
                    p1 = io_live.lookup(bench, c)
                    m = mult_map.get(c) or 0.0
                    if p0 is None or p1 is None or not m:
                        diag["n_unpriced"] += 1
                        continue
                    total += d * (p1 - p0) * m
            dev: dict[str, float] = {}
            for c in set(pos) | set(targets):
                d = (pos.get(c, 0.0) - float(targets.get(c, 0) or 0)
                     - float(dbook_prev.get(c, 0.0)))
                if d:
                    dev[c] = d
            diag["n_dev_contracts"] = max(diag["n_dev_contracts"], len(dev))
            prev_dev, prev_bench = dev, bench
        return total, diag
    except Exception as exc:  # noqa: BLE001 - term degrades to resid, never breaks the bridge
        diag["error"] = str(exc)[:200]
        return 0.0, diag
