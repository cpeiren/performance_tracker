# Performance tracker - 2026-09-08   (reconciled through 2026-09-07)

## ALERTS
- BT PENDING 2026-09-08: no mature backtest row for stat_arb (nonzero weight) -- day held out of the bridge until the rows ship; it re-enters automatically.
- WEIGHTS CHANGE on 2026-09-01: ks_ext: 0.0->0.25.
- WEIGHTS CHANGE on 2026-09-02: stat_arb: 1.0->0.0.
- WEIGHTS CHANGE on 2026-09-03: stat_arb: 0.0->1.0.
- MISSING LIVE DAY 2026-08-28: trading day with a backtest row but no daily_pnl/state file; excluded from the bridge, expected pnl held in the missing-day bucket.
- SCALE 2026-08-28: no usable run record; previous scale carried forward.
- SCALE CHANGE on 2026-08-27: now 0.2.
- SCALE CHANGE on 2026-09-01: now 0.5.
- SLIPPAGE 2026-09-08: 5 unbenchmarked leg(s), +135 CNY exec cost without a shipped decision price.
- BROKER DIFF 2026-09-08: daily_summary diff_vs_broker = -3040.00 CNY (should be 0).
- RESIDUAL 2026-08-27: -17482 CNY vs trailing median |resid| 1250, offset by neither neighbour (2026-08-26 +2944, 2026-08-31 -22890) -- attribution quality changed. (A break-out that a neighbouring day mirrors is the backtest/live day-window straddle and is not alerted.)
- RESIDUAL 2026-09-02: -40238 CNY vs trailing median |resid| 1864, offset by neither neighbour (2026-09-01 +19604, 2026-09-03 -34344) -- attribution quality changed. (A break-out that a neighbouring day mirrors is the backtest/live day-window straddle and is not alerted.)
- RESIDUAL 2026-09-03: -34344 CNY vs trailing median |resid| 2513, offset by neither neighbour (2026-09-02 -40238, 2026-09-04 -44954) -- attribution quality changed. (A break-out that a neighbouring day mirrors is the backtest/live day-window straddle and is not alerted.)

## Latest reconciled day (2026-09-07, forward regime)
live gross +41,645 | expected (0.5 x bt +13,361) = +6,681 | gap +34,964
  exec_cost +4,230 (slip +4,090, unbench +140) | marking +2,515 | bookdiff +2,380 (carry -340, new +2,720) | intraday +2,982 | residual +31,317 (live re-marked to first decision, vs the previous backtest row)
  fees +493 | broker residual +0 -> live net +41,152

## Cumulative bridge (live since 2026-08-18, 14 reconciled days)
| expected | -exec | +marking | +bookdiff | +intraday | +resid | = live gross | -fees | +broker_resid | = live net |
|---|---|---|---|---|---|---|---|---|---|
| +149,754 | +1,678 | +5,980 | +16,990 | +8,315 | -102,211 | +80,505 | -7,151 | +0 | +73,354 |
missing live days excluded: 2026-08-28 (expected +4,849 held in bucket)

## Stats (daily CNY pnl)
| window | days | total | sharpe | mdd | hit |
|---|---|---|---|---|---|
| live net live-to-date | 14 | +73,354 | 4.44 | -44,401 | 57% | (small sample)
| live net last-20d | 14 | +73,354 | 4.44 | -44,401 | 57% | (small sample)
| live net 2026-YTD | 14 | +73,354 | 4.44 | -44,401 | 57% | (small sample)
| bt scaled live-to-date | 14 | +149,754 | 4.32 | -67,976 | 79% | (small sample)
| bt scaled last-20d | 14 | +149,754 | 4.32 | -67,976 | 79% | (small sample)
| bt scaled 2026-YTD | 14 | +149,754 | 4.32 | -67,976 | 79% | (small sample)

## Slippage (+ = cost; bps vs benchmarked notional)
| day | lots | notional M | slip total | drift | exec | bps | unbench legs | unbench CNY |
|---|---|---|---|---|---|---|---|---|
| 2026-08-25 | 53 | 2.2 | +405 | +240 | +165 | +2.15 | 4 | -35 |
| 2026-08-26 | 45 | 2.4 | +65 | +62 | +2 | +0.29 | 1 | +15 |
| 2026-08-27 | 388 | 21.4 | -1,865 | -2,018 | +152 | -0.97 | 2 | +250 |
| 2026-08-31 | 371 | 15.9 | +505 | -1,230 | +1,735 | +0.33 | 10 | +75 |
| 2026-09-01 | 747 | 50.2 | +2,725 | +1,685 | +1,040 | +1.35 | 85 | +9,392 |
| 2026-09-02 | 353 | 15.2 | -270 | -1,055 | +785 | -0.19 | 5 | +20 |
| 2026-09-03 | 302 | 15.8 | -12,160 | -13,282 | +1,122 | -8.28 | 4 | +30 |
| 2026-09-04 | 225 | 10.8 | -5,350 | -5,442 | +92 | -5.39 | 4 | -35 |
| 2026-09-07 | 200 | 12.6 | +4,090 | +3,312 | +778 | +3.31 | 3 | +140 |
| 2026-09-08 | 286 | 21.3 | +7,165 | +7,250 | -85 | +3.58 | 5 | +135 |
| live window (15d) | 3213 | 178.3 | -4,545 | -10,598 | +6,052 | -0.32 | 131 | +10,168 |
exec-only bps over the window: +0.43; benchmark coverage 79% of traded notional

| product | days | lots | notional M | drift | exec (incl. unbench) | all-in | bps |
|---|---|---|---|---|---|---|---|
| zn | 11 | 76 | 10.1 | -5,288 | +125 | -5,162 | -5.11 |
| cu | 4 | 13 | 7.0 | -4,625 | +275 | -4,350 | -6.17 |
| l | 14 | 63 | 2.5 | +4,270 | -145 | +4,125 | +16.33 |
| y | 11 | 65 | 5.8 | +3,190 | +800 | +3,990 | +6.86 |
| OI | 8 | 89 | 9.2 | -4,125 | +230 | -3,895 | -4.25 |
| eg | 5 | 10 | 0.5 | +3,100 | +60 | +3,160 | +62.63 |
| CY | 8 | 44 | 5.0 | -4,350 | +1,475 | -2,875 | -5.72 |
| hc | 12 | 338 | 11.4 | +1,580 | +1,160 | +2,740 | +2.40 |
| SF | 13 | 125 | 3.9 | +2,340 | +355 | +2,695 | +6.97 |
| a | 12 | 76 | 3.8 | +1,210 | +1,415 | +2,625 | +6.84 |
| p | 9 | 38 | 3.9 | -3,655 | +1,310 | -2,345 | -5.94 |
| pg | 6 | 7 | 0.9 | +2,000 | +170 | +2,170 | +24.42 |
| rb | 13 | 280 | 8.8 | -1,090 | -1,070 | -2,160 | -2.46 |
| br | 3 | 6 | 0.5 | +1,800 | +125 | +1,925 | +42.11 |
| cs | 14 | 215 | 5.6 | -600 | +2,445 | +1,845 | +3.29 |
| other (32) | - | 1768 | 99.3 | -6,355 | +7,490 | +1,135 | +0.11 |
| all products | - | 3213 | 178.3 | -10,598 | +16,220 | +5,622 | +0.32 |
ranked by |all-in| over the live window (all-in = drift + exec = the bridge's exec_cost by product); product bps are vs traded notional

## Per strategy
| strategy | live? | bt 2026 pnl (full) | bt scaled+weighted (live window) | live attributed | note |
|---|---|---|---|---|---|
| Calendar main pool (branch) | yes | +561,175 | +24,497 | +46,785 | forward w=0.8 |
| Fundamental factor | yes | +683,453 | +106,310 | +74,264 | forward w=2 |
| Cross-product pairs | yes | +130,920 | +26,041 | -8,052 | forward w=1.5 |
| Calendar extended pool | yes | +566,110 | -212 | +6,966 | forward w=0.25 |
| Chemical fundamental | yes | +426,260 | -743 | -20,387 | forward w=1.5 |
| Agriculture event-driven | yes | +144,185 | +5,082 | +5,595 | forward w=1 |
| Factor-neutral stat arb | yes | +270,979 | -11,220 | -10,191 | forward w=1 |
| shared bucket | - | - | - | -9,870 | legacy multi-holder / forward offsetting |
| neither bucket (no target) | - | - | - | -4,605 | inherited/manual/rounding |
forward-day attribution is pro-rated by weighted full-size lots; legacy days remain exclusive-holder.

## Per strategy gap by day, last 10 reconciled days (live attributed - expected, CNY)
| day | ks_branch | fund_v3 | china_pairs | ks_ext | chem_fund | agri_event | stat_arb | total |
|---|---|---|---|---|---|---|---|---|
| 2026-08-24 | +3,066 | +682 | +0 | +0 | +0 | +0 | +0 | +3,749 |
| 2026-08-25 | +7,289 | -737 | +0 | +0 | +0 | +0 | +0 | +6,552 |
| 2026-08-26 | -4,102 | +3,347 | +0 | +0 | +0 | +0 | +0 | -755 |
| 2026-08-27 | -10,253 | -7,970 | +0 | +0 | +0 | +0 | +0 | -18,223 |
| 2026-08-31 | +413 | +49,833 | -2,804 | +0 | -19,031 | +1,960 | +244 | +30,614 |
| 2026-09-01 | +17,681 | -29,415 | -2,790 | +54 | -9,023 | -4,782 | -3,186 | -31,459 |
| 2026-09-02 | +13,512 | -99,657 | -22,485 | +1,282 | +15,964 | +426 | +0 | -90,958 |
| 2026-09-03 | -12,509 | +43,683 | -4,578 | +2,302 | -12,407 | +7,612 | +5,220 | +29,323 |
| 2026-09-04 | +6,112 | +10,838 | -9,893 | -1,861 | -6,843 | +1,891 | -4,736 | -4,492 |
| 2026-09-07 | +10,211 | -174 | +8,457 | +5,402 | +11,696 | -6,594 | +3,487 | +32,484 |
| sum | +31,420 | -29,569 | -34,093 | +7,179 | -19,644 | +513 | +1,030 | -43,164 |
full series: data/per_strategy_daily.csv (day, strategy, expected, attributed, gap); a strategy's daily total foots to expected - live_gross once the shared and neither buckets are added.

## Data health
scale: 0.5 (since 2026-09-01)
regime: forward (merged weighted book) since 2026-08-31; 6 forward day(s), 8 legacy day(s)
merge weights (2026-09-08): ks_branch 0.8, fund_v3 2, china_pairs 1.5, ks_ext 0.25, chem_fund 1.5, agri_event 1, stat_arb 1
as-shipped pins: 15 live day(s) pinned; current series diverges from pins on fund_v3: 11 day(s), max 22,922 CNY, ks_branch: 9 day(s), max 35,915 CNY, stat_arb: 11 day(s), max 7,622 CNY, ks_ext: 2 day(s), max 950 CNY, agri_event: 4 day(s), max 5,680 CNY; standing counts -- a divergence is announced as an alert once, the first run it appears, and kept here afterwards
inbox ks summary mtime: 2026-09-08 05:52 UTC
