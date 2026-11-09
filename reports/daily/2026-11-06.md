# Performance tracker - 2026-11-06   (reconciled through 2026-11-06)

## ALERTS
- VINTAGE agri_event: 1 historical row(s) restated (net -50 CNY, cause data, commit 8f0b7b9) -- kept as vintages/agri_event/20261106091340_8f0b7b90cc1f.csv; the bridge keeps the as-shipped pins
- WEIGHTS 2026-10-09: day's own merge weights not shipped yet -- carried forward from an earlier day.
- WEIGHTS 2026-10-16: day's own merge weights not shipped yet -- carried forward from an earlier day.
- WEIGHTS 2026-10-22: day's own merge weights not shipped yet -- carried forward from an earlier day.
- BT PENDING 2026-11-06: no mature backtest row for stat_arb (nonzero weight) -- day reconciled WITHOUT that sleeve's expected; its live P&L sits in bt_pending_live, not resid, until the rows ship.
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
- SLIPPAGE 2026-11-06: 1 unbenchmarked leg(s), +45 CNY exec cost without a shipped decision price.
- RESIDUAL 2026-08-27: -17267 CNY vs trailing median |resid| 2062, offset by neither neighbour (2026-08-26 +3749, 2026-08-31 -17348) -- attribution quality changed. (A break-out that a neighbouring day mirrors is the backtest/live day-window straddle and is not alerted.)
- RESIDUAL 2026-08-31: -17348 CNY vs trailing median |resid| 2277, offset by neither neighbour (2026-08-27 -17267, 2026-09-01 -8190) -- attribution quality changed. (A break-out that a neighbouring day mirrors is the backtest/live day-window straddle and is not alerted.)
- RESIDUAL 2026-09-01: -8190 CNY vs trailing median |resid| 2492, offset by neither neighbour (2026-08-31 -17348, 2026-09-02 -30063) -- attribution quality changed. (A break-out that a neighbouring day mirrors is the backtest/live day-window straddle and is not alerted.)
- RESIDUAL 2026-09-02: -30063 CNY vs trailing median |resid| 3121, offset by neither neighbour (2026-09-01 -8190, 2026-09-03 -29049) -- attribution quality changed. (A break-out that a neighbouring day mirrors is the backtest/live day-window straddle and is not alerted.)
- RESIDUAL 2026-09-03: -29049 CNY vs trailing median |resid| 3941, offset by neither neighbour (2026-09-02 -30063, 2026-09-04 -5584) -- attribution quality changed. (A break-out that a neighbouring day mirrors is the backtest/live day-window straddle and is not alerted.)
- RESIDUAL 2026-09-16: -103509 CNY vs trailing median |resid| 22936, offset by neither neighbour (2026-09-15 -28634, 2026-09-17 +23811) -- attribution quality changed. (A break-out that a neighbouring day mirrors is the backtest/live day-window straddle and is not alerted.)
- RESIDUAL 2026-10-26: +29017 CNY vs trailing median |resid| 7638, offset by neither neighbour (2026-10-23 +7825, 2026-10-27 +81673) -- attribution quality changed. (A break-out that a neighbouring day mirrors is the backtest/live day-window straddle and is not alerted.)
- RESIDUAL 2026-10-27: +81673 CNY vs trailing median |resid| 9046, offset by neither neighbour (2026-10-26 +29017, 2026-10-28 +2573) -- attribution quality changed. (A break-out that a neighbouring day mirrors is the backtest/live day-window straddle and is not alerted.)

## Latest reconciled day (2026-11-06, forward regime, PROVISIONAL: marked at the 16:00 close, re-marked to settlement after the next capture)
live gross +21,315 | expected (1 x bt +8,606) = +8,606 | gap +12,709
  exec_cost +13,800 (slip +13,755, unbench +45) | marking +21,990 | bookdiff +1,230 (carry +1,420, new -190) | intraday -1,400 | offbook +0 (0 contract(s)) | residual +8,399 (live re-marked to first decision, vs the previous backtest row)
  PARTIAL: no backtest row yet for stat_arb -- expected excludes it; its live P&L -3,710 is held out of resid
  fees +2,257 | broker residual +0 -> live net +19,058

## Cumulative bridge (live since 2026-08-18, 52 reconciled days, 1 with a sleeve's backtest pending)
| expected | -exec | +marking | +bookdiff | +intraday | +offbook | +bt pending | +resid | = live gross | -fees | +broker_resid | = live net |
|---|---|---|---|---|---|---|---|---|---|---|---|
| +324,841 | -84,060 | +7,895 | +90,047 | -6,568 | -50 | -3,710 | -6,931 | +321,465 | -51,404 | +11,084 | +281,145 |
missing live days excluded: 2026-08-28 (expected +4,849 held in bucket)

## Stats (daily CNY pnl)
| window | days | total | sharpe | mdd | hit |
|---|---|---|---|---|---|
| live net live-to-date | 52 | +281,145 | 1.50 | -330,281 | 52% |
| live net last-20d | 20 | -12,870 | -0.19 | -317,945 | 40% | (small sample)
| live net 2026-YTD | 52 | +281,145 | 1.50 | -330,281 | 52% |
| bt scaled live-to-date | 52 | +324,841 | 1.62 | -381,526 | 65% |
| bt scaled last-20d | 20 | -34,936 | -0.43 | -381,526 | 60% | (small sample)
| bt scaled 2026-YTD | 52 | +324,841 | 1.62 | -381,526 | 65% |

## Slippage (+ = cost; bps vs benchmarked notional)
| day | lots | notional M | slip total | drift | exec | bps | unbench legs | unbench CNY |
|---|---|---|---|---|---|---|---|---|
| 2026-10-26 | 423 | 16.9 | +3,130 | +2,752 | +378 | +1.86 | 1 | +105 |
| 2026-10-27 | 720 | 42.7 | +11,470 | +8,082 | +3,388 | +2.83 | 2 | -335 |
| 2026-10-28 | 220 | 17.2 | +7,060 | +6,922 | +138 | +4.23 | 3 | +320 |
| 2026-10-29 | 393 | 27.9 | +4,825 | +3,225 | +1,600 | +2.13 | 6 | -620 |
| 2026-10-30 | 249 | 14.1 | +6,150 | +6,185 | -35 | +4.49 | 4 | +5 |
| 2026-11-02 | 258 | 19.2 | +7,360 | +6,620 | +740 | +3.92 | 3 | -5 |
| 2026-11-03 | 379 | 25.3 | +7,160 | +5,542 | +1,618 | +2.94 | 2 | +2,140 |
| 2026-11-04 | 364 | 32.1 | +2,030 | +1,422 | +608 | +0.64 | 1 | +275 |
| 2026-11-05 | 462 | 30.3 | +3,350 | +942 | +2,408 | +1.15 | 4 | -45 |
| 2026-11-06 | 863 | 42.1 | +13,755 | +6,750 | +7,005 | +3.27 | 1 | +45 |
| live window (52d) | 19454 | 1203.9 | +68,460 | +7,662 | +60,798 | +0.61 | 250 | +15,600 |
exec-only bps over the window: +0.54; benchmark coverage 93% of traded notional

| product | days | lots | notional M | drift | exec (incl. unbench) | all-in | bps |
|---|---|---|---|---|---|---|---|
| IH | 33 | 130 | 108.3 | -28,410 | +5,130 | -23,280 | -2.15 |
| IF | 20 | 72 | 92.6 | -20,130 | +2,670 | -17,460 | -1.88 |
| pg | 27 | 47 | 6.4 | +15,150 | +170 | +15,320 | +23.84 |
| CY | 39 | 282 | 31.1 | +9,862 | +5,438 | +15,300 | +4.92 |
| bu | 45 | 499 | 23.9 | -14,075 | +1,565 | -12,510 | -5.23 |
| rb | 42 | 1432 | 44.2 | +9,640 | +1,600 | +11,240 | +2.54 |
| y | 43 | 307 | 27.3 | +8,990 | +2,050 | +11,040 | +4.04 |
| FG | 51 | 980 | 17.7 | +5,580 | +5,020 | +10,600 | +5.98 |
| SF | 48 | 454 | 13.6 | +9,105 | +960 | +10,065 | +7.39 |
| ru | 32 | 100 | 19.3 | +8,150 | -125 | +8,025 | +4.16 |
| a | 47 | 601 | 31.7 | +4,605 | +3,260 | +7,865 | +2.48 |
| SR | 46 | 947 | 51.2 | +5,630 | +1,725 | +7,355 | +1.44 |
| pb | 41 | 863 | 69.3 | +3,612 | +2,838 | +6,450 | +0.93 |
| PF | 43 | 252 | 10.4 | -6,970 | +690 | -6,280 | -6.02 |
| cs | 50 | 951 | 23.9 | +1,770 | +4,435 | +6,205 | +2.60 |
| other (34) | - | 11537 | 632.8 | -4,848 | +38,972 | +34,125 | +0.54 |
| all products | - | 19454 | 1203.9 | +7,662 | +76,398 | +84,060 | +0.70 |
ranked by |all-in| over the live window (all-in = drift + exec = the bridge's exec_cost by product); product bps are vs traded notional

## Per strategy
| strategy | live? | bt 2026 pnl (full) | bt scaled+weighted (live window) | live attributed | note |
|---|---|---|---|---|---|
| Calendar main pool (branch) | yes | +994,415 | -6,612 | +23,099 | forward w=0.8 |
| Fundamental factor | yes | +790,726 | +314,276 | +268,125 | forward w=2 |
| Cross-product pairs | yes | +70,775 | +20,063 | -4,924 | forward w=1.5 |
| Calendar extended pool | yes | +487,515 | +12,644 | +68,964 | forward w=0.25 |
| Chemical fundamental | yes | +524,405 | +65,688 | +28,548 | forward w=1.5 |
| Agriculture event-driven | no | +29,030 | -111,243 | -152,798 | forward w=0 (parked) |
| Factor-neutral stat arb | yes | +340,516 | +30,024 | +66,428 | forward w=1 |
| shared bucket | - | - | - | +3,575 | legacy days only: a contract both per-source books held |
| neither bucket (no target) | - | - | - | +2,330 | named by no book that day or the day before |
| trading bucket | - | - | - | +18,118 | forward days: live P&L minus the strategies' holdings (fills vs settlement on rebalances, lot rounding, scale changes) |
forward days: each strategy is its own previous-day weighted book x scale x the settlement-to-settlement move (holdings); legacy days remain exclusive-holder. The gap tables (attributed - expected) therefore exclude execution, which sits in trading.

## Live P&L by strategy, last 10 reconciled days (attributed gross CNY)
| day | ks_branch | fund_v3 | china_pairs | ks_ext | chem_fund | agri_event | stat_arb | shared | neither | trading | total |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 2026-10-26 | -240 | -4,570 | +2,258 | +11,030 | +17,498 | -9,650 | -10,845 | +0 | +0 | -1,445 | +4,035 |
| 2026-10-27 | +35,236 | -2,240 | -9,068 | +6,356 | +9,218 | -37,080 | -20,025 | +0 | +0 | -21,217 | -38,820 |
| 2026-10-28 | +4,048 | -15,440 | -5,362 | -7,313 | -2,760 | -10,980 | -2,965 | +0 | +0 | -2,938 | -43,710 |
| 2026-10-29 | -49,776 | -53,440 | -825 | +6,281 | -6,968 | -18,070 | -15,165 | +0 | +0 | -8,983 | -146,945 |
| 2026-10-30 | -16,068 | -66,600 | -1,560 | +2,871 | +9,292 | +8,605 | +13,805 | +0 | -275 | +17,859 | -32,070 |
| 2026-11-02 | +4,260 | -660 | +7,845 | -25,403 | +15,420 | -3,995 | +12,980 | +0 | +0 | -12,588 | -2,140 |
| 2026-11-03 | -9,816 | +21,940 | -8,490 | -123 | -13,485 | +0 | +1,335 | +0 | +0 | +2,793 | -5,845 |
| 2026-11-04 | +7,320 | -21,410 | -2,842 | -13,680 | +11,618 | +0 | +12,140 | +0 | +0 | +4,875 | -1,980 |
| 2026-11-05 | -33,388 | +1,260 | -532 | +8,112 | -8,992 | +0 | +12,415 | +0 | +0 | -13,885 | -35,010 |
| 2026-11-06 | -8,156 | +10,200 | +21,930 | +5,700 | -6,435 | +0 | -3,710 | +0 | +0 | +1,786 | +21,315 |
| sum | -66,580 | -130,960 | +3,352 | -6,166 | +24,405 | -71,170 | -35 | +0 | -275 | -33,741 | -281,170 |
forward days: previous-day weighted book x scale x settlement move per strategy, the rest in trading; total foots to live gross. Live-window sums: 'Per strategy' above; full series: data/per_strategy_daily.csv (attributed)

## Per strategy gap by day, last 10 reconciled days (live attributed - expected, CNY)
| day | ks_branch | fund_v3 | china_pairs | ks_ext | chem_fund | agri_event | stat_arb | total |
|---|---|---|---|---|---|---|---|---|
| 2026-10-26 | -16,908 | +16,537 | -1,418 | +7,696 | +6,255 | -7,360 | -4,496 | +307 |
| 2026-10-27 | +83,988 | -3,013 | +4,755 | +3,094 | -12,608 | +9,880 | +11,794 | +97,890 |
| 2026-10-28 | -13,640 | +4,387 | -210 | -11,386 | +10,568 | -8,470 | -10,748 | -29,499 |
| 2026-10-29 | +31,404 | -1,601 | +480 | +7,169 | +7,665 | +585 | +3,032 | +48,734 |
| 2026-10-30 | +9,708 | -35,219 | -2,768 | -241 | +3,375 | +8,655 | -2,361 | -18,851 |
| 2026-11-02 | +9,376 | +63,262 | -1,358 | -26,996 | +3,038 | -3,995 | -3,385 | +39,942 |
| 2026-11-03 | -18,168 | -12,215 | -1,110 | +13,477 | -7,695 | +0 | +3,215 | -22,496 |
| 2026-11-04 | +2,600 | -42,652 | -6,390 | -17,409 | -240 | +0 | +12,722 | -51,368 |
| 2026-11-05 | -20,828 | -38,627 | +5,752 | +2,836 | +1,545 | +0 | +26,370 | -22,951 |
| 2026-11-06 | +7,584 | +21,635 | -2,768 | +1,021 | -12,840 | +0 | - | +14,633 |
| sum | +75,116 | -27,506 | -5,032 | -20,739 | -938 | -705 | +36,144 | +56,341 |
full series: data/per_strategy_daily.csv (day, strategy, expected, attributed, gap); a strategy's daily total foots to expected - live_gross once the shared, neither and trading buckets are added. '-' = that sleeve's backtest row has not shipped yet (BT PENDING).

## Live P&L by product, last 10 reconciled days (gross CNY, worst first)
| product | 10-26 | 10-27 | 10-28 | 10-29 | 10-30 | 11-02 | 11-03 | 11-04 | 11-05 | 11-06 | 10d sum | live window |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| TA | -6,270 | +2,620 | +290 | +1,770 | -2,960 | +6,350 | -42,080 | -9,440 | -44,250 | -1,260 | -95,230 | -64,140 |
| y | -9,590 | +840 | -3,550 | -7,880 | -2,330 | +8,940 | -25,520 | -29,090 | -8,710 | -15,080 | -91,970 | -117,630 |
| a | -11,510 | -2,340 | -2,580 | -16,320 | -4,410 | +2,070 | -6,810 | -12,270 | +5,100 | -8,900 | -57,970 | -5,230 |
| pp | -2,380 | -6,235 | -1,165 | -8,380 | +1,800 | +410 | -14,870 | -2,660 | -17,820 | +1,755 | -49,545 | -52,875 |
| p | +1,810 | -35,990 | -8,710 | -22,970 | -5,410 | +4,090 | +5,620 | +15,810 | +4,650 | -8,100 | -49,200 | -10,250 |
| CF | -3,100 | -22,400 | -14,350 | -7,350 | +6,175 | -2,700 | -6,300 | +1,650 | +5,325 | -4,100 | -47,150 | -95,850 |
| eb | +2,335 | -1,505 | -2,215 | -5,445 | -190 | +7,710 | -19,680 | -5,700 | -12,610 | -3,895 | -41,195 | +27,340 |
| cs | -50 | +860 | -3,860 | -10,540 | +3,410 | -10,770 | -1,060 | -3,440 | -13,080 | +920 | -37,610 | +90,810 |
| IF | +5,400 | -1,080 | -5,040 | +2,880 | +9,120 | -26,400 | +3,420 | -15,000 | +900 | -1,980 | -27,780 | -67,860 |
| al | -14,925 | -2,525 | -14,850 | -950 | +4,900 | +4,200 | -5,775 | +3,475 | -2,675 | +2,350 | -26,775 | +118,375 |
| pg | +280 | -2,800 | -420 | -720 | -2,600 | +6,020 | -7,040 | -2,980 | -8,020 | -7,620 | -25,900 | -52,860 |
| i | +1,000 | +7,300 | -1,800 | -20,800 | +9,000 | -4,400 | +4,900 | -6,950 | -12,250 | -1,500 | -25,500 | -12,450 |
| b | -310 | -5,420 | +5,350 | -8,470 | -410 | -670 | -1,460 | -1,480 | +260 | -1,310 | -13,920 | -12,250 |
| ni | +1,750 | +1,460 | +650 | -1,220 | +1,730 | +180 | +2,470 | -410 | -10,520 | -9,020 | -12,930 | -32,460 |
| ru | +1,600 | -5,350 | +3,150 | -5,900 | -1,800 | +150 | +1,200 | -5,800 | -900 | +750 | -12,900 | -4,900 |
| other (24) | -9,400 | +3,435 | -900 | -50,490 | -15,805 | +20,030 | +49,115 | +13,955 | +6,365 | +47,825 | +64,130 | +442,495 |
| IH | +5,100 | +3,420 | -2,100 | +2,640 | +420 | -60 | -1,620 | +2,520 | -180 | +5,040 | +15,180 | +76,800 |
| CY | +1,800 | +12,200 | +4,800 | +6,800 | -14,450 | -1,100 | +8,875 | -1,900 | +800 | -1,450 | +16,375 | -3,650 |
| SF | +3,660 | +2,690 | -11,690 | +2,090 | -340 | +2,260 | +10,220 | +6,310 | -1,530 | +3,090 | +16,760 | +36,350 |
| hc | +4,110 | -2,160 | -3,020 | +17,000 | -9,790 | -6,480 | -9,690 | +750 | +19,770 | +9,570 | +20,060 | -141,580 |
| fu | -5,750 | -2,570 | -360 | -10,780 | +1,410 | +4,000 | +9,400 | +11,500 | +21,060 | -2,820 | +25,090 | +52,870 |
| zn | +12,975 | +3,000 | +1,400 | +850 | -250 | -150 | +1,450 | +4,900 | -2,825 | +5,400 | +26,750 | +34,100 |
| PF | -900 | +270 | -850 | -940 | -1,430 | -4,860 | +23,910 | +2,570 | +13,630 | -210 | +31,190 | +82,130 |
| SA | +20,000 | +11,760 | +11,360 | -7,140 | +180 | -6,340 | +6,760 | +10,000 | -2,580 | -8,660 | +35,340 | -27,180 |
| cu | +2,700 | +1,900 | +3,550 | +3,600 | -2,500 | -1,400 | -5,000 | +19,650 | -1,600 | +19,650 | +40,550 | +14,950 |
| eg | +3,700 | -200 | +3,200 | +1,720 | -5,540 | -3,220 | +13,720 | +2,050 | +26,680 | +870 | +42,980 | +46,410 |
| all products | +4,035 | -38,820 | -43,710 | -146,945 | -32,070 | -2,140 | -5,845 | -1,980 | -35,010 | +21,315 | -281,170 | +321,465 |
executor total_pnl (holding + trading, settlement-to-settlement once the next capture lands, before fees) summed by product root; 'all products' foots to live gross. Full series: data/product_daily.csv

## Worst (strategy, product) cells, last 10 reconciled days (attributed gross CNY)
| strategy | product | 10-26 | 10-27 | 10-28 | 10-29 | 10-30 | 11-02 | 11-03 | 11-04 | 11-05 | 11-06 | sum |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| china_pairs | y | +3,870 | -18,375 | +1,785 | -105 | +480 | +11,400 | -15,660 | -16,065 | -5,130 | -10,395 | -48,195 |
| fund_v3 | p | +1,840 | -19,280 | -3,280 | -8,720 | -160 | +4,660 | -2,120 | -8,760 | -5,160 | -5,500 | -46,480 |
| fund_v3 | cs | -1,200 | +640 | -3,400 | -10,780 | +2,720 | -11,120 | -1,120 | -3,900 | -16,200 | +1,220 | -43,140 |
| ks_ext | IF | +5,670 | -630 | -4,830 | +2,625 | -405 | -23,940 | +1,590 | -15,795 | +255 | -6,285 | -41,745 |
| china_pairs | TA | -3,060 | +1,020 | -60 | -540 | -1,740 | +4,785 | -15,360 | -4,050 | -19,305 | +2,970 | -35,340 |
| fund_v3 | eb | +8,510 | -3,730 | -930 | -3,170 | +0 | +6,840 | -18,620 | -6,840 | -10,980 | -4,060 | -32,980 |
| fund_v3 | FG | -3,360 | +6,160 | -8,400 | -3,920 | -10,840 | +800 | -6,240 | -4,200 | +0 | -1,120 | -31,120 |
| ks_branch | y | -8,904 | -1,400 | -3,672 | -6,808 | -2,320 | +6,032 | -3,712 | -7,072 | +912 | -2,392 | -29,336 |
| fund_v3 | a | -4,680 | -680 | -480 | -4,060 | -2,960 | +60 | -6,520 | -6,320 | +2,520 | -5,260 | -28,380 |
| stat_arb | p | +1,040 | -11,750 | -2,760 | -7,440 | +250 | +3,800 | -640 | -2,370 | -1,200 | -6,600 | -27,670 |
| fund_v3 | TA | +3,960 | -780 | +80 | +3,440 | -2,400 | +1,600 | -17,320 | -3,100 | -11,500 | -480 | -26,500 |
| ks_branch | p | -1,408 | -520 | -2,232 | -4,896 | -5,536 | -5,544 | +2,536 | +5,208 | -696 | -12,320 | -25,408 |
| fund_v3 | i | +1,000 | +6,600 | -1,700 | -21,200 | +7,900 | -2,900 | +5,100 | -7,300 | -11,200 | -600 | -24,300 |
| agri_event | p | +2,340 | -21,150 | -4,140 | -11,160 | +2,250 | +8,550 | +0 | +0 | +0 | +0 | -23,310 |
| chem_fund | TA | -6,150 | +1,590 | -75 | -975 | +510 | +2,415 | -9,525 | -2,265 | -10,305 | +1,800 | -22,980 |
same holdings split as 'Live P&L by strategy'; summing a strategy's products reproduces its row there (trading / neither included as their own strategy). Full series: data/strategy_product_daily.csv

## Paper strategies (weight 0 in the forward book: tracked, not traded)
| strategy | weight 0 since | bt since (full) | bt last 20d | drawdown now | worst before pause | 60d Sharpe | paper-live since (full) | paper days | book coverage |
|---|---|---|---|---|---|---|---|---|---|
| agri_event | 2026-11-02 | -14,860 | -112,690 | -158,440 | -149,795 | -2.67 | -15,045 | 4 | 100% |
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
decision-price coverage (2026-11-06): 100% of held notional benchmarked (0 contract(s) unbenchmarked); 11 contract(s) (17%) first decided after the 0900 snap, so they straddle their own overnight leg
scale: 1 (since 2026-09-09)
regime: forward (merged weighted book) since 2026-08-31; 44 forward day(s), 8 legacy day(s)
merge weights (2026-11-06): ks_branch 0.8, fund_v3 2, china_pairs 1.5, ks_ext 0.25, chem_fund 1.5, agri_event 0, stat_arb 1
as-shipped pins: 52 live day(s) pinned; current series diverges from pins on chem_fund: 30 day(s), max 9,725 CNY, fund_v3: 47 day(s), max 22,683 CNY, ks_branch: 43 day(s), max 82,125 CNY, ks_ext: 35 day(s), max 42,170 CNY, stat_arb: 43 day(s), max 9,982 CNY, china_pairs: 23 day(s), max 10,910 CNY, agri_event: 10 day(s), max 7,250 CNY; standing counts -- a divergence is announced as an alert once, the first run it appears, and kept here afterwards
inbox ks summary mtime: 2026-11-06 05:57 UTC
