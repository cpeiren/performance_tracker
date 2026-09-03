# Performance tracker - 2026-09-03   (reconciled through 2026-09-02)

## ALERTS
- BT PENDING 2026-09-03: no mature backtest row for agri_event, chem_fund, china_pairs, fund_v3, ks_ext, stat_arb (nonzero weight) -- day held out of the bridge until the rows ship; it re-enters automatically.
- WEIGHTS CHANGE on 2026-09-01: ks_ext: 0.0->0.25.
- WEIGHTS CHANGE on 2026-09-02: stat_arb: 1.0->0.0.
- WEIGHTS CHANGE on 2026-09-03: stat_arb: 0.0->1.0.
- MISSING LIVE DAY 2026-08-28: trading day with a backtest row but no daily_pnl/state file; excluded from the bridge, expected pnl held in the missing-day bucket.
- SCALE 2026-08-28: no usable run record; previous scale carried forward.
- SCALE CHANGE on 2026-08-27: now 0.2.
- SCALE CHANGE on 2026-09-01: now 0.5.
- SLIPPAGE 2026-09-03: 4 unbenchmarked leg(s), +30 CNY exec cost without a shipped decision price.
- RESIDUAL 2026-09-01: -40058 CNY vs trailing median |resid| 5210, offset by neither neighbour (2026-08-31 +6748, 2026-09-02 +90351) -- attribution quality changed. (A break-out that a neighbouring day mirrors is the backtest/live day-window straddle and is not alerted.)

## Latest reconciled day (2026-09-02, forward regime)
live gross +40,175 | expected (0.5 x bt -93,760) = -46,880 | gap +87,055
  exec_cost -250 (slip -270, unbench +20) | marking +23,820 | bookdiff +4,132 (carry +6,410, new -2,278) | intraday +7,852 | residual +90,351 (window-straddled: judge with the next day's) | broker basis -39,351
  fees +824 | broker residual +6,034 -> live net +45,385

## Cumulative bridge (live since 2026-08-18, 11 reconciled days)
| expected | -exec | +marking | +bookdiff | +intraday | +resid | +broker basis | = live gross | -fees | +broker_resid | = live net |
|---|---|---|---|---|---|---|---|---|---|---|
| +108,975 | -11,608 | -5,760 | +5,998 | +5,372 | +55,540 | -76,603 | +81,915 | -5,312 | -15,130 | +61,473 |
missing live days excluded: 2026-08-28 (expected +2,838 held in bucket)

## Stats (daily CNY pnl)
| window | days | total | sharpe | mdd | hit |
|---|---|---|---|---|---|
| live net live-to-date | 11 | +61,473 | 5.73 | -8,766 | 45% | (small sample)
| live net last-20d | 11 | +61,473 | 5.73 | -8,766 | 45% | (small sample)
| live net 2026-YTD | 11 | +61,473 | 5.73 | -8,766 | 45% | (small sample)
| bt scaled live-to-date | 11 | +108,975 | 3.97 | -46,880 | 82% | (small sample)
| bt scaled last-20d | 11 | +108,975 | 3.97 | -46,880 | 82% | (small sample)
| bt scaled 2026-YTD | 11 | +108,975 | 3.97 | -46,880 | 82% | (small sample)

## Per strategy
| strategy | live? | bt 2026 pnl (full) | bt scaled+weighted (live window) | live attributed | note |
|---|---|---|---|---|---|
| Calendar main pool (branch) | yes | +529,355 | +19,348 | +43,021 | forward w=0.8 |
| Fundamental factor | yes | +658,264 | +67,593 | +55,103 | forward w=2 |
| Cross-product pairs | yes | +126,250 | +22,488 | -7,453 | forward w=1.5 |
| Calendar extended pool | yes | +560,640 | -2,537 | -222 | forward w=0.25 |
| Chemical fundamental | yes | +430,860 | -72 | +10,638 | forward w=1.5 |
| Agriculture event-driven | yes | +127,625 | +2,516 | +1,176 | forward w=1 |
| Factor-neutral stat arb | no | +315,503 | -361 | -3,303 | forward w=1 |
| shared bucket | - | - | - | -16,900 | legacy multi-holder / forward offsetting |
| neither bucket (no target) | - | - | - | +76,458 | inherited/manual/rounding |
forward-day attribution is pro-rated by weighted full-size lots; legacy days remain exclusive-holder.

## Data health
scale: 0.5 (since 2026-09-01)
regime: forward (merged weighted book) since 2026-08-31; 3 forward day(s), 8 legacy day(s)
merge weights (2026-09-03): ks_branch 0.8, fund_v3 2, china_pairs 1.5, ks_ext 0.25, chem_fund 1.5, agri_event 1, stat_arb 1
as-shipped pins: 12 live day(s) pinned; current series diverges from pins on fund_v3: 10 day(s), max 22,925 CNY, ks_branch: 9 day(s), max 35,915 CNY, stat_arb: 10 day(s), max 7,372 CNY, ks_ext: 2 day(s), max 950 CNY, agri_event: 3 day(s), max 5,680 CNY; standing counts -- a divergence is announced as an alert once, the first run it appears, and kept here afterwards
inbox ks summary mtime: 2026-09-03 05:52 UTC
