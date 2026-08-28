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
    bt = io_backtest.bt_gross_for_bridge()

    scales_df = compute_scales()
    scales = scales_df.set_index("date")["scale"] if len(scales_df) else pd.Series(dtype=float)

    recon, missing = reconcile.bridge_all(bt, scales)
    if len(recon):
        recon.to_csv(C.RECON_CSV)
        print(f"reconciled {len(recon)} day(s): {recon.index[0]} -> {recon.index[-1]}")
    else:
        print("no reconcilable live days found")

    missing_bucket = 0.0
    for d in missing:
        s = scales.get(d)
        if s is not None and not pd.isna(s) and d in bt.index:
            missing_bucket += float(s) * float(bt.loc[d].fillna(0.0).sum())

    attribution = AT.attribute_all(list(recon.index)) if len(recon) else pd.DataFrame()
    flags = AT.live_flags(list(recon.index)) if len(recon) else {
        k: False for k in C.STRATEGIES}

    alert_list = problems + A.check_all(recon, missing, scales_df, state,
                                        bt_series, today)

    report.write_report(today, recon, state.get("missing_live_days", []),
                        missing_bucket, scales_df, attribution, bt_series,
                        flags, alert_list)
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
