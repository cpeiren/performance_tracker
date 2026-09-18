"""Readers for the live side: pyexec's P&L, slippage, fills and books.

Everything here is a plain read of cnexec DATA files (schemas verified
2026-08-28).  No cnexec code is imported.  All dates in and out are ISO
'YYYY-MM-DD'; every file with a compact key is converted at the boundary.
"""

from __future__ import annotations

import json
from pathlib import Path

import pandas as pd

import config as C
from . import names
from .dates import compact, normalize_date



def lookup(d: dict, ticker: str, default=None):
    """Dict lookup tolerant of the two CZCE year-digit forms."""
    if ticker in d:
        return d[ticker]
    alt = names.alt_ticker(ticker)
    if alt is not None and alt in d:
        return d[alt]
    return default


# --------------------------------------------------------------------------
# Account-level daily P&L
# --------------------------------------------------------------------------

def daily_summary() -> pd.DataFrame:
    """pnl/daily_summary.csv indexed by ISO date. Empty frame if absent."""
    p = C.PNL_DIR / "daily_summary.csv"
    if not p.exists():
        return pd.DataFrame()
    df = pd.read_csv(p)
    df["date"] = df["date"].map(normalize_date)
    return df.drop_duplicates("date", keep="last").set_index("date").sort_index()


def is_final(row) -> bool:
    """A daily_summary row whose settle-to-settle columns are filled (F134)."""
    return (str(row.get("final_status", "") or "").startswith("final")
            and not pd.isna(row.get("final_pnl")))


def account_pnl(row) -> dict:
    """Account-level gross / fees / net for one daily_summary row.

    pyexec captures at 16:00, before settlement (F134): ``gross`` runs from
    yesterday's SETTLEMENT to today's CLOSE, and ``aggregate`` is a raw
    balance delta that includes deposits.  Once the next capture lands the
    row is final and ``settle_implied`` (this day's positions x (settlement -
    close) x mult) completes it to settlement-to-settlement; ``final_pnl`` is
    the net of that, cash flows excluded.  Until 2026-09-18 the tracker used
    gross + aggregate: every day's close->settlement move was booked in no
    day (09-17: -63,945 read vs -34,100 settled) and the two 1,000,000
    deposits sat in live net.  A provisional day stays close-marked.
    """
    gross, fees = float(row["gross"]), float(row["fees"])
    cash = float(row.get("deposit", 0.0) or 0.0) - float(row.get("withdraw", 0.0) or 0.0)
    if is_final(row):
        g = gross + float(row.get("settle_implied", 0.0) or 0.0)
        net = float(row["final_pnl"])
    else:
        g, net = gross, float(row["aggregate"]) - cash
    return {"live_gross": g, "fees": fees, "live_net": net,
            "broker_resid": net - (g - fees), "final": is_final(row)}


def _next_state(day: str) -> dict | None:
    """The first state capture AFTER ``day`` (whose pre_settle is day's
    official settlement), or None while ``day`` is the latest capture."""
    key = compact(day)
    later = sorted(p.stem[len("state_"):] for p in C.PNL_DIR.glob("state_*.json")
                   if p.stem[len("state_"):] > key)
    return state(later[0]) if later else None


def final_settles(day: str) -> dict[str, float]:
    """{ticker: official settlement of ``day``} from the next capture's
    pre_settle; empty while the day is provisional."""
    nxt = _next_state(day)
    if nxt is None:
        return {}
    out = {}
    for block in ("marks", "positions"):
        for sym, v in (nxt.get(block) or {}).items():
            if sym not in out and v.get("pre_settle") is not None:
                out[sym] = float(v["pre_settle"])
    return out


def day_settles(day: str) -> dict[str, float]:
    """End-of-day marks for ``day``: official settlement where known, the
    16:00 close mark otherwise (provisional day, or a contract the next
    capture does not carry)."""
    st = state(day)
    out = settles(st) if st else {}
    out.update({t: v for t, v in final_settles(day).items() if t in out})
    return out


def daily_pnl(day: str) -> pd.DataFrame | None:
    """Per-symbol daily P&L for one day, sentinel rows removed. None if missing.

    pyexec appends account-level rows whose symbol starts with "_" (_GROSS,
    _FEES, _AGGREGATE, _RESIDUAL, _RESTATEMENT ...).  Strip by prefix: until
    2026-09-03 only two names were listed, so the per-symbol sum came out as
    2*gross - fees and leaked into the residual, a phantom "broker basis"
    term and the no-target attribution bucket.

    ``total_pnl`` is returned SETTLEMENT-TO-SETTLEMENT: pyexec's file stops
    at the close, so ``settle_adj`` = net_now x (settlement - close) x mult
    is added once the next capture publishes the settlement (see
    account_pnl); the file's own number is kept as ``total_pnl_close``.
    """
    p = C.PNL_DIR / f"daily_pnl_{compact(day)}.csv"
    if not p.exists():
        return None
    df = pd.read_csv(p)
    df = df[~df["symbol"].astype(str).str.startswith("_")].reset_index(drop=True)
    for c in ("net_now", "settle_now", "total_pnl"):
        df[c] = pd.to_numeric(df[c], errors="coerce").fillna(0.0)
    fin = final_settles(day)
    st = state(day) or {}
    mult = {s: float(p.get("multiplier") or 0.0)
            for s, p in (st.get("positions") or {}).items()}
    df["settle_adj"] = [
        n * (lookup(fin, s) - c) * (lookup(mult, s) or 0.0)
        if n and lookup(fin, s) is not None else 0.0
        for s, n, c in zip(df["symbol"].astype(str), df["net_now"], df["settle_now"])]
    df["total_pnl_close"] = df["total_pnl"]
    df["total_pnl"] = df["total_pnl"] + df["settle_adj"]
    return df


def product_daily_pnl(days) -> pd.DataFrame:
    """Executor per-symbol P&L rolled up to product root, long format.

    Columns: day, product, holding_pnl, trading_pnl, total_pnl (gross, fees
    are account-level only; settlement-to-settlement once final, see
    daily_pnl).  Sums to the day's per-symbol total, i.e. the
    same total the attribution buckets split.  Days without a file are
    skipped.
    """
    cols = ["holding_pnl", "trading_pnl", "settle_adj", "total_pnl"]
    frames = []
    for d in days:
        df = daily_pnl(d)
        if df is None or not len(df):
            continue
        g = df.assign(product=df["symbol"].astype(str).map(names.product_root))
        g[cols] = g.reindex(columns=cols).apply(pd.to_numeric, errors="coerce").fillna(0.0)
        g = g.groupby("product", as_index=False)[cols].sum()
        g.insert(0, "day", normalize_date(d))
        frames.append(g)
    if not frames:
        return pd.DataFrame(columns=["day", "product"] + cols)
    return pd.concat(frames, ignore_index=True)


def symbol_pnl(day: str, tickers) -> tuple[float, int]:
    """(summed gross total_pnl, n symbols matched) for `tickers` on one day.

    The executor's own per-symbol number -- holding + trading, settle-marked,
    the exact contribution those contracts make to live_gross.  Used for
    contracts the bridge cannot price any other way (see reconcile's off-book
    term); tolerant of the two CZCE year-digit forms.
    """
    df = daily_pnl(day)
    if df is None or not tickers:
        return 0.0, 0
    want = set(tickers)
    for t in tickers:
        alt = names.alt_ticker(t)
        if alt:
            want.add(alt)
    hit = df[df["symbol"].astype(str).isin(want)]
    if not len(hit):
        return 0.0, 0
    return float(pd.to_numeric(hit["total_pnl"], errors="coerce").fillna(0.0).sum()), int(len(hit))


def state(day: str) -> dict | None:
    """pnl/state_<D>.json parsed, or None."""
    p = C.PNL_DIR / f"state_{compact(day)}.json"
    if not p.exists():
        return None
    with open(p) as fh:
        return json.load(fh)


def live_positions(st: dict) -> dict[str, tuple[float, float]]:
    """{ticker: (net_lots, multiplier)} from a state snapshot."""
    out = {}
    for sym, pos in (st.get("positions") or {}).items():
        out[sym] = (float(pos.get("net") or 0.0), float(pos.get("multiplier") or 0.0))
    return out


def settles(st: dict) -> dict[str, float]:
    """{ticker: settle} from a state snapshot; None settles (unpublished) skipped."""
    out = {}
    for sym, mk in (st.get("marks") or {}).items():
        s = mk.get("settle")
        if s is not None:
            out[sym] = float(s)
    # positions block carries settle too and can cover symbols missing in marks
    for sym, pos in (st.get("positions") or {}).items():
        if sym not in out and pos.get("settle") is not None:
            out[sym] = float(pos["settle"])
    return out


# --------------------------------------------------------------------------
# Slippage / execution quality
# --------------------------------------------------------------------------

def exec_summary() -> pd.DataFrame:
    """analysis/exec_summary.csv indexed by ISO date."""
    p = C.ANALYSIS_DIR / "exec_summary.csv"
    if not p.exists():
        return pd.DataFrame()
    df = pd.read_csv(p)
    df["date"] = df["date"].map(normalize_date)
    return df.drop_duplicates("date", keep="last").set_index("date").sort_index()


def exec_products() -> pd.DataFrame:
    """analysis/exec_products.csv: one row per date x product, ISO dates."""
    p = C.ANALYSIS_DIR / "exec_products.csv"
    if not p.exists():
        return pd.DataFrame()
    df = pd.read_csv(p)
    df["date"] = df["date"].map(normalize_date)
    return df.drop_duplicates(["date", "product"], keep="last").sort_values("date")


# --------------------------------------------------------------------------
# Run detail: scale, sources, targets
# --------------------------------------------------------------------------

def run_records(day: str) -> list[dict]:
    p = C.DETAIL_DIR / f"{compact(day)}.jsonl"
    if not p.exists():
        return []
    out = []
    with open(p) as fh:
        for line in fh:
            line = line.strip()
            if not line:
                continue
            try:
                rec = json.loads(line)
            except json.JSONDecodeError:
                continue
            if rec.get("type") == "run":
                out.append(rec)
    return out


def fills_by_run(day: str) -> dict[str, dict[str, float]]:
    """{run_id: {symbol: signed filled lots}} from the day's leg records.

    ``trade_pos`` is the signed request and ``filled`` the filled count, so a
    partial fill contributes sign(trade_pos) * filled, not the request.
    """
    p = C.DETAIL_DIR / f"{compact(day)}.jsonl"
    if not p.exists():
        return {}
    out: dict[str, dict[str, float]] = {}
    with open(p) as fh:
        for line in fh:
            line = line.strip()
            if not line:
                continue
            try:
                rec = json.loads(line)
            except json.JSONDecodeError:
                continue
            if rec.get("type") != "leg":
                continue
            sym = rec.get("symbol")
            signed = float(rec.get("trade_pos") or 0.0)
            filled = float(rec.get("filled") or 0.0)
            if not sym or not signed or not filled:
                continue
            run = out.setdefault(rec.get("run_id", ""), {})
            run[sym] = run.get(sym, 0.0) + (1.0 if signed > 0 else -1.0) * filled
    return out


def _cst_naive_from_epoch(epoch: float):
    """Box clock is UTC; run ids and advisor generated_at are CST wall time."""
    import datetime as dt
    return (dt.datetime.fromtimestamp(epoch, dt.timezone.utc)
            .astimezone(dt.timezone(dt.timedelta(hours=8)))
            .replace(tzinfo=None))


def snap_price_sets(day: str) -> list[tuple]:
    """Every decision-price set shipped for the day, time-sorted.

    Returns [(naive-CST decision datetime, {preferred ticker: price})].
    Forward meta (the union set) and the legacy ks meta both load -- they
    coexist during the transition and later entries simply overwrite the
    same contracts at the same snap.  Fundamental's daily marks enter at
    their file mtime.
    """
    import datetime as dt
    sets: list[tuple] = []
    for source in (C.FORWARD_SOURCE, "ks"):
        meta = C.INBOX / source / "meta"
        for p in sorted(meta.glob(f"snap_prices_{normalize_date(day)}_*.json")):
            try:
                with open(p) as fh:
                    raw = json.load(fh)
                ts = dt.datetime.fromisoformat(raw["generated_at"])
                if ts.tzinfo is not None:
                    ts = ts.astimezone(
                        dt.timezone(dt.timedelta(hours=8))).replace(tzinfo=None)
            except (OSError, ValueError, KeyError):
                continue
            prices = {}
            for human, px in (raw.get("prices") or {}).items():
                if not px or px <= 0:
                    continue
                t = names.resolve(human)
                if t is not None:
                    prices[t] = float(px)
            if prices:
                sets.append((ts, prices))
    fp = C.INBOX / "fundamental" / "meta" / f"positions_{normalize_date(day)}.json"
    if fp.exists():
        fprices = fund_prices(day)
        if fprices:
            sets.append((_cst_naive_from_epoch(fp.stat().st_mtime), fprices))
    sets.sort(key=lambda s: s[0])
    return sets


def scale_for_day(day: str, prev_scale: float | None) -> tuple[float | None, list[str]]:
    """Authoritative execution scale for the day, plus flags.

    Last NUMERIC scale on a non-BLOCKED run record wins.  Runs record
    ``scale: null`` occasionally -- those never define the day.  With no
    usable record the previous day's scale carries forward with an alert;
    with several distinct numeric scales in one day the last wins with an
    alert (the intraday split lands in the residual).
    """
    flags: list[str] = []
    runs = run_records(day)
    numeric = [r for r in runs
               if isinstance(r.get("scale"), (int, float)) and r.get("state") != "BLOCKED"]
    if any(r.get("scale") is None for r in runs):
        flags.append("null_scale_run")
    if runs and all(r.get("state") == "BLOCKED" for r in runs):
        flags.append("all_runs_blocked")
    if not numeric:
        blocked_numeric = [r for r in runs if isinstance(r.get("scale"), (int, float))]
        if blocked_numeric:
            numeric = blocked_numeric
        else:
            flags.append("scale_carried_forward")
            return prev_scale, flags
    scales = {float(r["scale"]) for r in numeric}
    if len(scales) > 1:
        flags.append(f"multiple_scales:{sorted(scales)}")
    return float(numeric[-1]["scale"]), flags


def executed_sources(day: str) -> set[str]:
    """Inbox sources that fed at least one non-BLOCKED run on the day."""
    out: set[str] = set()
    for rec in run_records(day):
        if rec.get("state") == "BLOCKED":
            continue
        for src in rec.get("sources") or []:
            name = src.get("source")
            if name:
                out.add(name)
    return out


def is_forward_day(day: str) -> bool:
    """True when the merged forward book fed any run on the day.

    BLOCKED runs count: they still establish which book pyexec targeted
    (the regime), even when nothing executed.
    """
    for rec in run_records(day):
        for src in rec.get("sources") or []:
            if src.get("source") == C.FORWARD_SOURCE:
                return True
    return False


# --------------------------------------------------------------------------
# Shipped books and decision prices (inbox)
# --------------------------------------------------------------------------

def book(source: str, day: str) -> dict[str, float] | None:
    """Full-size shipped book for one source, keyed by preferred ticker."""
    p = C.INBOX / source / f"final_position_round_{normalize_date(day)}.json"
    if not p.exists():
        return None
    with open(p) as fh:
        raw = json.load(fh)
    out: dict[str, float] = {}
    for human, lots in raw.items():
        t = names.resolve(human)
        if t is None:
            continue
        out[t] = out.get(t, 0.0) + float(lots)
    return out


def combined_fullsize_book(day: str) -> tuple[dict[str, float], dict[str, dict[str, float]]]:
    """LEGACY-day book: sum of the per-source full-size books, plus each."""
    per: dict[str, dict[str, float]] = {}
    total: dict[str, float] = {}
    for src in C.LIVE_BOOK_SOURCES:
        b = book(src, day)
        if b is None:
            continue
        per[src] = b
        for t, lots in b.items():
            total[t] = total.get(t, 0.0) + lots
    return total, per


def fullsize_book_for_bridge(day: str, forward: bool) -> dict[str, float]:
    """The full-size book pyexec actually targeted (scale applies on top).

    FORWARD days: the merged weighted book from inbox/forward -- weights are
    already inside it.  LEGACY days: ks + fundamental summed, unweighted.
    """
    if forward:
        return book(C.FORWARD_SOURCE, day) or {}
    total, _ = combined_fullsize_book(day)
    return total


def snap_prices(day: str, snap: str, source: str = "ks") -> dict[str, float] | None:
    p = C.INBOX / source / "meta" / f"snap_prices_{normalize_date(day)}_{snap}.json"
    if not p.exists():
        return None
    with open(p) as fh:
        raw = json.load(fh)
    out = {}
    for human, px in (raw.get("prices") or {}).items():
        if not px or px <= 0:
            continue
        t = names.resolve(human)
        if t is not None:
            out[t] = float(px)
    return out


def fund_prices(day: str) -> dict[str, float]:
    p = C.INBOX / "fundamental" / "meta" / f"positions_{normalize_date(day)}.json"
    if not p.exists():
        return {}
    with open(p) as fh:
        raw = json.load(fh)
    out = {}
    for human, rec in raw.items():
        if not isinstance(rec, dict) or not rec.get("price"):
            continue
        t = names.resolve(human)
        if t is not None:
            out[t] = float(rec["price"])
    return out


def bench_prices(day: str) -> dict[str, float]:
    """First decision price of the day per ticker (the backtest window start),
    then fund price.

    Snaps are folded in preference order (config.SNAP_PREFERENCE, earliest
    first) and a ticker keeps the FIRST price seen, so a contract decided only
    from 0930 on (ksext) or 1330 on gets that snap's price rather than no
    bench.  Forward meta first (the only set guaranteed once the legacy
    per-source ships stop at Phase 5), then the legacy ks meta.  A contract
    with no decision price at all falls back to its settle downstream, which
    zeroes its marking term by construction.
    """
    return {t: px for t, (px, _) in bench_prices_with_snap(day).items()}


def bench_prices_with_snap(day: str) -> dict[str, tuple[float, str]]:
    """{ticker: (first decision price, snap label)} -- bench_prices plus WHICH
    decision it came from.

    The snap label is what makes a window mismatch visible: a backtest row
    spans 0900 -> 0900, so a contract whose first decision of the day is the
    0930 or 1330 snap is benchmarked late and carries its own straddle (the
    CFFEX index legs have no 0900 price at all).  "fund" is the fundamental
    sleeve's daily mark.
    """
    out: dict[str, tuple[float, str]] = {}
    for source in (C.FORWARD_SOURCE, "ks"):
        for snap in C.SNAP_PREFERENCE:
            for t, px in (snap_prices(day, snap, source=source) or {}).items():
                out.setdefault(t, (px, snap))
    for t, px in fund_prices(day).items():
        out.setdefault(t, (px, "fund"))
    return out


def inbox_ks_summary() -> pd.DataFrame:
    """inbox/ks/meta/summary.csv -- the ks backtest series shipped daily."""
    p = C.INBOX / "ks" / "meta" / "summary.csv"
    if not p.exists():
        return pd.DataFrame()
    df = pd.read_csv(p)
    df["date"] = df["date"].map(normalize_date)
    return df.drop_duplicates("date", keep="last").set_index("date").sort_index()


def inbox_ks_summary_mtime() -> float | None:
    p = C.INBOX / "ks" / "meta" / "summary.csv"
    return p.stat().st_mtime if p.exists() else None
