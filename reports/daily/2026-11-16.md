# Performance tracker - 2026-11-16   (reconciled through 2026-11-16)

## ALERTS
- VINTAGE agri_event: 7 historical row(s) restated (net -1,750 CNY, cause data, commit 8f0b7b9) -- kept as vintages/agri_event/20261116091117_8f0b7b90cc1f.csv; the bridge keeps the as-shipped pins
- VINTAGE fund_v3: 4 historical row(s) restated (net -11 CNY, cause data, commit 0712a04) -- kept as vintages/fund_v3/20261116091117_0712a0472bd7.csv; the bridge keeps the as-shipped pins
- VINTAGE stat_arb: 3 historical row(s) restated (net -3,932 CNY, cause data, commit 9f7e9a7) -- kept as vintages/stat_arb/20261116091117_9f7e9a742805.csv; the bridge keeps the as-shipped pins
- WEIGHTS 2026-10-09: day's own merge weights not shipped yet -- carried forward from an earlier day.
- WEIGHTS 2026-10-16: day's own merge weights not shipped yet -- carried forward from an earlier day.
- WEIGHTS 2026-10-22: day's own merge weights not shipped yet -- carried forward from an earlier day.
- BT PENDING 2026-11-16: no mature backtest row for stat_arb (nonzero weight) -- day reconciled WITHOUT that sleeve's expected; its live P&L sits in bt_pending_live, not resid, until the rows ship.
- WEIGHTS CHANGE on 2026-09-01: ks_ext: 0.0->0.25.
- WEIGHTS CHANGE on 2026-09-02: stat_arb: 1.0->0.0.
- WEIGHTS CHANGE on 2026-09-03: stat_arb: 0.0->1.0.
- WEIGHTS CHANGE on 2026-11-02: agri_event: 1.0->0.0.
- WEIGHTS CHANGE on 2026-11-11: fpe: None->0.1, ks_outright: None->0.5.
- BT REVISED vs PINS: fund_v3 current history differs from pinned as-shipped values on 3 new live-window day(s) (max |diff| 22683 CNY, first 2026-11-06); the bridge keeps the pins.
- BT REVISED vs PINS: stat_arb current history differs from pinned as-shipped values on 2 new live-window day(s) (max |diff| 9982 CNY, first 2026-11-10); the bridge keeps the pins.
- MISSING LIVE DAY 2026-08-28: trading day with a backtest row but no daily_pnl/state file; excluded from the bridge, expected pnl held in the missing-day bucket.
- SCALE 2026-08-28: no usable run record; previous scale carried forward.
- SCALE 2026-09-25: no usable run record; previous scale carried forward.
- SCALE CHANGE on 2026-08-27: now 0.2.
- SCALE CHANGE on 2026-09-01: now 0.5.
- SCALE CHANGE on 2026-09-09: now 1.
- BACKTEST REVISED: agri_event -- 7 mature row(s) changed since last run (net -1750 CNY, largest 2026-04-30 +25440 -> +22940; first 2026-02-05, last 2026-05-06). Regeneration upstream; baseline re-set.
- SLIPPAGE 2026-11-16: 8 unbenchmarked leg(s), +28 CNY exec cost without a shipped decision price.
- RESIDUAL 2026-08-27: -17267 CNY vs trailing median |resid| 2062, offset by neither neighbour (2026-08-26 +3749, 2026-08-31 -17348) -- attribution quality changed. (A break-out that a neighbouring day mirrors is the backtest/live day-window straddle and is not alerted.)
- RESIDUAL 2026-08-31: -17348 CNY vs trailing median |resid| 2277, offset by neither neighbour (2026-08-27 -17267, 2026-09-01 -8190) -- attribution quality changed. (A break-out that a neighbouring day mirrors is the backtest/live day-window straddle and is not alerted.)
- RESIDUAL 2026-09-01: -8190 CNY vs trailing median |resid| 2492, offset by neither neighbour (2026-08-31 -17348, 2026-09-02 -30063) -- attribution quality changed. (A break-out that a neighbouring day mirrors is the backtest/live day-window straddle and is not alerted.)
- RESIDUAL 2026-09-02: -30063 CNY vs trailing median |resid| 3121, offset by neither neighbour (2026-09-01 -8190, 2026-09-03 -29049) -- attribution quality changed. (A break-out that a neighbouring day mirrors is the backtest/live day-window straddle and is not alerted.)
- RESIDUAL 2026-09-03: -29049 CNY vs trailing median |resid| 3941, offset by neither neighbour (2026-09-02 -30063, 2026-09-04 -5584) -- attribution quality changed. (A break-out that a neighbouring day mirrors is the backtest/live day-window straddle and is not alerted.)
- RESIDUAL 2026-09-16: -103509 CNY vs trailing median |resid| 22936, offset by neither neighbour (2026-09-15 -28634, 2026-09-17 +23811) -- attribution quality changed. (A break-out that a neighbouring day mirrors is the backtest/live day-window straddle and is not alerted.)
- RESIDUAL 2026-10-26: +29017 CNY vs trailing median |resid| 7638, offset by neither neighbour (2026-10-23 +7825, 2026-10-27 +81673) -- attribution quality changed. (A break-out that a neighbouring day mirrors is the backtest/live day-window straddle and is not alerted.)
- RESIDUAL 2026-10-27: +81673 CNY vs trailing median |resid| 9046, offset by neither neighbour (2026-10-26 +29017, 2026-10-28 +2573) -- attribution quality changed. (A break-out that a neighbouring day mirrors is the backtest/live day-window straddle and is not alerted.)

## Latest reconciled day (2026-11-16, forward regime, PROVISIONAL: marked at the 16:00 close, re-marked to settlement after the next capture)
live gross +155,750 | expected (1 x bt +84,372) = +84,372 | gap +71,378
  exec_cost +14,938 (slip +14,910, unbench +28) | marking +95,595 | bookdiff +0 (carry +0, new +0) | intraday +0 | offbook +0 (0 contract(s)) | residual +12,541 (live re-marked to first decision, vs the previous backtest row)
  PARTIAL: no backtest row yet for stat_arb -- expected excludes it; its live P&L -21,820 is held out of resid
  fees +1,507 | broker residual +0 -> live net +154,243

## Cumulative bridge (live since 2026-08-18, 58 reconciled days, 1 with a sleeve's backtest pending)
| expected | -exec | +marking | +bookdiff | +intraday | +offbook | +bt pending | +resid | = live gross | -fees | +broker_resid | = live net |
|---|---|---|---|---|---|---|---|---|---|---|---|
| +727,281 | -95,458 | +84,300 | +90,047 | -6,568 | -50 | -21,820 | +16,832 | +794,565 | -59,532 | +11,124 | +746,157 |
missing live days excluded: 2026-08-28 (expected +4,849 held in bucket)

## Stats (daily CNY pnl)
| window | days | total | sharpe | mdd | hit |
|---|---|---|---|---|---|
| live net live-to-date | 58 | +746,157 | 3.39 | -330,281 | 57% |
| live net last-20d | 20 | +213,022 | 2.66 | -317,945 | 50% | (small sample)
| live net 2026-YTD | 58 | +746,157 | 3.39 | -330,281 | 57% |
| bt scaled live-to-date | 58 | +727,281 | 3.11 | -381,526 | 67% |
| bt scaled last-20d | 20 | +90,455 | 0.97 | -381,526 | 60% | (small sample)
| bt scaled 2026-YTD | 58 | +727,281 | 3.11 | -381,526 | 67% |

## Slippage (+ = cost; bps vs benchmarked notional)
| day | lots | notional M | slip total | drift | exec | bps | unbench legs | unbench CNY |
|---|---|---|---|---|---|---|---|---|
| 2026-11-03 | 379 | 25.3 | +7,160 | +5,542 | +1,618 | +2.94 | 2 | +2,140 |
| 2026-11-04 | 364 | 32.1 | +2,030 | +1,422 | +608 | +0.64 | 1 | +275 |
| 2026-11-05 | 462 | 30.3 | +3,350 | +942 | +2,408 | +1.15 | 4 | -45 |
| 2026-11-06 | 863 | 42.1 | +13,755 | +6,750 | +7,005 | +3.27 | 1 | +45 |
| 2026-11-09 | 519 | 27.4 | -5,690 | -6,638 | +948 | -2.09 | 1 | -30 |
| 2026-11-10 | 484 | 26.2 | +1,890 | +445 | +1,445 | +0.75 | 2 | +118 |
| 2026-11-11 | 445 | 37.7 | -5,640 | -6,922 | +1,282 | -1.52 | 3 | +50 |
| 2026-11-12 | 508 | 31.3 | +3,550 | +2,372 | +1,178 | +1.15 | 2 | -100 |
| 2026-11-13 | 504 | 35.5 | +2,085 | -325 | +2,410 | +0.62 | 5 | +228 |
| 2026-11-16 | 540 | 42.9 | +14,910 | +13,128 | +1,782 | +3.92 | 8 | +28 |
| live window (58d) | 22454 | 1404.8 | +79,565 | +9,722 | +69,842 | +0.61 | 271 | +15,892 |
exec-only bps over the window: +0.53; benchmark coverage 93% of traded notional

| product | days | lots | notional M | drift | exec (incl. unbench) | all-in | bps |
|---|---|---|---|---|---|---|---|
| IH | 38 | 158 | 131.1 | -26,310 | +5,670 | -20,640 | -1.57 |
| CY | 44 | 323 | 35.5 | +14,625 | +5,950 | +20,575 | +5.80 |
| IF | 25 | 86 | 109.3 | -20,340 | +3,300 | -17,040 | -1.56 |
| pg | 29 | 50 | 6.8 | +16,300 | +160 | +16,460 | +24.20 |
| y | 48 | 327 | 29.1 | +9,940 | +2,130 | +12,070 | +4.15 |
| rb | 47 | 1540 | 47.5 | +9,930 | +1,790 | +11,720 | +2.47 |
| bu | 50 | 595 | 28.1 | -13,120 | +1,515 | -11,605 | -4.13 |
| SA | 54 | 861 | 17.3 | +6,780 | +3,260 | +10,040 | +5.79 |
| al | 45 | 736 | 85.4 | +6,825 | +3,125 | +9,950 | +1.17 |
| SF | 54 | 589 | 17.6 | +8,850 | +995 | +9,845 | +5.61 |
| FG | 57 | 1113 | 20.1 | +2,650 | +6,110 | +8,760 | +4.36 |
| SR | 52 | 1036 | 55.8 | +5,845 | +1,990 | +7,835 | +1.40 |
| PF | 49 | 336 | 13.7 | -8,615 | +810 | -7,805 | -5.70 |
| a | 53 | 650 | 34.2 | +3,850 | +3,485 | +7,335 | +2.14 |
| pb | 47 | 1059 | 84.9 | +1,950 | +4,738 | +6,688 | +0.79 |
| other (38) | - | 12995 | 688.5 | -9,438 | +40,708 | +31,270 | +0.45 |
| all products | - | 22454 | 1404.8 | +9,722 | +85,735 | +95,458 | +0.68 |
ranked by |all-in| over the live window (all-in = drift + exec = the bridge's exec_cost by product); product bps are vs traded notional

## Per strategy
| strategy | live? | bt 2026 pnl (full) | bt scaled+weighted (live window) | live attributed | note |
|---|---|---|---|---|---|
| Calendar main pool (branch) | yes | +1,151,620 | +119,152 | +171,799 | forward w=0.8 |
| Fundamental factor | yes | +894,491 | +522,094 | +517,275 | forward w=2 |
| Cross-product pairs | yes | +74,345 | +25,418 | +4,908 | forward w=1.5 |
| Calendar extended pool | yes | +505,485 | +17,137 | +60,345 | forward w=0.25 |
| Chemical fundamental | yes | +500,410 | +29,696 | -20,494 | forward w=1.5 |
| Agriculture event-driven | no | +39,710 | -111,243 | -152,798 | forward w=0 (parked) |
| Factor-neutral stat arb | yes | +338,986 | +32,859 | +38,024 | forward w=1 |
| Fund pipeline ensemble | yes | +2,855,665 | +68,888 | +81,242 | forward w=0.1 |
| Outright trend + basis | yes | +561,990 | +23,280 | +24,135 | forward w=0.5 |
| shared bucket | - | - | - | +3,575 | legacy days only: a contract both per-source books held |
| neither bucket (no target) | - | - | - | +2,585 | named by no book that day or the day before |
| trading bucket | - | - | - | +63,970 | forward days: live P&L minus the strategies' holdings (fills vs settlement on rebalances, lot rounding, scale changes) |
forward days: each strategy is its own previous-day weighted book x scale x the settlement-to-settlement move (holdings); legacy days remain exclusive-holder. The gap tables (attributed - expected) therefore exclude execution, which sits in trading.

## Live P&L by strategy, last 10 reconciled days (attributed gross CNY)
| day | ks_branch | fund_v3 | china_pairs | ks_ext | chem_fund | agri_event | stat_arb | fpe | ks_outright | shared | neither | trading | total |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 2026-11-03 | -9,816 | +21,940 | -8,490 | -123 | -13,485 | +0 | +1,335 | +0 | +0 | +0 | +0 | +2,793 | -5,845 |
| 2026-11-04 | +7,320 | -21,410 | -2,842 | -13,680 | +11,618 | +0 | +12,140 | +0 | +0 | +0 | +0 | +4,875 | -1,980 |
| 2026-11-05 | -33,388 | +1,260 | -532 | +8,112 | -8,992 | +0 | +12,415 | +0 | +0 | +0 | +0 | -13,885 | -35,010 |
| 2026-11-06 | +316 | -2,180 | +21,278 | +4,886 | -10,478 | +0 | -8,320 | +0 | +0 | +0 | +0 | +6,048 | +11,550 |
| 2026-11-09 | -224 | +21,420 | +11,745 | -3,271 | -4,425 | +0 | -745 | +0 | +0 | +0 | +0 | +4,255 | +28,755 |
| 2026-11-10 | +10,060 | +60,290 | -5,542 | +4,261 | -39,090 | +0 | -8,585 | +0 | +0 | +0 | +0 | +1,881 | +23,275 |
| 2026-11-11 | -48 | +81,680 | +7,920 | -1,788 | -14,685 | +0 | +7,710 | +0 | +0 | +0 | +0 | +7,396 | +88,185 |
| 2026-11-12 | +57,280 | +15,540 | -5,798 | -3,425 | +975 | +0 | -5,505 | +30,757 | +8,365 | +0 | +255 | -1,640 | +96,805 |
| 2026-11-13 | +25,720 | +17,270 | +1,598 | -6,845 | -652 | +0 | +5,150 | +20,356 | +14,980 | +0 | +0 | +12,519 | +90,095 |
| 2026-11-16 | +47,440 | +65,330 | +562 | +3,262 | +12,878 | +0 | -21,820 | +30,129 | +790 | +0 | +0 | +17,179 | +155,750 |
| sum | +104,660 | +261,140 | +19,898 | -8,609 | -66,338 | +0 | -6,225 | +81,242 | +24,135 | +0 | +255 | +41,422 | +451,580 |
forward days: previous-day weighted book x scale x settlement move per strategy, the rest in trading; total foots to live gross. Live-window sums: 'Per strategy' above; full series: data/per_strategy_daily.csv (attributed)

## Per strategy gap by day, last 10 reconciled days (live attributed - expected, CNY)
| day | ks_branch | fund_v3 | china_pairs | ks_ext | chem_fund | agri_event | stat_arb | fpe | ks_outright | total |
|---|---|---|---|---|---|---|---|---|---|---|
| 2026-11-03 | -18,168 | -12,215 | -1,110 | +13,477 | -7,695 | +0 | +3,215 | +0 | +0 | -22,496 |
| 2026-11-04 | +2,600 | -42,652 | -6,390 | -17,409 | -240 | +0 | +12,722 | +0 | +0 | -51,368 |
| 2026-11-05 | -20,828 | -38,627 | +5,752 | +2,836 | +1,545 | +0 | +26,370 | +0 | +0 | -22,951 |
| 2026-11-06 | +16,056 | +9,255 | -3,420 | +208 | -16,882 | +0 | -4,371 | +0 | +0 | +845 |
| 2026-11-09 | -3,548 | +39,923 | -5,205 | +4,985 | +3,098 | +0 | -4,969 | +0 | +0 | +34,284 |
| 2026-11-10 | -18,696 | +40,476 | +870 | -1,682 | -10,462 | +0 | -3,516 | +0 | +0 | +6,989 |
| 2026-11-11 | +13,352 | -41,720 | +892 | -9,048 | -22,582 | +0 | -5,842 | +0 | +0 | -64,948 |
| 2026-11-12 | +26,396 | +1,299 | +390 | -855 | +18,465 | +0 | +840 | +17,117 | +5,348 | +69,000 |
| 2026-11-13 | -40,452 | +8,720 | +2,962 | -7,659 | -14,955 | +0 | +4,729 | -14,154 | -4,085 | -64,893 |
| 2026-11-16 | +37,412 | +5,013 | +5,220 | +1,961 | +17,430 | +0 | - | +9,391 | -408 | +76,020 |
| sum | -5,876 | -30,527 | -38 | -13,185 | -32,280 | +0 | +29,178 | +12,354 | +855 | -39,519 |
full series: data/per_strategy_daily.csv (day, strategy, expected, attributed, gap); a strategy's daily total foots to expected - live_gross once the shared, neither and trading buckets are added. '-' = that sleeve's backtest row has not shipped yet (BT PENDING).

## Live P&L by product, last 10 reconciled days (gross CNY, worst first)
| product | 11-03 | 11-04 | 11-05 | 11-06 | 11-09 | 11-10 | 11-11 | 11-12 | 11-13 | 11-16 | 10d sum | live window |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| TA | -42,080 | -9,440 | -44,250 | -5,800 | +4,200 | -10,140 | +140 | +930 | +2,300 | -10 | -104,150 | -71,260 |
| y | -25,520 | -29,090 | -8,710 | -12,240 | -7,260 | -1,200 | +8,330 | +4,870 | +2,490 | -540 | -68,870 | -108,100 |
| pp | -14,870 | -2,660 | -17,820 | +955 | -11,905 | -37,895 | -560 | +9,640 | +13,050 | -3,045 | -65,110 | -84,390 |
| a | -6,810 | -12,270 | +5,100 | -5,410 | +5,480 | +1,700 | +3,830 | +140 | -5,620 | -32,130 | -45,990 | -28,340 |
| eb | -19,680 | -5,700 | -12,610 | -3,905 | -2,700 | -6,390 | +745 | +2,810 | +5,685 | +7,090 | -34,655 | +34,570 |
| MA | -12,150 | -3,700 | -11,620 | -5,080 | -1,850 | -4,400 | +1,240 | +1,950 | +2,220 | +930 | -32,460 | +10,580 |
| br | -5,350 | -300 | -8,350 | -2,750 | +1,150 | -2,350 | -400 | -950 | -3,200 | -4,300 | -26,800 | -24,975 |
| c | +1,050 | -1,880 | +4,280 | -2,560 | +2,470 | -13,550 | -5,180 | -2,210 | -4,200 | +1,900 | -19,880 | -36,320 |
| ru | +1,200 | -5,800 | -900 | -450 | +500 | -2,600 | -1,800 | -2,250 | -4,300 | -300 | -16,700 | -16,850 |
| rb | +16,450 | +4,400 | -17,450 | -5,660 | -2,340 | -7,540 | +12,660 | -11,320 | +10,320 | -16,080 | -16,560 | +111,490 |
| pg | -7,040 | -2,980 | -8,020 | -7,720 | +3,480 | +8,740 | -260 | +400 | +140 | +3,260 | -10,000 | -37,200 |
| FG | -5,880 | -6,200 | -5,700 | +720 | -8,160 | -5,320 | +4,100 | +9,820 | +25,820 | -18,920 | -9,720 | +79,740 |
| IF | +3,420 | -15,000 | +900 | -540 | +1,320 | -240 | -120 | +720 | +3,480 | -840 | -6,900 | -62,100 |
| j | +0 | +50 | -1,950 | +0 | +0 | +0 | +900 | -3,000 | +0 | -600 | -4,600 | +1,550 |
| lh | +0 | +0 | +0 | +0 | +0 | +0 | -880 | -240 | -2,480 | +720 | -2,880 | +21,120 |
| other (28) | +68,460 | +57,615 | +21,885 | +13,775 | +15,350 | +17,825 | +17,715 | +13,300 | -12,210 | +23,695 | +237,410 | +244,185 |
| m | +90 | +5,870 | +3,880 | +6,680 | +6,660 | +12,590 | -7,690 | +6,060 | -3,220 | +3,000 | +33,920 | +8,020 |
| eg | +13,720 | +2,050 | +26,680 | +4,990 | -1,340 | +3,920 | -1,800 | -3,920 | -3,870 | -780 | +39,650 | +42,740 |
| PF | +23,910 | +2,570 | +13,630 | +3,580 | -2,250 | -1,980 | -570 | +850 | +530 | +630 | +40,900 | +83,130 |
| cs | -1,060 | -3,440 | -13,080 | +2,940 | -11,790 | +23,800 | +22,430 | +8,100 | +9,940 | +12,900 | +50,740 | +158,210 |
| fu | +9,400 | +11,500 | +21,060 | +1,620 | +3,490 | -2,650 | -2,080 | +2,360 | +5,420 | +5,590 | +55,710 | +69,440 |
| cu | -5,000 | +19,650 | -1,600 | +11,150 | -2,400 | -5,300 | +8,600 | +1,150 | +5,900 | +27,600 | +59,750 | +42,000 |
| hc | -9,690 | +750 | +19,770 | +3,300 | +5,630 | +7,780 | +1,710 | +9,190 | -1,820 | +24,710 | +61,330 | -100,650 |
| i | +4,900 | -6,950 | -12,250 | -3,700 | +4,000 | -3,550 | +5,100 | +8,750 | +7,350 | +65,200 | +68,850 | +72,200 |
| l | +12,460 | -4,500 | +14,790 | +25,555 | +3,770 | +16,200 | +1,975 | -745 | -1,780 | +2,795 | +70,520 | +66,700 |
| al | -5,775 | +3,475 | -2,675 | -7,900 | +23,250 | +35,825 | +20,050 | +40,400 | +38,150 | +53,275 | +198,075 | +319,075 |
| all products | -5,845 | -1,980 | -35,010 | +11,550 | +28,755 | +23,275 | +88,185 | +96,805 | +90,095 | +155,750 | +451,580 | +794,565 |
executor total_pnl (holding + trading, settlement-to-settlement once the next capture lands, before fees) summed by product root; 'all products' foots to live gross. Full series: data/product_daily.csv

## Worst (strategy, product) cells, last 10 reconciled days (attributed gross CNY)
| strategy | product | 11-03 | 11-04 | 11-05 | 11-06 | 11-09 | 11-10 | 11-11 | 11-12 | 11-13 | 11-16 | sum |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| china_pairs | pp | -18,322 | -3,098 | -16,380 | -20,700 | -2,362 | -30,772 | -742 | +7,155 | +8,032 | -4,320 | -81,510 |
| china_pairs | rb | +14,280 | +2,520 | -21,855 | -7,755 | -1,290 | -3,870 | +6,120 | -9,600 | +2,400 | -22,800 | -41,850 |
| china_pairs | TA | -15,360 | -4,050 | -19,305 | -1,485 | +2,520 | -5,550 | -375 | +2,025 | +3,825 | -1,425 | -39,180 |
| fund_v3 | eb | -18,620 | -6,840 | -10,980 | -4,000 | -5,850 | -9,570 | +1,020 | +3,810 | +6,390 | +7,070 | -37,570 |
| china_pairs | y | -15,660 | -16,065 | -5,130 | -7,455 | -4,920 | -240 | +6,600 | +5,280 | +720 | -630 | -37,500 |
| fund_v3 | TA | -17,320 | -3,100 | -11,500 | -1,240 | +0 | +1,420 | +360 | -1,140 | -2,560 | +720 | -34,360 |
| stat_arb | pg | -7,040 | -2,980 | -8,020 | -5,640 | -2,440 | -6,380 | -60 | +360 | +980 | +0 | -31,220 |
| chem_fund | TA | -9,525 | -2,265 | -10,305 | -1,455 | +2,010 | -5,505 | -435 | +285 | +960 | +15 | -26,220 |
| stat_arb | l | -6,725 | +310 | -2,960 | -5,160 | -1,365 | -7,275 | -850 | +630 | +2,250 | -2,130 | -23,275 |
| ks_ext | IF | +1,590 | -15,795 | +255 | -4,635 | +1,455 | -135 | +75 | -2,580 | -1,695 | -1,365 | -22,830 |
| chem_fund | pp | -2,468 | -338 | -5,692 | -5,130 | -4,762 | -16,830 | +1,530 | +3,330 | +7,110 | +795 | -22,455 |
| ks_branch | pp | -6,564 | -1,644 | -6,552 | +7,924 | -6,280 | -6,044 | -676 | +88 | -1,100 | -880 | -21,728 |
| fund_v3 | c | -100 | -1,360 | +3,340 | -2,840 | +2,000 | -11,520 | -4,980 | -1,260 | -3,020 | -1,920 | -21,660 |
| ks_branch | bu | -6,664 | -1,560 | -9,608 | -1,456 | +1,408 | -1,976 | -672 | +64 | +16 | +64 | -20,384 |
| fund_v3 | y | -6,960 | -7,380 | -2,160 | -1,720 | +2,460 | -40 | +0 | -2,060 | -660 | +0 | -18,520 |
same holdings split as 'Live P&L by strategy'; summing a strategy's products reproduces its row there (trading / neither included as their own strategy). Full series: data/strategy_product_daily.csv

## Paper strategies (weight 0 in the forward book: tracked, not traded)
| strategy | weight 0 since | bt since (full) | bt last 20d | drawdown now | worst before pause | 60d Sharpe | paper-live since (full) | paper days | book coverage |
|---|---|---|---|---|---|---|---|---|---|
| agri_event | 2026-11-02 | -8,030 | -94,440 | -151,660 | -149,845 | -2.70 | -9,215 | 10 | 100% |
paper-live = the strategy's own pinned full-size book of D-1 x the settlement-to-settlement move of D, priced like the live attribution, on contracts the day's state capture marks (coverage). Re-entry: owner's call, at an attended morning merge; reweighting is Execution/weights_forward.json + weights_changelog.csv.

## Backtest vintages (full series kept on every restatement)
expected on the CURRENT series minus expected on the as-shipped pins, live window, weighted CNY (the bridge uses the pins):
| strategy | restated |
|---|---|
| ks_branch | +65,633 |
| fund_v3 | -42,308 |
| china_pairs | -24,878 |
| ks_ext | +6,911 |
| chem_fund | -6,668 |
| agri_event | +9,350 |
| stat_arb | +12,379 |
| all | +20,419 |
| strategy | vintages | latest | cause | commit | rows restated | net change (full size) |
|---|---|---|---|---|---|---|
| ks_branch | 2 | 20261102090932_cbbdd7664522.csv | unknown | cbbdd76 | 165 | +341,255 |
| ks_ext | 2 | 20261102090932_1a03a09367cb.csv | unknown | 1a03a09 | 91 | +31,590 |
| china_pairs | 2 | 20261102090932_51a17747e0e0.csv | unknown | 51a1774 | 44 | -46,815 |
| chem_fund | 3 | 20261105091241_a98238f08285.csv | data | a98238f | 1 | -480 |
| ks_outright | 1 | 20261111091151_49ac2cfb3881.csv | first | 49ac2cf | 0 | +0 |
| fpe | 1 | 20261111091151_01eab32dfcbf.csv | first | 01eab32 | 0 | +0 |
| agri_event | 11 | 20261116091117_8f0b7b90cc1f.csv | data | 8f0b7b9 | 7 | -1,750 |
| fund_v3 | 5 | 20261116091117_0712a0472bd7.csv | data | 0712a04 | 4 | -11 |
| stat_arb | 4 | 20261116091117_9f7e9a742805.csv | data | 9f7e9a7 | 3 | -3,932 |
full series: data/backtest/vintages/<strategy>/; index: data/backtest/vintages/index.csv

## Data health
decision-price coverage (2026-11-16): 100% of held notional benchmarked (1 contract(s) unbenchmarked); 13 contract(s) (19%) first decided after the 0900 snap, so they straddle their own overnight leg
scale: 1 (since 2026-09-09)
regime: forward (merged weighted book) since 2026-08-31; 50 forward day(s), 8 legacy day(s)
merge weights (2026-11-16): ks_branch 0.8, fund_v3 2, china_pairs 1.5, ks_ext 0.25, chem_fund 1.5, agri_event 0, stat_arb 1, fpe 0.1, ks_outright 0.5
as-shipped pins: 58 live day(s) pinned; current series diverges from pins on chem_fund: 30 day(s), max 9,725 CNY, fund_v3: 52 day(s), max 22,683 CNY, 3 NEW, ks_branch: 43 day(s), max 82,125 CNY, ks_ext: 35 day(s), max 42,170 CNY, stat_arb: 45 day(s), max 9,982 CNY, 2 NEW, china_pairs: 23 day(s), max 10,910 CNY, agri_event: 11 day(s), max 7,250 CNY; standing counts -- a divergence is announced as an alert once, the first run it appears, and kept here afterwards
inbox ks summary mtime: 2026-11-16 05:57 UTC
