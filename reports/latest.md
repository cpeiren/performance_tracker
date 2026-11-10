# Performance tracker - 2026-11-09   (reconciled through 2026-11-09)

## ALERTS
- WEIGHTS 2026-10-09: day's own merge weights not shipped yet -- carried forward from an earlier day.
- WEIGHTS 2026-10-16: day's own merge weights not shipped yet -- carried forward from an earlier day.
- WEIGHTS 2026-10-22: day's own merge weights not shipped yet -- carried forward from an earlier day.
- BT PENDING 2026-11-09: no mature backtest row for stat_arb (nonzero weight) -- day reconciled WITHOUT that sleeve's expected; its live P&L sits in bt_pending_live, not resid, until the rows ship.
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
- SLIPPAGE 2026-11-09: 1 unbenchmarked leg(s), -30 CNY exec cost without a shipped decision price.
- RESIDUAL 2026-08-27: -17267 CNY vs trailing median |resid| 2062, offset by neither neighbour (2026-08-26 +3749, 2026-08-31 -17348) -- attribution quality changed. (A break-out that a neighbouring day mirrors is the backtest/live day-window straddle and is not alerted.)
- RESIDUAL 2026-08-31: -17348 CNY vs trailing median |resid| 2277, offset by neither neighbour (2026-08-27 -17267, 2026-09-01 -8190) -- attribution quality changed. (A break-out that a neighbouring day mirrors is the backtest/live day-window straddle and is not alerted.)
- RESIDUAL 2026-09-01: -8190 CNY vs trailing median |resid| 2492, offset by neither neighbour (2026-08-31 -17348, 2026-09-02 -30063) -- attribution quality changed. (A break-out that a neighbouring day mirrors is the backtest/live day-window straddle and is not alerted.)
- RESIDUAL 2026-09-02: -30063 CNY vs trailing median |resid| 3121, offset by neither neighbour (2026-09-01 -8190, 2026-09-03 -29049) -- attribution quality changed. (A break-out that a neighbouring day mirrors is the backtest/live day-window straddle and is not alerted.)
- RESIDUAL 2026-09-03: -29049 CNY vs trailing median |resid| 3941, offset by neither neighbour (2026-09-02 -30063, 2026-09-04 -5584) -- attribution quality changed. (A break-out that a neighbouring day mirrors is the backtest/live day-window straddle and is not alerted.)
- RESIDUAL 2026-09-16: -103509 CNY vs trailing median |resid| 22936, offset by neither neighbour (2026-09-15 -28634, 2026-09-17 +23811) -- attribution quality changed. (A break-out that a neighbouring day mirrors is the backtest/live day-window straddle and is not alerted.)
- RESIDUAL 2026-10-26: +29017 CNY vs trailing median |resid| 7638, offset by neither neighbour (2026-10-23 +7825, 2026-10-27 +81673) -- attribution quality changed. (A break-out that a neighbouring day mirrors is the backtest/live day-window straddle and is not alerted.)
- RESIDUAL 2026-10-27: +81673 CNY vs trailing median |resid| 9046, offset by neither neighbour (2026-10-26 +29017, 2026-10-28 +2573) -- attribution quality changed. (A break-out that a neighbouring day mirrors is the backtest/live day-window straddle and is not alerted.)

## Latest reconciled day (2026-11-09, forward regime, PROVISIONAL: marked at the 16:00 close, re-marked to settlement after the next capture)
live gross +23,870 | expected (1 x bt -13,884) = -13,884 | gap +37,754
  exec_cost -5,720 (slip -5,690, unbench -30) | marking +18,780 | bookdiff +0 (carry +0, new +0) | intraday +0 | offbook +0 (0 contract(s)) | residual +15,569 (live re-marked to first decision, vs the previous backtest row)
  PARTIAL: no backtest row yet for stat_arb -- expected excludes it; its live P&L -2,315 is held out of resid
  fees +1,211 | broker residual +0 -> live net +22,659

## Cumulative bridge (live since 2026-08-18, 53 reconciled days, 1 with a sleeve's backtest pending)
| expected | -exec | +marking | +bookdiff | +intraday | +offbook | +bt pending | +resid | = live gross | -fees | +broker_resid | = live net |
|---|---|---|---|---|---|---|---|---|---|---|---|
| +307,009 | -78,340 | +16,910 | +90,047 | -6,568 | -50 | -2,315 | +8,877 | +335,570 | -52,615 | +11,088 | +294,043 |
missing live days excluded: 2026-08-28 (expected +4,849 held in bucket)

## Stats (daily CNY pnl)
| window | days | total | sharpe | mdd | hit |
|---|---|---|---|---|---|
| live net live-to-date | 53 | +294,043 | 1.56 | -330,281 | 53% |
| live net last-20d | 20 | -111,810 | -1.94 | -317,945 | 40% | (small sample)
| live net 2026-YTD | 53 | +294,043 | 1.56 | -330,281 | 53% |
| bt scaled live-to-date | 53 | +307,009 | 1.52 | -381,526 | 64% |
| bt scaled last-20d | 20 | -163,686 | -2.18 | -381,526 | 55% | (small sample)
| bt scaled 2026-YTD | 53 | +307,009 | 1.52 | -381,526 | 64% |

## Slippage (+ = cost; bps vs benchmarked notional)
| day | lots | notional M | slip total | drift | exec | bps | unbench legs | unbench CNY |
|---|---|---|---|---|---|---|---|---|
| 2026-10-27 | 720 | 42.7 | +11,470 | +8,082 | +3,388 | +2.83 | 2 | -335 |
| 2026-10-28 | 220 | 17.2 | +7,060 | +6,922 | +138 | +4.23 | 3 | +320 |
| 2026-10-29 | 393 | 27.9 | +4,825 | +3,225 | +1,600 | +2.13 | 6 | -620 |
| 2026-10-30 | 249 | 14.1 | +6,150 | +6,185 | -35 | +4.49 | 4 | +5 |
| 2026-11-02 | 258 | 19.2 | +7,360 | +6,620 | +740 | +3.92 | 3 | -5 |
| 2026-11-03 | 379 | 25.3 | +7,160 | +5,542 | +1,618 | +2.94 | 2 | +2,140 |
| 2026-11-04 | 364 | 32.1 | +2,030 | +1,422 | +608 | +0.64 | 1 | +275 |
| 2026-11-05 | 462 | 30.3 | +3,350 | +942 | +2,408 | +1.15 | 4 | -45 |
| 2026-11-06 | 863 | 42.1 | +13,755 | +6,750 | +7,005 | +3.27 | 1 | +45 |
| 2026-11-09 | 519 | 27.4 | -5,690 | -6,638 | +948 | -2.09 | 1 | -30 |
| live window (53d) | 19973 | 1231.2 | +62,770 | +1,025 | +61,745 | +0.55 | 251 | +15,570 |
exec-only bps over the window: +0.54; benchmark coverage 93% of traded notional

| product | days | lots | notional M | drift | exec (incl. unbench) | all-in | bps |
|---|---|---|---|---|---|---|---|
| IH | 33 | 130 | 108.3 | -28,410 | +5,130 | -23,280 | -2.15 |
| IF | 21 | 74 | 95.0 | -20,220 | +2,580 | -17,640 | -1.86 |
| CY | 40 | 288 | 31.7 | +10,688 | +5,662 | +16,350 | +5.15 |
| pg | 27 | 47 | 6.4 | +15,150 | +170 | +15,320 | +23.84 |
| bu | 46 | 534 | 25.5 | -13,700 | +1,550 | -12,150 | -4.77 |
| y | 44 | 315 | 28.0 | +9,750 | +2,150 | +11,900 | +4.24 |
| rb | 43 | 1451 | 44.8 | +9,745 | +1,505 | +11,250 | +2.51 |
| SF | 49 | 459 | 13.8 | +9,530 | +935 | +10,465 | +7.61 |
| FG | 52 | 991 | 17.9 | +4,970 | +5,090 | +10,060 | +5.62 |
| PF | 44 | 269 | 11.1 | -8,695 | +765 | -7,930 | -7.14 |
| ru | 33 | 104 | 20.1 | +7,100 | -75 | +7,025 | +3.50 |
| pb | 42 | 920 | 73.9 | +3,850 | +3,000 | +6,850 | +0.93 |
| SR | 47 | 954 | 51.5 | +5,005 | +1,690 | +6,695 | +1.30 |
| SA | 49 | 704 | 14.2 | +5,790 | +790 | +6,580 | +4.63 |
| cs | 51 | 965 | 24.2 | +1,890 | +4,485 | +6,375 | +2.63 |
| other (35) | - | 11768 | 664.8 | -11,418 | +41,888 | +30,470 | +0.46 |
| all products | - | 19973 | 1231.2 | +1,025 | +77,315 | +78,340 | +0.64 |
ranked by |all-in| over the live window (all-in = drift + exec = the bridge's exec_cost by product); product bps are vs traded notional

## Per strategy
| strategy | live? | bt 2026 pnl (full) | bt scaled+weighted (live window) | live attributed | note |
|---|---|---|---|---|---|
| Calendar main pool (branch) | yes | +998,570 | -3,288 | +23,587 | forward w=0.8 |
| Fundamental factor | yes | +781,537 | +295,897 | +290,785 | forward w=2 |
| Cross-product pairs | yes | +82,075 | +37,013 | +14,666 | forward w=1.5 |
| Calendar extended pool | yes | +454,490 | +4,388 | +66,072 | forward w=0.25 |
| Chemical fundamental | yes | +519,390 | +58,166 | +14,628 | forward w=1.5 |
| Agriculture event-driven | no | +22,820 | -111,243 | -152,798 | forward w=0 (parked) |
| Factor-neutral stat arb | yes | +336,567 | +26,076 | +59,504 | forward w=1 |
| shared bucket | - | - | - | +3,575 | legacy days only: a contract both per-source books held |
| neither bucket (no target) | - | - | - | +2,330 | named by no book that day or the day before |
| trading bucket | - | - | - | +13,221 | forward days: live P&L minus the strategies' holdings (fills vs settlement on rebalances, lot rounding, scale changes) |
forward days: each strategy is its own previous-day weighted book x scale x the settlement-to-settlement move (holdings); legacy days remain exclusive-holder. The gap tables (attributed - expected) therefore exclude execution, which sits in trading.

## Live P&L by strategy, last 10 reconciled days (attributed gross CNY)
| day | ks_branch | fund_v3 | china_pairs | ks_ext | chem_fund | agri_event | stat_arb | shared | neither | trading | total |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 2026-10-27 | +35,236 | -2,240 | -9,068 | +6,356 | +9,218 | -37,080 | -20,025 | +0 | +0 | -21,217 | -38,820 |
| 2026-10-28 | +4,048 | -15,440 | -5,362 | -7,313 | -2,760 | -10,980 | -2,965 | +0 | +0 | -2,938 | -43,710 |
| 2026-10-29 | -49,776 | -53,440 | -825 | +6,281 | -6,968 | -18,070 | -15,165 | +0 | +0 | -8,983 | -146,945 |
| 2026-10-30 | -16,068 | -66,600 | -1,560 | +2,871 | +9,292 | +8,605 | +13,805 | +0 | -275 | +17,859 | -32,070 |
| 2026-11-02 | +4,260 | -660 | +7,845 | -25,403 | +15,420 | -3,995 | +12,980 | +0 | +0 | -12,588 | -2,140 |
| 2026-11-03 | -9,816 | +21,940 | -8,490 | -123 | -13,485 | +0 | +1,335 | +0 | +0 | +2,793 | -5,845 |
| 2026-11-04 | +7,320 | -21,410 | -2,842 | -13,680 | +11,618 | +0 | +12,140 | +0 | +0 | +4,875 | -1,980 |
| 2026-11-05 | -33,388 | +1,260 | -532 | +8,112 | -8,992 | +0 | +12,415 | +0 | +0 | -13,885 | -35,010 |
| 2026-11-06 | +316 | -2,180 | +21,278 | +4,886 | -10,478 | +0 | -8,320 | +0 | +0 | +6,048 | +11,550 |
| 2026-11-09 | -7,984 | +35,040 | +20,242 | -2,078 | -9,878 | +0 | -2,315 | +0 | +0 | -9,158 | +23,870 |
| sum | -65,852 | -103,730 | +20,685 | -20,088 | -7,012 | -61,520 | +3,885 | +0 | -275 | -37,193 | -271,100 |
forward days: previous-day weighted book x scale x settlement move per strategy, the rest in trading; total foots to live gross. Live-window sums: 'Per strategy' above; full series: data/per_strategy_daily.csv (attributed)

## Per strategy gap by day, last 10 reconciled days (live attributed - expected, CNY)
| day | ks_branch | fund_v3 | china_pairs | ks_ext | chem_fund | agri_event | stat_arb | total |
|---|---|---|---|---|---|---|---|---|
| 2026-10-27 | +83,988 | -3,013 | +4,755 | +3,094 | -12,608 | +9,880 | +11,794 | +97,890 |
| 2026-10-28 | -13,640 | +4,387 | -210 | -11,386 | +10,568 | -8,470 | -10,748 | -29,499 |
| 2026-10-29 | +31,404 | -1,601 | +480 | +7,169 | +7,665 | +585 | +3,032 | +48,734 |
| 2026-10-30 | +9,708 | -35,219 | -2,768 | -241 | +3,375 | +8,655 | -2,361 | -18,851 |
| 2026-11-02 | +9,376 | +63,262 | -1,358 | -26,996 | +3,038 | -3,995 | -3,385 | +39,942 |
| 2026-11-03 | -18,168 | -12,215 | -1,110 | +13,477 | -7,695 | +0 | +3,215 | -22,496 |
| 2026-11-04 | +2,600 | -42,652 | -6,390 | -17,409 | -240 | +0 | +12,722 | -51,368 |
| 2026-11-05 | -20,828 | -38,627 | +5,752 | +2,836 | +1,545 | +0 | +26,370 | -22,951 |
| 2026-11-06 | +16,056 | +9,255 | -3,420 | +208 | -16,882 | +0 | -4,371 | +845 |
| 2026-11-09 | -11,308 | +53,419 | +3,292 | +6,179 | -2,355 | +0 | - | +49,227 |
| sum | +89,188 | -3,004 | -975 | -23,070 | -13,590 | +6,655 | +36,269 | +91,473 |
full series: data/per_strategy_daily.csv (day, strategy, expected, attributed, gap); a strategy's daily total foots to expected - live_gross once the shared, neither and trading buckets are added. '-' = that sleeve's backtest row has not shipped yet (BT PENDING).

## Live P&L by product, last 10 reconciled days (gross CNY, worst first)
| product | 10-27 | 10-28 | 10-29 | 10-30 | 11-02 | 11-03 | 11-04 | 11-05 | 11-06 | 11-09 | 10d sum | live window |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| TA | +2,620 | +290 | +1,770 | -2,960 | +6,350 | -42,080 | -9,440 | -44,250 | -5,800 | -80 | -93,580 | -68,760 |
| y | +840 | -3,550 | -7,880 | -2,330 | +8,940 | -25,520 | -29,090 | -8,710 | -12,240 | -12,940 | -92,480 | -127,730 |
| pp | -6,235 | -1,165 | -8,380 | +1,800 | +410 | -14,870 | -2,660 | -17,820 | +955 | -27,145 | -75,110 | -80,820 |
| cs | +860 | -3,860 | -10,540 | +3,410 | -10,770 | -1,060 | -3,440 | -13,080 | +2,940 | -14,770 | -50,310 | +78,060 |
| eb | -1,505 | -2,215 | -5,445 | -190 | +7,710 | -19,680 | -5,700 | -12,610 | -3,905 | -5,130 | -48,670 | +22,200 |
| CF | -22,400 | -14,350 | -7,350 | +6,175 | -2,700 | -6,300 | +1,650 | +5,325 | -2,500 | -3,800 | -46,250 | -98,050 |
| p | -35,990 | -8,710 | -22,970 | -5,410 | +4,090 | +5,620 | +15,810 | +4,650 | -820 | +4,430 | -39,300 | +1,460 |
| a | -2,340 | -2,580 | -16,320 | -4,410 | +2,070 | -6,810 | -12,270 | +5,100 | -5,410 | +4,930 | -38,040 | +3,190 |
| IF | -1,080 | -5,040 | +2,880 | +9,120 | -26,400 | +3,420 | -15,000 | +900 | -540 | +840 | -30,900 | -65,580 |
| i | +7,300 | -1,800 | -20,800 | +9,000 | -4,400 | +4,900 | -6,950 | -12,250 | -3,700 | +700 | -28,000 | -13,950 |
| pg | -2,800 | -420 | -720 | -2,600 | +6,020 | -7,040 | -2,980 | -8,020 | -7,720 | +6,360 | -19,920 | -46,600 |
| ru | -5,350 | +3,150 | -5,900 | -1,800 | +150 | +1,200 | -5,800 | -900 | -450 | +1,650 | -14,050 | -4,450 |
| ni | +1,460 | +650 | -1,220 | +1,730 | +180 | +2,470 | -410 | -10,520 | -9,800 | +1,560 | -13,900 | -31,680 |
| br | -100 | +400 | +0 | +800 | +1,100 | -5,350 | -300 | -8,350 | -2,750 | +800 | -13,750 | -14,125 |
| b | -5,420 | +5,350 | -8,470 | -410 | -670 | -1,460 | -1,480 | +260 | -3,030 | +4,720 | -10,610 | -9,250 |
| other (25) | +10,405 | -27,985 | -25,645 | -13,330 | +37,000 | +45,670 | +19,980 | -32,555 | +20,340 | +24,695 | +58,575 | +675,085 |
| CY | +12,200 | +4,800 | +6,800 | -14,450 | -1,100 | +8,875 | -1,900 | +800 | -2,250 | +2,200 | +15,975 | -2,250 |
| SA | +11,760 | +11,360 | -7,140 | +180 | -6,340 | +6,760 | +10,000 | -2,580 | -4,760 | -1,560 | +17,680 | -24,840 |
| hc | -2,160 | -3,020 | +17,000 | -9,790 | -6,480 | -9,690 | +750 | +19,770 | +3,300 | +10,630 | +20,310 | -137,220 |
| m | -1,320 | +2,110 | -6,330 | +1,280 | -3,810 | +90 | +5,870 | +3,880 | +6,680 | +13,160 | +21,610 | +3,780 |
| cu | +1,900 | +3,550 | +3,600 | -2,500 | -1,400 | -5,000 | +19,650 | -1,600 | +11,150 | -3,900 | +25,450 | +2,550 |
| v | +2,505 | -7,400 | -4,440 | -2,440 | +1,815 | +520 | +10,110 | +21,390 | -3,885 | +10,455 | +28,630 | +30,240 |
| PF | +270 | -850 | -940 | -1,430 | -4,860 | +23,910 | +2,570 | +13,630 | +3,580 | -3,010 | +32,870 | +82,910 |
| fu | -2,570 | -360 | -10,780 | +1,410 | +4,000 | +9,400 | +11,500 | +21,060 | +1,620 | +1,480 | +36,760 | +58,790 |
| l | -1,470 | +4,735 | -9,445 | +2,615 | -9,825 | +12,460 | -4,500 | +14,790 | +25,555 | +7,235 | +42,150 | +51,720 |
| eg | -200 | +3,200 | +1,720 | -5,540 | -3,220 | +13,720 | +2,050 | +26,680 | +4,990 | +360 | +43,760 | +50,890 |
| all products | -38,820 | -43,710 | -146,945 | -32,070 | -2,140 | -5,845 | -1,980 | -35,010 | +11,550 | +23,870 | -271,100 | +335,570 |
executor total_pnl (holding + trading, settlement-to-settlement once the next capture lands, before fees) summed by product root; 'all products' foots to live gross. Full series: data/product_daily.csv

## Worst (strategy, product) cells, last 10 reconciled days (attributed gross CNY)
| strategy | product | 10-27 | 10-28 | 10-29 | 10-30 | 11-02 | 11-03 | 11-04 | 11-05 | 11-06 | 11-09 | sum |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| fund_v3 | p | -19,280 | -3,280 | -8,720 | -160 | +4,660 | -2,120 | -8,760 | -5,160 | -4,100 | -11,560 | -58,480 |
| fund_v3 | cs | +640 | -3,400 | -10,780 | +2,720 | -11,120 | -1,120 | -3,900 | -16,200 | +3,940 | -17,640 | -56,860 |
| china_pairs | y | -18,375 | +1,785 | -105 | +480 | +11,400 | -15,660 | -16,065 | -5,130 | -7,455 | -7,440 | -56,565 |
| fund_v3 | eb | -3,730 | -930 | -3,170 | +0 | +6,840 | -18,620 | -6,840 | -10,980 | -4,000 | -9,540 | -50,970 |
| ks_ext | IF | -630 | -4,830 | +2,625 | -405 | -23,940 | +1,590 | -15,795 | +255 | -4,635 | +390 | -45,375 |
| china_pairs | pp | +5,888 | +4,762 | +4,425 | +6,030 | +5,760 | -18,322 | -3,098 | -16,380 | -20,700 | -10,462 | -42,098 |
| chem_fund | pp | -510 | -3,938 | -4,792 | -2,228 | -1,162 | -2,468 | -338 | -5,692 | -5,130 | -12,278 | -38,535 |
| china_pairs | TA | +1,020 | -60 | -540 | -1,740 | +4,785 | -15,360 | -4,050 | -19,305 | -1,485 | -180 | -36,915 |
| stat_arb | p | -11,750 | -2,760 | -7,440 | +250 | +3,800 | -640 | -2,370 | -1,200 | -5,480 | -8,350 | -35,940 |
| fund_v3 | TA | -780 | +80 | +3,440 | -2,400 | +1,600 | -17,320 | -3,100 | -11,500 | -1,240 | +0 | -31,220 |
| fund_v3 | i | +6,600 | -1,700 | -21,200 | +7,900 | -2,900 | +5,100 | -7,300 | -11,200 | -5,000 | +2,400 | -27,300 |
| agri_event | p | -21,150 | -4,140 | -11,160 | +2,250 | +8,550 | +0 | +0 | +0 | +0 | +0 | -25,650 |
| ks_branch | y | -1,400 | -3,672 | -6,808 | -2,320 | +6,032 | -3,712 | -7,072 | +912 | -1,560 | -5,200 | -24,800 |
| fund_v3 | FG | +6,160 | -8,400 | -3,920 | -10,840 | +800 | -6,240 | -4,200 | +0 | +2,000 | -40 | -24,680 |
| chem_fund | TA | +1,590 | -75 | -975 | +510 | +2,415 | -9,525 | -2,265 | -10,305 | -1,455 | -255 | -20,340 |
same holdings split as 'Live P&L by strategy'; summing a strategy's products reproduces its row there (trading / neither included as their own strategy). Full series: data/strategy_product_daily.csv

## Paper strategies (weight 0 in the forward book: tracked, not traded)
| strategy | weight 0 since | bt since (full) | bt last 20d | drawdown now | worst before pause | 60d Sharpe | paper-live since (full) | paper days | book coverage |
|---|---|---|---|---|---|---|---|---|---|
| agri_event | 2026-11-02 | -21,070 | -137,985 | -164,650 | -149,795 | -2.93 | -31,305 | 5 | 100% |
paper-live = the strategy's own pinned full-size book of D-1 x the settlement-to-settlement move of D, priced like the live attribution, on contracts the day's state capture marks (coverage). Re-entry: owner's call, at an attended morning merge; reweighting is Execution/weights_forward.json + weights_changelog.csv.

## Backtest vintages (full series kept on every restatement)
expected on the CURRENT series minus expected on the as-shipped pins, live window, weighted CNY (the bridge uses the pins):
| strategy | restated |
|---|---|
| ks_branch | +65,633 |
| fund_v3 | -42,020 |
| china_pairs | -24,878 |
| ks_ext | +6,911 |
| chem_fund | -6,668 |
| agri_event | +9,400 |
| stat_arb | +16,744 |
| all | +25,122 |
| strategy | vintages | latest | cause | commit | rows restated | net change (full size) |
|---|---|---|---|---|---|---|
| ks_branch | 2 | 20261102090932_cbbdd7664522.csv | unknown | cbbdd76 | 165 | +341,255 |
| ks_ext | 2 | 20261102090932_1a03a09367cb.csv | unknown | 1a03a09 | 91 | +31,590 |
| china_pairs | 2 | 20261102090932_51a17747e0e0.csv | unknown | 51a1774 | 44 | -46,815 |
| chem_fund | 3 | 20261105091241_a98238f08285.csv | data | a98238f | 1 | -480 |
| fund_v3 | 3 | 20261105091241_0712a0472bd7.csv | data | 0712a04 | 3 | -53 |
| stat_arb | 2 | 20261105091241_9f7e9a742805.csv | unknown | 9f7e9a7 | 1 | -7,530 |
| agri_event | 7 | 20261106091340_8f0b7b90cc1f.csv | data | 8f0b7b9 | 1 | -50 |
full series: data/backtest/vintages/<strategy>/; index: data/backtest/vintages/index.csv

## Data health
decision-price coverage (2026-11-09): 100% of held notional benchmarked (0 contract(s) unbenchmarked); 12 contract(s) (17%) first decided after the 0900 snap, so they straddle their own overnight leg
scale: 1 (since 2026-09-09)
regime: forward (merged weighted book) since 2026-08-31; 45 forward day(s), 8 legacy day(s)
merge weights (2026-11-09): ks_branch 0.8, fund_v3 2, china_pairs 1.5, ks_ext 0.25, chem_fund 1.5, agri_event 0, stat_arb 1
as-shipped pins: 53 live day(s) pinned; current series diverges from pins on chem_fund: 30 day(s), max 9,725 CNY, fund_v3: 47 day(s), max 22,683 CNY, ks_branch: 43 day(s), max 82,125 CNY, ks_ext: 35 day(s), max 42,170 CNY, stat_arb: 43 day(s), max 9,982 CNY, china_pairs: 23 day(s), max 10,910 CNY, agri_event: 10 day(s), max 7,250 CNY; standing counts -- a divergence is announced as an alert once, the first run it appears, and kept here afterwards
inbox ks summary mtime: 2026-11-09 05:57 UTC
