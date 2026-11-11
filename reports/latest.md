# Performance tracker - 2026-11-10   (reconciled through 2026-11-10)

## ALERTS
- VINTAGE fund_v3: 3 historical row(s) restated (net -184 CNY, cause data, commit 0712a04) -- kept as vintages/fund_v3/20261110091023_0712a0472bd7.csv; the bridge keeps the as-shipped pins
- WEIGHTS 2026-10-09: day's own merge weights not shipped yet -- carried forward from an earlier day.
- WEIGHTS 2026-10-16: day's own merge weights not shipped yet -- carried forward from an earlier day.
- WEIGHTS 2026-10-22: day's own merge weights not shipped yet -- carried forward from an earlier day.
- BT PENDING 2026-11-10: no mature backtest row for stat_arb (nonzero weight) -- day reconciled WITHOUT that sleeve's expected; its live P&L sits in bt_pending_live, not resid, until the rows ship.
- WEIGHTS CHANGE on 2026-09-01: ks_ext: 0.0->0.25.
- WEIGHTS CHANGE on 2026-09-02: stat_arb: 1.0->0.0.
- WEIGHTS CHANGE on 2026-09-03: stat_arb: 0.0->1.0.
- WEIGHTS CHANGE on 2026-11-02: agri_event: 1.0->0.0.
- BT REVISED vs PINS: fund_v3 current history differs from pinned as-shipped values on 2 new live-window day(s) (max |diff| 22683 CNY, first 2026-11-04); the bridge keeps the pins.
- MISSING LIVE DAY 2026-08-28: trading day with a backtest row but no daily_pnl/state file; excluded from the bridge, expected pnl held in the missing-day bucket.
- SCALE 2026-08-28: no usable run record; previous scale carried forward.
- SCALE 2026-09-25: no usable run record; previous scale carried forward.
- SCALE CHANGE on 2026-08-27: now 0.2.
- SCALE CHANGE on 2026-09-01: now 0.5.
- SCALE CHANGE on 2026-09-09: now 1.
- SLIPPAGE 2026-11-10: 2 unbenchmarked leg(s), +118 CNY exec cost without a shipped decision price.
- RESIDUAL 2026-08-27: -17267 CNY vs trailing median |resid| 2062, offset by neither neighbour (2026-08-26 +3749, 2026-08-31 -17348) -- attribution quality changed. (A break-out that a neighbouring day mirrors is the backtest/live day-window straddle and is not alerted.)
- RESIDUAL 2026-08-31: -17348 CNY vs trailing median |resid| 2277, offset by neither neighbour (2026-08-27 -17267, 2026-09-01 -8190) -- attribution quality changed. (A break-out that a neighbouring day mirrors is the backtest/live day-window straddle and is not alerted.)
- RESIDUAL 2026-09-01: -8190 CNY vs trailing median |resid| 2492, offset by neither neighbour (2026-08-31 -17348, 2026-09-02 -30063) -- attribution quality changed. (A break-out that a neighbouring day mirrors is the backtest/live day-window straddle and is not alerted.)
- RESIDUAL 2026-09-02: -30063 CNY vs trailing median |resid| 3121, offset by neither neighbour (2026-09-01 -8190, 2026-09-03 -29049) -- attribution quality changed. (A break-out that a neighbouring day mirrors is the backtest/live day-window straddle and is not alerted.)
- RESIDUAL 2026-09-03: -29049 CNY vs trailing median |resid| 3941, offset by neither neighbour (2026-09-02 -30063, 2026-09-04 -5584) -- attribution quality changed. (A break-out that a neighbouring day mirrors is the backtest/live day-window straddle and is not alerted.)
- RESIDUAL 2026-09-16: -103509 CNY vs trailing median |resid| 22936, offset by neither neighbour (2026-09-15 -28634, 2026-09-17 +23811) -- attribution quality changed. (A break-out that a neighbouring day mirrors is the backtest/live day-window straddle and is not alerted.)
- RESIDUAL 2026-10-26: +29017 CNY vs trailing median |resid| 7638, offset by neither neighbour (2026-10-23 +7825, 2026-10-27 +81673) -- attribution quality changed. (A break-out that a neighbouring day mirrors is the backtest/live day-window straddle and is not alerted.)
- RESIDUAL 2026-10-27: +81673 CNY vs trailing median |resid| 9046, offset by neither neighbour (2026-10-26 +29017, 2026-10-28 +2573) -- attribution quality changed. (A break-out that a neighbouring day mirrors is the backtest/live day-window straddle and is not alerted.)

## Latest reconciled day (2026-11-10, forward regime, PROVISIONAL: marked at the 16:00 close, re-marked to settlement after the next capture)
live gross +58,290 | expected (1 x bt +19,473) = +19,473 | gap +38,817
  exec_cost +2,008 (slip +1,890, unbench +118) | marking +32,465 | bookdiff +0 (carry +0, new +0) | intraday +0 | offbook +0 (0 contract(s)) | residual +16,189 (live re-marked to first decision, vs the previous backtest row)
  PARTIAL: no backtest row yet for stat_arb -- expected excludes it; its live P&L -7,830 is held out of resid
  fees +1,086 | broker residual +0 -> live net +57,204

## Cumulative bridge (live since 2026-08-18, 54 reconciled days, 1 with a sleeve's backtest pending)
| expected | -exec | +marking | +bookdiff | +intraday | +offbook | +bt pending | +resid | = live gross | -fees | +broker_resid | = live net |
|---|---|---|---|---|---|---|---|---|---|---|---|
| +330,582 | -80,348 | +54,260 | +90,047 | -6,568 | -50 | -7,830 | +18,651 | +398,745 | -53,701 | +11,091 | +356,135 |
missing live days excluded: 2026-08-28 (expected +4,849 held in bucket)

## Stats (daily CNY pnl)
| window | days | total | sharpe | mdd | hit |
|---|---|---|---|---|---|
| live net live-to-date | 54 | +356,135 | 1.85 | -330,281 | 54% |
| live net last-20d | 20 | -131,951 | -2.39 | -317,945 | 40% | (small sample)
| live net 2026-YTD | 54 | +356,135 | 1.85 | -330,281 | 54% |
| bt scaled live-to-date | 54 | +330,582 | 1.62 | -381,526 | 65% |
| bt scaled last-20d | 20 | -248,512 | -3.69 | -381,526 | 55% | (small sample)
| bt scaled 2026-YTD | 54 | +330,582 | 1.62 | -381,526 | 65% |

## Slippage (+ = cost; bps vs benchmarked notional)
| day | lots | notional M | slip total | drift | exec | bps | unbench legs | unbench CNY |
|---|---|---|---|---|---|---|---|---|
| 2026-10-28 | 220 | 17.2 | +7,060 | +6,922 | +138 | +4.23 | 3 | +320 |
| 2026-10-29 | 393 | 27.9 | +4,825 | +3,225 | +1,600 | +2.13 | 6 | -620 |
| 2026-10-30 | 249 | 14.1 | +6,150 | +6,185 | -35 | +4.49 | 4 | +5 |
| 2026-11-02 | 258 | 19.2 | +7,360 | +6,620 | +740 | +3.92 | 3 | -5 |
| 2026-11-03 | 379 | 25.3 | +7,160 | +5,542 | +1,618 | +2.94 | 2 | +2,140 |
| 2026-11-04 | 364 | 32.1 | +2,030 | +1,422 | +608 | +0.64 | 1 | +275 |
| 2026-11-05 | 462 | 30.3 | +3,350 | +942 | +2,408 | +1.15 | 4 | -45 |
| 2026-11-06 | 863 | 42.1 | +13,755 | +6,750 | +7,005 | +3.27 | 1 | +45 |
| 2026-11-09 | 519 | 27.4 | -5,690 | -6,638 | +948 | -2.09 | 1 | -30 |
| 2026-11-10 | 484 | 26.2 | +1,890 | +445 | +1,445 | +0.75 | 2 | +118 |
| live window (54d) | 20457 | 1257.4 | +64,660 | +1,470 | +63,190 | +0.55 | 253 | +15,688 |
exec-only bps over the window: +0.54; benchmark coverage 93% of traded notional

| product | days | lots | notional M | drift | exec (incl. unbench) | all-in | bps |
|---|---|---|---|---|---|---|---|
| IH | 34 | 132 | 109.9 | -28,080 | +5,040 | -23,040 | -2.10 |
| IF | 22 | 76 | 97.4 | -20,040 | +2,700 | -17,340 | -1.78 |
| CY | 41 | 298 | 32.8 | +11,162 | +5,638 | +16,800 | +5.12 |
| pg | 27 | 47 | 6.4 | +15,150 | +170 | +15,320 | +23.84 |
| bu | 47 | 573 | 27.1 | -14,110 | +1,470 | -12,640 | -4.66 |
| rb | 44 | 1489 | 46.0 | +10,315 | +1,695 | +12,010 | +2.61 |
| y | 45 | 318 | 28.3 | +9,705 | +2,135 | +11,840 | +4.18 |
| FG | 53 | 1020 | 18.4 | +5,140 | +5,700 | +10,840 | +5.88 |
| SF | 50 | 460 | 13.8 | +9,635 | +930 | +10,565 | +7.67 |
| PF | 45 | 281 | 11.6 | -8,475 | +765 | -7,710 | -6.67 |
| SR | 48 | 996 | 53.7 | +5,495 | +2,040 | +7,535 | +1.40 |
| ru | 34 | 107 | 20.6 | +7,150 | -125 | +7,025 | +3.41 |
| SA | 50 | 717 | 14.5 | +5,580 | +760 | +6,340 | +4.38 |
| hc | 46 | 1740 | 57.1 | -11,315 | +5,005 | -6,310 | -1.10 |
| a | 49 | 610 | 32.2 | +2,970 | +3,185 | +6,155 | +1.91 |
| other (35) | - | 11593 | 687.6 | +1,188 | +41,770 | +42,958 | +0.62 |
| all products | - | 20457 | 1257.4 | +1,470 | +78,878 | +80,348 | +0.64 |
ranked by |all-in| over the live window (all-in = drift + exec = the bridge's exec_cost by product); product bps are vs traded notional

## Per strategy
| strategy | live? | bt 2026 pnl (full) | bt scaled+weighted (live window) | live attributed | note |
|---|---|---|---|---|---|
| Calendar main pool (branch) | yes | +1,034,515 | +25,468 | +37,151 | forward w=0.8 |
| Fundamental factor | yes | +791,259 | +315,587 | +402,265 | forward w=2 |
| Cross-product pairs | yes | +77,800 | +30,601 | -9,020 | forward w=1.5 |
| Calendar extended pool | yes | +478,265 | +10,332 | +70,301 | forward w=0.25 |
| Chemical fundamental | yes | +500,305 | +29,538 | -25,497 | forward w=1.5 |
| Agriculture event-driven | no | +12,035 | -111,243 | -152,798 | forward w=0 (parked) |
| Factor-neutral stat arb | yes | +340,791 | +30,299 | +53,244 | forward w=1 |
| shared bucket | - | - | - | +3,575 | legacy days only: a contract both per-source books held |
| neither bucket (no target) | - | - | - | +2,330 | named by no book that day or the day before |
| trading bucket | - | - | - | +17,194 | forward days: live P&L minus the strategies' holdings (fills vs settlement on rebalances, lot rounding, scale changes) |
forward days: each strategy is its own previous-day weighted book x scale x the settlement-to-settlement move (holdings); legacy days remain exclusive-holder. The gap tables (attributed - expected) therefore exclude execution, which sits in trading.

## Live P&L by strategy, last 10 reconciled days (attributed gross CNY)
| day | ks_branch | fund_v3 | china_pairs | ks_ext | chem_fund | agri_event | stat_arb | shared | neither | trading | total |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 2026-10-28 | +4,048 | -15,440 | -5,362 | -7,313 | -2,760 | -10,980 | -2,965 | +0 | +0 | -2,938 | -43,710 |
| 2026-10-29 | -49,776 | -53,440 | -825 | +6,281 | -6,968 | -18,070 | -15,165 | +0 | +0 | -8,983 | -146,945 |
| 2026-10-30 | -16,068 | -66,600 | -1,560 | +2,871 | +9,292 | +8,605 | +13,805 | +0 | -275 | +17,859 | -32,070 |
| 2026-11-02 | +4,260 | -660 | +7,845 | -25,403 | +15,420 | -3,995 | +12,980 | +0 | +0 | -12,588 | -2,140 |
| 2026-11-03 | -9,816 | +21,940 | -8,490 | -123 | -13,485 | +0 | +1,335 | +0 | +0 | +2,793 | -5,845 |
| 2026-11-04 | +7,320 | -21,410 | -2,842 | -13,680 | +11,618 | +0 | +12,140 | +0 | +0 | +4,875 | -1,980 |
| 2026-11-05 | -33,388 | +1,260 | -532 | +8,112 | -8,992 | +0 | +12,415 | +0 | +0 | -13,885 | -35,010 |
| 2026-11-06 | +316 | -2,180 | +21,278 | +4,886 | -10,478 | +0 | -8,320 | +0 | +0 | +6,048 | +11,550 |
| 2026-11-09 | -224 | +21,420 | +11,745 | -3,271 | -4,425 | +0 | -745 | +0 | +0 | +4,255 | +28,755 |
| 2026-11-10 | +5,804 | +125,100 | -15,188 | +5,423 | -45,578 | +0 | -7,830 | +0 | +0 | -9,442 | +58,290 |
| sum | -87,524 | +9,990 | +6,068 | -22,215 | -56,355 | -24,440 | +17,650 | +0 | -275 | -12,004 | -169,105 |
forward days: previous-day weighted book x scale x settlement move per strategy, the rest in trading; total foots to live gross. Live-window sums: 'Per strategy' above; full series: data/per_strategy_daily.csv (attributed)

## Per strategy gap by day, last 10 reconciled days (live attributed - expected, CNY)
| day | ks_branch | fund_v3 | china_pairs | ks_ext | chem_fund | agri_event | stat_arb | total |
|---|---|---|---|---|---|---|---|---|
| 2026-10-28 | -13,640 | +4,387 | -210 | -11,386 | +10,568 | -8,470 | -10,748 | -29,499 |
| 2026-10-29 | +31,404 | -1,601 | +480 | +7,169 | +7,665 | +585 | +3,032 | +48,734 |
| 2026-10-30 | +9,708 | -35,219 | -2,768 | -241 | +3,375 | +8,655 | -2,361 | -18,851 |
| 2026-11-02 | +9,376 | +63,262 | -1,358 | -26,996 | +3,038 | -3,995 | -3,385 | +39,942 |
| 2026-11-03 | -18,168 | -12,215 | -1,110 | +13,477 | -7,695 | +0 | +3,215 | -22,496 |
| 2026-11-04 | +2,600 | -42,652 | -6,390 | -17,409 | -240 | +0 | +12,722 | -51,368 |
| 2026-11-05 | -20,828 | -38,627 | +5,752 | +2,836 | +1,545 | +0 | +26,370 | -22,951 |
| 2026-11-06 | +16,056 | +9,255 | -3,420 | +208 | -16,882 | +0 | -4,371 | +845 |
| 2026-11-09 | -3,548 | +39,923 | -5,205 | +4,985 | +3,098 | +0 | -4,969 | +34,284 |
| 2026-11-10 | -22,952 | +105,286 | -8,775 | -521 | -16,950 | +0 | - | +56,088 |
| sum | -9,992 | +91,799 | -23,002 | -27,879 | -12,480 | -3,225 | +19,506 | +34,727 |
full series: data/per_strategy_daily.csv (day, strategy, expected, attributed, gap); a strategy's daily total foots to expected - live_gross once the shared, neither and trading buckets are added. '-' = that sleeve's backtest row has not shipped yet (BT PENDING).

## Live P&L by product, last 10 reconciled days (gross CNY, worst first)
| product | 10-28 | 10-29 | 10-30 | 11-02 | 11-03 | 11-04 | 11-05 | 11-06 | 11-09 | 11-10 | 10d sum | live window |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| TA | +290 | +1,770 | -2,960 | +6,350 | -42,080 | -9,440 | -44,250 | -5,800 | +4,200 | -12,940 | -104,860 | -77,420 |
| pp | -1,165 | -8,380 | +1,800 | +410 | -14,870 | -2,660 | -17,820 | +955 | -11,905 | -47,185 | -100,820 | -112,765 |
| y | -3,550 | -7,880 | -2,330 | +8,940 | -25,520 | -29,090 | -8,710 | -12,240 | -7,260 | +1,470 | -86,170 | -120,580 |
| eb | -2,215 | -5,445 | -190 | +7,710 | -19,680 | -5,700 | -12,610 | -3,905 | -2,700 | -7,860 | -52,595 | +16,770 |
| a | -2,580 | -16,320 | -4,410 | +2,070 | -6,810 | -12,270 | +5,100 | -5,410 | +5,480 | +1,640 | -33,510 | +5,380 |
| i | -1,800 | -20,800 | +9,000 | -4,400 | +4,900 | -6,950 | -12,250 | -3,700 | +4,000 | -1,050 | -33,050 | -11,700 |
| IF | -5,040 | +2,880 | +9,120 | -26,400 | +3,420 | -15,000 | +900 | -540 | +1,320 | -840 | -30,180 | -65,940 |
| FG | +1,060 | -2,300 | -2,820 | +6,160 | -5,880 | -6,200 | -5,700 | +720 | -8,160 | -6,520 | -29,640 | +57,720 |
| CF | -14,350 | -7,350 | +6,175 | -2,700 | -6,300 | +1,650 | +5,325 | -2,500 | -4,075 | -25 | -24,150 | -98,350 |
| MA | +2,530 | +2,260 | +5,380 | +11,020 | -12,150 | -3,700 | -11,620 | -5,080 | -1,850 | -5,710 | -18,920 | +2,930 |
| sp | +3,880 | +1,340 | -16,700 | +2,940 | +5,600 | -5,340 | -5,160 | -2,860 | +420 | -2,920 | -18,800 | +28,620 |
| br | +400 | +0 | +800 | +1,100 | -5,350 | -300 | -8,350 | -2,750 | +1,150 | -2,300 | -15,600 | -16,075 |
| ru | +3,150 | -5,900 | -1,800 | +150 | +1,200 | -5,800 | -900 | -450 | +500 | -2,650 | -12,500 | -8,250 |
| c | +3,630 | +90 | -2,200 | +2,780 | +1,050 | -1,880 | +4,280 | -2,560 | +2,470 | -18,650 | -10,990 | -31,730 |
| pg | -420 | -720 | -2,600 | +6,020 | -7,040 | -2,980 | -8,020 | -7,720 | +3,480 | +11,640 | -8,360 | -37,840 |
| other (25) | -14,120 | -68,775 | -19,340 | -5,610 | +76,480 | +52,355 | -38,700 | +20,975 | -1,495 | +47,870 | +49,640 | +496,025 |
| ss | -525 | -850 | +2,500 | +900 | +7,550 | -150 | +6,550 | -675 | +1,000 | +4,850 | +21,150 | +14,925 |
| m | +2,110 | -6,330 | +1,280 | -3,810 | +90 | +5,870 | +3,880 | +6,680 | +6,660 | +5,440 | +21,870 | +2,720 |
| cu | +3,550 | +3,600 | -2,500 | -1,400 | -5,000 | +19,650 | -1,600 | +11,150 | -2,400 | -1,100 | +23,950 | +2,950 |
| hc | -3,020 | +17,000 | -9,790 | -6,480 | -9,690 | +750 | +19,770 | +3,300 | +5,630 | +7,780 | +25,250 | -134,440 |
| PF | -850 | -940 | -1,430 | -4,860 | +23,910 | +2,570 | +13,630 | +3,580 | -2,250 | -1,340 | +32,020 | +82,330 |
| fu | -360 | -10,780 | +1,410 | +4,000 | +9,400 | +11,500 | +21,060 | +1,620 | +3,490 | -3,970 | +37,370 | +56,830 |
| v | -7,400 | -4,440 | -2,440 | +1,815 | +520 | +10,110 | +21,390 | -3,885 | +5,370 | +22,280 | +43,320 | +47,435 |
| eg | +3,200 | +1,720 | -5,540 | -3,220 | +13,720 | +2,050 | +26,680 | +4,990 | -1,340 | +4,540 | +46,800 | +53,730 |
| al | -14,850 | -950 | +4,900 | +4,200 | -5,775 | +3,475 | -2,675 | -7,900 | +23,250 | +43,200 | +46,875 | +174,575 |
| l | +4,735 | -9,445 | +2,615 | -9,825 | +12,460 | -4,500 | +14,790 | +25,555 | +3,770 | +22,640 | +62,795 | +70,895 |
| all products | -43,710 | -146,945 | -32,070 | -2,140 | -5,845 | -1,980 | -35,010 | +11,550 | +28,755 | +58,290 | -169,105 | +398,745 |
executor total_pnl (holding + trading, settlement-to-settlement once the next capture lands, before fees) summed by product root; 'all products' foots to live gross. Full series: data/product_daily.csv

## Worst (strategy, product) cells, last 10 reconciled days (attributed gross CNY)
| strategy | product | 10-28 | 10-29 | 10-30 | 11-02 | 11-03 | 11-04 | 11-05 | 11-06 | 11-09 | 11-10 | sum |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| china_pairs | pp | +4,762 | +4,425 | +6,030 | +5,760 | -18,322 | -3,098 | -16,380 | -20,700 | -2,362 | -45,292 | -85,178 |
| fund_v3 | eb | -930 | -3,170 | +0 | +6,840 | -18,620 | -6,840 | -10,980 | -4,000 | -5,850 | -12,630 | -56,180 |
| chem_fund | pp | -3,938 | -4,792 | -2,228 | -1,162 | -2,468 | -338 | -5,692 | -5,130 | -4,762 | -20,205 | -50,715 |
| ks_ext | IF | -4,830 | +2,625 | -405 | -23,940 | +1,590 | -15,795 | +255 | -4,635 | +1,455 | -1,485 | -45,165 |
| china_pairs | TA | -60 | -540 | -1,740 | +4,785 | -15,360 | -4,050 | -19,305 | -1,485 | +2,520 | -7,350 | -42,585 |
| fund_v3 | FG | -8,400 | -3,920 | -10,840 | +800 | -6,240 | -4,200 | +0 | +2,000 | +7,080 | -16,040 | -39,760 |
| china_pairs | y | +1,785 | -105 | +480 | +11,400 | -15,660 | -16,065 | -5,130 | -7,455 | -4,920 | +1,440 | -34,230 |
| fund_v3 | i | -1,700 | -21,200 | +7,900 | -2,900 | +5,100 | -7,300 | -11,200 | -5,000 | +5,400 | +1,400 | -29,500 |
| fund_v3 | TA | +80 | +3,440 | -2,400 | +1,600 | -17,320 | -3,100 | -11,500 | -1,240 | +0 | +1,860 | -28,580 |
| fund_v3 | p | -3,280 | -8,720 | -160 | +4,660 | -2,120 | -8,760 | -5,160 | -4,100 | -4,600 | +3,900 | -28,340 |
| chem_fund | TA | -75 | -975 | +510 | +2,415 | -9,525 | -2,265 | -10,305 | -1,455 | +2,010 | -7,275 | -26,940 |
| stat_arb | pg | +340 | +400 | +2,360 | +6,640 | -7,040 | -2,980 | -8,020 | -5,640 | -2,440 | -8,640 | -25,020 |
| chem_fund | bu | -780 | -2,415 | -1,470 | -1,080 | +3,870 | +180 | -3,840 | -1,020 | -4,050 | -11,175 | -21,780 |
| ks_branch | y | -3,672 | -6,808 | -2,320 | +6,032 | -3,712 | -7,072 | +912 | -1,560 | -2,456 | +432 | -20,224 |
| ks_branch | CF | -6,240 | +0 | -1,040 | +0 | -4,160 | -1,040 | +1,040 | -2,320 | -5,200 | +780 | -18,180 |
same holdings split as 'Live P&L by strategy'; summing a strategy's products reproduces its row there (trading / neither included as their own strategy). Full series: data/strategy_product_daily.csv

## Paper strategies (weight 0 in the forward book: tracked, not traded)
| strategy | weight 0 since | bt since (full) | bt last 20d | drawdown now | worst before pause | 60d Sharpe | paper-live since (full) | paper days | book coverage |
|---|---|---|---|---|---|---|---|---|---|
| agri_event | 2026-11-02 | -31,855 | -149,030 | -175,435 | -149,795 | -3.31 | -17,700 | 6 | 100% |
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
| agri_event | 7 | 20261106091340_8f0b7b90cc1f.csv | data | 8f0b7b9 | 1 | -50 |
| fund_v3 | 4 | 20261110091023_0712a0472bd7.csv | data | 0712a04 | 3 | -184 |
full series: data/backtest/vintages/<strategy>/; index: data/backtest/vintages/index.csv

## Data health
decision-price coverage (2026-11-10): 100% of held notional benchmarked (0 contract(s) unbenchmarked); 12 contract(s) (16%) first decided after the 0900 snap, so they straddle their own overnight leg
scale: 1 (since 2026-09-09)
regime: forward (merged weighted book) since 2026-08-31; 46 forward day(s), 8 legacy day(s)
merge weights (2026-11-10): ks_branch 0.8, fund_v3 2, china_pairs 1.5, ks_ext 0.25, chem_fund 1.5, agri_event 0, stat_arb 1
as-shipped pins: 54 live day(s) pinned; current series diverges from pins on chem_fund: 30 day(s), max 9,725 CNY, fund_v3: 49 day(s), max 22,683 CNY, 2 NEW, ks_branch: 43 day(s), max 82,125 CNY, ks_ext: 35 day(s), max 42,170 CNY, stat_arb: 43 day(s), max 9,982 CNY, china_pairs: 23 day(s), max 10,910 CNY, agri_event: 10 day(s), max 7,250 CNY; standing counts -- a divergence is announced as an alert once, the first run it appears, and kept here afterwards
inbox ks summary mtime: 2026-11-10 05:57 UTC
