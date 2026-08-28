"""Failure-mode detection.  Every alert is a plain sentence; the report puts
them first, always.  Sticky facts (missing live days, fingerprints, scale
history) live in data/state.json."""

from __future__ import annotations

import datetime as dt

import pandas as pd

import config as C
from . import io_backtest, io_live
from .dates import as_date, business_days_between, is_weekday, normalize_date


def check_all(recon: pd.DataFrame, missing_days: list[str], scales: pd.DataFrame,
              state: dict, bt_series: dict[str, pd.DataFrame],
              today: str) -> list[str]:
    alerts: list[str] = []

    # -- missing live days (sticky) --------------------------------------
    known = set(state.get("missing_live_days", []))
    for d in missing_days:
        known.add(normalize_date(d))
    state["missing_live_days"] = sorted(known)
    for d in state["missing_live_days"]:
        alerts.append(f"MISSING LIVE DAY {d}: trading day with a backtest row "
                      f"but no daily_pnl/state file; excluded from the bridge, "
                      f"expected pnl held in the missing-day bucket.")

    # -- inbox ks summary freshness --------------------------------------
    mt = io_live.inbox_ks_summary_mtime()
    if mt is None:
        alerts.append("INBOX: ks/meta/summary.csv is MISSING.")
    else:
        age_h = (dt.datetime.now(dt.timezone.utc)
                 - dt.datetime.fromtimestamp(mt, dt.timezone.utc)).total_seconds() / 3600
        if is_weekday(today) and age_h > 30:
            alerts.append(f"INBOX: ks/meta/summary.csv is stale ({age_h:.0f}h old).")

    # -- scale changes / null-scale days ---------------------------------
    for _, row in scales.iterrows():
        for f in row["flags"]:
            if f == "scale_carried_forward":
                alerts.append(f"SCALE {row['date']}: no usable run record; "
                              f"previous scale carried forward.")
            elif f == "all_runs_blocked":
                alerts.append(f"SCALE {row['date']}: every run was BLOCKED -- "
                              f"nothing executed that day.")
            elif f.startswith("multiple_scales"):
                alerts.append(f"SCALE {row['date']}: {f} -- intraday scale "
                              f"change; split lands in residual.")
    ser = scales.dropna(subset=["scale"])
    changes = ser[ser["scale"].ne(ser["scale"].shift())].iloc[1:]
    for _, row in changes.iterrows():
        alerts.append(f"SCALE CHANGE on {row['date']}: now {row['scale']:g}.")

    # -- backtest history revisions --------------------------------------
    fp_state = state.setdefault("backtest_fingerprints", {})
    for key, df in bt_series.items():
        fp = io_backtest.series_fingerprint(df)
        old = fp_state.get(key)
        if old and old.get("sha256") and fp["sha256"] and old["sha256"] != fp["sha256"]:
            alerts.append(f"BACKTEST REVISED: {key} history (rows before the "
                          f"trailing 5 days) changed since last run -- "
                          f"regeneration upstream. Fingerprint re-baselined.")
        fp_state[key] = fp

    # -- exec quality -----------------------------------------------------
    ex = io_live.exec_summary()
    if len(ex):
        last = ex.iloc[-1]
        if float(last.get("unbenchmarked_legs", 0) or 0) > 0:
            alerts.append(f"SLIPPAGE {ex.index[-1]}: "
                          f"{int(last['unbenchmarked_legs'])} unbenchmarked "
                          f"leg(s), {float(last['exec_unbenchmarked']):+.0f} CNY "
                          f"exec cost without a shipped decision price.")

    # -- broker reconciliation --------------------------------------------
    summ = io_live.daily_summary()
    if len(summ):
        last_day = summ.index[-1]
        dvb = summ.iloc[-1].get("diff_vs_broker")
        if pd.notna(dvb) and abs(float(dvb)) > 0.01:
            alerts.append(f"BROKER DIFF {last_day}: daily_summary diff_vs_broker "
                          f"= {float(dvb):+.2f} CNY (should be 0).")

    # -- residual blowouts -------------------------------------------------
    # The day-window mismatch (see reconcile.py) makes daily residuals noisy
    # by construction, so a residual only alerts when it breaks out of its
    # own trailing distribution -- a CHANGE in attribution quality.
    if len(recon) >= 3:
        med = recon["resid"].abs().rolling(10, min_periods=3).median().shift(1)
        for d, row in recon.iterrows():
            base = med.get(d)
            if base is None or pd.isna(base):
                continue
            thresh = max(C.RESID_ABS_FLOOR, 3.0 * float(base))
            if abs(row["resid"]) > thresh:
                alerts.append(f"RESIDUAL {d}: {row['resid']:+.0f} CNY vs trailing "
                              f"median |resid| {base:.0f} -- attribution quality "
                              f"changed that day.")

    # -- ship staleness ----------------------------------------------------
    newest = None
    for key, df in bt_series.items():
        if key == "ks_branch":
            continue
        if len(df) and "shipped_at" in df.columns:
            m = pd.to_datetime(df["shipped_at"], errors="coerce").max()
            if pd.notna(m):
                newest = m if newest is None or m > newest else newest
    if newest is None:
        alerts.append("SHIP: no shipped backtest payload found yet -- run "
                      "scripts/ship_backtest_pnl from the local machine.")
    elif business_days_between(newest.date(), as_date(today)) > C.SHIP_STALE_BDAYS:
        alerts.append(f"SHIP: newest backtest payload is from "
                      f"{newest.date()} (> {C.SHIP_STALE_BDAYS} business days old).")

    # -- ks cross-check ----------------------------------------------------
    ks_ship = bt_series.get("ks_branch", pd.DataFrame())
    ks_inbox = io_live.inbox_ks_summary()
    if len(ks_ship) and len(ks_inbox):
        j = ks_ship.join(ks_inbox[["gross_pnl_shipped"]], how="inner")
        if len(j):
            diff = (j["gross_pnl"] - j["gross_pnl_shipped"]).abs()
            bad = diff[diff > 1.0]
            if len(bad):
                alerts.append(f"KS CROSS-CHECK: shipped ks_branch series differs "
                              f"from inbox summary on {len(bad)} date(s), max "
                              f"|diff| {bad.max():.0f} CNY (first: {bad.index[0]}).")
    return alerts
