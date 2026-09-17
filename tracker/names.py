"""Contract-name helpers, mirrored from cnexec/pyexec/names.py (NOT imported).

The shipped books key contracts by human name ("rb Oct26", "SA Jan27",
"if Dec26"); the live side keys them by exchange ticker ("rb2610", "SA701",
"IF2612").  Two exchange conventions have to be mapped:

  * CZCE quotes a single year digit, every other exchange two, and the static
    CZCE set can lag new listings -- so resolution offers both forms,
    preferred first.
  * CASE is the counter's own (pyexec F118): CZCE and CFFEX instrument ids are
    UPPERCASE, every other exchange lowercase.  The books emit lowercase roots
    ("if Dec26") while the counter says IF2612.

This module is a MIRROR, and on 2026-09-17 the mirror was found to have
drifted: it predated F118, so every CFFEX leg resolved to a lowercase ticker
("if2612") that matched nothing on the live side.  The merged book's four
index-futures legs therefore looked absent (ideal 0 -> the whole on-target
position booked as a deviation), their shipped decision prices looked absent
(marking, bookdiff_creation and the intraday term all zeroed), and every lot
traded in them landed in the residual: -90,000 of 2026-09-15's -150,644.
tests/test_names_sync.py now diffs this module against the production one
wherever both exist.
"""

from __future__ import annotations

import re

#: CZCE quotes contracts with a single year digit (SA605); membership is by
#: product code, upper-cased.  Kept in step with pyexec (PL added 2026-09-09).
CZCE_SYMBOLS = {
    "CF", "SR", "TA", "OI", "RI", "WH", "PM", "RM", "RS", "JR", "LR",
    "SF", "SM", "FG", "CY", "AP", "CJ", "PK", "PF", "SA", "UR", "MA", "ZC",
    "SH", "PX", "PR", "PL",
}

#: CFFEX instrument ids are UPPERCASE (IF2612) while the books emit lowercase
#: roots ("if Dec26"), so the root's case must be mapped like CZCE's year
#: digit.  Index futures IF/IH/IM/IC and the bond futures T/TF/TL/TS, matching
#: pyexec's F118 set.
CFFEX_SYMBOLS = {"IF", "IH", "IM", "IC", "T", "TF", "TL", "TS"}

MONTH_MAP = {
    "Jan": "01", "Feb": "02", "Mar": "03", "Apr": "04",
    "May": "05", "Jun": "06", "Jul": "07", "Aug": "08",
    "Sep": "09", "Oct": "10", "Nov": "11", "Dec": "12",
}

#: Human names this process could not resolve, {name: times seen}.  Readers
#: call resolve() instead of swallowing the ValueError, so a name the tracker
#: cannot map is reported rather than silently dropped.
UNRESOLVED: dict[str, int] = {}


def _canonical_symbol(symbol: str) -> str:
    """The exchange's own casing for a product root (pyexec F118).

    CZCE and CFFEX ids are uppercase (SA701, IF2612); everything else is
    lowercase (rb2610).  Canonicalizing here means the produced ticker is the
    instrument id the counter's position rows carry, whatever case the book
    shipped.
    """
    upper = symbol.upper()
    if upper in CZCE_SYMBOLS or upper in CFFEX_SYMBOLS:
        return upper
    return symbol.lower()


def _split_name(contract: str) -> tuple[str, str, str]:
    parts = contract.split()
    if len(parts) != 2:
        raise ValueError(f"Invalid contract format: {contract!r}")
    symbol, month_year = parts
    month_str, year_str = month_year[:-2], month_year[-2:]
    if month_str not in MONTH_MAP:
        raise ValueError(f"Unknown month {month_str!r} in {contract!r}")
    if not year_str.isdigit():
        raise ValueError(f"Invalid year {year_str!r} in {contract!r}")
    return symbol, MONTH_MAP[month_str], year_str


def _ticker_forms(symbol: str, month: str, year_str: str) -> tuple[str, str]:
    """(three_digit, four_digit) forms, e.g. ("SH607", "SH2607").

    The symbol is canonicalized first, so both forms come out exchange-true
    ("if" -> IF612/IF2612, "SA" -> SA701/SA2701).
    """
    symbol = _canonical_symbol(symbol)
    return f"{symbol}{year_str[1]}{month}", f"{symbol}{year_str}{month}"


def contract_ticker_candidates(contract: str) -> list[str]:
    """Both plausible tickers for a human name, preferred form first."""
    symbol, month, year_str = _split_name(contract)
    three, four = _ticker_forms(symbol, month, year_str)
    return [three, four] if symbol.upper() in CZCE_SYMBOLS else [four, three]


def preferred_ticker(contract: str) -> str:
    return contract_ticker_candidates(contract)[0]


def resolve(contract: str) -> str | None:
    """preferred_ticker, or None with the failure RECORDED in UNRESOLVED.

    Every reader that walks a shipped file uses this: an unparseable name is
    a shipping-format change and must surface as an alert, not as a leg that
    quietly stops existing.
    """
    try:
        return preferred_ticker(contract)
    except ValueError:
        UNRESOLVED[contract] = UNRESOLVED.get(contract, 0) + 1
        return None


def alt_ticker(ticker: str) -> str | None:
    """The other year-digit form of an exchange ticker, if parseable.

    "SA701" <-> "SA2701", "rb2610" <-> "rb610".  Used when merging dicts whose
    producers disagreed on the CZCE form; never for month/year arithmetic, and
    never for case -- casing is settled by _canonical_symbol at resolution.
    """
    m = re.match(r"^([A-Za-z]+)(\d{3,4})$", ticker)
    if not m:
        return None
    sym, digits = m.group(1), m.group(2)
    if len(digits) == 4:
        return f"{sym}{digits[1:]}"
    return None  # 3-digit form is ambiguous in the decade; do not guess upward


def product_root(symbol: str) -> str:
    match = re.match(r"^([A-Za-z]+)", symbol)
    if not match:
        raise ValueError(f"Cannot parse product root from {symbol!r}")
    return match.group(1)
