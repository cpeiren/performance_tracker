# Performance tracker - 2026-09-18   (reconciled through 2026-09-17)

## ALERTS
- BT PENDING 2026-09-18: no mature backtest row for stat_arb (nonzero weight) -- day held out of the bridge until the rows ship; it re-enters automatically.
- WEIGHTS CHANGE on 2026-09-01: ks_ext: 0.0->0.25.
- WEIGHTS CHANGE on 2026-09-02: stat_arb: 1.0->0.0.
- WEIGHTS CHANGE on 2026-09-03: stat_arb: 0.0->1.0.
- MISSING LIVE DAY 2026-08-28: trading day with a backtest row but no daily_pnl/state file; excluded from the bridge, expected pnl held in the missing-day bucket.
- SCALE 2026-08-28: no usable run record; previous scale carried forward.
- SCALE CHANGE on 2026-08-27: now 0.2.
- SCALE CHANGE on 2026-09-01: now 0.5.
- SCALE CHANGE on 2026-09-09: now 1.
- SLIPPAGE 2026-09-18: 6 unbenchmarked leg(s), +35 CNY exec cost without a shipped decision price.
- RESIDUAL 2026-08-27: -17267 CNY vs trailing median |resid| 2062, offset by neither neighbour (2026-08-26 +3749, 2026-08-31 -17348) -- attribution quality changed. (A break-out that a neighbouring day mirrors is the backtest/live day-window straddle and is not alerted.)
- RESIDUAL 2026-08-31: -17348 CNY vs trailing median |resid| 2277, offset by neither neighbour (2026-08-27 -17267, 2026-09-01 -8190) -- attribution quality changed. (A break-out that a neighbouring day mirrors is the backtest/live day-window straddle and is not alerted.)
- RESIDUAL 2026-09-01: -8190 CNY vs trailing median |resid| 2492, offset by neither neighbour (2026-08-31 -17348, 2026-09-02 -30063) -- attribution quality changed. (A break-out that a neighbouring day mirrors is the backtest/live day-window straddle and is not alerted.)
- RESIDUAL 2026-09-02: -30063 CNY vs trailing median |resid| 3121, offset by neither neighbour (2026-09-01 -8190, 2026-09-03 -29049) -- attribution quality changed. (A break-out that a neighbouring day mirrors is the backtest/live day-window straddle and is not alerted.)
- RESIDUAL 2026-09-03: -29049 CNY vs trailing median |resid| 3941, offset by neither neighbour (2026-09-02 -30063, 2026-09-04 -5584) -- attribution quality changed. (A break-out that a neighbouring day mirrors is the backtest/live day-window straddle and is not alerted.)
- RESIDUAL 2026-09-16: -103509 CNY vs trailing median |resid| 22936, offset by neither neighbour (2026-09-15 -28634, 2026-09-17 +23811) -- attribution quality changed. (A break-out that a neighbouring day mirrors is the backtest/live day-window straddle and is not alerted.)

## Latest reconciled day (2026-09-17, forward regime, settled)
live gross -34,100 | expected (1 x bt -26,438) = -26,438 | gap -7,662
  exec_cost +4,012 (slip +3,490, unbench +522) | marking -27,460 | bookdiff +0 (carry +0, new +0) | intraday +0 | offbook +0 (0 contract(s)) | residual +23,811 (live re-marked to first decision, vs the previous backtest row)
  fees +953 | broker residual +10 -> live net -35,042

## Cumulative bridge (live since 2026-08-18, 22 reconciled days)
| expected | -exec | +marking | +bookdiff | +intraday | +offbook | +resid | = live gross | -fees | +broker_resid | = live net |
|---|---|---|---|---|---|---|---|---|---|---|
| +301,407 | +7,325 | +10,150 | +88,792 | -2,108 | -50 | -136,691 | +268,825 | -20,164 | +140 | +248,801 |
missing live days excluded: 2026-08-28 (expected +4,849 held in bucket)

## Stats (daily CNY pnl)
| window | days | total | sharpe | mdd | hit |
|---|---|---|---|---|---|
| live net live-to-date | 22 | +248,801 | 3.31 | -113,801 | 59% | (small sample)
| live net last-20d | 20 | +248,204 | 3.46 | -113,801 | 60% | (small sample)
| live net 2026-YTD | 22 | +248,801 | 3.31 | -113,801 | 59% | (small sample)
| bt scaled live-to-date | 22 | +301,407 | 3.86 | -132,136 | 73% | (small sample)
| bt scaled last-20d | 20 | +300,163 | 4.03 | -132,136 | 70% | (small sample)
| bt scaled 2026-YTD | 22 | +301,407 | 3.86 | -132,136 | 73% | (small sample)

## Slippage (+ = cost; bps vs benchmarked notional)
| day | lots | notional M | slip total | drift | exec | bps | unbench legs | unbench CNY |
|---|---|---|---|---|---|---|---|---|
| 2026-09-07 | 200 | 12.6 | +4,090 | +3,312 | +778 | +3.31 | 3 | +140 |
| 2026-09-08 | 286 | 21.3 | +7,165 | +7,250 | -85 | +3.58 | 5 | +135 |
| 2026-09-09 | 909 | 61.5 | -695 | -5,608 | +4,912 | -0.11 | 9 | +75 |
| 2026-09-10 | 319 | 16.6 | +20 | -132 | +152 | +0.01 | 1 | +15 |
| 2026-09-11 | 315 | 16.0 | +2,620 | +1,885 | +735 | +1.65 | 1 | +45 |
| 2026-09-14 | 854 | 51.8 | -2,855 | -4,120 | +1,265 | -0.55 | 2 | +40 |
| 2026-09-15 | 596 | 51.4 | -7,045 | -10,212 | +3,168 | -1.46 | 3 | -110 |
| 2026-09-16 | 855 | 61.8 | -8,925 | -12,015 | +3,090 | -1.53 | 5 | -145 |
| 2026-09-17 | 382 | 21.0 | +3,490 | +1,630 | +1,860 | +2.14 | 8 | +522 |
| 2026-09-18 | 597 | 37.1 | +1,185 | +32 | +1,152 | +0.34 | 6 | +35 |
| live window (23d) | 8040 | 495.5 | -16,750 | -39,138 | +22,388 | -0.38 | 166 | +10,645 |
exec-only bps over the window: +0.51; benchmark coverage 89% of traded notional

| product | days | lots | notional M | drift | exec (incl. unbench) | all-in | bps |
|---|---|---|---|---|---|---|---|
| IH | 11 | 48 | 40.6 | -20,850 | +2,250 | -18,600 | -4.58 |
| rb | 21 | 701 | 21.9 | +18,275 | -2,785 | +15,490 | +7.08 |
| IF | 7 | 36 | 47.6 | -11,640 | +1,080 | -10,560 | -2.22 |
| PF | 15 | 91 | 3.7 | -8,490 | +255 | -8,235 | -22.00 |
| hc | 20 | 867 | 29.0 | -12,335 | +4,135 | -8,200 | -2.83 |
| zn | 17 | 191 | 25.4 | -6,888 | +175 | -6,712 | -2.65 |
| cs | 22 | 398 | 10.2 | +3,335 | +3,000 | +6,335 | +6.19 |
| SF | 21 | 198 | 6.1 | +5,465 | +420 | +5,885 | +9.66 |
| FG | 22 | 374 | 7.1 | +4,550 | +1,290 | +5,840 | +8.25 |
| y | 19 | 133 | 11.9 | +3,100 | +1,520 | +4,620 | +3.87 |
| cu | 8 | 26 | 14.2 | -5,150 | +650 | -4,500 | -3.17 |
| pb | 15 | 288 | 23.1 | +3,050 | +1,175 | +4,225 | +1.83 |
| al | 18 | 213 | 25.7 | +1,625 | +2,312 | +3,938 | +1.53 |
| fu | 15 | 55 | 2.3 | -3,975 | +95 | -3,880 | -17.10 |
| br | 8 | 18 | 1.4 | +3,300 | +75 | +3,375 | +24.54 |
| other (34) | - | 4403 | 225.3 | -12,510 | +17,385 | +4,875 | +0.22 |
| all products | - | 8040 | 495.5 | -39,138 | +33,032 | -6,105 | -0.12 |
ranked by |all-in| over the live window (all-in = drift + exec = the bridge's exec_cost by product); product bps are vs traded notional

## Per strategy
| strategy | live? | bt 2026 pnl (full) | bt scaled+weighted (live window) | live attributed | note |
|---|---|---|---|---|---|
| Calendar main pool (branch) | yes | +621,315 | +6,529 | +162,853 | forward w=0.8 |
| Fundamental factor | yes | +773,179 | +356,326 | +246,384 | forward w=2 |
| Cross-product pairs | yes | +116,990 | +13,306 | -23,222 | forward w=1.5 |
| Calendar extended pool | yes | +423,530 | +6,013 | +57,362 | forward w=0.25 |
| Chemical fundamental | yes | +434,470 | +18,873 | -6,484 | forward w=1.5 |
| Agriculture event-driven | yes | +80,705 | -53,283 | -2,745 | forward w=1 |
| Factor-neutral stat arb | yes | +260,073 | -46,357 | -68,078 | forward w=1 |
| shared bucket | - | - | - | -43,565 | legacy multi-holder / forward offsetting |
| neither bucket (no target) | - | - | - | -53,680 | inherited/manual/rounding |
forward-day attribution is pro-rated by weighted full-size lots; legacy days remain exclusive-holder.

## Live P&L by strategy, last 10 reconciled days (attributed gross CNY)
| day | ks_branch | fund_v3 | china_pairs | ks_ext | chem_fund | agri_event | stat_arb | shared | neither | total |
|---|---|---|---|---|---|---|---|---|---|---|
| 2026-09-04 | -1,745 | -15,118 | -9,587 | +208 | -7,639 | +516 | -1,020 | +7,025 | -1,300 | -28,660 |
| 2026-09-07 | +11,861 | +12,714 | +1,573 | +4,602 | -4,325 | -1,735 | -2,445 | +2,800 | -760 | +24,285 |
| 2026-09-08 | +31,797 | +12,901 | +1,167 | +4,299 | +7,680 | +2,967 | -5,805 | +3,850 | -2,950 | +55,905 |
| 2026-09-09 | +10,781 | -15,894 | -7,210 | +2,903 | -5,759 | +1,364 | -3,664 | +2,735 | -3,380 | -18,125 |
| 2026-09-10 | +8,153 | -2,745 | -5,986 | +12,583 | +26,171 | -8,482 | +14,125 | -4,810 | +0 | +39,010 |
| 2026-09-11 | +25,179 | +108,588 | +12,217 | +64,705 | +13,268 | -1,343 | -14,799 | +925 | +0 | +208,740 |
| 2026-09-14 | +79,654 | -34,357 | -16,641 | +8,446 | -6,594 | +2,408 | -11,405 | -29,965 | -6,400 | -14,855 |
| 2026-09-15 | -42,941 | +39,447 | -2,310 | -77,028 | -12,853 | +1,020 | -2,841 | +12,925 | -7,200 | -91,780 |
| 2026-09-16 | +29,645 | +34,877 | +2,266 | +28,070 | +7,170 | -3,416 | -26,475 | -5,640 | -31,640 | +34,855 |
| 2026-09-17 | -28,037 | +25,676 | +7,972 | +8,207 | -21,232 | -2,113 | -16,383 | -10,205 | +2,015 | -34,100 |
| sum | +124,346 | +166,089 | -16,539 | +56,994 | -4,114 | -8,814 | -70,712 | -20,360 | -51,615 | +175,275 |
forward days pro-rate each contract's live P&L by weighted full-size lots; total foots to live gross. Live-window sums: 'Per strategy' above; full series: data/per_strategy_daily.csv (attributed)

## Per strategy gap by day, last 10 reconciled days (live attributed - expected, CNY)
| day | ks_branch | fund_v3 | china_pairs | ks_ext | chem_fund | agri_event | stat_arb | total |
|---|---|---|---|---|---|---|---|---|
| 2026-09-04 | -3,117 | +5,305 | -9,831 | -2,502 | -5,183 | -14 | -420 | -15,762 |
| 2026-09-07 | +14,497 | -13,469 | +5,034 | +4,389 | +5,238 | -5,895 | +5,696 | +15,489 |
| 2026-09-08 | +17,805 | -8,077 | -5,553 | +6,538 | -1,317 | -623 | -2,646 | +6,127 |
| 2026-09-09 | -7,595 | -33,341 | +11,030 | +264 | -4,004 | +264 | -11,081 | -44,463 |
| 2026-09-10 | +23,009 | -15,227 | -6,098 | +8,543 | +17,433 | -3,382 | +6,600 | +30,878 |
| 2026-09-11 | +29,683 | -84,428 | -16 | +65,014 | +9,555 | +5,657 | -12,742 | +12,723 |
| 2026-09-14 | +88,782 | +4,357 | -3,914 | +12,671 | -30,819 | +21,428 | -10,504 | +82,001 |
| 2026-09-15 | -6,961 | +21,190 | +2,625 | -77,908 | -58 | +13,975 | +6,862 | -40,274 |
| 2026-09-16 | +6,605 | +6,290 | +8,956 | +16,578 | +10,627 | +11,524 | -469 | +60,111 |
| 2026-09-17 | -19,361 | +27,766 | -2,820 | +14,258 | -13,185 | +1,927 | -8,057 | +528 |
| sum | +143,346 | -89,634 | -587 | +47,846 | -11,711 | +44,861 | -26,760 | +107,360 |
full series: data/per_strategy_daily.csv (day, strategy, expected, attributed, gap); a strategy's daily total foots to expected - live_gross once the shared and neither buckets are added.

## Live P&L by product, last 10 reconciled days (gross CNY, worst first)
| product | 09-04 | 09-07 | 09-08 | 09-09 | 09-10 | 09-11 | 09-14 | 09-15 | 09-16 | 09-17 | 10d sum | live window |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| bu | -950 | -2,750 | -1,280 | -1,300 | -4,020 | -10,100 | -24,440 | -34,350 | -13,360 | -16,680 | -109,230 | -117,270 |
| hc | +9,930 | -2,150 | +2,690 | +1,920 | -24,030 | -38,740 | -36,660 | +830 | +7,090 | +8,640 | -70,480 | -87,040 |
| CF | -2,050 | +150 | +975 | -100 | -6,425 | -7,900 | -8,575 | -18,450 | -8,225 | -10,050 | -60,650 | -61,225 |
| pp | -4,245 | +2,595 | -680 | +1,015 | -28,720 | +510 | -2,050 | -1,960 | +1,570 | -9,930 | -41,895 | -42,330 |
| p | -1,330 | +6,760 | +12,900 | -4,880 | -15,310 | +5,330 | -16,810 | -11,090 | +890 | -970 | -24,510 | -11,880 |
| c | +1,230 | -1,280 | +790 | -2,120 | -6,040 | -2,600 | -4,020 | -5,120 | -1,050 | -1,580 | -21,790 | -19,310 |
| lh | +560 | -480 | +640 | -1,920 | -4,800 | -2,880 | -1,440 | -8,640 | +1,440 | -320 | -17,840 | -18,240 |
| y | +850 | +1,420 | +10,620 | -8,520 | -14,550 | +6,760 | -11,240 | -7,760 | +6,560 | -1,160 | -17,020 | -15,070 |
| ni | -670 | +80 | -1,470 | +2,060 | +2,670 | -6,360 | -2,380 | -3,380 | -6,960 | +970 | -15,440 | -16,500 |
| IF | -240 | -480 | +3,180 | +6,240 | +8,460 | +15,480 | +6,480 | -65,940 | +6,540 | +6,300 | -13,980 | -12,540 |
| ss | -300 | +850 | -1,000 | -375 | +1,625 | -15,600 | -4,250 | +400 | -2,750 | +8,500 | -12,900 | -12,600 |
| br | +0 | +500 | -700 | -2,025 | -2,250 | -200 | +350 | -650 | -850 | -2,400 | -8,225 | -8,275 |
| j | +0 | +0 | +0 | +950 | -3,550 | -3,400 | -4,000 | -700 | +1,550 | +1,150 | -8,000 | -8,000 |
| SH | +1,290 | +1,890 | -120 | -30 | +120 | -120 | -5,400 | -1,050 | -1,890 | +420 | -4,890 | -6,120 |
| MA | +180 | +940 | +1,160 | -2,460 | +5,960 | +3,480 | -3,200 | -4,610 | -6,170 | +690 | -4,030 | -4,200 |
| other (23) | +8,455 | +9,570 | +22,370 | -9,015 | +35,385 | +51,020 | -9,795 | +9,870 | +19,755 | -815 | +136,800 | +201,430 |
| l | +860 | -2,730 | +4,915 | +1,275 | +27,585 | +3,050 | -200 | -10,735 | +5,445 | -9,270 | +20,195 | +38,040 |
| SF | -20,880 | +13,280 | +6,400 | +6,800 | +4,620 | +10,770 | -500 | +2,350 | +820 | -990 | +22,670 | +9,490 |
| pg | -1,300 | +680 | +4,500 | +760 | +11,760 | +6,600 | +4,720 | +1,640 | +6,300 | -10,180 | +25,480 | +34,700 |
| TA | -3,940 | -2,260 | +4,540 | +4,050 | +10,360 | +4,850 | +9,200 | +5,310 | +3,020 | -4,680 | +30,450 | +36,190 |
| fu | +330 | +600 | +190 | +730 | -600 | +15,360 | +5,450 | +14,310 | +7,620 | -3,700 | +40,290 | +35,420 |
| CY | +100 | -2,325 | +1,100 | +475 | -1,150 | -1,450 | +8,500 | +17,600 | +14,500 | +4,575 | +41,925 | +42,625 |
| IH | +180 | +960 | -1,440 | -1,140 | +4,320 | +43,860 | +300 | -12,300 | +11,700 | -1,500 | +44,940 | +43,140 |
| zn | -4,850 | -10,775 | -16,575 | -5,225 | -15,000 | +68,550 | +21,625 | +22,525 | -3,600 | +1,750 | +58,425 | +63,550 |
| rb | -11,740 | -400 | -2,870 | -3,050 | +24,800 | +43,910 | +31,050 | +1,260 | -10,520 | -3,390 | +69,050 | +92,880 |
| cs | -130 | +9,640 | +5,070 | -2,240 | +27,790 | +18,560 | +32,430 | +18,860 | -4,570 | +10,520 | +115,930 | +111,960 |
| all products | -28,660 | +24,285 | +55,905 | -18,125 | +39,010 | +208,740 | -14,855 | -91,780 | +34,855 | -34,100 | +175,275 | +268,825 |
executor total_pnl (holding + trading, settlement-to-settlement once the next capture lands, before fees) summed by product root; 'all products' foots to live gross. Full series: data/product_daily.csv

## Data health
decision-price coverage (2026-09-17): 100% of held notional benchmarked (1 contract(s) unbenchmarked); 9 contract(s) (19%) first decided after the 0900 snap, so they straddle their own overnight leg
scale: 1 (since 2026-09-09)
regime: forward (merged weighted book) since 2026-08-31; 14 forward day(s), 8 legacy day(s)
merge weights (2026-09-18): ks_branch 0.8, fund_v3 2, china_pairs 1.5, ks_ext 0.25, chem_fund 1.5, agri_event 1, stat_arb 1
as-shipped pins: 23 live day(s) pinned; current series diverges from pins on fund_v3: 21 day(s), max 22,676 CNY, ks_branch: 20 day(s), max 33,735 CNY, ks_ext: 19 day(s), max 42,170 CNY, stat_arb: 14 day(s), max 10,719 CNY, china_pairs: 17 day(s), max 2,120 CNY, agri_event: 5 day(s), max 5,680 CNY, chem_fund: 1 day(s), max 20 CNY; standing counts -- a divergence is announced as an alert once, the first run it appears, and kept here afterwards
inbox ks summary mtime: 2026-09-18 05:53 UTC
