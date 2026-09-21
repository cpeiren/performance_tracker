# Performance tracker - 2026-09-21   (reconciled through 2026-09-18)

## ALERTS
- BT PENDING 2026-09-21: no mature backtest row for stat_arb (nonzero weight) -- day held out of the bridge until the rows ship; it re-enters automatically.
- WEIGHTS CHANGE on 2026-09-01: ks_ext: 0.0->0.25.
- WEIGHTS CHANGE on 2026-09-02: stat_arb: 1.0->0.0.
- WEIGHTS CHANGE on 2026-09-03: stat_arb: 0.0->1.0.
- MISSING LIVE DAY 2026-08-28: trading day with a backtest row but no daily_pnl/state file; excluded from the bridge, expected pnl held in the missing-day bucket.
- SCALE 2026-08-28: no usable run record; previous scale carried forward.
- SCALE CHANGE on 2026-08-27: now 0.2.
- SCALE CHANGE on 2026-09-01: now 0.5.
- SCALE CHANGE on 2026-09-09: now 1.
- SLIPPAGE 2026-09-21: 4 unbenchmarked leg(s), +750 CNY exec cost without a shipped decision price.
- RESIDUAL 2026-08-27: -17267 CNY vs trailing median |resid| 2062, offset by neither neighbour (2026-08-26 +3749, 2026-08-31 -17348) -- attribution quality changed. (A break-out that a neighbouring day mirrors is the backtest/live day-window straddle and is not alerted.)
- RESIDUAL 2026-08-31: -17348 CNY vs trailing median |resid| 2277, offset by neither neighbour (2026-08-27 -17267, 2026-09-01 -8190) -- attribution quality changed. (A break-out that a neighbouring day mirrors is the backtest/live day-window straddle and is not alerted.)
- RESIDUAL 2026-09-01: -8190 CNY vs trailing median |resid| 2492, offset by neither neighbour (2026-08-31 -17348, 2026-09-02 -30063) -- attribution quality changed. (A break-out that a neighbouring day mirrors is the backtest/live day-window straddle and is not alerted.)
- RESIDUAL 2026-09-02: -30063 CNY vs trailing median |resid| 3121, offset by neither neighbour (2026-09-01 -8190, 2026-09-03 -29049) -- attribution quality changed. (A break-out that a neighbouring day mirrors is the backtest/live day-window straddle and is not alerted.)
- RESIDUAL 2026-09-03: -29049 CNY vs trailing median |resid| 3941, offset by neither neighbour (2026-09-02 -30063, 2026-09-04 -5584) -- attribution quality changed. (A break-out that a neighbouring day mirrors is the backtest/live day-window straddle and is not alerted.)
- RESIDUAL 2026-09-16: -103509 CNY vs trailing median |resid| 22936, offset by neither neighbour (2026-09-15 -28634, 2026-09-17 +23811) -- attribution quality changed. (A break-out that a neighbouring day mirrors is the backtest/live day-window straddle and is not alerted.)

## Latest reconciled day (2026-09-18, forward regime, settled)
live gross -103,055 | expected (1 x bt -60,354) = -60,354 | gap -42,701
  exec_cost +1,220 (slip +1,185, unbench +35) | marking -42,690 | bookdiff +0 (carry +0, new +0) | intraday +0 | offbook +0 (0 contract(s)) | residual +1,209 (live re-marked to first decision, vs the previous backtest row)
  fees +1,434 | broker residual +3 -> live net -104,486

## Cumulative bridge (live since 2026-08-18, 23 reconciled days)
| expected | -exec | +marking | +bookdiff | +intraday | +offbook | +resid | = live gross | -fees | +broker_resid | = live net |
|---|---|---|---|---|---|---|---|---|---|---|
| +241,053 | +6,105 | -32,540 | +88,792 | -2,108 | -50 | -135,482 | +165,770 | -21,598 | +143 | +144,315 |
missing live days excluded: 2026-08-28 (expected +4,849 held in bucket)

## Stats (daily CNY pnl)
| window | days | total | sharpe | mdd | hit |
|---|---|---|---|---|---|
| live net live-to-date | 23 | +144,315 | 1.71 | -218,287 | 57% | (small sample)
| live net last-20d | 20 | +140,742 | 1.78 | -218,287 | 55% | (small sample)
| live net 2026-YTD | 23 | +144,315 | 1.71 | -218,287 | 57% | (small sample)
| bt scaled live-to-date | 23 | +241,053 | 2.91 | -192,490 | 70% | (small sample)
| bt scaled last-20d | 20 | +237,999 | 3.08 | -192,490 | 65% | (small sample)
| bt scaled 2026-YTD | 23 | +241,053 | 2.91 | -192,490 | 70% | (small sample)

## Slippage (+ = cost; bps vs benchmarked notional)
| day | lots | notional M | slip total | drift | exec | bps | unbench legs | unbench CNY |
|---|---|---|---|---|---|---|---|---|
| 2026-09-08 | 286 | 21.3 | +7,165 | +7,250 | -85 | +3.58 | 5 | +135 |
| 2026-09-09 | 909 | 61.5 | -695 | -5,608 | +4,912 | -0.11 | 9 | +75 |
| 2026-09-10 | 319 | 16.6 | +20 | -132 | +152 | +0.01 | 1 | +15 |
| 2026-09-11 | 315 | 16.0 | +2,620 | +1,885 | +735 | +1.65 | 1 | +45 |
| 2026-09-14 | 854 | 51.8 | -2,855 | -4,120 | +1,265 | -0.55 | 2 | +40 |
| 2026-09-15 | 596 | 51.4 | -7,045 | -10,212 | +3,168 | -1.46 | 3 | -110 |
| 2026-09-16 | 855 | 61.8 | -8,925 | -12,015 | +3,090 | -1.53 | 5 | -145 |
| 2026-09-17 | 382 | 21.0 | +3,490 | +1,630 | +1,860 | +2.14 | 8 | +522 |
| 2026-09-18 | 597 | 37.1 | +1,185 | +32 | +1,152 | +0.34 | 6 | +35 |
| 2026-09-21 | 370 | 29.7 | +1,965 | -735 | +2,700 | +0.74 | 4 | +750 |
| live window (24d) | 8410 | 525.2 | -14,785 | -39,872 | +25,088 | -0.31 | 170 | +11,395 |
exec-only bps over the window: +0.53; benchmark coverage 89% of traded notional

| product | days | lots | notional M | drift | exec (incl. unbench) | all-in | bps |
|---|---|---|---|---|---|---|---|
| IH | 12 | 58 | 49.0 | -21,540 | +3,420 | -18,120 | -3.69 |
| rb | 21 | 701 | 21.9 | +18,275 | -2,785 | +15,490 | +7.08 |
| IF | 8 | 40 | 52.9 | -11,670 | +1,110 | -10,560 | -2.00 |
| PF | 16 | 92 | 3.8 | -8,495 | +260 | -8,235 | -21.75 |
| hc | 20 | 867 | 29.0 | -12,335 | +4,135 | -8,200 | -2.83 |
| zn | 17 | 191 | 25.4 | -6,888 | +175 | -6,712 | -2.65 |
| cs | 23 | 411 | 10.5 | +3,170 | +3,055 | +6,225 | +5.90 |
| FG | 23 | 397 | 7.5 | +4,580 | +1,560 | +6,140 | +8.18 |
| SF | 22 | 199 | 6.1 | +5,440 | +415 | +5,855 | +9.56 |
| b | 17 | 320 | 13.2 | -7,680 | +3,150 | -4,530 | -3.42 |
| cu | 8 | 26 | 14.2 | -5,150 | +650 | -4,500 | -3.17 |
| eg | 11 | 25 | 1.4 | +4,355 | +95 | +4,450 | +32.93 |
| y | 20 | 136 | 12.2 | +2,745 | +1,525 | +4,270 | +3.50 |
| al | 18 | 213 | 25.7 | +1,625 | +2,312 | +3,938 | +1.53 |
| pb | 16 | 318 | 25.6 | +2,550 | +1,275 | +3,825 | +1.49 |
| other (34) | - | 4416 | 226.8 | -8,855 | +16,130 | +7,275 | +0.32 |
| all products | - | 8410 | 525.2 | -39,872 | +36,482 | -3,390 | -0.06 |
ranked by |all-in| over the live window (all-in = drift + exec = the bridge's exec_cost by product); product bps are vs traded notional

## Per strategy
| strategy | live? | bt 2026 pnl (full) | bt scaled+weighted (live window) | live attributed | note |
|---|---|---|---|---|---|
| Calendar main pool (branch) | yes | +561,990 | +15,777 | +135,164 | forward w=0.8 |
| Fundamental factor | yes | +760,598 | +280,637 | +152,849 | forward w=2 |
| Cross-product pairs | yes | +111,345 | +19,163 | -16,949 | forward w=1.5 |
| Calendar extended pool | yes | +358,965 | +1,897 | +52,590 | forward w=0.25 |
| Chemical fundamental | yes | +420,300 | +20,598 | -33,007 | forward w=1.5 |
| Agriculture event-driven | yes | +120,720 | -40,083 | -5,106 | forward w=1 |
| Factor-neutral stat arb | yes | +249,494 | -56,936 | -80,996 | forward w=1 |
| shared bucket | - | - | - | -35,545 | legacy multi-holder / forward offsetting (split refused, not a cost) |
| neither bucket (no target) | - | - | - | -3,230 | named by no book that day or the day before |
forward-day attribution is pro-rated by weighted full-size lots; legacy days remain exclusive-holder. A contract the day's own books do not name resolves against the previous same-regime day, so a roll-out's exit P&L is charged to whoever held it.

## Live P&L by strategy, last 10 reconciled days (attributed gross CNY)
| day | ks_branch | fund_v3 | china_pairs | ks_ext | chem_fund | agri_event | stat_arb | shared | neither | total |
|---|---|---|---|---|---|---|---|---|---|---|
| 2026-09-07 | +11,861 | +12,714 | +1,573 | +4,535 | -4,325 | -1,735 | -3,138 | +2,800 | +0 | +24,285 |
| 2026-09-08 | +33,217 | +9,824 | -107 | +4,299 | +7,680 | +2,967 | -5,824 | +3,850 | +0 | +55,905 |
| 2026-09-09 | +10,781 | -15,894 | -7,210 | +2,903 | -9,139 | +1,364 | -3,664 | +2,735 | +0 | -18,125 |
| 2026-09-10 | +8,153 | -2,745 | -5,986 | +12,583 | +26,171 | -8,482 | +14,125 | -4,810 | +0 | +39,010 |
| 2026-09-11 | +25,179 | +108,588 | +12,217 | +64,705 | +13,268 | -1,343 | -14,799 | +925 | +0 | +208,740 |
| 2026-09-14 | +79,654 | -36,097 | -16,641 | +8,446 | -7,254 | +2,408 | -15,405 | -29,965 | +0 | -14,855 |
| 2026-09-15 | -42,941 | +30,807 | -2,310 | -75,588 | -12,853 | +1,020 | -2,841 | +12,925 | +0 | -91,780 |
| 2026-09-16 | +3,527 | +33,527 | +2,266 | +25,850 | +7,170 | -3,416 | -28,428 | -5,640 | +0 | +34,855 |
| 2026-09-17 | -20,273 | +17,342 | +8,734 | +8,207 | -17,932 | -2,113 | -18,535 | -9,530 | +0 | -34,100 |
| 2026-09-18 | -12,017 | -66,793 | +9,710 | -4,925 | -26,003 | -2,361 | -11,001 | +10,335 | +0 | -103,055 |
| sum | +97,141 | +91,274 | +2,245 | +51,015 | -23,218 | -11,691 | -89,511 | -16,375 | +0 | +100,880 |
forward days pro-rate each contract's live P&L by weighted full-size lots; total foots to live gross. Live-window sums: 'Per strategy' above; full series: data/per_strategy_daily.csv (attributed)

## Per strategy gap by day, last 10 reconciled days (live attributed - expected, CNY)
| day | ks_branch | fund_v3 | china_pairs | ks_ext | chem_fund | agri_event | stat_arb | total |
|---|---|---|---|---|---|---|---|---|
| 2026-09-07 | +14,497 | -13,469 | +5,034 | +4,322 | +5,238 | -5,895 | +5,002 | +14,729 |
| 2026-09-08 | +19,225 | -11,154 | -6,827 | +6,538 | -1,317 | -623 | -2,665 | +3,177 |
| 2026-09-09 | -7,595 | -33,341 | +11,030 | +264 | -7,384 | +264 | -11,081 | -47,843 |
| 2026-09-10 | +23,009 | -15,227 | -6,098 | +8,543 | +17,433 | -3,382 | +6,600 | +30,878 |
| 2026-09-11 | +29,683 | -84,428 | -16 | +65,014 | +9,555 | +5,657 | -12,742 | +12,723 |
| 2026-09-14 | +88,782 | +2,617 | -3,914 | +12,671 | -31,479 | +21,428 | -14,504 | +75,601 |
| 2026-09-15 | -6,961 | +12,550 | +2,625 | -76,468 | -58 | +13,975 | +6,862 | -47,474 |
| 2026-09-16 | -19,513 | +4,940 | +8,956 | +14,358 | +10,627 | +11,524 | -2,421 | +28,471 |
| 2026-09-17 | -11,597 | +19,432 | -2,058 | +14,258 | -9,885 | +1,927 | -10,209 | +1,868 |
| 2026-09-18 | -21,265 | +8,897 | +3,852 | -809 | -27,728 | -15,561 | -423 | -53,036 |
| sum | +108,265 | -109,183 | +12,584 | +48,692 | -34,997 | +29,314 | -35,580 | +19,096 |
full series: data/per_strategy_daily.csv (day, strategy, expected, attributed, gap); a strategy's daily total foots to expected - live_gross once the shared and neither buckets are added.

## Live P&L by product, last 10 reconciled days (gross CNY, worst first)
| product | 09-07 | 09-08 | 09-09 | 09-10 | 09-11 | 09-14 | 09-15 | 09-16 | 09-17 | 09-18 | 10d sum | live window |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| bu | -2,750 | -1,280 | -1,300 | -4,020 | -10,100 | -24,440 | -34,350 | -13,360 | -16,680 | -20,460 | -128,740 | -137,730 |
| hc | -2,150 | +2,690 | +1,920 | -24,030 | -38,740 | -36,660 | +830 | +7,090 | +8,640 | -37,360 | -117,770 | -124,400 |
| CF | +150 | +975 | -100 | -6,425 | -7,900 | -8,575 | -18,450 | -8,225 | -10,050 | -7,250 | -65,850 | -68,475 |
| pp | +2,595 | -680 | +1,015 | -28,720 | +510 | -2,050 | -1,960 | +1,570 | -9,930 | +6,805 | -30,845 | -35,525 |
| y | +1,420 | +10,620 | -8,520 | -14,550 | +6,760 | -11,240 | -7,760 | +6,560 | -1,160 | -9,440 | -27,310 | -24,510 |
| c | -1,280 | +790 | -2,120 | -6,040 | -2,600 | -4,020 | -5,120 | -1,050 | -1,580 | -680 | -23,700 | -19,990 |
| p | +6,760 | +12,900 | -4,880 | -15,310 | +5,330 | -16,810 | -11,090 | +890 | -970 | -410 | -23,590 | -12,290 |
| IF | -480 | +3,180 | +6,240 | +8,460 | +15,480 | +6,480 | -65,940 | +6,540 | +6,300 | -6,300 | -20,040 | -18,840 |
| v | -430 | +435 | +280 | +3,485 | -1,205 | -4,600 | -330 | -5,295 | +425 | -11,615 | -18,850 | -1,710 |
| lh | -480 | +640 | -1,920 | -4,800 | -2,880 | -1,440 | -8,640 | +1,440 | -320 | +3,360 | -15,040 | -14,880 |
| ni | +80 | -1,470 | +2,060 | +2,670 | -6,360 | -2,380 | -3,380 | -6,960 | +970 | +4,230 | -10,540 | -12,270 |
| br | +500 | -700 | -2,025 | -2,250 | -200 | +350 | -650 | -850 | -2,400 | +750 | -7,475 | -7,525 |
| ss | +850 | -1,000 | -375 | +1,625 | -15,600 | -4,250 | +400 | -2,750 | +8,500 | +6,225 | -6,375 | -6,375 |
| MA | +940 | +1,160 | -2,460 | +5,960 | +3,480 | -3,200 | -4,610 | -6,170 | +690 | -1,770 | -5,980 | -5,970 |
| SH | +1,890 | -120 | -30 | +120 | -120 | -5,400 | -1,050 | -1,890 | +420 | +660 | -5,520 | -5,460 |
| other (24) | +12,230 | +24,045 | -2,885 | +46,100 | +61,795 | -11,825 | +12,790 | +24,490 | -14,650 | -65,285 | +86,805 | +149,290 |
| l | -2,730 | +4,915 | +1,275 | +27,585 | +3,050 | -200 | -10,735 | +5,445 | -9,270 | -775 | +18,560 | +37,265 |
| SA | -3,260 | +5,580 | -1,160 | +2,100 | -2,740 | +15,080 | +3,460 | -100 | -1,540 | +2,200 | +19,620 | +12,560 |
| zn | -10,775 | -16,575 | -5,225 | -15,000 | +68,550 | +21,625 | +22,525 | -3,600 | +1,750 | -27,325 | +35,950 | +36,225 |
| PF | -550 | +1,350 | +510 | +2,270 | +1,220 | +1,470 | +200 | +11,530 | +1,240 | +17,710 | +36,950 | +47,190 |
| IH | +960 | -1,440 | -1,140 | +4,320 | +43,860 | +300 | -12,300 | +11,700 | -1,500 | -7,260 | +37,500 | +35,880 |
| fu | +600 | +190 | +730 | -600 | +15,360 | +5,450 | +14,310 | +7,620 | -3,700 | -2,360 | +37,600 | +33,060 |
| SF | +13,280 | +6,400 | +6,800 | +4,620 | +10,770 | -500 | +2,350 | +820 | -990 | +3,860 | +47,410 | +13,350 |
| CY | -2,325 | +1,100 | +475 | -1,150 | -1,450 | +8,500 | +17,600 | +14,500 | +4,575 | +6,425 | +48,250 | +49,050 |
| rb | -400 | -2,870 | -3,050 | +24,800 | +43,910 | +31,050 | +1,260 | -10,520 | -3,390 | +35,620 | +116,410 | +128,500 |
| cs | +9,640 | +5,070 | -2,240 | +27,790 | +18,560 | +32,430 | +18,860 | -4,570 | +10,520 | +7,390 | +123,450 | +119,350 |
| all products | +24,285 | +55,905 | -18,125 | +39,010 | +208,740 | -14,855 | -91,780 | +34,855 | -34,100 | -103,055 | +100,880 | +165,770 |
executor total_pnl (holding + trading, settlement-to-settlement once the next capture lands, before fees) summed by product root; 'all products' foots to live gross. Full series: data/product_daily.csv

## Data health
decision-price coverage (2026-09-18): 100% of held notional benchmarked (1 contract(s) unbenchmarked); 10 contract(s) (18%) first decided after the 0900 snap, so they straddle their own overnight leg
scale: 1 (since 2026-09-09)
regime: forward (merged weighted book) since 2026-08-31; 15 forward day(s), 8 legacy day(s)
merge weights (2026-09-21): ks_branch 0.8, fund_v3 2, china_pairs 1.5, ks_ext 0.25, chem_fund 1.5, agri_event 1, stat_arb 1
as-shipped pins: 24 live day(s) pinned; current series diverges from pins on fund_v3: 21 day(s), max 22,676 CNY, ks_branch: 20 day(s), max 33,735 CNY, ks_ext: 19 day(s), max 42,170 CNY, stat_arb: 14 day(s), max 10,719 CNY, china_pairs: 17 day(s), max 2,120 CNY, agri_event: 5 day(s), max 5,680 CNY, chem_fund: 1 day(s), max 20 CNY; standing counts -- a divergence is announced as an alert once, the first run it appears, and kept here afterwards
inbox ks summary mtime: 2026-09-21 05:53 UTC
