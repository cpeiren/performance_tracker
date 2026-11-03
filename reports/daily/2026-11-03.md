# Performance tracker - 2026-11-03   (reconciled through 2026-11-02)

## ALERTS
- WEIGHTS 2026-10-09: day's own merge weights not shipped yet -- carried forward from an earlier day.
- WEIGHTS 2026-10-16: day's own merge weights not shipped yet -- carried forward from an earlier day.
- WEIGHTS 2026-10-22: day's own merge weights not shipped yet -- carried forward from an earlier day.
- BT PENDING 2026-11-02: no mature backtest row for stat_arb (nonzero weight) -- day reconciled WITHOUT that sleeve's expected; its live P&L sits in bt_pending_live, not resid, until the rows ship.
- WEIGHTS CHANGE on 2026-09-01: ks_ext: 0.0->0.25.
- WEIGHTS CHANGE on 2026-09-02: stat_arb: 1.0->0.0.
- WEIGHTS CHANGE on 2026-09-03: stat_arb: 0.0->1.0.
- WEIGHTS CHANGE on 2026-11-02: agri_event: 1.0->0.0.
- MISSING LIVE DAY 2026-08-28: trading day with a backtest row but no daily_pnl/state file; excluded from the bridge, expected pnl held in the missing-day bucket.
- SCALE 2026-08-28: no usable run record; previous scale carried forward.
- SCALE 2026-09-25: no usable run record; previous scale carried forward.
- SCALE CHANGE on 2026-08-27: now 0.2.
- SCALE CHANGE on 2026-09-01: now 0.5.
- SCALE CHANGE on 2026-09-09: now 1.
- SLIPPAGE 2026-11-02: 3 unbenchmarked leg(s), -5 CNY exec cost without a shipped decision price.
- RESIDUAL 2026-08-27: -17267 CNY vs trailing median |resid| 2062, offset by neither neighbour (2026-08-26 +3749, 2026-08-31 -17348) -- attribution quality changed. (A break-out that a neighbouring day mirrors is the backtest/live day-window straddle and is not alerted.)
- RESIDUAL 2026-08-31: -17348 CNY vs trailing median |resid| 2277, offset by neither neighbour (2026-08-27 -17267, 2026-09-01 -8190) -- attribution quality changed. (A break-out that a neighbouring day mirrors is the backtest/live day-window straddle and is not alerted.)
- RESIDUAL 2026-09-01: -8190 CNY vs trailing median |resid| 2492, offset by neither neighbour (2026-08-31 -17348, 2026-09-02 -30063) -- attribution quality changed. (A break-out that a neighbouring day mirrors is the backtest/live day-window straddle and is not alerted.)
- RESIDUAL 2026-09-02: -30063 CNY vs trailing median |resid| 3121, offset by neither neighbour (2026-09-01 -8190, 2026-09-03 -29049) -- attribution quality changed. (A break-out that a neighbouring day mirrors is the backtest/live day-window straddle and is not alerted.)
- RESIDUAL 2026-09-03: -29049 CNY vs trailing median |resid| 3941, offset by neither neighbour (2026-09-02 -30063, 2026-09-04 -5584) -- attribution quality changed. (A break-out that a neighbouring day mirrors is the backtest/live day-window straddle and is not alerted.)
- RESIDUAL 2026-09-16: -103509 CNY vs trailing median |resid| 22936, offset by neither neighbour (2026-09-15 -28634, 2026-09-17 +23811) -- attribution quality changed. (A break-out that a neighbouring day mirrors is the backtest/live day-window straddle and is not alerted.)
- RESIDUAL 2026-10-26: +29017 CNY vs trailing median |resid| 7638, offset by neither neighbour (2026-10-23 +7825, 2026-10-27 +81673) -- attribution quality changed. (A break-out that a neighbouring day mirrors is the backtest/live day-window straddle and is not alerted.)
- RESIDUAL 2026-10-27: +81673 CNY vs trailing median |resid| 9046, offset by neither neighbour (2026-10-26 +29017, 2026-10-28 +2573) -- attribution quality changed. (A break-out that a neighbouring day mirrors is the backtest/live day-window straddle and is not alerted.)

## Latest reconciled day (2026-11-02, forward regime, PROVISIONAL: marked at the 16:00 close, re-marked to settlement after the next capture)
live gross -7,880 | expected (1 x bt -45,859) = -45,859 | gap +37,979
  exec_cost +7,355 (slip +7,360, unbench -5) | marking +3,010 | bookdiff -2,740 (carry -2,740, new +0) | intraday +0 | offbook +0 (0 contract(s)) | residual +31,654 (live re-marked to first decision, vs the previous backtest row)
  PARTIAL: no backtest row yet for stat_arb -- expected excludes it; its live P&L +13,410 is held out of resid
  fees +675 | broker residual +0 -> live net -8,555

## Cumulative bridge (live since 2026-08-18, 48 reconciled days, 1 with a sleeve's backtest pending)
| expected | -exec | +marking | +bookdiff | +intraday | +offbook | +bt pending | +resid | = live gross | -fees | +broker_resid | = live net |
|---|---|---|---|---|---|---|---|---|---|---|---|
| +239,674 | -55,350 | +3,545 | +87,097 | -5,168 | -50 | +13,410 | +54,086 | +337,245 | -45,534 | +11,069 | +302,780 |
missing live days excluded: 2026-08-28 (expected +4,849 held in bucket)

## Stats (daily CNY pnl)
| window | days | total | sharpe | mdd | hit |
|---|---|---|---|---|---|
| live net live-to-date | 48 | +302,780 | 1.70 | -330,281 | 54% |
| live net last-20d | 20 | +91,691 | 1.23 | -277,252 | 45% | (small sample)
| live net 2026-YTD | 48 | +302,780 | 1.70 | -330,281 | 54% |
| bt scaled live-to-date | 48 | +239,674 | 1.24 | -397,891 | 62% |
| bt scaled last-20d | 20 | -3,853 | -0.04 | -397,891 | 55% | (small sample)
| bt scaled 2026-YTD | 48 | +239,674 | 1.24 | -397,891 | 62% |

## Slippage (+ = cost; bps vs benchmarked notional)
| day | lots | notional M | slip total | drift | exec | bps | unbench legs | unbench CNY |
|---|---|---|---|---|---|---|---|---|
| 2026-10-20 | 476 | 30.2 | -7,010 | -8,490 | +1,480 | -2.49 | 6 | +145 |
| 2026-10-21 | 342 | 21.4 | +3,385 | +2,920 | +465 | +2.04 | 6 | +270 |
| 2026-10-22 | 408 | 18.0 | +1,025 | +60 | +965 | +0.58 | 2 | +30 |
| 2026-10-23 | 345 | 14.2 | -310 | -1,435 | +1,125 | -0.23 | 2 | -20 |
| 2026-10-26 | 423 | 16.9 | +3,130 | +2,752 | +378 | +1.86 | 1 | +105 |
| 2026-10-27 | 720 | 42.7 | +11,470 | +8,082 | +3,388 | +2.83 | 2 | -335 |
| 2026-10-28 | 220 | 17.2 | +7,060 | +6,922 | +138 | +4.23 | 3 | +320 |
| 2026-10-29 | 393 | 27.9 | +4,825 | +3,225 | +1,600 | +2.13 | 6 | -620 |
| 2026-10-30 | 249 | 14.1 | +6,150 | +6,185 | -35 | +4.49 | 4 | +5 |
| 2026-11-02 | 258 | 19.2 | +7,360 | +6,620 | +740 | +3.92 | 3 | -5 |
| live window (48d) | 17386 | 1074.1 | +42,165 | -6,995 | +49,160 | +0.43 | 242 | +13,185 |
exec-only bps over the window: +0.50; benchmark coverage 92% of traded notional

| product | days | lots | notional M | drift | exec (incl. unbench) | all-in | bps |
|---|---|---|---|---|---|---|---|
| IH | 29 | 116 | 96.8 | -29,010 | +5,430 | -23,580 | -2.44 |
| IF | 17 | 62 | 80.7 | -21,690 | +2,970 | -18,720 | -2.32 |
| CY | 36 | 261 | 28.9 | +13,325 | +4,750 | +18,075 | +6.26 |
| rb | 39 | 1229 | 38.1 | +17,305 | -3,635 | +13,670 | +3.59 |
| hc | 40 | 1457 | 48.1 | -17,890 | +5,540 | -12,350 | -2.57 |
| bu | 41 | 426 | 20.5 | -13,230 | +1,560 | -11,670 | -5.69 |
| FG | 47 | 881 | 16.0 | +6,190 | +4,550 | +10,740 | +6.73 |
| pg | 26 | 45 | 6.2 | +10,410 | +310 | +10,720 | +17.38 |
| SF | 44 | 396 | 12.0 | +8,845 | +610 | +9,455 | +7.91 |
| y | 40 | 268 | 24.0 | +6,130 | +1,980 | +8,110 | +3.38 |
| a | 43 | 561 | 29.6 | +3,665 | +2,880 | +6,545 | +2.21 |
| SR | 42 | 864 | 46.8 | +4,630 | +1,685 | +6,315 | +1.35 |
| cs | 46 | 935 | 23.5 | +1,295 | +4,480 | +5,775 | +2.46 |
| ru | 29 | 90 | 17.4 | +5,925 | -300 | +5,625 | +3.23 |
| al | 36 | 518 | 61.2 | +2,350 | +3,112 | +5,462 | +0.89 |
| other (34) | - | 9277 | 524.5 | -5,245 | +26,422 | +21,178 | +0.40 |
| all products | - | 17386 | 1074.1 | -6,995 | +62,345 | +55,350 | +0.52 |
ranked by |all-in| over the live window (all-in = drift + exec = the bridge's exec_cost by product); product bps are vs traded notional

## Per strategy
| strategy | live? | bt 2026 pnl (full) | bt scaled+weighted (live window) | live attributed | note |
|---|---|---|---|---|---|
| Calendar main pool (branch) | yes | +1,013,450 | +8,616 | +67,355 | forward w=0.8 |
| Fundamental factor | yes | +749,000 | +230,428 | +258,105 | forward w=2 |
| Cross-product pairs | yes | +61,055 | +5,483 | -14,224 | forward w=1.5 |
| Calendar extended pool | yes | +487,180 | +12,561 | +61,465 | forward w=0.25 |
| Chemical fundamental | yes | +523,115 | +63,753 | +39,423 | forward w=1.5 |
| Agriculture event-driven | no | +42,290 | -111,243 | -153,338 | forward w=0 (parked) |
| Factor-neutral stat arb | yes | +340,568 | +30,077 | +44,678 | forward w=1 |
| shared bucket | - | - | - | +3,575 | legacy days only: a contract both per-source books held |
| neither bucket (no target) | - | - | - | +2,330 | named by no book that day or the day before |
| trading bucket | - | - | - | +27,876 | forward days: live P&L minus the strategies' holdings (fills vs settlement on rebalances, lot rounding, scale changes) |
forward days: each strategy is its own previous-day weighted book x scale x the settlement-to-settlement move (holdings); legacy days remain exclusive-holder. The gap tables (attributed - expected) therefore exclude execution, which sits in trading.

## Live P&L by strategy, last 10 reconciled days (attributed gross CNY)
| day | ks_branch | fund_v3 | china_pairs | ks_ext | chem_fund | agri_event | stat_arb | shared | neither | trading | total |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 2026-10-20 | +1,052 | -3,650 | -165 | +6,715 | -8,692 | -9,105 | -1,070 | +0 | +0 | +7,916 | -7,000 |
| 2026-10-21 | -7,536 | +34,220 | -6,472 | -1,204 | -3,150 | +10,620 | +8,660 | +0 | +0 | +4,072 | +39,210 |
| 2026-10-22 | -1,172 | +12,220 | +11,835 | -1,720 | +982 | -3,140 | -740 | +0 | +1,170 | -1,965 | +17,470 |
| 2026-10-23 | -8,796 | -9,130 | +6,262 | -2,563 | +11,032 | -19,495 | +8,845 | +0 | +0 | +2,289 | -11,555 |
| 2026-10-26 | -240 | -4,570 | +2,258 | +11,030 | +17,498 | -9,650 | -10,845 | +0 | +0 | -1,445 | +4,035 |
| 2026-10-27 | +35,236 | -2,240 | -9,068 | +6,356 | +9,218 | -37,080 | -20,025 | +0 | +0 | -21,217 | -38,820 |
| 2026-10-28 | +4,048 | -15,440 | -5,362 | -7,313 | -2,760 | -10,980 | -2,965 | +0 | +0 | -2,938 | -43,710 |
| 2026-10-29 | -49,776 | -53,440 | -825 | +6,281 | -6,968 | -18,070 | -15,165 | +0 | +0 | -8,983 | -146,945 |
| 2026-10-30 | -16,068 | -66,600 | -1,560 | +2,871 | +9,292 | +8,605 | +13,805 | +0 | -275 | +17,859 | -32,070 |
| 2026-11-02 | +4,476 | +1,310 | +8,610 | -32,891 | +9,000 | -4,535 | +13,410 | +0 | +0 | -7,260 | -7,880 |
| sum | -38,776 | -107,320 | +5,512 | -12,436 | +35,452 | -92,830 | -6,090 | +0 | +895 | -11,673 | -227,265 |
forward days: previous-day weighted book x scale x settlement move per strategy, the rest in trading; total foots to live gross. Live-window sums: 'Per strategy' above; full series: data/per_strategy_daily.csv (attributed)

## Per strategy gap by day, last 10 reconciled days (live attributed - expected, CNY)
| day | ks_branch | fund_v3 | china_pairs | ks_ext | chem_fund | agri_event | stat_arb | total |
|---|---|---|---|---|---|---|---|---|
| 2026-10-20 | +17,516 | -2,515 | -3,202 | +4,021 | -8,782 | -185 | +15,214 | +22,066 |
| 2026-10-21 | -4,280 | +13,949 | -1,508 | -2,398 | -338 | +4,200 | +3,114 | +12,740 |
| 2026-10-22 | +18,340 | -9,712 | +6,202 | -1,081 | -585 | -6,370 | -3,852 | +2,942 |
| 2026-10-23 | +3,360 | -4,852 | -3,255 | +1,446 | +4,328 | +3,345 | -5,275 | -904 |
| 2026-10-26 | -16,908 | +16,537 | -1,418 | +7,696 | +6,255 | -7,360 | -4,496 | +307 |
| 2026-10-27 | +83,988 | -3,013 | +4,755 | +3,094 | -12,608 | +9,880 | +11,794 | +97,890 |
| 2026-10-28 | -13,640 | +4,387 | -210 | -11,386 | +10,568 | -8,470 | -10,748 | -29,499 |
| 2026-10-29 | +31,404 | -1,601 | +480 | +7,169 | +7,665 | +585 | +3,032 | +48,734 |
| 2026-10-30 | +9,708 | -35,219 | -2,768 | -241 | +3,375 | +8,655 | -2,361 | -18,851 |
| 2026-11-02 | +9,592 | +65,232 | -592 | -34,485 | -3,382 | -4,535 | - | +31,829 |
| sum | +139,080 | +43,193 | -1,515 | -26,165 | +6,495 | -255 | +6,422 | +167,255 |
full series: data/per_strategy_daily.csv (day, strategy, expected, attributed, gap); a strategy's daily total foots to expected - live_gross once the shared, neither and trading buckets are added. '-' = that sleeve's backtest row has not shipped yet (BT PENDING).

## Live P&L by product, last 10 reconciled days (gross CNY, worst first)
| product | 10-20 | 10-21 | 10-22 | 10-23 | 10-26 | 10-27 | 10-28 | 10-29 | 10-30 | 11-02 | 10d sum | live window |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| p | -2,030 | -4,730 | -2,560 | +15,090 | +1,810 | -35,990 | -8,710 | -22,970 | -5,410 | +2,610 | -62,890 | -29,710 |
| cs | -5,780 | +9,980 | -670 | -30,200 | -50 | +860 | -3,860 | -10,540 | +3,410 | -17,840 | -54,690 | +100,400 |
| pp | -4,005 | -11,800 | -2,460 | -4,590 | -2,380 | -6,235 | -1,165 | -8,380 | +1,800 | -3,510 | -42,725 | -23,200 |
| l | -1,295 | +185 | -1,280 | -8,200 | -14,180 | -1,470 | +4,735 | -9,445 | +2,615 | -6,605 | -34,940 | -600 |
| CF | +1,075 | +13,325 | +1,250 | -3,750 | -3,100 | -22,400 | -14,350 | -7,350 | +6,175 | -3,000 | -32,125 | -92,725 |
| y | -3,410 | -800 | -2,170 | -1,210 | -9,590 | +840 | -3,550 | -7,880 | -2,330 | +2,080 | -28,020 | -46,090 |
| m | -8,680 | +840 | -6,140 | -4,080 | +100 | -1,320 | +2,110 | -6,330 | +1,280 | -5,280 | -27,500 | -27,370 |
| OI | +790 | -2,780 | -1,310 | -7,940 | -1,930 | -3,800 | +340 | -10,220 | -9,480 | +8,990 | -27,340 | -42,730 |
| a | -5,600 | +1,130 | +6,190 | +4,610 | -11,510 | -2,340 | -2,580 | -16,320 | -4,410 | +4,140 | -26,690 | +19,720 |
| IF | -480 | -3,000 | -900 | -1,500 | +5,400 | -1,080 | -5,040 | +2,880 | +9,120 | -28,320 | -22,920 | -57,120 |
| fu | -1,800 | +3,770 | +360 | -9,800 | -5,750 | -2,570 | -360 | -10,780 | +1,410 | +7,020 | -18,500 | +16,750 |
| TA | -430 | +2,460 | -950 | -3,880 | -6,270 | +2,620 | +290 | +1,770 | -2,960 | -10,330 | -17,680 | +16,210 |
| bu | -600 | +3,510 | -520 | +5,450 | +880 | -6,520 | +3,830 | -13,710 | -8,900 | -440 | -17,020 | -63,800 |
| v | +1,705 | -915 | +95 | -90 | -4,755 | +2,505 | -7,400 | -4,440 | -2,440 | +1,290 | -14,445 | -8,875 |
| SH | -270 | +1,350 | -1,260 | -810 | -3,990 | -7,200 | -570 | +390 | +3,240 | -4,260 | -13,380 | +24,210 |
| other (24) | +3,515 | +6,400 | -4,115 | +6,945 | +13,485 | +7,580 | -22,875 | -37,340 | -2,360 | +32,775 | +4,010 | +509,690 |
| br | -150 | -1,000 | +750 | +2,500 | +5,100 | -100 | +400 | +0 | +800 | +650 | +8,950 | +1,375 |
| IH | +5,160 | +1,860 | -1,200 | -1,200 | +5,100 | +3,420 | -2,100 | +2,640 | +420 | -480 | +13,620 | +70,620 |
| hc | +2,130 | -1,440 | +7,230 | +9,540 | +4,110 | -2,160 | -3,020 | +17,000 | -9,790 | -9,580 | +14,020 | -165,080 |
| c | -70 | +1,110 | +7,610 | +3,300 | -1,270 | -1,130 | +3,630 | +90 | -2,200 | +4,720 | +15,790 | -14,500 |
| RM | +7,310 | +4,730 | +2,080 | +840 | +1,090 | +2,280 | -1,770 | +680 | -600 | +1,320 | +17,960 | +14,100 |
| ss | +875 | +8,275 | +21,550 | -4,850 | -2,025 | -7,950 | -525 | -850 | +2,500 | +2,550 | +19,550 | -2,550 |
| sp | +5,500 | +2,920 | +1,400 | +3,440 | +5,000 | +7,160 | +3,880 | +1,340 | -16,700 | +6,060 | +20,000 | +42,000 |
| FG | +10,120 | +1,140 | +7,520 | +3,720 | -5,700 | +18,640 | +1,060 | -2,300 | -2,820 | -3,960 | +27,420 | +79,340 |
| SA | -6,740 | +5,740 | -16,300 | +11,440 | +20,000 | +11,760 | +11,360 | -7,140 | +180 | +1,800 | +32,100 | -24,560 |
| MA | -3,840 | -3,050 | +3,270 | +3,670 | +14,460 | +5,780 | +2,530 | +2,260 | +5,380 | +9,720 | +40,180 | +41,740 |
| all products | -7,000 | +39,210 | +17,470 | -11,555 | +4,035 | -38,820 | -43,710 | -146,945 | -32,070 | -7,880 | -227,265 | +337,245 |
executor total_pnl (holding + trading, settlement-to-settlement once the next capture lands, before fees) summed by product root; 'all products' foots to live gross. Full series: data/product_daily.csv

## Worst (strategy, product) cells, last 10 reconciled days (attributed gross CNY)
| strategy | product | 10-20 | 10-21 | 10-22 | 10-23 | 10-26 | 10-27 | 10-28 | 10-29 | 10-30 | 11-02 | sum |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| china_pairs | l | +1,822 | +1,688 | -150 | -12,900 | -17,752 | -5,100 | -4,650 | -10,425 | -11,715 | -8,415 | -67,598 |
| fund_v3 | cs | -8,220 | +4,600 | +4,320 | -26,840 | -1,200 | +640 | -3,400 | -10,780 | +2,720 | -19,240 | -57,400 |
| fund_v3 | pp | +2,960 | +2,520 | +80 | -10,160 | -16,240 | -5,160 | -5,080 | -4,720 | -5,360 | -3,160 | -44,320 |
| ks_branch | OI | +1,600 | -3,800 | -2,800 | -6,600 | -1,584 | -5,672 | -440 | -9,096 | -7,176 | +5,872 | -29,696 |
| ks_ext | IF | -900 | -2,850 | -855 | -1,425 | +5,670 | -630 | -4,830 | +2,625 | -405 | -25,530 | -29,130 |
| fund_v3 | CF | -5,400 | +200 | +3,600 | +0 | -5,800 | -17,600 | -2,700 | -2,700 | +2,700 | -1,350 | -29,050 |
| agri_event | SR | -2,240 | +3,680 | -3,040 | -2,240 | -2,240 | -13,280 | +1,760 | -1,760 | -320 | -6,560 | -26,240 |
| ks_branch | pp | -2,000 | -8,124 | -2,120 | -4,176 | -7,540 | -1,540 | +3,636 | -3,568 | +4,864 | -3,100 | -23,668 |
| ks_branch | y | -2,592 | -144 | -2,304 | -2,592 | -8,904 | -1,400 | -3,672 | -6,808 | -2,320 | +7,792 | -22,944 |
| stat_arb | SH | +420 | -930 | -5,130 | -1,980 | -6,750 | -6,600 | -2,070 | -720 | +5,400 | -4,410 | -22,770 |
| fund_v3 | pg | +0 | +0 | +0 | +0 | -9,280 | -8,120 | +1,520 | -1,120 | -5,000 | +0 | -22,000 |
| fund_v3 | p | +440 | +4,060 | -2,060 | +2,000 | +1,840 | -19,280 | -3,280 | -8,720 | -160 | +3,700 | -21,460 |
| agri_event | CY | -4,950 | -150 | +3,900 | -2,100 | -2,700 | -12,150 | -3,900 | -3,000 | +4,950 | +300 | -19,800 |
| agri_event | p | +2,160 | +8,190 | -3,150 | -1,080 | +2,340 | -21,150 | -4,140 | -11,160 | +2,250 | +7,650 | -18,090 |
| ks_branch | p | -2,792 | -7,728 | +480 | +13,696 | -1,408 | -520 | -2,232 | -4,896 | -5,536 | -7,120 | -18,056 |
same holdings split as 'Live P&L by strategy'; summing a strategy's products reproduces its row there (trading / neither included as their own strategy). Full series: data/strategy_product_daily.csv

## Paper strategies (weight 0 in the forward book: tracked, not traded)
| strategy | weight 0 since | bt since (full) | bt last 20d | drawdown now | worst before pause | 60d Sharpe | paper-live since (full) | paper days | book coverage |
|---|---|---|---|---|---|---|---|---|---|
| agri_event | 2026-11-02 | +0 | -112,425 | -145,905 | -152,120 | -2.00 | +0 | 0 | - |
paper-live = the strategy's own pinned full-size book of D-1 x the settlement-to-settlement move of D, priced like the live attribution, on contracts the day's state capture marks (coverage). Re-entry: owner's call, at an attended morning merge; reweighting is Execution/weights_forward.json + weights_changelog.csv.

## Backtest vintages (full series kept on every restatement)
expected on the CURRENT series minus expected on the as-shipped pins, live window, weighted CNY (the bridge uses the pins):
| strategy | restated |
|---|---|
| ks_branch | +65,633 |
| fund_v3 | -41,623 |
| china_pairs | -24,878 |
| ks_ext | +6,911 |
| chem_fund | -6,668 |
| agri_event | +7,075 |
| stat_arb | +16,744 |
| all | +23,194 |
| strategy | vintages | latest | cause | commit | rows restated | net change (full size) |
|---|---|---|---|---|---|---|
| fund_v3 | 1 | 20261029084152_nocommit.csv | baseline | - | 0 | +0 |
| stat_arb | 1 | 20261029084152_nocommit.csv | baseline | - | 0 | +0 |
| ks_branch | 2 | 20261102090932_cbbdd7664522.csv | unknown | cbbdd76 | 165 | +341,255 |
| ks_ext | 2 | 20261102090932_1a03a09367cb.csv | unknown | 1a03a09 | 91 | +31,590 |
| china_pairs | 2 | 20261102090932_51a17747e0e0.csv | unknown | 51a1774 | 44 | -46,815 |
| agri_event | 3 | 20261102090932_8f0b7b90cc1f.csv | unknown | 8f0b7b9 | 49 | +14,980 |
| chem_fund | 2 | 20261102090932_a98238f08285.csv | unknown | a98238f | 120 | +51,865 |
full series: data/backtest/vintages/<strategy>/; index: data/backtest/vintages/index.csv

## Data health
decision-price coverage (2026-11-02): 100% of held notional benchmarked (0 contract(s) unbenchmarked); 9 contract(s) (18%) first decided after the 0900 snap, so they straddle their own overnight leg
scale: 1 (since 2026-09-09)
regime: forward (merged weighted book) since 2026-08-31; 40 forward day(s), 8 legacy day(s)
merge weights (2026-11-02): ks_branch 0.8, fund_v3 2, china_pairs 1.5, ks_ext 0.25, chem_fund 1.5, agri_event 0, stat_arb 1
as-shipped pins: 48 live day(s) pinned; current series diverges from pins on chem_fund: 30 day(s), max 9,725 CNY, fund_v3: 43 day(s), max 22,683 CNY, ks_branch: 43 day(s), max 82,125 CNY, ks_ext: 35 day(s), max 42,170 CNY, stat_arb: 43 day(s), max 9,982 CNY, china_pairs: 23 day(s), max 10,910 CNY, agri_event: 15 day(s), max 7,250 CNY; standing counts -- a divergence is announced as an alert once, the first run it appears, and kept here afterwards
inbox ks summary mtime: 2026-11-02 05:53 UTC
