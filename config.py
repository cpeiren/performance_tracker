"""Performance tracker configuration -- every path, name and threshold.

The tracker compares the SHIPPED backtest books against what the live account
on this box (CME-Server2, pyexec, environment prod_yingxi) actually earned,
and decomposes the gap so the two curves reconcile.  It reads cnexec DATA
files only and never imports cnexec code.
"""

from __future__ import annotations

from pathlib import Path

# --------------------------------------------------------------------------
# Paths (this box)
# --------------------------------------------------------------------------

TRACKER_ROOT = Path(__file__).resolve().parent
CNEXEC = Path.home() / "cnexec"

PNL_DIR = CNEXEC / "pnl"                       # daily_pnl_<D>.csv, daily_summary.csv, state_<D>.json
ANALYSIS_DIR = CNEXEC / "analysis"             # exec_summary.csv, exec_daily_<D>.csv
DETAIL_DIR = CNEXEC / "pyexec_runs" / "detail"  # <YYYYMMDD>.jsonl (runs + legs)
INBOX = CNEXEC / "inbox"                       # ks/, fundamental/ (books + meta)

INCOMING = TRACKER_ROOT / "incoming"           # ship-script payloads land here
DATA = TRACKER_ROOT / "data"
BACKTEST_DIR = DATA / "backtest"               # canonical per-strategy series
RECON_CSV = DATA / "reconciliation.csv"
STATE_JSON = DATA / "state.json"
REPORT_DIR = TRACKER_ROOT / "reports"
DAILY_DIR = REPORT_DIR / "daily"

for _d in (INCOMING, BACKTEST_DIR, DAILY_DIR):
    _d.mkdir(parents=True, exist_ok=True)

# --------------------------------------------------------------------------
# Strategy registry
# --------------------------------------------------------------------------

#: strategy key -> (label, inbox source name or None if not live-shipped).
#: A strategy is treated as LIVE on a given day when its inbox source appears
#: in that day's executed run records -- never by editing this table.
STRATEGIES = {
    "ks_branch":   ("Calendar main pool (branch)", "ks"),
    "fund_v3":     ("Fundamental factor",          "fundamental"),
    "china_pairs": ("Cross-product pairs",         "pairs"),
    "ks_ext":      ("Calendar extended pool",      None),
    "chem_fund":   ("Chemical fundamental",        None),
    "agri_event":  ("Agriculture event-driven",    None),
    "stat_arb":    ("Factor-neutral stat arb",     None),
}

#: Inbox source -> strategy key (reverse of the live half of STRATEGIES).
SOURCE_TO_STRATEGY = {v[1]: k for k, v in STRATEGIES.items() if v[1]}

#: Sources whose dated full-size books feed the ideal-book construction.
LIVE_BOOK_SOURCES = ("ks", "fundamental")

# --------------------------------------------------------------------------
# Reconciliation conventions
# --------------------------------------------------------------------------

#: First trading day with live daily P&L on this account.
LIVE_START = "2026-08-18"

#: OOS window the tracker reports on.
OOS_START = "2026-01-01"

#: End-of-day decision price preference for the marking benchmark.
SNAP_PREFERENCE = ("1330", "1030", "0930", "0900")

#: |residual| alert threshold: max(RESID_ABS_FLOOR, RESID_REL * |live_gross|).
RESID_ABS_FLOOR = 500.0
RESID_REL = 0.5

#: Ship payload considered stale after this many business days.
SHIP_STALE_BDAYS = 3

#: Inbox ks summary.csv is expected refreshed by this UTC hour on weekdays.
INBOX_SUMMARY_DUE_UTC_HOUR = 6.5

#: Small-sample tag on stats windows shorter than this.
SMALL_SAMPLE_DAYS = 30

ANN_DAYS = 252
