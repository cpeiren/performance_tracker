# Performance tracker - 2026-08-31   (reconciled through 2026-08-31)

## ALERTS
- MISSING LIVE DAY 2026-08-28: trading day with a backtest row but no daily_pnl/state file; excluded from the bridge, expected pnl held in the missing-day bucket.
- SCALE 2026-08-28: no usable run record; previous scale carried forward.
- SCALE CHANGE on 2026-08-27: now 0.2.
- SLIPPAGE 2026-08-31: 8 unbenchmarked leg(s), +70 CNY exec cost without a shipped decision price.
- RESIDUAL 2026-08-31: +36013 CNY vs trailing median |resid| 3313 -- attribution quality changed that day.

## Latest reconciled day (2026-08-31, forward regime)
live gross +22,465 | expected (0.2 x bt +3,872) = +774 | gap +21,691
  exec_cost +5 (slip -65, unbench +70) | marking +8,965 | bookdiff -1,630 (carry -3,496, new +1,866) | residual +36,013 | broker basis -21,653
  fees +812 | broker residual +2,267 -> live net +23,920

## Cumulative bridge (live since 2026-08-18, 9 reconciled days)
| expected | -exec | +marking | +bookdiff | +resid | +broker basis | = live gross | -fees | +broker_resid | = live net |
|---|---|---|---|---|---|---|---|---|---|
| +9,677 | +835 | +8,835 | -2,494 | +32,012 | -23,170 | +25,695 | -2,525 | +1,684 | +24,854 |
missing live days excluded: 2026-08-28 (expected +2,838 held in bucket)

## Stats (daily CNY pnl)
| window | days | total | sharpe | mdd | hit |
|---|---|---|---|---|---|
| live net live-to-date | 9 | +24,854 | 5.38 | -3,260 | 44% | (small sample)
| live net last-20d | 9 | +24,854 | 5.38 | -3,260 | 44% | (small sample)
| live net 2026-YTD | 9 | +24,854 | 5.38 | -3,260 | 44% | (small sample)
| bt scaled live-to-date | 9 | +9,677 | 6.77 | -3,685 | 89% | (small sample)
| bt scaled last-20d | 9 | +9,677 | 6.77 | -3,685 | 89% | (small sample)
| bt scaled 2026-YTD | 9 | +9,677 | 6.77 | -3,685 | 89% | (small sample)

## Per strategy
| strategy | live? | bt 2026 pnl (full) | bt scaled+weighted (live window) | live attributed | note |
|---|---|---|---|---|---|
| Calendar main pool (branch) | yes | +498,475 | +10,058 | +689 | forward w=0.8 |
| Fundamental factor | yes | +590,768 | -381 | +51,179 | forward w=2 |
| Cross-product pairs | yes | +89,555 | - | -1,067 | forward w=1.5 |
| Calendar extended pool | no | +608,215 | - | - | forward w=0 (parked) |
| Chemical fundamental | yes | +421,280 | - | -15,000 | forward w=1.5 |
| Agriculture event-driven | yes | +108,565 | - | -1,508 | forward w=1 |
| Factor-neutral stat arb | yes | +267,909 | - | +3,847 | forward w=1 |
| shared bucket | - | - | - | -5,870 | legacy multi-holder / forward offsetting |
| neither bucket (no target) | - | - | - | +16,595 | inherited/manual/rounding |
forward-day attribution is pro-rated by weighted full-size lots; legacy days remain exclusive-holder.

## Data health
scale: 0.2 (since 2026-08-27)
regime: forward (merged weighted book) since 2026-08-31; 1 forward day(s), 8 legacy day(s)
merge weights (2026-08-31): ks_branch 0.8, fund_v3 2, china_pairs 1.5, ks_ext 0, chem_fund 1.5, agri_event 1, stat_arb 1
as-shipped pins: 9 live day(s) pinned; current series diverges on fund_v3: 8, ks_branch: 9
inbox ks summary mtime: 2026-08-31 05:51 UTC
