"""Daily report: one markdown, one png. Brief enough for one read. ASCII only."""

from __future__ import annotations

import shutil

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
import pandas as pd

import config as C
from . import stats as S


def _f(x, dp=0):
    if x is None or pd.isna(x):
        return "-"
    return f"{x:+,.{dp}f}"


def _stat_row(name: str, p: dict) -> str:
    tag = " (small sample)" if p.get("small_sample") else ""
    sh = f"{p['sharpe']:.2f}" if p.get("sharpe") is not None else "-"
    mdd = _f(p.get("mdd"))
    hit = f"{p['hit'] * 100:.0f}%" if p.get("hit") is not None else "-"
    return (f"| {name} | {p['n_days']} | {_f(p.get('total'))} | {sh} | "
            f"{mdd} | {hit} |{tag}")


def write_report(day: str, recon: pd.DataFrame, missing: list[str],
                 missing_bucket: float, scales: pd.DataFrame,
                 attribution: pd.DataFrame, bt_series: dict[str, pd.DataFrame],
                 live_flags: dict[str, bool], alerts: list[str],
                 bt_bridge: pd.DataFrame | None = None,
                 pin_info: dict | None = None,
                 weights_hist: dict[str, dict[str, float]] | None = None,
                 forward_flags: dict[str, bool] | None = None) -> None:
    weights_hist = weights_hist or {}
    forward_flags = forward_flags or {}
    md_path = C.DAILY_DIR / f"{day}.md"
    png_path = C.DAILY_DIR / f"{day}.png"

    live = recon.loc[recon.index <= day] if len(recon) else recon
    last = live.iloc[-1] if len(live) else None
    lines: list[str] = []
    a = lines.append

    reconciled_through = live.index[-1] if len(live) else "-"
    a(f"# Performance tracker - {day}   (reconciled through {reconciled_through})")
    a("")
    a("## ALERTS")
    if alerts:
        for al in alerts:
            a(f"- {al}")
    else:
        a("- none")
    a("")

    if last is not None:
        d = live.index[-1]
        regime = last.get("regime", "legacy") if hasattr(last, "get") else "legacy"
        a(f"## Latest reconciled day ({d}, {regime} regime)")
        a(f"live gross {_f(last['live_gross'])} | expected "
          f"({last['scale']:g} x bt {_f(last['bt_gross_fullsize'])}) = "
          f"{_f(last['expected'])} | gap {_f(last['live_gross'] - last['expected'])}")
        a(f"  exec_cost {_f(last['exec_cost'])} (slip {_f(last['slip_total'])}, "
          f"unbench {_f(last['exec_unbenchmarked'])}) | marking {_f(last['marking'])} | "
          f"bookdiff {_f(last['bookdiff_carry'] + last['bookdiff_creation'])} "
          f"(carry {_f(last['bookdiff_carry'])}, new {_f(last['bookdiff_creation'])}) | "
          f"residual {_f(last['resid'])} | broker basis {_f(last['broker_basis'])}")
        a(f"  fees {_f(last['fees'])} | broker residual {_f(last['broker_resid'])} "
          f"-> live net {_f(last['live_net'])}")
        a("")

    if len(live):
        cum = live[["expected", "exec_cost", "marking", "bookdiff_carry",
                    "bookdiff_creation", "resid", "broker_basis", "live_gross",
                    "fees", "broker_resid", "live_net"]].sum()
        a(f"## Cumulative bridge (live since {C.LIVE_START}, "
          f"{len(live)} reconciled days)")
        a("| expected | -exec | +marking | +bookdiff | +resid | +broker basis "
          "| = live gross | -fees | +broker_resid | = live net |")
        a("|---|---|---|---|---|---|---|---|---|---|")
        a(f"| {_f(cum['expected'])} | {_f(-cum['exec_cost'])} | "
          f"{_f(cum['marking'])} | "
          f"{_f(cum['bookdiff_carry'] + cum['bookdiff_creation'])} | "
          f"{_f(cum['resid'])} | {_f(cum['broker_basis'])} | "
          f"{_f(cum['live_gross'])} | {_f(-cum['fees'])} | "
          f"{_f(cum['broker_resid'])} | {_f(cum['live_net'])} |")
        if missing:
            a(f"missing live days excluded: {', '.join(missing)} "
              f"(expected {_f(missing_bucket)} held in bucket)")
        a("")

        a("## Stats (daily CNY pnl)")
        a("| window | days | total | sharpe | mdd | hit |")
        a("|---|---|---|---|---|---|")
        for name, p in S.windows(live["live_net"]).items():
            a(_stat_row(f"live net {name}", p))
        for name, p in S.windows(live["expected"]).items():
            a(_stat_row(f"bt scaled {name}", p))
        a("")

    a("## Per strategy")
    a("| strategy | live? | bt 2026 pnl (full) | bt scaled+weighted (live window) | "
      "live attributed | note |")
    a("|---|---|---|---|---|---|")
    cur_w = weights_hist[max(weights_hist)] if weights_hist else {}
    forward_active = (any(bool(forward_flags.get(d)) for d in live.index)
                      if len(live) else False)
    for key, (label, source) in C.STRATEGIES.items():
        df = bt_series.get(key, pd.DataFrame())
        bt2026 = _f(df["gross_pnl"].sum()) if len(df) else "-"
        is_live = live_flags.get(key, False)
        scaled = attributed = "-"
        note = ""
        if len(live) and bt_bridge is not None and key in bt_bridge.columns:
            # bt_bridge holds per-day WEIGHTED full-size values, so this
            # column foots against the bridge's expected by construction
            aligned = bt_bridge[key].reindex(live.index).fillna(0.0)
            if aligned.abs().sum() > 0:
                scaled = _f((aligned * live["scale"]).sum())
        if len(attribution) and key in attribution.columns:
            s = attribution[key].sum()
            if is_live or s:
                attributed = _f(s)
        if forward_active and key in cur_w:
            note = f"forward w={cur_w[key]:g}" + ("" if cur_w[key] else " (parked)")
        elif is_live:
            note = "legacy per-source"
        elif source:
            note = "source configured, not executing"
        else:
            note = "not shipped to execution"
        a(f"| {label} | {'yes' if is_live else 'no'} | {bt2026} | {scaled} | "
          f"{attributed} | {note} |")
    if len(attribution):
        a(f"| shared bucket | - | - | - | "
          f"{_f(attribution['shared'].sum())} | legacy multi-holder / forward offsetting |")
        a(f"| neither bucket (no target) | - | - | - | "
          f"{_f(attribution['neither'].sum())} | inherited/manual/rounding |")
        a("forward-day attribution is pro-rated by weighted full-size lots; "
          "legacy days remain exclusive-holder.")
    a("")

    a("## Data health")
    if len(scales):
        cur = scales.dropna(subset=["scale"]).iloc[-1] if len(
            scales.dropna(subset=["scale"])) else None
        if cur is not None:
            since = scales[scales["scale"] == cur["scale"]]["date"].min()
            a(f"scale: {cur['scale']:g} (since {since})")
    if len(live) and "regime" in live.columns:
        fwd = live[live["regime"] == "forward"]
        if len(fwd):
            a(f"regime: forward (merged weighted book) since {fwd.index[0]}; "
              f"{len(fwd)} forward day(s), {len(live) - len(fwd)} legacy day(s)")
    if weights_hist:
        wd = max(weights_hist)
        w = weights_hist[wd]
        a("merge weights (" + wd + "): "
          + ", ".join(f"{k} {w.get(k, 0):g}" for k in C.STRATEGIES))
    if pin_info:
        div = ", ".join(f"{s}: {n}" for s, n in pin_info.get("divergent", {}).items())
        a(f"as-shipped pins: {pin_info.get('n_days', 0)} live day(s) pinned"
          + (f"; current series diverges on {div}" if div else ""))
    from . import io_live as _il
    mt = _il.inbox_ks_summary_mtime()
    if mt:
        import datetime as dt
        a(f"inbox ks summary mtime: "
          f"{dt.datetime.fromtimestamp(mt, dt.timezone.utc):%Y-%m-%d %H:%M} UTC")
    a("")

    md_path.write_text("\n".join(lines), encoding="ascii", errors="replace")
    shutil.copyfile(md_path, C.REPORT_DIR / "latest.md")

    _plot(png_path, live, bt_series, cur_w)
    if png_path.exists():
        shutil.copyfile(png_path, C.REPORT_DIR / "latest.png")


def _plot(path, live: pd.DataFrame, bt_series: dict[str, pd.DataFrame],
          cur_w: dict[str, float] | None = None) -> None:
    if not len(live):
        return
    fig, axes = plt.subplots(3, 1, figsize=(10, 10),
                             gridspec_kw={"height_ratios": [2, 1.3, 1.3]})
    x = pd.to_datetime(live.index)

    ax = axes[0]
    ax.plot(x, live["live_gross"].cumsum(), lw=1.8, color="#2b6cb0",
            label="live gross (cum)")
    ax.plot(x, live["expected"].cumsum(), lw=1.6, color="#4a5568", ls="--",
            label="scaled backtest (cum)")
    ax.fill_between(x, live["expected"].cumsum(), live["live_gross"].cumsum(),
                    color="#c05621", alpha=0.18, label="gap")
    ax.plot(x, live["live_net"].cumsum(), lw=1.3, color="#c05621",
            label="live net (cum)")
    ax.axhline(0, color="black", lw=0.7)
    ax.set_ylabel("CNY (cum)")
    ax.set_title("Live vs scaled backtest -- cumulative since live start")
    ax.legend(fontsize=8, frameon=False)
    ax.grid(alpha=0.25)

    ax = axes[1]
    # .values everywhere: the live frame is string-date indexed, and pandas
    # would silently reindex (to all-NaN) against the datetime x otherwise.
    comp = {
        "-exec_cost": (-live["exec_cost"].cumsum()).values,
        "+marking": live["marking"].cumsum().values,
        "+bookdiff": (live["bookdiff_carry"] + live["bookdiff_creation"]).cumsum().values,
        "+resid": live["resid"].cumsum().values,
        "+broker_basis": live["broker_basis"].cumsum().values,
        "-fees": (-live["fees"].cumsum()).values,
    }
    for (col, vals), colr in zip(comp.items(),
                                 ["#a33a2e", "#2f855a", "#805ad5", "#9a6b1e",
                                  "#2b6cb0", "#4a5568"]):
        ax.plot(x, vals, lw=1.4, label=col, color=colr)
    ax.axhline(0, color="black", lw=0.7)
    ax.set_ylabel("CNY (cum)")
    ax.set_title("Gap decomposition -- cumulative components")
    ax.legend(fontsize=8, frameon=False, ncol=3)
    ax.grid(alpha=0.25)

    ax = axes[2]
    total = wtotal = None
    for key, df in bt_series.items():
        if not len(df):
            continue
        s = df["gross_pnl"]
        total = s if total is None else total.add(s, fill_value=0.0)
        w = (cur_w or {}).get(key, 0.0)
        if w:
            ws = s * w
            wtotal = ws if wtotal is None else wtotal.add(ws, fill_value=0.0)
    if total is not None and len(total):
        xt = pd.to_datetime(total.index)
        ax.plot(xt, total.cumsum(), lw=1.4, color="#4a5568",
                label="all 7 backtests, full size (cum, 2026)")
        if wtotal is not None:
            xw = pd.to_datetime(wtotal.index)
            ax.plot(xw, wtotal.cumsum(), lw=1.4, color="#2f855a",
                    label="forward-weighted (current w), full size")
        ax.axvline(pd.Timestamp(C.LIVE_START), color="#c05621", ls=":",
                   lw=1.2, label="live start")
    ax.axhline(0, color="black", lw=0.7)
    ax.set_ylabel("CNY (cum)")
    ax.set_title("Full-size backtest context (2026 OOS)")
    ax.legend(fontsize=8, frameon=False)
    ax.grid(alpha=0.25)

    for ax in axes:
        for lab in ax.get_xticklabels():
            lab.set_rotation(20)
            lab.set_ha("right")
    fig.tight_layout()
    fig.savefig(path, dpi=130)
    plt.close(fig)
