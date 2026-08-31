"""The per-day bridge between shipped backtest and realized live P&L.

Account-level, GROSS (fees are shown separately -- the backtest is gross).
Per trading day D and contract c with multiplier m_c:

    fullsize_c(D)  = LEGACY days: ks_book_c(D) + fund_book_c(D)
                     FORWARD days (2026-08-31 on): forward_book_c(D), the
                     merged weighted book pyexec actually targeted
    ideal_c(D)     = scale_D * fullsize_c(D)
    dbook_c(D)     = live_net_c(D) - ideal_c(D)
    bench_c(D)     = EOD decision price (1330 snap, fund price, else settle)

    expected_D          = scale_D * sum_i w_i(D) * bt_i(D)
                          (legacy days: w = 1 on ks_branch + fund_v3 only)
    exec_cost_D         = slip_total_D + exec_unbenchmarked_D    (+ = cost)
    marking_D           = basis(D) - basis(D-1)
        basis(D) = sum_c live_net_c(D) * (settle_c(D) - bench_c(D)) * m_c
    bookdiff_carry_D    = sum_c dbook_c(D-1) * (settle_c(D) - settle_c(D-1)) * m_c
    bookdiff_creation_D = sum_c (dbook_c(D) - dbook_c(D-1)) * (settle_c(D) - bench_c(D)) * m_c
    broker_basis_D      = live_gross_D - settle_sum_D
        (settle_sum_D = sum of per-symbol total_pnl in daily_pnl_<D>.csv --
         the settle-marked frame every other term lives in; the account
         'gross' is broker-equity based and differs by 1-3k CNY daily)
    intraday_unfilled_D = per-snap deviation term (see tracker/intraday.py):
                          the desired-vs-achieved book BETWEEN runs, priced
                          decision-to-decision -- disjoint from the bookdiff
                          terms by construction
    resid_D             = settle_sum_D - expected_D + exec_cost_D
                          - marking_D - bookdiff_carry_D - bookdiff_creation_D
                          - intraday_unfilled_D

    live_gross_D = expected_D - exec_cost_D + marking_D + bookdiff_carry_D
                   + bookdiff_creation_D + intraday_unfilled_D + resid_D
                   + broker_basis_D   (exact)
    live_net_D   = live_gross_D - fees_D + broker_resid_D

Why these terms: exec_cost prices fills away from the shipped decision
(positive = paid); the telescoping marking term absorbs the settle-vs-snap
marking basis so its CUMULATIVE value is just the current open book's basis
(bounded, cannot drift); the two bookdiff terms price LOTS NOT HELD -- lot
rounding at small scale, unfilled legs, BLOCKED runs, manual intervention --
with no double count against slippage (which prices filled lots only).
``resid`` closes the identity; its magnitude is the tracker's quality metric.

KNOWN LIMITATION (day-window mismatch): a backtest day D spans snap 0900(D)
through the overnight leg into D+1, while a live trading day spans
settle(D-1) -> settle(D).  Daily terms therefore straddle windows and the
same-day expected can even anti-correlate with live on short samples; the
CUMULATIVE curves differ only by boundary legs.  Judge daily residuals by
their trailing distribution, not day by day.  Revisit alignment once 30+
live days exist.
"""

from __future__ import annotations

import pandas as pd

import config as C
from . import intraday as intr
from . import io_live
from .dates import normalize_date


def _multipliers(st: dict) -> dict[str, float]:
    out = {}
    for sym, pos in (st.get("positions") or {}).items():
        m = pos.get("multiplier")
        if m:
            out[sym] = float(m)
    return out


def _all_tickers(*dicts) -> set[str]:
    out: set[str] = set()
    for d in dicts:
        out.update(d.keys())
    return out


def bridge_day(day: str, prev_day: str | None, scale: float,
               bt_gross: float, prev_scale: float | None = None,
               forward: bool = False, prev_forward: bool = False) -> dict | None:
    """One day's bridge terms.  Returns None when the day has no live state.

    ``bt_gross`` is the FULL-SIZE combined backtest gross for the day --
    ks + fundamental unweighted on legacy days, the weighted sum of all
    shipped series on forward days (matching the weighted merged book);
    ``scale`` the day's execution scale; ``prev_scale`` the previous live
    day's scale (defaults to today's), used to price yesterday's standing
    book difference at yesterday's ideal.  ``forward``/``prev_forward``
    select which full-size book the ideal is built from.
    """
    st = io_live.state(day)
    if st is None:
        return None
    st_prev = io_live.state(prev_day) if prev_day else None

    live_pos = io_live.live_positions(st)
    settle = io_live.settles(st)
    mult = _multipliers(st)
    bench = io_live.bench_prices(day)

    full = io_live.fullsize_book_for_bridge(day, forward)

    prev_pos = io_live.live_positions(st_prev) if st_prev else {}
    prev_settle = io_live.settles(st_prev) if st_prev else {}
    prev_mult = _multipliers(st_prev) if st_prev else {}
    prev_full = (io_live.fullsize_book_for_bridge(prev_day, prev_forward)
                 if prev_day else {})
    if prev_scale is None:
        prev_scale = scale

    # -- marking basis ----------------------------------------------------
    def basis(pos: dict, settles_: dict, mults: dict, bench_: dict) -> tuple[float, int]:
        tot, nobench = 0.0, 0
        for t, (net, m) in pos.items():
            if net == 0 or not m:
                continue
            s = io_live.lookup(settles_, t)
            if s is None:
                continue
            b = io_live.lookup(bench_, t)
            if b is None:
                nobench += 1
                continue  # bench falls back to settle -> term 0
            tot += net * (s - b) * m
        return tot, nobench

    basis_now, n_nobench = basis(live_pos, settle, mult, bench)
    bench_prev = io_live.bench_prices(prev_day) if prev_day else {}
    basis_prev, _ = basis(prev_pos, prev_settle, prev_mult, bench_prev)
    marking = basis_now - basis_prev

    # -- book differences -------------------------------------------------
    def dbook(pos: dict, full_book: dict, s: float) -> dict[str, float]:
        out = {}
        for t in _all_tickers(pos, full_book):
            net = pos.get(t, (0.0, 0.0))[0]
            ideal = s * io_live.lookup(full_book, t, 0.0)
            d = net - ideal
            if d:
                out[t] = d
        return out

    db_now = dbook(live_pos, full, scale)
    db_prev = dbook(prev_pos, prev_full, prev_scale) if prev_day else {}

    def mult_of(t: str) -> float:
        return mult.get(t) or prev_mult.get(t) or 0.0

    carry = 0.0
    for t, d in db_prev.items():
        s0 = io_live.lookup(prev_settle, t)
        s1 = io_live.lookup(settle, t)
        if s0 is not None and s1 is not None:
            carry += d * (s1 - s0) * mult_of(t)

    creation = 0.0
    for t in _all_tickers(db_now, db_prev):
        dd = db_now.get(t, 0.0) - db_prev.get(t, 0.0)
        if not dd:
            continue
        s1 = io_live.lookup(settle, t)
        if s1 is None:
            continue
        b = io_live.lookup(bench, t)
        if b is None:
            b = s1  # no decision price -> term 0 by construction
        creation += dd * (s1 - b) * mult_of(t)

    # -- per-snap deviation between decisions ------------------------------
    # Prices the book held BETWEEN runs against each run's own target, so an
    # intraday round trip / unfilled leg / BLOCKED run no longer lands in
    # resid.  Subtracting db_prev inside keeps it disjoint from carry (which
    # prices yesterday's standing deviation) and from creation (which prices
    # the last run's deviation from its bench to settle).
    intraday_unfilled, intraday_diag = intr.unfilled_between_snaps(
        day, prev_pos, db_prev, {**prev_mult, **mult})

    # -- assemble ----------------------------------------------------------
    summ = io_live.daily_summary()
    if day not in summ.index:
        return None
    row = summ.loc[day]
    live_gross = float(row["gross"])
    fees = float(row["fees"])
    broker_resid = float(row.get("residual", 0.0) or 0.0)
    live_net = float(row["aggregate"])

    ex = io_live.exec_summary()
    slip_total = float(ex.loc[day, "slip_total"]) if day in ex.index else 0.0
    unbench = float(ex.loc[day, "exec_unbenchmarked"]) if day in ex.index else 0.0
    exec_cost = slip_total + unbench

    pnl_tbl = io_live.daily_pnl(day)
    settle_sum = float(pnl_tbl["total_pnl"].sum()) if pnl_tbl is not None else live_gross
    broker_basis = live_gross - settle_sum

    expected = scale * bt_gross
    resid = (settle_sum - expected + exec_cost - marking - carry - creation
             - intraday_unfilled)

    gross_book = sum(abs(net) * (io_live.lookup(settle, t) or 0.0) * m
                     for t, (net, m) in live_pos.items())

    return {
        "date": normalize_date(day),
        "regime": "forward" if forward else "legacy",
        "scale": scale,
        "bt_gross_fullsize": bt_gross,
        "expected": expected,
        "exec_cost": exec_cost,
        "slip_total": slip_total,
        "exec_unbenchmarked": unbench,
        "marking": marking,
        "basis_eod": basis_now,
        "bookdiff_carry": carry,
        "bookdiff_creation": creation,
        "intraday_unfilled": intraday_unfilled,
        "intraday_runs_used": intraday_diag.get("n_runs_used", 0),
        "intraday_unpriced": intraday_diag.get("n_unpriced", 0),
        "resid": resid,
        "settle_sum": settle_sum,
        "broker_basis": broker_basis,
        "live_gross": live_gross,
        "fees": fees,
        "broker_resid": broker_resid,
        "live_net": live_net,
        "n_live_contracts": sum(1 for v in live_pos.values() if v[0] != 0),
        "n_nobench": n_nobench,
        "live_gross_notional": gross_book,
    }


def weighted_bt(bt: pd.DataFrame, forward_flags: dict[str, bool],
                weights_hist: dict[str, dict[str, float]]
                ) -> tuple[pd.DataFrame, list[str], dict[str, list[str]]]:
    """Per-day WEIGHTED full-size backtest frame for the live window.

    date x strategy-key, value = w_i(day) * bt_i(day).  Legacy days weight
    ks_branch + fund_v3 at 1 and everything else 0 (the account traded those
    two books unweighted).  Forward days use the day's shipped merge weights,
    carrying the latest earlier day's forward when the day's own are not
    shipped yet.

    A strategy with nonzero weight but NO mature backtest row makes the
    day's expected UNKNOWN, not smaller: the day is listed in the returned
    ``incomplete`` map ({day: [missing strategy keys]}) and the bridge holds
    it out until the rows ship (they self-heal on the next payload -- e.g.
    stat_arb's ledger is structurally T-1).  Silently zero-filling those
    rows is how a same-day expected once shrank to the ks sleeve alone.

    Returns (frame, weight problem messages, incomplete).
    """
    from . import io_backtest  # local import: avoid module cycle

    problems: list[str] = []
    incomplete: dict[str, list[str]] = {}
    days = [d for d in bt.index if d >= C.LIVE_START]
    out = pd.DataFrame(0.0, index=days, columns=list(C.STRATEGIES))
    out.index.name = "date"
    for d in days:
        if forward_flags.get(d):
            w, exact = io_backtest.weights_for_day(d, weights_hist)
            if w is None:
                w = C.LEGACY_BRIDGE_WEIGHTS
                problems.append(
                    f"WEIGHTS {d}: forward day with no shipped merge weights "
                    f"at all -- fell back to legacy ks+fund weighting; "
                    f"expected is wrong until weights ship.")
            elif not exact:
                problems.append(
                    f"WEIGHTS {d}: day's own merge weights not shipped yet -- "
                    f"carried forward from an earlier day.")
        else:
            w = C.LEGACY_BRIDGE_WEIGHTS
        missing: list[str] = []
        for key, wi in w.items():
            if not wi:
                continue
            v = bt.at[d, key] if key in bt.columns else float("nan")
            if pd.notna(v):
                out.at[d, key] = wi * float(v)
            else:
                missing.append(key)
        if missing:
            incomplete[d] = sorted(missing)
    return out, problems, incomplete


def bridge_all(bt_weighted: pd.DataFrame, scales: pd.Series,
               forward_flags: dict[str, bool],
               incomplete: dict[str, list[str]] | None = None
               ) -> tuple[pd.DataFrame, list[str], list[str]]:
    """Bridge every live day present in daily_summary from LIVE_START on.

    ``bt_weighted``: date x strategy-key WEIGHTED full-size gross (from
    weighted_bt); a day's combined backtest gross is its row sum.
    ``scales``: date -> scale (from main's scale pass).
    ``forward_flags``: date -> True when the merged forward book executed.
    ``incomplete``: days whose expected is unknown (weighted_bt found a
    nonzero-weight strategy without a mature backtest row) -- those days are
    HELD OUT of the bridge rather than reconciled against a partial
    expected, and re-enter automatically once the rows ship (the whole
    computation reruns from source every day).
    Returns (frame indexed by date, missing-live days, pending days).
    """
    incomplete = incomplete or {}
    summ = io_live.daily_summary()
    live_days = [d for d in summ.index if d >= C.LIVE_START]

    # trading days = union of backtest dates in the live window; live gaps
    # inside it are the missing days the report must carry forever.
    bt_days = [d for d in bt_weighted.index if d >= C.LIVE_START]
    missing = sorted(set(bt_days) - set(live_days))
    # exclude today-like trailing dates with backtest rows but no dailypnl YET
    # (dailypnl runs 16:00 CST): only count a day missing once a LATER live
    # day exists.
    if missing and live_days:
        last_live = max(live_days)
        missing = [d for d in missing if d < last_live]

    rows = []
    pending: list[str] = []
    prev = None
    for day in live_days:
        if day in incomplete:
            # prev still advances: the day's live state exists and the next
            # day's carry/marking legitimately reference it.
            pending.append(day)
            prev = day
            continue
        bt_row = bt_weighted.reindex([day]).fillna(0.0)
        bt_gross = float(bt_row.sum(axis=1).iloc[0]) if len(bt_row) else 0.0
        scale = float(scales.get(day, float("nan")))
        pscale = float(scales.get(prev)) if prev is not None and prev in scales.index else None
        rec = bridge_day(day, prev, scale, bt_gross, prev_scale=pscale,
                         forward=bool(forward_flags.get(day)),
                         prev_forward=bool(forward_flags.get(prev)) if prev else False)
        if rec is not None:
            rows.append(rec)
        prev = day

    df = pd.DataFrame(rows)
    if len(df):
        df = df.set_index("date").sort_index()
    return df, missing, pending
