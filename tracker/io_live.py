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

SENTINELS = {"_AGGREGATE", "_RESIDUAL"}


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


def daily_pnl(day: str) -> pd.DataFrame | None:
    """Per-symbol daily P&L for one day, sentinel rows removed. None if missing."""
    p = C.PNL_DIR / f"daily_pnl_{compact(day)}.csv"
    if not p.exists():
        return None
    df = pd.read_csv(p)
    return df[~df["symbol"].isin(SENTINELS)].reset_index(drop=True)


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
        try:
            t = names.preferred_ticker(human)
        except ValueError:
            continue
        out[t] = out.get(t, 0.0) + float(lots)
    return out


def combined_fullsize_book(day: str) -> tuple[dict[str, float], dict[str, dict[str, float]]]:
    """Sum of the live sources' full-size books, plus the per-source books."""
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


def snap_prices(day: str, snap: str) -> dict[str, float] | None:
    p = C.INBOX / "ks" / "meta" / f"snap_prices_{normalize_date(day)}_{snap}.json"
    if not p.exists():
        return None
    with open(p) as fh:
        raw = json.load(fh)
    out = {}
    for human, px in (raw.get("prices") or {}).items():
        if not px or px <= 0:
            continue
        try:
            out[names.preferred_ticker(human)] = float(px)
        except ValueError:
            continue
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
        try:
            out[names.preferred_ticker(human)] = float(rec["price"])
        except ValueError:
            continue
    return out


def bench_prices(day: str) -> dict[str, float]:
    """End-of-day decision price per ticker: latest ks snap, then fund price.

    A contract with no decision price falls back to its settle downstream,
    which zeroes its marking term by construction.
    """
    out: dict[str, float] = {}
    for snap in C.SNAP_PREFERENCE:  # first snap file that exists is the EOD set
        prices = snap_prices(day, snap)
        if prices:
            out.update(prices)
            break
    for t, px in fund_prices(day).items():
        out.setdefault(t, px)
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
