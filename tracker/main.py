"""Orchestrator: full recompute from sources every run (idempotent).

    python -m tracker.main [--date YYYY-MM-DD]

Late-arriving data self-heals on the next run; a same-day rerun overwrites the
same report.  State (fingerprints, scale history, missing days) updates only
after the report is written.
"""

from __future__ import annotations

import argparse
import datetime as dt
import sys

import pandas as pd

import config as C
from . import alerts as A
from . import attribution as AT
from . import ingest, io_backtest, io_live, reconcile, report


def compute_scales() -> pd.DataFrame:
    """Per live day: authoritative execution scale + flags."""
    summ = io_live.daily_summary()
    days = [d for d in summ.index if d >= C.LIVE_START]
    # include detail-jsonl days beyond dailypnl (e.g. today pre-16:00 CST)
    extra = sorted({p.stem for p in C.DETAIL_DIR.glob("*.jsonl")})
    from .dates import normalize_date
    for e in extra:
        try:
            iso = normalize_date(e)
        except ValueError:
            continue
        if iso >= C.LIVE_START and iso not in days:
            days.append(iso)
    days = sorted(days)

    rows, prev = [], None
    for d in days:
        scale, flags = io_live.scale_for_day(d, prev)
        rows.append({"date": d, "scale": scale, "flags": flags})
        prev = scale if scale is not None else prev
    return pd.DataFrame(rows)


def main(argv=None) -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--date", default=None, help="report date (default: today UTC)")
    args = ap.parse_args(argv)
    today = args.date or dt.datetime.now(dt.timezone.utc).strftime("%Y-%m-%d")

    promoted, problems = ingest.promote_incoming()
    if promoted:
        print(f"ingest: promoted {sorted(set(promoted))}")
    for p in problems:
        print(f"ingest problem: {p}")

    state = io_backtest.load_state()
    bt_series = io_backtest.all_series()
    bt_raw = io_backtest.bt_gross_for_bridge()
    # divergence vs EXISTING pins first, then pin newly-matured days + overlay
    pin_div = io_backtest.pin_divergence(bt_raw, state)
    bt, n_new_pins = io_backtest.overlay_and_update_pins(bt_raw.copy(), state)
    if n_new_pins:
        print(f"pinned {n_new_pins} new as-shipped backtest value(s)")

    scales_df = compute_scales()
    scales = scales_df.set_index("date")["scale"] if len(scales_df) else pd.Series(dtype=float)

    # -- regime per day: forward once the merged book feeds pyexec ---------
    scale_days = set(scales_df["date"]) if len(scales_df) else set()
    days_needed = sorted({d for d in bt.index if d >= C.LIVE_START} | scale_days)
    raw_fwd = {d: io_live.is_forward_day(d) for d in days_needed}
    fwd_dates = sorted(d for d, v in raw_fwd.items() if v)
    first_fwd = fwd_dates[0] if fwd_dates else None
    # a day with no run records at all (holiday gap, lost file) keeps the
    # standing regime rather than flipping back to legacy
    forward_flags = {
        d: raw_fwd[d] or (first_fwd is not None and d >= first_fwd
                          and not io_live.run_records(d))
        for d in days_needed}
    if first_fwd:
        print(f"forward regime since {first_fwd} "
              f"({len(fwd_dates)} day(s) with forward runs)")

    weights_hist = io_backtest.weights_history()
    bt_weighted, weight_problems = reconcile.weighted_bt(bt, forward_flags,
                                                         weights_hist)

    recon, missing = reconcile.bridge_all(bt_weighted, scales, forward_flags)
    if len(recon):
        recon.to_csv(C.RECON_CSV)
        print(f"reconciled {len(recon)} day(s): {recon.index[0]} -> {recon.index[-1]}")
    else:
        print("no reconcilable live days found")

    missing_bucket = 0.0
    for d in missing:
        s = scales.get(d)
        if s is not None and not pd.isna(s) and d in bt_weighted.index:
            missing_bucket += float(s) * float(bt_weighted.loc[d].fillna(0.0).sum())

    attribution = (AT.attribute_all(list(recon.index), forward_flags, weights_hist)
                   if len(recon) else pd.DataFrame())
    flags = (AT.live_flags(list(recon.index), forward_flags, weights_hist)
             if len(recon) else {k: False for k in C.STRATEGIES})

    alert_list = problems + weight_problems + A.check_all(
        recon, missing, scales_df, state, bt_series, today, pin_div=pin_div,
        forward_flags=forward_flags, weights_hist=weights_hist)

    pin_info = {
        "n_days": len(state.get("bt_pinned", {})),
        "divergent": {s: len(e["dates"]) for s, e in pin_div.items()},
    }
    report.write_report(today, recon, state.get("missing_live_days", []),
                        missing_bucket, scales_df, attribution, bt_series,
                        flags, alert_list, bt_bridge=bt_weighted,
                        pin_info=pin_info, weights_hist=weights_hist,
                        forward_flags=forward_flags)
    print(f"report: reports/daily/{today}.md (+ latest.md/png)")

    state["scale_history"] = [
        {"date": r["date"], "scale": r["scale"], "flags": r["flags"]}
        for _, r in scales_df.iterrows()]
    state["last_run"] = {
        "at": dt.datetime.now(dt.timezone.utc).isoformat(timespec="seconds"),
        "reconciled_through": str(recon.index[-1]) if len(recon) else None,
        "n_alerts": len(alert_list),
    }
    io_backtest.save_state(state)
    return 0


if __name__ == "__main__":
    sys.exit(main())
