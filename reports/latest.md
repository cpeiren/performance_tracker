# Performance tracker - 2026-11-11   (reconciled through 2026-11-11)

## ALERTS
- VINTAGE agri_event: 14 historical row(s) restated (net +5,175 CNY, cause data, commit 8f0b7b9) -- kept as vintages/agri_event/20261111091151_8f0b7b90cc1f.csv; the bridge keeps the as-shipped pins
- WEIGHTS 2026-10-09: day's own merge weights not shipped yet -- carried forward from an earlier day.
- WEIGHTS 2026-10-16: day's own merge weights not shipped yet -- carried forward from an earlier day.
- WEIGHTS 2026-10-22: day's own merge weights not shipped yet -- carried forward from an earlier day.
- BT PENDING 2026-11-11: no mature backtest row for stat_arb (nonzero weight) -- day reconciled WITHOUT that sleeve's expected; its live P&L sits in bt_pending_live, not resid, until the rows ship.
- WEIGHTS CHANGE on 2026-09-01: ks_ext: 0.0->0.25.
- WEIGHTS CHANGE on 2026-09-02: stat_arb: 1.0->0.0.
- WEIGHTS CHANGE on 2026-09-03: stat_arb: 0.0->1.0.
- WEIGHTS CHANGE on 2026-11-02: agri_event: 1.0->0.0.
- WEIGHTS CHANGE on 2026-11-11: fpe: None->0.1, ks_outright: None->0.5.
- MISSING LIVE DAY 2026-08-28: trading day with a backtest row but no daily_pnl/state file; excluded from the bridge, expected pnl held in the missing-day bucket.
- SCALE 2026-08-28: no usable run record; previous scale carried forward.
- SCALE 2026-09-25: no usable run record; previous scale carried forward.
- SCALE CHANGE on 2026-08-27: now 0.2.
- SCALE CHANGE on 2026-09-01: now 0.5.
- SCALE CHANGE on 2026-09-09: now 1.
- BACKTEST REVISED: agri_event -- 14 mature row(s) changed since last run (net +5175 CNY, largest 2026-02-24 +47280 -> +50705; first 2026-02-09, last 2026-03-06). Regeneration upstream; baseline re-set.
- SLIPPAGE 2026-11-11: 3 unbenchmarked leg(s), +50 CNY exec cost without a shipped decision price.
- RESIDUAL 2026-08-27: -17267 CNY vs trailing median |resid| 2062, offset by neither neighbour (2026-08-26 +3749, 2026-08-31 -17348) -- attribution quality changed. (A break-out that a neighbouring day mirrors is the backtest/live day-window straddle and is not alerted.)
- RESIDUAL 2026-08-31: -17348 CNY vs trailing median |resid| 2277, offset by neither neighbour (2026-08-27 -17267, 2026-09-01 -8190) -- attribution quality changed. (A break-out that a neighbouring day mirrors is the backtest/live day-window straddle and is not alerted.)
- RESIDUAL 2026-09-01: -8190 CNY vs trailing median |resid| 2492, offset by neither neighbour (2026-08-31 -17348, 2026-09-02 -30063) -- attribution quality changed. (A break-out that a neighbouring day mirrors is the backtest/live day-window straddle and is not alerted.)
- RESIDUAL 2026-09-02: -30063 CNY vs trailing median |resid| 3121, offset by neither neighbour (2026-09-01 -8190, 2026-09-03 -29049) -- attribution quality changed. (A break-out that a neighbouring day mirrors is the backtest/live day-window straddle and is not alerted.)
- RESIDUAL 2026-09-03: -29049 CNY vs trailing median |resid| 3941, offset by neither neighbour (2026-09-02 -30063, 2026-09-04 -5584) -- attribution quality changed. (A break-out that a neighbouring day mirrors is the backtest/live day-window straddle and is not alerted.)
- RESIDUAL 2026-09-16: -103509 CNY vs trailing median |resid| 22936, offset by neither neighbour (2026-09-15 -28634, 2026-09-17 +23811) -- attribution quality changed. (A break-out that a neighbouring day mirrors is the backtest/live day-window straddle and is not alerted.)
- RESIDUAL 2026-10-26: +29017 CNY vs trailing median |resid| 7638, offset by neither neighbour (2026-10-23 +7825, 2026-10-27 +81673) -- attribution quality changed. (A break-out that a neighbouring day mirrors is the backtest/live day-window straddle and is not alerted.)
- RESIDUAL 2026-10-27: +81673 CNY vs trailing median |resid| 9046, offset by neither neighbour (2026-10-26 +29017, 2026-10-28 +2573) -- attribution quality changed. (A break-out that a neighbouring day mirrors is the backtest/live day-window straddle and is not alerted.)

## Latest reconciled day (2026-11-11, forward regime, PROVISIONAL: marked at the 16:00 close, re-marked to settlement after the next capture)
live gross +137,490 | expected (1 x bt +132,185) = +132,185 | gap +5,305
  exec_cost -5,590 (slip -5,640, unbench +50) | marking +20,710 | bookdiff +0 (carry +0, new +0) | intraday +0 | offbook +0 (0 contract(s)) | residual -27,955 (live re-marked to first decision, vs the previous backtest row)
  PARTIAL: no backtest row yet for stat_arb -- expected excludes it; its live P&L +6,960 is held out of resid
  fees +1,863 | broker residual +0 -> live net +135,627

## Cumulative bridge (live since 2026-08-18, 55 reconciled days, 1 with a sleeve's backtest pending)
| expected | -exec | +marking | +bookdiff | +intraday | +offbook | +bt pending | +resid | = live gross | -fees | +broker_resid | = live net |
|---|---|---|---|---|---|---|---|---|---|---|---|
| +457,698 | -74,758 | +39,955 | +90,047 | -6,568 | -50 | +6,960 | -12,065 | +501,220 | -55,564 | +11,094 | +456,749 |
missing live days excluded: 2026-08-28 (expected +4,849 held in bucket)

## Stats (daily CNY pnl)
| window | days | total | sharpe | mdd | hit |
|---|---|---|---|---|---|
| live net live-to-date | 55 | +456,749 | 2.26 | -330,281 | 55% |
| live net last-20d | 20 | -79,322 | -1.22 | -317,945 | 40% | (small sample)
| live net 2026-YTD | 55 | +456,749 | 2.26 | -330,281 | 55% |
| bt scaled live-to-date | 55 | +457,698 | 2.14 | -381,526 | 65% |
| bt scaled last-20d | 20 | -150,320 | -1.93 | -381,526 | 55% | (small sample)
| bt scaled 2026-YTD | 55 | +457,698 | 2.14 | -381,526 | 65% |

## Slippage (+ = cost; bps vs benchmarked notional)
| day | lots | notional M | slip total | drift | exec | bps | unbench legs | unbench CNY |
|---|---|---|---|---|---|---|---|---|
| 2026-10-29 | 393 | 27.9 | +4,825 | +3,225 | +1,600 | +2.13 | 6 | -620 |
| 2026-10-30 | 249 | 14.1 | +6,150 | +6,185 | -35 | +4.49 | 4 | +5 |
| 2026-11-02 | 258 | 19.2 | +7,360 | +6,620 | +740 | +3.92 | 3 | -5 |
| 2026-11-03 | 379 | 25.3 | +7,160 | +5,542 | +1,618 | +2.94 | 2 | +2,140 |
| 2026-11-04 | 364 | 32.1 | +2,030 | +1,422 | +608 | +0.64 | 1 | +275 |
| 2026-11-05 | 462 | 30.3 | +3,350 | +942 | +2,408 | +1.15 | 4 | -45 |
| 2026-11-06 | 863 | 42.1 | +13,755 | +6,750 | +7,005 | +3.27 | 1 | +45 |
| 2026-11-09 | 519 | 27.4 | -5,690 | -6,638 | +948 | -2.09 | 1 | -30 |
| 2026-11-10 | 484 | 26.2 | +1,890 | +445 | +1,445 | +0.75 | 2 | +118 |
| 2026-11-11 | 445 | 37.7 | -5,640 | -6,922 | +1,282 | -1.52 | 3 | +50 |
| live window (55d) | 20902 | 1295.1 | +59,020 | -5,452 | +64,472 | +0.49 | 256 | +15,738 |
exec-only bps over the window: +0.53; benchmark coverage 93% of traded notional

| product | days | lots | notional M | drift | exec (incl. unbench) | all-in | bps |
|---|---|---|---|---|---|---|---|
| IH | 35 | 142 | 118.1 | -28,170 | +5,010 | -23,160 | -1.96 |
| IF | 23 | 80 | 102.2 | -20,280 | +3,060 | -17,220 | -1.68 |
| CY | 42 | 304 | 33.4 | +10,688 | +5,912 | +16,600 | +4.96 |
| pg | 27 | 47 | 6.4 | +15,150 | +170 | +15,320 | +23.84 |
| bu | 48 | 586 | 27.7 | -14,215 | +1,510 | -12,705 | -4.59 |
| y | 46 | 322 | 28.6 | +9,945 | +2,135 | +12,080 | +4.22 |
| rb | 45 | 1509 | 46.6 | +9,605 | +1,765 | +11,370 | +2.44 |
| FG | 54 | 1036 | 18.7 | +4,720 | +6,140 | +10,860 | +5.81 |
| SF | 51 | 464 | 13.9 | +9,215 | +950 | +10,165 | +7.31 |
| SR | 49 | 1009 | 54.4 | +5,870 | +2,015 | +7,885 | +1.45 |
| PF | 46 | 302 | 12.4 | -7,875 | +755 | -7,120 | -5.75 |
| hc | 47 | 1759 | 57.7 | -11,580 | +4,910 | -6,670 | -1.16 |
| ru | 35 | 117 | 22.6 | +6,450 | -75 | +6,375 | +2.83 |
| cs | 53 | 1001 | 25.1 | +1,770 | +4,495 | +6,265 | +2.50 |
| SA | 51 | 730 | 14.7 | +5,430 | +650 | +6,080 | +4.13 |
| other (38) | - | 11494 | 712.5 | -2,175 | +40,808 | +38,632 | +0.54 |
| all products | - | 20902 | 1295.1 | -5,452 | +80,210 | +74,758 | +0.58 |
ranked by |all-in| over the live window (all-in = drift + exec = the bridge's exec_cost by product); product bps are vs traded notional

## Per strategy
| strategy | live? | bt 2026 pnl (full) | bt scaled+weighted (live window) | live attributed | note |
|---|---|---|---|---|---|
| Calendar main pool (branch) | yes | +1,017,765 | +12,068 | +81,211 | forward w=0.8 |
| Fundamental factor | yes | +852,959 | +438,987 | +396,195 | forward w=2 |
| Cross-product pairs | yes | +82,485 | +37,628 | +17,088 | forward w=1.5 |
| Calendar extended pool | yes | +507,305 | +17,592 | +69,925 | forward w=0.25 |
| Chemical fundamental | yes | +505,570 | +37,436 | -24,304 | forward w=1.5 |
| Agriculture event-driven | no | +29,375 | -111,243 | -152,798 | forward w=0 (parked) |
| Factor-neutral stat arb | yes | +335,722 | +25,231 | +59,448 | forward w=1 |
| Fund pipeline ensemble | yes | +2,166,788 | - | +0 | forward w=0.1 |
| Outright trend + basis | yes | +515,430 | - | +0 | forward w=0.5 |
| shared bucket | - | - | - | +3,575 | legacy days only: a contract both per-source books held |
| neither bucket (no target) | - | - | - | +2,330 | named by no book that day or the day before |
| trading bucket | - | - | - | +48,550 | forward days: live P&L minus the strategies' holdings (fills vs settlement on rebalances, lot rounding, scale changes) |
forward days: each strategy is its own previous-day weighted book x scale x the settlement-to-settlement move (holdings); legacy days remain exclusive-holder. The gap tables (attributed - expected) therefore exclude execution, which sits in trading.

## Live P&L by strategy, last 10 reconciled days (attributed gross CNY)
| day | ks_branch | fund_v3 | china_pairs | ks_ext | chem_fund | agri_event | stat_arb | fpe | ks_outright | shared | neither | trading | total |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 2026-10-29 | -49,776 | -53,440 | -825 | +6,281 | -6,968 | -18,070 | -15,165 | +0 | +0 | +0 | +0 | -8,983 | -146,945 |
| 2026-10-30 | -16,068 | -66,600 | -1,560 | +2,871 | +9,292 | +8,605 | +13,805 | +0 | +0 | +0 | -275 | +17,859 | -32,070 |
| 2026-11-02 | +4,260 | -660 | +7,845 | -25,403 | +15,420 | -3,995 | +12,980 | +0 | +0 | +0 | +0 | -12,588 | -2,140 |
| 2026-11-03 | -9,816 | +21,940 | -8,490 | -123 | -13,485 | +0 | +1,335 | +0 | +0 | +0 | +0 | +2,793 | -5,845 |
| 2026-11-04 | +7,320 | -21,410 | -2,842 | -13,680 | +11,618 | +0 | +12,140 | +0 | +0 | +0 | +0 | +4,875 | -1,980 |
| 2026-11-05 | -33,388 | +1,260 | -532 | +8,112 | -8,992 | +0 | +12,415 | +0 | +0 | +0 | +0 | -13,885 | -35,010 |
| 2026-11-06 | +316 | -2,180 | +21,278 | +4,886 | -10,478 | +0 | -8,320 | +0 | +0 | +0 | +0 | +6,048 | +11,550 |
| 2026-11-09 | -224 | +21,420 | +11,745 | -3,271 | -4,425 | +0 | -745 | +0 | +0 | +0 | +0 | +4,255 | +28,755 |
| 2026-11-10 | +10,060 | +60,290 | -5,542 | +4,261 | -39,090 | +0 | -8,585 | +0 | +0 | +0 | +0 | +1,881 | +23,275 |
| 2026-11-11 | +39,804 | +58,740 | +16,462 | +785 | -5,295 | +0 | +6,960 | +0 | +0 | +0 | +0 | +20,033 | +137,490 |
| sum | -47,512 | +19,360 | +37,538 | -15,279 | -52,402 | -13,460 | +26,820 | +0 | +0 | +0 | -275 | +22,291 | -22,920 |
forward days: previous-day weighted book x scale x settlement move per strategy, the rest in trading; total foots to live gross. Live-window sums: 'Per strategy' above; full series: data/per_strategy_daily.csv (attributed)

## Per strategy gap by day, last 10 reconciled days (live attributed - expected, CNY)
| day | ks_branch | fund_v3 | china_pairs | ks_ext | chem_fund | agri_event | stat_arb | fpe | ks_outright | total |
|---|---|---|---|---|---|---|---|---|---|---|
| 2026-10-29 | +31,404 | -1,601 | +480 | +7,169 | +7,665 | +585 | +3,032 | +0 | +0 | +48,734 |
| 2026-10-30 | +9,708 | -35,219 | -2,768 | -241 | +3,375 | +8,655 | -2,361 | +0 | +0 | -18,851 |
| 2026-11-02 | +9,376 | +63,262 | -1,358 | -26,996 | +3,038 | -3,995 | -3,385 | +0 | +0 | +39,942 |
| 2026-11-03 | -18,168 | -12,215 | -1,110 | +13,477 | -7,695 | +0 | +3,215 | +0 | +0 | -22,496 |
| 2026-11-04 | +2,600 | -42,652 | -6,390 | -17,409 | -240 | +0 | +12,722 | +0 | +0 | -51,368 |
| 2026-11-05 | -20,828 | -38,627 | +5,752 | +2,836 | +1,545 | +0 | +26,370 | +0 | +0 | -22,951 |
| 2026-11-06 | +16,056 | +9,255 | -3,420 | +208 | -16,882 | +0 | -4,371 | +0 | +0 | +845 |
| 2026-11-09 | -3,548 | +39,923 | -5,205 | +4,985 | +3,098 | +0 | -4,969 | +0 | +0 | +34,284 |
| 2026-11-10 | -18,696 | +40,476 | +870 | -1,682 | -10,462 | +0 | -3,516 | +0 | +0 | +6,989 |
| 2026-11-11 | +53,204 | -64,660 | +9,435 | -6,475 | -13,192 | +0 | - | +0 | +0 | -21,688 |
| sum | +61,108 | -42,058 | -3,712 | -24,129 | -29,752 | +5,245 | +26,738 | +0 | +0 | -6,561 |
full series: data/per_strategy_daily.csv (day, strategy, expected, attributed, gap); a strategy's daily total foots to expected - live_gross once the shared, neither and trading buckets are added. '-' = that sleeve's backtest row has not shipped yet (BT PENDING).

## Live P&L by product, last 10 reconciled days (gross CNY, worst first)
| product | 10-29 | 10-30 | 11-02 | 11-03 | 11-04 | 11-05 | 11-06 | 11-09 | 11-10 | 11-11 | 10d sum | live window |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| TA | +1,770 | -2,960 | +6,350 | -42,080 | -9,440 | -44,250 | -5,800 | +4,200 | -10,140 | +1,900 | -100,450 | -72,720 |
| pp | -8,380 | +1,800 | +410 | -14,870 | -2,660 | -17,820 | +955 | -11,905 | -37,895 | +13,410 | -76,955 | -90,065 |
| y | -7,880 | -2,330 | +8,940 | -25,520 | -29,090 | -8,710 | -12,240 | -7,260 | -1,200 | +12,740 | -72,550 | -110,510 |
| eb | -5,445 | -190 | +7,710 | -19,680 | -5,700 | -12,610 | -3,905 | -2,700 | -6,390 | +3,240 | -45,670 | +21,480 |
| i | -20,800 | +9,000 | -4,400 | +4,900 | -6,950 | -12,250 | -3,700 | +4,000 | -3,550 | +3,300 | -30,450 | -10,900 |
| IF | +2,880 | +9,120 | -26,400 | +3,420 | -15,000 | +900 | -540 | +1,320 | -240 | -600 | -25,140 | -65,940 |
| a | -16,320 | -4,410 | +2,070 | -6,810 | -12,270 | +5,100 | -5,410 | +5,480 | +1,700 | +6,030 | -24,840 | +11,470 |
| sp | +1,340 | -16,700 | +2,940 | +5,600 | -5,340 | -5,160 | -2,860 | +420 | +1,820 | -5,400 | -23,340 | +27,960 |
| ru | -5,900 | -1,800 | +150 | +1,200 | -5,800 | -900 | -450 | +500 | -2,600 | -6,700 | -22,300 | -14,900 |
| FG | -2,300 | -2,820 | +6,160 | -5,880 | -6,200 | -5,700 | +720 | -8,160 | -5,320 | +9,900 | -19,600 | +68,820 |
| br | +0 | +800 | +1,100 | -5,350 | -300 | -8,350 | -2,750 | +1,150 | -2,350 | -600 | -16,650 | -16,725 |
| c | +90 | -2,200 | +2,780 | +1,050 | -1,880 | +4,280 | -2,560 | +2,470 | -13,550 | -6,420 | -15,940 | -33,050 |
| MA | +2,260 | +5,380 | +11,020 | -12,150 | -3,700 | -11,620 | -5,080 | -1,850 | -4,400 | +5,260 | -14,880 | +9,500 |
| pg | -720 | -2,600 | +6,020 | -7,040 | -2,980 | -8,020 | -7,720 | +3,480 | +8,740 | -2,540 | -13,380 | -43,280 |
| ni | -1,220 | +1,730 | +180 | +2,470 | -410 | -10,520 | -9,800 | -1,020 | +3,290 | +2,350 | -12,950 | -28,620 |
| other (28) | -55,595 | -24,325 | -26,970 | +46,260 | +69,665 | -7,005 | +45,085 | -4,610 | +13,585 | +55,595 | +111,685 | +333,870 |
| rb | -15,710 | +6,930 | +17,080 | +16,450 | +4,400 | -17,450 | -5,660 | -2,340 | -7,540 | +23,760 | +19,920 | +139,670 |
| ss | -850 | +2,500 | +900 | +7,550 | -150 | +6,550 | -675 | +1,000 | +2,400 | +4,025 | +23,250 | +16,500 |
| m | -6,330 | +1,280 | -3,810 | +90 | +5,870 | +3,880 | +6,680 | +6,660 | +12,590 | -2,550 | +24,360 | +7,320 |
| hc | +17,000 | -9,790 | -6,480 | -9,690 | +750 | +19,770 | +3,300 | +5,630 | +7,780 | -130 | +28,140 | -134,570 |
| v | -4,440 | -2,440 | +1,815 | +520 | +10,110 | +21,390 | -3,885 | +5,370 | +15,230 | -10,775 | +32,895 | +29,610 |
| PF | -940 | -1,430 | -4,860 | +23,910 | +2,570 | +13,630 | +3,580 | -2,250 | -1,980 | +1,120 | +33,350 | +82,810 |
| eg | +1,720 | -5,540 | -3,220 | +13,720 | +2,050 | +26,680 | +4,990 | -1,340 | +3,920 | -4,220 | +38,760 | +48,890 |
| fu | -10,780 | +1,410 | +4,000 | +9,400 | +11,500 | +21,060 | +1,620 | +3,490 | -2,650 | -40 | +39,010 | +58,110 |
| l | -9,445 | +2,615 | -9,825 | +12,460 | -4,500 | +14,790 | +25,555 | +3,770 | +16,200 | +85 | +51,705 | +64,540 |
| al | -950 | +4,900 | +4,200 | -5,775 | +3,475 | -2,675 | -7,900 | +23,250 | +35,825 | +34,750 | +89,100 | +201,950 |
| all products | -146,945 | -32,070 | -2,140 | -5,845 | -1,980 | -35,010 | +11,550 | +28,755 | +23,275 | +137,490 | -22,920 | +501,220 |
executor total_pnl (holding + trading, settlement-to-settlement once the next capture lands, before fees) summed by product root; 'all products' foots to live gross. Full series: data/product_daily.csv

## Worst (strategy, product) cells, last 10 reconciled days (attributed gross CNY)
| strategy | product | 10-29 | 10-30 | 11-02 | 11-03 | 11-04 | 11-05 | 11-06 | 11-09 | 11-10 | 11-11 | sum |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| china_pairs | pp | +4,425 | +6,030 | +5,760 | -18,322 | -3,098 | -16,380 | -20,700 | -2,362 | -30,772 | +8,910 | -66,510 |
| fund_v3 | eb | -3,170 | +0 | +6,840 | -18,620 | -6,840 | -10,980 | -4,000 | -5,850 | -9,570 | +4,110 | -48,080 |
| ks_ext | IF | +2,625 | -405 | -23,940 | +1,590 | -15,795 | +255 | -4,635 | +1,455 | -135 | -525 | -39,510 |
| china_pairs | TA | -540 | -1,740 | +4,785 | -15,360 | -4,050 | -19,305 | -1,485 | +2,520 | -5,550 | +2,025 | -38,700 |
| chem_fund | pp | -4,792 | -2,228 | -1,162 | -2,468 | -338 | -5,692 | -5,130 | -4,762 | -16,830 | +7,470 | -35,932 |
| fund_v3 | TA | +3,440 | -2,400 | +1,600 | -17,320 | -3,100 | -11,500 | -1,240 | +0 | +1,420 | -600 | -29,700 |
| fund_v3 | i | -21,200 | +7,900 | -2,900 | +5,100 | -7,300 | -11,200 | -5,000 | +5,400 | -2,100 | +3,400 | -27,900 |
| china_pairs | y | -105 | +480 | +11,400 | -15,660 | -16,065 | -5,130 | -7,455 | -4,920 | -240 | +12,000 | -25,695 |
| chem_fund | TA | -975 | +510 | +2,415 | -9,525 | -2,265 | -10,305 | -1,455 | +2,010 | -5,505 | +1,845 | -23,250 |
| fund_v3 | FG | -3,920 | -10,840 | +800 | -6,240 | -4,200 | +0 | +2,000 | +7,080 | -13,320 | +6,920 | -21,720 |
| stat_arb | pg | +400 | +2,360 | +6,640 | -7,040 | -2,980 | -8,020 | -5,640 | -2,440 | -6,380 | +1,940 | -21,160 |
| fund_v3 | p | -8,720 | -160 | +4,660 | -2,120 | -8,760 | -5,160 | -4,100 | -4,600 | -1,620 | +10,240 | -20,340 |
| fund_v3 | sp | +960 | -14,720 | +3,360 | +6,120 | -5,560 | -5,080 | -2,560 | +400 | +1,800 | -4,560 | -19,840 |
| ks_branch | pp | -3,568 | +4,864 | -664 | -6,564 | -1,644 | -6,552 | +7,924 | -6,280 | -6,044 | -1,072 | -19,600 |
| chem_fund | bu | -2,415 | -1,470 | -1,080 | +3,870 | +180 | -3,840 | -1,020 | -4,050 | -8,115 | +480 | -17,460 |
same holdings split as 'Live P&L by strategy'; summing a strategy's products reproduces its row there (trading / neither included as their own strategy). Full series: data/strategy_product_daily.csv

## Paper strategies (weight 0 in the forward book: tracked, not traded)
| strategy | weight 0 since | bt since (full) | bt last 20d | drawdown now | worst before pause | 60d Sharpe | paper-live since (full) | paper days | book coverage |
|---|---|---|---|---|---|---|---|---|---|
| agri_event | 2026-11-02 | -19,690 | -137,880 | -163,270 | -149,795 | -3.13 | -12,760 | 7 | 100% |
paper-live = the strategy's own pinned full-size book of D-1 x the settlement-to-settlement move of D, priced like the live attribution, on contracts the day's state capture marks (coverage). Re-entry: owner's call, at an attended morning merge; reweighting is Execution/weights_forward.json + weights_changelog.csv.

## Backtest vintages (full series kept on every restatement)
expected on the CURRENT series minus expected on the as-shipped pins, live window, weighted CNY (the bridge uses the pins):
| strategy | restated |
|---|---|
| ks_branch | +65,633 |
| fund_v3 | -42,265 |
| china_pairs | -24,878 |
| ks_ext | +6,911 |
| chem_fund | -6,668 |
| agri_event | +9,400 |
| stat_arb | +16,744 |
| all | +24,877 |
| strategy | vintages | latest | cause | commit | rows restated | net change (full size) |
|---|---|---|---|---|---|---|
| ks_branch | 2 | 20261102090932_cbbdd7664522.csv | unknown | cbbdd76 | 165 | +341,255 |
| ks_ext | 2 | 20261102090932_1a03a09367cb.csv | unknown | 1a03a09 | 91 | +31,590 |
| china_pairs | 2 | 20261102090932_51a17747e0e0.csv | unknown | 51a1774 | 44 | -46,815 |
| chem_fund | 3 | 20261105091241_a98238f08285.csv | data | a98238f | 1 | -480 |
| stat_arb | 2 | 20261105091241_9f7e9a742805.csv | unknown | 9f7e9a7 | 1 | -7,530 |
| fund_v3 | 4 | 20261110091023_0712a0472bd7.csv | data | 0712a04 | 3 | -184 |
| agri_event | 8 | 20261111091151_8f0b7b90cc1f.csv | data | 8f0b7b9 | 14 | +5,175 |
| ks_outright | 1 | 20261111091151_49ac2cfb3881.csv | first | 49ac2cf | 0 | +0 |
| fpe | 1 | 20261111091151_01eab32dfcbf.csv | first | 01eab32 | 0 | +0 |
full series: data/backtest/vintages/<strategy>/; index: data/backtest/vintages/index.csv

## Data health
decision-price coverage (2026-11-11): 100% of held notional benchmarked (0 contract(s) unbenchmarked); 17 contract(s) (10%) first decided after the 0900 snap, so they straddle their own overnight leg
scale: 1 (since 2026-09-09)
regime: forward (merged weighted book) since 2026-08-31; 47 forward day(s), 8 legacy day(s)
merge weights (2026-11-11): ks_branch 0.8, fund_v3 2, china_pairs 1.5, ks_ext 0.25, chem_fund 1.5, agri_event 0, stat_arb 1, fpe 0.1, ks_outright 0.5
as-shipped pins: 55 live day(s) pinned; current series diverges from pins on chem_fund: 30 day(s), max 9,725 CNY, fund_v3: 49 day(s), max 22,683 CNY, ks_branch: 43 day(s), max 82,125 CNY, ks_ext: 35 day(s), max 42,170 CNY, stat_arb: 43 day(s), max 9,982 CNY, china_pairs: 23 day(s), max 10,910 CNY, agri_event: 10 day(s), max 7,250 CNY; standing counts -- a divergence is announced as an alert once, the first run it appears, and kept here afterwards
inbox ks summary mtime: 2026-11-11 05:57 UTC
