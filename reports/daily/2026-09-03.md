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
- RESIDUAL 2026-08-31: -14905 CNY vs trailing median |resid| 2633, offset by neither neighbour (2026-08-27 -4644, 2026-09-01 -54141) -- attribution quality changed. (A break-out that a neighbouring day mirrors is the backtest/live day-window straddle and is not alerted.)

## Latest reconciled day (2026-09-02, forward regime)
live gross +40,175 | expected (0.5 x bt -93,760) = -46,880 | gap +87,055
  exec_cost -250 (slip -270, unbench +20) | marking +23,820 | bookdiff +4,132 (carry +6,410, new -2,278) | intraday +7,852 | residual +51,000 (window-straddled: judge with the next day's)
  fees +824 | broker residual +0 -> live net +39,351

## Cumulative bridge (live since 2026-08-18, 11 reconciled days)
| expected | -exec | +marking | +bookdiff | +intraday | +resid | = live gross | -fees | +broker_resid | = live net |
|---|---|---|---|---|---|---|---|---|---|
| +108,975 | -11,608 | -5,760 | +5,998 | +5,372 | -21,063 | +81,915 | -5,312 | +0 | +76,603 |
missing live days excluded: 2026-08-28 (expected +2,838 held in bucket)

## Stats (daily CNY pnl)
| window | days | total | sharpe | mdd | hit |
|---|---|---|---|---|---|
| live net live-to-date | 11 | +76,603 | 8.47 | -2,658 | 64% | (small sample)
| live net last-20d | 11 | +76,603 | 8.47 | -2,658 | 64% | (small sample)
| live net 2026-YTD | 11 | +76,603 | 8.47 | -2,658 | 64% | (small sample)
| bt scaled live-to-date | 11 | +108,975 | 3.97 | -46,880 | 82% | (small sample)
| bt scaled last-20d | 11 | +108,975 | 3.97 | -46,880 | 82% | (small sample)
| bt scaled 2026-YTD | 11 | +108,975 | 3.97 | -46,880 | 82% | (small sample)

## Slippage (+ = cost; bps vs benchmarked notional)
| day | lots | notional M | slip total | drift | exec | bps | unbench legs | unbench CNY |
|---|---|---|---|---|---|---|---|---|
| 2026-08-20 | 71 | 3.0 | -505 | -588 | +82 | -1.82 | 4 | -12 |
| 2026-08-21 | 22 | 1.0 | +160 | +138 | +22 | +1.59 | 1 | -2 |
| 2026-08-24 | 44 | 2.3 | +710 | +630 | +80 | +3.15 | 0 | +0 |
| 2026-08-25 | 53 | 2.2 | +405 | +240 | +165 | +2.15 | 4 | -35 |
| 2026-08-26 | 45 | 2.4 | +65 | +62 | +2 | +0.29 | 1 | +15 |
| 2026-08-27 | 388 | 21.4 | -1,865 | -2,018 | +152 | -0.97 | 2 | +250 |
| 2026-08-31 | 371 | 15.9 | +505 | -1,230 | +1,735 | +0.33 | 10 | +75 |
| 2026-09-01 | 747 | 50.2 | +2,725 | +1,685 | +1,040 | +1.35 | 85 | +9,392 |
| 2026-09-02 | 353 | 15.2 | -270 | -1,055 | +785 | -0.19 | 5 | +20 |
| 2026-09-03 | 302 | 15.8 | -12,160 | -13,282 | +1,122 | -8.28 | 4 | +30 |
| live window (12d) | 2502 | 133.5 | -10,450 | -15,718 | +5,268 | -1.06 | 119 | +9,928 |
exec-only bps over the window: +0.54; benchmark coverage 74% of traded notional

| product | days | lots | notional M | drift | exec (incl. unbench) | all-in | bps |
|---|---|---|---|---|---|---|---|
| zn | 9 | 72 | 9.6 | -6,412 | +50 | -6,362 | -6.66 |
| y | 9 | 53 | 4.7 | +4,420 | +830 | +5,250 | +11.13 |
| CY | 5 | 28 | 3.2 | -5,775 | +1,100 | -4,675 | -14.63 |
| cu | 4 | 13 | 7.0 | -4,625 | +275 | -4,350 | -6.17 |
| l | 11 | 56 | 2.2 | +4,128 | -102 | +4,025 | +18.02 |
| hc | 9 | 272 | 9.2 | +3,030 | +430 | +3,460 | +3.77 |
| rb | 10 | 191 | 6.0 | -2,555 | -715 | -3,270 | -5.47 |
| a | 9 | 59 | 3.0 | +1,460 | +1,375 | +2,835 | +9.54 |
| OI | 5 | 37 | 3.8 | -2,830 | +120 | -2,710 | -7.10 |
| IH | 3 | 8 | 6.9 | +1,440 | +840 | +2,280 | +3.29 |
| cs | 11 | 200 | 5.2 | -475 | +2,490 | +2,015 | +3.86 |
| p | 7 | 34 | 3.5 | -3,105 | +1,300 | -1,805 | -5.11 |
| FG | 11 | 106 | 2.0 | +1,160 | +420 | +1,580 | +7.83 |
| SR | 9 | 73 | 4.0 | +910 | +475 | +1,385 | +3.50 |
| eg | 3 | 8 | 0.4 | +1,210 | +100 | +1,310 | +33.68 |
| other (31) | - | 1292 | 62.8 | -7,698 | +6,208 | -1,490 | -0.24 |
| all products | - | 2502 | 133.5 | -15,718 | +15,195 | -522 | -0.04 |
ranked by |all-in| over the live window (all-in = drift + exec = the bridge's exec_cost by product); product bps are vs traded notional

## Per strategy
| strategy | live? | bt 2026 pnl (full) | bt scaled+weighted (live window) | live attributed | note |
|---|---|---|---|---|---|
| Calendar main pool (branch) | yes | +529,355 | +19,348 | +43,021 | forward w=0.8 |
| Fundamental factor | yes | +658,264 | +67,593 | +55,103 | forward w=2 |
| Cross-product pairs | yes | +126,250 | +22,488 | -7,453 | forward w=1.5 |
| Calendar extended pool | yes | +560,640 | -2,537 | -222 | forward w=0.25 |
| Chemical fundamental | yes | +430,860 | -72 | +10,638 | forward w=1.5 |
| Agriculture event-driven | yes | +127,625 | +2,516 | +1,176 | forward w=1 |
| Factor-neutral stat arb | yes | +315,503 | -361 | -3,303 | forward w=1 |
| shared bucket | - | - | - | -16,900 | legacy multi-holder / forward offsetting |
| neither bucket (no target) | - | - | - | -145 | inherited/manual/rounding |
forward-day attribution is pro-rated by weighted full-size lots; legacy days remain exclusive-holder.

## Data health
scale: 0.5 (since 2026-09-01)
regime: forward (merged weighted book) since 2026-08-31; 3 forward day(s), 8 legacy day(s)
merge weights (2026-09-03): ks_branch 0.8, fund_v3 2, china_pairs 1.5, ks_ext 0.25, chem_fund 1.5, agri_event 1, stat_arb 1
as-shipped pins: 12 live day(s) pinned; current series diverges from pins on fund_v3: 10 day(s), max 22,925 CNY, ks_branch: 9 day(s), max 35,915 CNY, stat_arb: 10 day(s), max 7,372 CNY, ks_ext: 2 day(s), max 950 CNY, agri_event: 3 day(s), max 5,680 CNY; standing counts -- a divergence is announced as an alert once, the first run it appears, and kept here afterwards
inbox ks summary mtime: 2026-09-03 05:52 UTC
