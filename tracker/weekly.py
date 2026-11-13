"""Weekly summary: a high-level read of the past week for the whole book.

    python -m tracker.weekly [--asof YYYY-MM-DD]

Built ONLY from what the daily run already wrote under data/
(reconciliation.csv, per_strategy_daily.csv, product_daily.csv,
strategy_product_daily.csv).  It recomputes nothing and writes nothing under
data/, so it can run on a Saturday cron without touching the daily run's
state or consuming its once-only alerts.  If the daily run has not reconciled
the last weekday yet, the report says so at the top instead of guessing.

The week is Monday..Sunday around the latest reconciled day <= asof
(default: today UTC).  Every table foots to live gross: strategies plus the
`trading/other` row (fills vs settlement, lot rounding, legacy buckets), and
sectors over products.
"""

from __future__ import annotations

import argparse
import datetime as dt
import shutil
import sys

import pandas as pd

import config as C
from . import io_backtest
from . import stats as S
from .dates import as_date
from .report import _f

PERIODS = ("week", "prior week", "4 weeks", "live-to-date")
TRADING_ROW = "trading/other"


def week_start(day) -> str:
    d = as_date(day)
    return (d - dt.timedelta(days=d.weekday())).isoformat()


def period_days(days: list[str]) -> dict[str, list[str]]:
    """The reconciled days in each reporting period, keyed by PERIODS."""
    days = sorted(days)
    weeks = sorted({week_start(d) for d in days})
    by_week = {w: [d for d in days if week_start(d) == w] for w in weeks}
    return {
        "week": by_week[weeks[-1]],
        "prior week": by_week[weeks[-2]] if len(weeks) > 1 else [],
        "4 weeks": [d for w in weeks[-4:] for d in by_week[w]],
        "live-to-date": days,
    }


def period_sums(wide: pd.DataFrame, periods: dict[str, list[str]]) -> pd.DataFrame:
    """day x key frame -> key x period sums (a day absent from `wide` adds 0)."""
    return pd.DataFrame({p: wide.reindex(ds).sum() for p, ds in periods.items()},
                        columns=list(periods)).fillna(0.0)


def summarize(recon: pd.DataFrame, psd: pd.DataFrame, prod: pd.DataFrame,
              sp: pd.DataFrame, asof: str) -> dict:
    """Pure: the daily outputs as of `asof` -> the weekly tables.

    recon is indexed by date; psd / prod / sp are the long CSVs as written.
    """
    recon = recon[recon.index <= asof]
    per = period_days(list(recon.index))
    week = per["week"]

    head = recon[["live_gross", "expected", "exec_cost", "fees", "live_net"]].copy()
    head.insert(2, "gap", head["live_gross"] - head["expected"])
    headline = period_sums(head, per)

    att = psd.pivot_table(index="day", columns="strategy", values="attributed",
                          aggfunc="sum").reindex(columns=list(C.STRATEGIES)).fillna(0.0)
    att[TRADING_ROW] = recon["live_gross"].reindex(att.index) - att.sum(axis=1)
    strat = period_sums(att, per)
    # expected/gap as the daily report has them: a pending sleeve-day (no
    # backtest row yet) is blank there and adds nothing here
    for col, name in (("expected", "week expected"), ("gap", "week gap")):
        x = psd[psd["day"].isin(week)].groupby("strategy")[col].sum()
        strat[name] = x.reindex(strat.index).fillna(0.0)
    strat.loc[TRADING_ROW, ["week expected", "week gap"]] = [0.0, strat.loc[TRADING_ROW, "week"]]

    prod = prod.assign(sector=prod["product"].map(C.PRODUCT_SECTOR).fillna("other"))
    by_prod = prod.pivot_table(index="day", columns="product", values="total_pnl",
                               aggfunc="sum")
    by_sec = prod.pivot_table(index="day", columns="sector", values="total_pnl",
                              aggfunc="sum")
    products = period_sums(by_prod, per)
    products["sector"] = products.index.map(C.PRODUCT_SECTOR).fillna("other")
    sectors = period_sums(by_sec, per)

    spw = sp[sp["day"].isin(week)].assign(
        sector=lambda x: x["product"].map(C.PRODUCT_SECTOR).fillna("other"))
    cross = spw.pivot_table(index="sector", columns="strategy", values="pnl",
                            aggfunc="sum").fillna(0.0)
    cells = spw.groupby(["product", "strategy"])["pnl"].sum()

    weekdays = [(as_date(week[0]) - dt.timedelta(days=as_date(week[0]).weekday())
                 + dt.timedelta(days=i)).isoformat() for i in range(5)]
    last = recon.iloc[-1]
    return {
        "periods": per, "headline": headline, "strategies": strat,
        "sectors": sectors, "products": products, "cross": cross, "cells": cells,
        "no_row": [d for d in weekdays if d not in week and d <= asof],
        "provisional": recon.index[-1] if not bool(last.get("pnl_final", True)) else None,
        "pending": [d for d in week if isinstance(recon.loc[d].get("bt_pending"), str)
                    and recon.loc[d]["bt_pending"]],
        "unmapped": sorted(products.index[products["sector"] == "other"]),
        "ltd": S.perf(recon["live_net"]),
        "dd_now": float((recon["live_net"].cumsum()
                         - recon["live_net"].cumsum().cummax()).iloc[-1]),
    }


def _driver(cells: pd.Series, product: str, sign: float) -> str:
    """The strategy that contributed most to a product's week, in its direction."""
    if product not in cells.index.get_level_values(0):
        return "-"
    c = cells.loc[product] * sign
    return f"{c.idxmax()} ({_f(c.max() * sign)})" if c.max() > 0 else "-"


def _table(a, df: pd.DataFrame, cols: list[str], label: str, extra=None) -> None:
    extra = extra or {}
    a(f"| {label} | " + " | ".join(cols + list(extra)) + " |")
    a("|---|" + "---|" * (len(cols) + len(extra)))
    for k, r in df.iterrows():
        a(f"| {k} | " + " | ".join(_f(r[c]) for c in cols)
          + "".join(f" | {fn(k, r)}" for fn in extra.values()) + " |")


def render(s: dict, weights: dict[str, float] | None, n_products: int = 5) -> str:
    per, hl, st, sec, pr = (s["periods"], s["headline"], s["strategies"],
                            s["sectors"], s["products"])
    week = per["week"]
    weights = weights or {}
    lines: list[str] = []
    a = lines.append
    a(f"# Weekly performance - week of {week_start(week[0])}   "
      f"({len(week)} trading day(s), {week[0]} .. {week[-1]})")
    a("")

    notes = []
    if s["no_row"]:
        notes.append(f"no reconciled day for {', '.join(s['no_row'])} "
                     "(holiday, or the daily run has not reconciled it yet)")
    if s["provisional"]:
        notes.append(f"{s['provisional']} is PROVISIONAL (16:00 close mark; "
                     "re-marked to settlement by the next daily run)")
    if s["pending"]:
        notes.append(f"backtest row pending on {', '.join(s['pending'])}: "
                     "expected excludes that sleeve")
    if s["unmapped"]:
        notes.append(f"products with no sector in config.SECTORS: "
                     f"{', '.join(s['unmapped'])}")
    for n in notes:
        a(f"- NOTE: {n}")
    if notes:
        a("")

    # ------------------------------------------------------------ summary
    w = hl["week"]
    active = st.drop(index=TRADING_ROW)
    active = active[(active["4 weeks"] != 0) | (active["week"] != 0)]
    gap = active["week gap"].dropna()
    a("## Summary")
    a(f"- Book: live net {_f(w['live_net'])} (gross {_f(w['live_gross'])} vs "
      f"backtest expected {_f(w['expected'])}, gap {_f(w['gap'])}); "
      f"prior week net {_f(hl.loc['live_net', 'prior week'])}.")
    if len(active):
        best, worst = active["week"].idxmax(), active["week"].idxmin()
        a(f"- Strategies: best {best} {_f(active.loc[best, 'week'])}, "
          f"worst {worst} {_f(active.loc[worst, 'week'])}.")
    if len(gap):
        a(f"- Vs backtest: furthest below {gap.idxmin()} {_f(gap.min())}, "
          f"furthest above {gap.idxmax()} {_f(gap.max())}.")
    sw = sec["week"].sort_values()
    a(f"- Sectors: best {sw.index[-1]} {_f(sw.iloc[-1])}, "
      f"worst {sw.index[0]} {_f(sw.iloc[0])}.")
    pw = pr["week"].sort_values()
    a("- Products: best " + ", ".join(f"{p} {_f(v)}" for p, v in pw.tail(3)[::-1].items())
      + "; worst " + ", ".join(f"{p} {_f(v)}" for p, v in pw.head(3).items()) + ".")
    ltd = s["ltd"]
    sh = f"{ltd['sharpe']:.2f}" if ltd.get("sharpe") is not None else "-"
    a(f"- Live-to-date: net {_f(ltd['total'])} over {ltd['n_days']} days, "
      f"Sharpe {sh}, max DD {_f(ltd.get('mdd'))}, drawdown now {_f(s['dd_now'])}.")
    a("")

    # ------------------------------------------------------------ headline
    a("## Book (CNY)")
    _table(a, hl, list(PERIODS), "")
    a("gap = live gross - expected (scale x weighted as-shipped backtest); "
      "exec_cost and fees are costs (+ = paid).")
    a("")

    # ---------------------------------------------------------- strategies
    a("## Strategies (live attributed gross, CNY, worst week first)")
    show = st[(st[list(PERIODS)] != 0).any(axis=1)]
    order = show.drop(index=TRADING_ROW, errors="ignore").sort_values("week").index
    show = show.loc[list(order) + [TRADING_ROW]]
    cols = ["week", "week expected", "week gap", "prior week", "4 weeks", "live-to-date"]
    _table(a, show, cols, "strategy",
           {"weight": lambda k, r: (f"{weights[k]:g}" if k in weights else "-")})
    tot = show[cols].sum()
    tot[["week", "week expected", "week gap"]] = [hl.loc[k, "week"] for k in
                                                  ("live_gross", "expected", "gap")]
    a("| total | " + " | ".join(_f(tot[c]) for c in cols) + " | |")
    a("holdings attribution from the daily report: previous-day weighted book x "
      f"scale x settlement move; `{TRADING_ROW}` is the rest of live gross (fills "
      "vs settlement on rebalances, lot rounding) so the column foots; its "
      "expected is 0, so its gap is its P&L.  A sleeve-day whose backtest row "
      "is pending is left out of expected and gap (as in the daily report).")
    a("")

    # ------------------------------------------------------------- sectors
    a("## Sectors (live gross, CNY, worst week first)")
    sec_s = sec.sort_values("week")
    _table(a, sec_s, list(PERIODS), "sector", {
        "best product (week)": lambda k, r: _best(pr, k, +1),
        "worst product (week)": lambda k, r: _best(pr, k, -1)})
    a("| total | " + " | ".join(_f(sec_s[c].sum()) for c in PERIODS) + " | | |")
    a("")

    cross = s["cross"]
    if len(cross):
        cross = cross.reindex(sec_s.index).fillna(0.0)
        cols = [c for c in list(C.STRATEGIES) + [TRADING_ROW.split("/")[0], "neither",
                                                 "shared"]
                if c in cross.columns and cross[c].abs().sum() > 0]
        a("### Sector x strategy, this week (attributed gross, CNY)")
        _table(a, cross, cols, "sector")
        a("")

    # ------------------------------------------------------------ products
    a(f"## Products: {n_products} worst and {n_products} best this week (live gross, CNY)")
    pick = pd.concat([pw.head(n_products), pw.tail(n_products)[::-1]])
    pick = pick[~pick.index.duplicated()]
    _table(a, pr.loc[pick.index], list(PERIODS), "product", {
        "sector": lambda k, r: r["sector"],
        "main driver (week)": lambda k, r: _driver(s["cells"], k,
                                                   1.0 if r["week"] >= 0 else -1.0)})
    a("main driver = the strategy with the largest contribution in the "
      "product's direction this week. Daily detail: reports/daily/.")
    a("")
    return "\n".join(lines) + "\n"


def _best(pr: pd.DataFrame, sector: str, sign: int) -> str:
    x = pr.loc[pr["sector"] == sector, "week"]
    if not len(x):
        return "-"
    k = x.idxmax() if sign > 0 else x.idxmin()
    return f"{k} {_f(x[k])}"


def load() -> tuple[pd.DataFrame, pd.DataFrame, pd.DataFrame, pd.DataFrame]:
    recon = pd.read_csv(C.RECON_CSV, index_col="date")
    recon.index = recon.index.astype(str)
    psd = pd.read_csv(C.DATA / "per_strategy_daily.csv", dtype={"day": str})
    prod = pd.read_csv(C.DATA / "product_daily.csv", dtype={"day": str})
    sp = pd.read_csv(C.DATA / "strategy_product_daily.csv", dtype={"day": str})
    return recon, psd, prod, sp


def main(argv=None) -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--asof", default=None, help="default: today UTC")
    args = ap.parse_args(argv)
    asof = args.asof or dt.datetime.now(dt.timezone.utc).strftime("%Y-%m-%d")

    s = summarize(*load(), asof)
    week = s["periods"]["week"]
    wh = io_backtest.weights_history()
    weights, _ = io_backtest.weights_for_day(week[-1], wh)
    text = render(s, weights)

    friday = (as_date(week_start(week[0])) + dt.timedelta(days=4)).isoformat()
    path = C.WEEKLY_DIR / f"{friday}.md"
    path.write_text(text, encoding="ascii")
    shutil.copyfile(path, C.REPORT_DIR / "latest_weekly.md")
    print(f"weekly report: reports/weekly/{friday}.md (+ latest_weekly.md)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
