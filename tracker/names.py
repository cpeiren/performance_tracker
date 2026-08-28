"""Contract-name helpers, mirrored from cnexec/pyexec/names.py (NOT imported).

The shipped books key contracts by human name ("rb Oct26", "SA Jan27"); the
live side keys them by exchange ticker ("rb2610", "SA701").  CZCE quotes a
single year digit, every other exchange two, and the static CZCE set can lag
new listings -- so resolution offers both forms, preferred first.
"""

from __future__ import annotations

import re

CZCE_SYMBOLS = {
    "CF", "SR", "TA", "OI", "RI", "WH", "PM", "RM", "RS", "JR", "LR",
    "SF", "SM", "FG", "CY", "AP", "CJ", "PK", "PF", "SA", "UR", "MA", "ZC",
    "SH", "PX", "PR",
}

MONTH_MAP = {
    "Jan": "01", "Feb": "02", "Mar": "03", "Apr": "04",
    "May": "05", "Jun": "06", "Jul": "07", "Aug": "08",
    "Sep": "09", "Oct": "10", "Nov": "11", "Dec": "12",
}


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
    """(three_digit, four_digit) forms, e.g. ("SH607", "SH2607")."""
    return f"{symbol}{year_str[1]}{month}", f"{symbol}{year_str}{month}"


def contract_ticker_candidates(contract: str) -> list[str]:
    """Both plausible tickers for a human name, preferred form first."""
    symbol, month, year_str = _split_name(contract)
    three, four = _ticker_forms(symbol, month, year_str)
    return [three, four] if symbol.upper() in CZCE_SYMBOLS else [four, three]


def preferred_ticker(contract: str) -> str:
    return contract_ticker_candidates(contract)[0]


def alt_ticker(ticker: str) -> str | None:
    """The other year-digit form of an exchange ticker, if parseable.

    "SA701" <-> "SA2701", "rb2610" <-> "rb610".  Used when merging dicts whose
    producers disagreed on the CZCE form; never for month/year arithmetic.
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
