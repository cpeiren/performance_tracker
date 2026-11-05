# Performance tracker - 2026-11-05   (reconciled through 2026-11-05)

## ALERTS
- VINTAGE agri_event: 54 historical row(s) restated (net +1,925 CNY, cause data, commit 8f0b7b9) -- kept as vintages/agri_event/20261105091241_8f0b7b90cc1f.csv; the bridge keeps the as-shipped pins
- VINTAGE chem_fund: 1 historical row(s) restated (net -480 CNY, cause data, commit a98238f) -- kept as vintages/chem_fund/20261105091241_a98238f08285.csv; the bridge keeps the as-shipped pins
- VINTAGE fund_v3: 3 historical row(s) restated (net -53 CNY, cause data, commit 0712a04) -- kept as vintages/fund_v3/20261105091241_0712a0472bd7.csv; the bridge keeps the as-shipped pins
- VINTAGE stat_arb: 1 historical row(s) restated (net -7,530 CNY, cause unknown, commit 9f7e9a7) -- kept as vintages/stat_arb/20261105091241_9f7e9a742805.csv; the bridge keeps the as-shipped pins
- WEIGHTS 2026-10-09: day's own merge weights not shipped yet -- carried forward from an earlier day.
- WEIGHTS 2026-10-16: day's own merge weights not shipped yet -- carried forward from an earlier day.
- WEIGHTS 2026-10-22: day's own merge weights not shipped yet -- carried forward from an earlier day.
- BT PENDING 2026-11-05: no mature backtest row for stat_arb (nonzero weight) -- day reconciled WITHOUT that sleeve's expected; its live P&L sits in bt_pending_live, not resid, until the rows ship.
- WEIGHTS CHANGE on 2026-09-01: ks_ext: 0.0->0.25.
- WEIGHTS CHANGE on 2026-09-02: stat_arb: 1.0->0.0.
- WEIGHTS CHANGE on 2026-09-03: stat_arb: 0.0->1.0.
- WEIGHTS CHANGE on 2026-11-02: agri_event: 1.0->0.0.
- BT REVISED vs PINS: fund_v3 current history differs from pinned as-shipped values on 1 new live-window day(s) (max |diff| 22683 CNY, first 2026-11-02); the bridge keeps the pins.
- MISSING LIVE DAY 2026-08-28: trading day with a backtest row but no daily_pnl/state file; excluded from the bridge, expected pnl held in the missing-day bucket.
- SCALE 2026-08-28: no usable run record; previous scale carried forward.
- SCALE 2026-09-25: no usable run record; previous scale carried forward.
- SCALE CHANGE on 2026-08-27: now 0.2.
- SCALE CHANGE on 2026-09-01: now 0.5.
- SCALE CHANGE on 2026-09-09: now 1.
- BACKTEST REVISED: agri_event -- 50 mature row(s) changed since last run (net +100 CNY, largest 2026-02-24 +49955 -> +47280; first 2026-01-07, last 2026-05-22). Regeneration upstream; baseline re-set.
- SLIPPAGE 2026-11-05: 4 unbenchmarked leg(s), -45 CNY exec cost without a shipped decision price.
- RESIDUAL 2026-08-27: -17267 CNY vs trailing median |resid| 2062, offset by neither neighbour (2026-08-26 +3749, 2026-08-31 -17348) -- attribution quality changed. (A break-out that a neighbouring day mirrors is the backtest/live day-window straddle and is not alerted.)
- RESIDUAL 2026-08-31: -17348 CNY vs trailing median |resid| 2277, offset by neither neighbour (2026-08-27 -17267, 2026-09-01 -8190) -- attribution quality changed. (A break-out that a neighbouring day mirrors is the backtest/live day-window straddle and is not alerted.)
- RESIDUAL 2026-09-01: -8190 CNY vs trailing median |resid| 2492, offset by neither neighbour (2026-08-31 -17348, 2026-09-02 -30063) -- attribution quality changed. (A break-out that a neighbouring day mirrors is the backtest/live day-window straddle and is not alerted.)
- RESIDUAL 2026-09-02: -30063 CNY vs trailing median |resid| 3121, offset by neither neighbour (2026-09-01 -8190, 2026-09-03 -29049) -- attribution quality changed. (A break-out that a neighbouring day mirrors is the backtest/live day-window straddle and is not alerted.)
- RESIDUAL 2026-09-03: -29049 CNY vs trailing median |resid| 3941, offset by neither neighbour (2026-09-02 -30063, 2026-09-04 -5584) -- attribution quality changed. (A break-out that a neighbouring day mirrors is the backtest/live day-window straddle and is not alerted.)
- RESIDUAL 2026-09-16: -103509 CNY vs trailing median |resid| 22936, offset by neither neighbour (2026-09-15 -28634, 2026-09-17 +23811) -- attribution quality changed. (A break-out that a neighbouring day mirrors is the backtest/live day-window straddle and is not alerted.)
- RESIDUAL 2026-10-26: +29017 CNY vs trailing median |resid| 7638, offset by neither neighbour (2026-10-23 +7825, 2026-10-27 +81673) -- attribution quality changed. (A break-out that a neighbouring day mirrors is the backtest/live day-window straddle and is not alerted.)
- RESIDUAL 2026-10-27: +81673 CNY vs trailing median |resid| 9046, offset by neither neighbour (2026-10-26 +29017, 2026-10-28 +2573) -- attribution quality changed. (A break-out that a neighbouring day mirrors is the backtest/live day-window straddle and is not alerted.)

## Latest reconciled day (2026-11-05, forward regime, PROVISIONAL: marked at the 16:00 close, re-marked to settlement after the next capture)
live gross -38,335 | expected (1 x bt +15,781) = +15,781 | gap -54,116
  exec_cost +3,305 (slip +3,350, unbench -45) | marking -13,285 | bookdiff -100 (carry +0, new -100) | intraday +0 | offbook +0 (0 contract(s)) | residual -57,156 (live re-marked to first decision, vs the previous backtest row)
  PARTIAL: no backtest row yet for stat_arb -- expected excludes it; its live P&L +19,730 is held out of resid
  fees +1,117 | broker residual +0 -> live net -39,452

## Cumulative bridge (live since 2026-08-18, 51 reconciled days, 1 with a sleeve's backtest pending)
| expected | -exec | +marking | +bookdiff | +intraday | +offbook | +bt pending | +resid | = live gross | -fees | +broker_resid | = live net |
|---|---|---|---|---|---|---|---|---|---|---|---|
| +330,190 | -70,260 | -17,420 | +91,187 | -5,168 | -50 | +19,730 | -51,385 | +296,825 | -49,147 | +11,081 | +258,759 |
missing live days excluded: 2026-08-28 (expected +4,849 held in bucket)

## Stats (daily CNY pnl)
| window | days | total | sharpe | mdd | hit |
|---|---|---|---|---|---|
| live net live-to-date | 51 | +258,759 | 1.40 | -330,281 | 51% |
| live net last-20d | 20 | -11,676 | -0.18 | -321,272 | 40% | (small sample)
| live net 2026-YTD | 51 | +258,759 | 1.40 | -330,281 | 51% |
| bt scaled live-to-date | 51 | +330,190 | 1.66 | -381,526 | 65% |
| bt scaled last-20d | 20 | +30,730 | 0.37 | -381,526 | 60% | (small sample)
| bt scaled 2026-YTD | 51 | +330,190 | 1.66 | -381,526 | 65% |

## Slippage (+ = cost; bps vs benchmarked notional)
| day | lots | notional M | slip total | drift | exec | bps | unbench legs | unbench CNY |
|---|---|---|---|---|---|---|---|---|
| 2026-10-23 | 345 | 14.2 | -310 | -1,435 | +1,125 | -0.23 | 2 | -20 |
| 2026-10-26 | 423 | 16.9 | +3,130 | +2,752 | +378 | +1.86 | 1 | +105 |
| 2026-10-27 | 720 | 42.7 | +11,470 | +8,082 | +3,388 | +2.83 | 2 | -335 |
| 2026-10-28 | 220 | 17.2 | +7,060 | +6,922 | +138 | +4.23 | 3 | +320 |
| 2026-10-29 | 393 | 27.9 | +4,825 | +3,225 | +1,600 | +2.13 | 6 | -620 |
| 2026-10-30 | 249 | 14.1 | +6,150 | +6,185 | -35 | +4.49 | 4 | +5 |
| 2026-11-02 | 258 | 19.2 | +7,360 | +6,620 | +740 | +3.92 | 3 | -5 |
| 2026-11-03 | 379 | 25.3 | +7,160 | +5,542 | +1,618 | +2.94 | 2 | +2,140 |
| 2026-11-04 | 364 | 32.1 | +2,030 | +1,422 | +608 | +0.64 | 1 | +275 |
| 2026-11-05 | 462 | 30.3 | +3,350 | +942 | +2,408 | +1.15 | 4 | -45 |
| live window (51d) | 18591 | 1161.8 | +54,705 | +912 | +53,792 | +0.51 | 249 | +15,555 |
exec-only bps over the window: +0.50; benchmark coverage 93% of traded notional

| product | days | lots | notional M | drift | exec (incl. unbench) | all-in | bps |
|---|---|---|---|---|---|---|---|
| IH | 32 | 128 | 106.6 | -28,020 | +5,220 | -22,800 | -2.14 |
| IF | 20 | 72 | 92.6 | -20,130 | +2,670 | -17,460 | -1.88 |
| rb | 41 | 1267 | 39.2 | +18,545 | -3,615 | +14,930 | +3.80 |
| CY | 38 | 280 | 30.9 | +9,162 | +5,438 | +14,600 | +4.73 |
| bu | 44 | 477 | 22.9 | -14,545 | +1,575 | -12,970 | -5.66 |
| hc | 43 | 1515 | 49.9 | -17,970 | +5,550 | -12,420 | -2.49 |
| FG | 50 | 954 | 17.2 | +6,320 | +4,880 | +11,200 | +6.49 |
| pg | 26 | 45 | 6.2 | +10,410 | +310 | +10,720 | +17.38 |
| SF | 47 | 443 | 13.3 | +8,870 | +855 | +9,725 | +7.31 |
| y | 42 | 300 | 26.7 | +6,880 | +2,080 | +8,960 | +3.35 |
| ru | 31 | 98 | 18.9 | +8,100 | -125 | +7,975 | +4.21 |
| a | 46 | 595 | 31.4 | +4,015 | +3,150 | +7,165 | +2.28 |
| SR | 45 | 904 | 48.9 | +4,865 | +1,780 | +6,645 | +1.36 |
| PF | 42 | 251 | 10.4 | -7,170 | +700 | -6,470 | -6.22 |
| cs | 49 | 947 | 23.8 | +1,760 | +4,455 | +6,215 | +2.62 |
| other (34) | - | 10315 | 622.7 | +9,820 | +34,425 | +44,245 | +0.71 |
| all products | - | 18591 | 1161.8 | +912 | +69,348 | +70,260 | +0.60 |
ranked by |all-in| over the live window (all-in = drift + exec = the bridge's exec_cost by product); product bps are vs traded notional

## Per strategy
| strategy | live? | bt 2026 pnl (full) | bt scaled+weighted (live window) | live attributed | note |
|---|---|---|---|---|---|
| Calendar main pool (branch) | yes | +1,014,090 | +9,128 | +44,727 | forward w=0.8 |
| Fundamental factor | yes | +796,444 | +325,711 | +259,465 | forward w=2 |
| Cross-product pairs | yes | +54,310 | -4,634 | -22,437 | forward w=1.5 |
| Calendar extended pool | yes | +468,800 | +7,966 | +70,962 | forward w=0.25 |
| Chemical fundamental | yes | +520,135 | +59,283 | +26,726 | forward w=1.5 |
| Agriculture event-driven | no | +32,185 | -111,243 | -152,798 | forward w=0 (parked) |
| Factor-neutral stat arb | yes | +354,471 | +43,979 | +77,454 | forward w=1 |
| shared bucket | - | - | - | +3,575 | legacy days only: a contract both per-source books held |
| neither bucket (no target) | - | - | - | +2,330 | named by no book that day or the day before |
| trading bucket | - | - | - | -13,179 | forward days: live P&L minus the strategies' holdings (fills vs settlement on rebalances, lot rounding, scale changes) |
forward days: each strategy is its own previous-day weighted book x scale x the settlement-to-settlement move (holdings); legacy days remain exclusive-holder. The gap tables (attributed - expected) therefore exclude execution, which sits in trading.

## Live P&L by strategy, last 10 reconciled days (attributed gross CNY)
| day | ks_branch | fund_v3 | china_pairs | ks_ext | chem_fund | agri_event | stat_arb | shared | neither | trading | total |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 2026-10-23 | -8,796 | -9,130 | +6,262 | -2,563 | +11,032 | -19,495 | +8,845 | +0 | +0 | +2,289 | -11,555 |
| 2026-10-26 | -240 | -4,570 | +2,258 | +11,030 | +17,498 | -9,650 | -10,845 | +0 | +0 | -1,445 | +4,035 |
| 2026-10-27 | +35,236 | -2,240 | -9,068 | +6,356 | +9,218 | -37,080 | -20,025 | +0 | +0 | -21,217 | -38,820 |
| 2026-10-28 | +4,048 | -15,440 | -5,362 | -7,313 | -2,760 | -10,980 | -2,965 | +0 | +0 | -2,938 | -43,710 |
| 2026-10-29 | -49,776 | -53,440 | -825 | +6,281 | -6,968 | -18,070 | -15,165 | +0 | +0 | -8,983 | -146,945 |
| 2026-10-30 | -16,068 | -66,600 | -1,560 | +2,871 | +9,292 | +8,605 | +13,805 | +0 | -275 | +17,859 | -32,070 |
| 2026-11-02 | +4,260 | -660 | +7,845 | -25,403 | +15,420 | -3,995 | +12,980 | +0 | +0 | -12,588 | -2,140 |
| 2026-11-03 | -9,816 | +21,940 | -8,490 | -123 | -13,485 | +0 | +1,335 | +0 | +0 | +2,793 | -5,845 |
| 2026-11-04 | +7,320 | -21,410 | -2,842 | -13,680 | +11,618 | +0 | +12,140 | +0 | +0 | +4,875 | -1,980 |
| 2026-11-05 | -19,916 | +2,800 | +3,885 | +15,811 | -17,250 | +0 | +19,730 | +0 | +0 | -43,395 | -38,335 |
| sum | -53,748 | -148,750 | -7,898 | -6,730 | +33,615 | -90,665 | +19,835 | +0 | -275 | -62,750 | -317,365 |
forward days: previous-day weighted book x scale x settlement move per strategy, the rest in trading; total foots to live gross. Live-window sums: 'Per strategy' above; full series: data/per_strategy_daily.csv (attributed)

## Per strategy gap by day, last 10 reconciled days (live attributed - expected, CNY)
| day | ks_branch | fund_v3 | china_pairs | ks_ext | chem_fund | agri_event | stat_arb | total |
|---|---|---|---|---|---|---|---|---|
| 2026-10-23 | +3,360 | -4,852 | -3,255 | +1,446 | +4,328 | +3,345 | -5,275 | -904 |
| 2026-10-26 | -16,908 | +16,537 | -1,418 | +7,696 | +6,255 | -7,360 | -4,496 | +307 |
| 2026-10-27 | +83,988 | -3,013 | +4,755 | +3,094 | -12,608 | +9,880 | +11,794 | +97,890 |
| 2026-10-28 | -13,640 | +4,387 | -210 | -11,386 | +10,568 | -8,470 | -10,748 | -29,499 |
| 2026-10-29 | +31,404 | -1,601 | +480 | +7,169 | +7,665 | +585 | +3,032 | +48,734 |
| 2026-10-30 | +9,708 | -35,219 | -2,768 | -241 | +3,375 | +8,655 | -2,361 | -18,851 |
| 2026-11-02 | +9,376 | +63,262 | -1,358 | -26,996 | +3,038 | -3,995 | -3,385 | +39,942 |
| 2026-11-03 | -18,168 | -12,215 | -1,110 | +13,477 | -7,695 | +0 | +3,215 | -22,496 |
| 2026-11-04 | +2,600 | -42,652 | -6,390 | -17,409 | -240 | +0 | +12,722 | -51,368 |
| 2026-11-05 | -7,356 | -37,087 | +10,170 | +10,535 | -6,712 | +0 | - | -30,450 |
| sum | +84,364 | -52,453 | -1,102 | -12,615 | +7,972 | +2,640 | +4,499 | +33,305 |
full series: data/per_strategy_daily.csv (day, strategy, expected, attributed, gap); a strategy's daily total foots to expected - live_gross once the shared, neither and trading buckets are added. '-' = that sleeve's backtest row has not shipped yet (BT PENDING).

## Live P&L by product, last 10 reconciled days (gross CNY, worst first)
| product | 10-23 | 10-26 | 10-27 | 10-28 | 10-29 | 10-30 | 11-02 | 11-03 | 11-04 | 11-05 | 10d sum | live window |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| TA | -3,880 | -6,270 | +2,620 | +290 | +1,770 | -2,960 | +6,350 | -42,080 | -9,440 | -58,600 | -112,200 | -77,230 |
| y | -1,210 | -9,590 | +840 | -3,550 | -7,880 | -2,330 | +8,940 | -25,520 | -29,090 | -13,390 | -82,780 | -107,230 |
| cs | -30,200 | -50 | +860 | -3,860 | -10,540 | +3,410 | -10,770 | -1,060 | -3,440 | -14,190 | -69,840 | +88,780 |
| pp | -4,590 | -2,380 | -6,235 | -1,165 | -8,380 | +1,800 | +410 | -14,870 | -2,660 | -18,725 | -56,795 | -55,535 |
| CF | -3,750 | -3,100 | -22,400 | -14,350 | -7,350 | +6,175 | -2,700 | -6,300 | +1,650 | +5,825 | -46,300 | -91,250 |
| a | +4,610 | -11,510 | -2,340 | -2,580 | -16,320 | -4,410 | +2,070 | -6,810 | -12,270 | +4,520 | -45,040 | +3,090 |
| eb | +835 | +2,335 | -1,505 | -2,215 | -5,445 | -190 | +7,710 | -19,680 | -5,700 | -17,120 | -40,975 | +26,725 |
| i | +600 | +1,000 | +7,300 | -1,800 | -20,800 | +9,000 | -4,400 | +4,900 | -6,950 | -21,700 | -32,850 | -20,400 |
| al | +2,575 | -14,925 | -2,525 | -14,850 | -950 | +4,900 | +4,200 | -5,775 | +3,475 | -6,800 | -30,675 | +111,900 |
| p | +15,090 | +1,810 | -35,990 | -8,710 | -22,970 | -5,410 | +4,090 | +5,620 | +15,810 | +4,250 | -26,410 | -2,550 |
| IF | -1,500 | +5,400 | -1,080 | -5,040 | +2,880 | +9,120 | -26,400 | +3,420 | -15,000 | +1,800 | -26,400 | -64,980 |
| ru | -1,500 | +1,600 | -5,350 | +3,150 | -5,900 | -1,800 | +150 | +1,200 | -5,800 | -650 | -14,900 | -5,400 |
| OI | -7,940 | -1,930 | -3,800 | +340 | -10,220 | -9,480 | +7,280 | +2,470 | -4,450 | +13,350 | -14,380 | -33,070 |
| ni | +2,010 | +1,750 | +1,460 | +650 | -1,220 | +1,730 | +180 | +2,470 | -410 | -20,400 | -11,780 | -33,320 |
| rb | -10,560 | +3,780 | +3,890 | -9,760 | -15,710 | +6,930 | +17,080 | +16,450 | +4,400 | -26,610 | -10,110 | +122,290 |
| other (24) | +20,665 | +11,075 | +215 | +23,375 | -30,995 | -13,680 | +1,570 | +13,980 | +2,930 | -5,025 | +24,110 | +293,440 |
| pb | -150 | +475 | -1,175 | -3,225 | +5,175 | +25 | -2,575 | +7,025 | +3,925 | +200 | +9,700 | +40,325 |
| SF | -3,340 | +3,660 | +2,690 | -11,690 | +2,090 | -340 | +2,260 | +10,220 | +6,310 | -970 | +10,890 | +33,820 |
| v | -90 | -4,755 | +2,505 | -7,400 | -4,440 | -2,440 | +1,815 | +520 | +10,110 | +22,550 | +18,375 | +24,830 |
| cu | -1,500 | +2,700 | +1,900 | +3,550 | +3,600 | -2,500 | -1,400 | -5,000 | +19,650 | -2,600 | +18,400 | -5,700 |
| CY | +1,850 | +1,800 | +12,200 | +4,800 | +6,800 | -14,450 | -1,100 | +8,875 | -1,900 | +700 | +19,575 | -2,300 |
| hc | +9,540 | +4,110 | -2,160 | -3,020 | +17,000 | -9,790 | -6,480 | -9,690 | +750 | +25,890 | +26,150 | -145,030 |
| fu | -9,800 | -5,750 | -2,570 | -360 | -10,780 | +1,410 | +4,000 | +9,400 | +11,500 | +33,910 | +30,960 | +68,540 |
| PF | -1,880 | -900 | +270 | -850 | -940 | -1,430 | -4,860 | +23,910 | +2,570 | +20,320 | +36,210 | +89,030 |
| eg | +1,120 | +3,700 | -200 | +3,200 | +1,720 | -5,540 | -3,220 | +13,720 | +2,050 | +33,930 | +50,480 | +52,790 |
| SA | +11,440 | +20,000 | +11,760 | +11,360 | -7,140 | +180 | -6,340 | +6,760 | +10,000 | +1,200 | +59,220 | -14,740 |
| all products | -11,555 | +4,035 | -38,820 | -43,710 | -146,945 | -32,070 | -2,140 | -5,845 | -1,980 | -38,335 | -317,365 | +296,825 |
executor total_pnl (holding + trading, settlement-to-settlement once the next capture lands, before fees) summed by product root; 'all products' foots to live gross. Full series: data/product_daily.csv

## Worst (strategy, product) cells, last 10 reconciled days (attributed gross CNY)
| strategy | product | 10-23 | 10-26 | 10-27 | 10-28 | 10-29 | 10-30 | 11-02 | 11-03 | 11-04 | 11-05 | sum |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| fund_v3 | cs | -26,840 | -1,200 | +640 | -3,400 | -10,780 | +2,720 | -11,120 | -1,120 | -3,900 | -17,400 | -72,400 |
| china_pairs | TA | +0 | -3,060 | +1,020 | -60 | -540 | -1,740 | +4,785 | -15,360 | -4,050 | -25,380 | -44,385 |
| fund_v3 | p | +2,000 | +1,840 | -19,280 | -3,280 | -8,720 | -160 | +4,660 | -2,120 | -8,760 | -6,440 | -40,260 |
| ks_ext | IF | -1,425 | +5,670 | -630 | -4,830 | +2,625 | -405 | -23,940 | +1,590 | -15,795 | +1,530 | -35,610 |
| fund_v3 | eb | +1,920 | +8,510 | -3,730 | -930 | -3,170 | +0 | +6,840 | -18,620 | -6,840 | -17,610 | -33,630 |
| ks_branch | y | -2,592 | -8,904 | -1,400 | -3,672 | -6,808 | -2,320 | +6,032 | -3,712 | -7,072 | -2,280 | -32,728 |
| china_pairs | y | +8,220 | +3,870 | -18,375 | +1,785 | -105 | +480 | +11,400 | -15,660 | -16,065 | -7,560 | -32,010 |
| chem_fund | TA | -3,705 | -6,150 | +1,590 | -75 | -975 | +510 | +2,415 | -9,525 | -2,265 | -13,830 | -32,010 |
| fund_v3 | i | +400 | +1,000 | +6,600 | -1,700 | -21,200 | +7,900 | -2,900 | +5,100 | -7,300 | -17,100 | -29,200 |
| fund_v3 | TA | +2,640 | +3,960 | -780 | +80 | +3,440 | -2,400 | +1,600 | -17,320 | -3,100 | -17,000 | -28,880 |
| fund_v3 | FG | +1,400 | -3,360 | +6,160 | -8,400 | -3,920 | -10,840 | +800 | -6,240 | -4,200 | +0 | -28,600 |
| ks_branch | OI | -6,600 | -1,584 | -5,672 | -440 | -9,096 | -7,176 | +5,656 | +2,056 | -1,584 | -1,312 | -25,752 |
| agri_event | p | -1,080 | +2,340 | -21,150 | -4,140 | -11,160 | +2,250 | +8,550 | +0 | +0 | +0 | -24,390 |
| fund_v3 | pg | +0 | -9,280 | -8,120 | +1,520 | -1,120 | -5,000 | +0 | +0 | +0 | +0 | -22,000 |
| agri_event | SR | -2,240 | -2,240 | -13,280 | +1,760 | -1,760 | -320 | -3,520 | +0 | +0 | +0 | -21,600 |
same holdings split as 'Live P&L by strategy'; summing a strategy's products reproduces its row there (trading / neither included as their own strategy). Full series: data/strategy_product_daily.csv

## Paper strategies (weight 0 in the forward book: tracked, not traded)
| strategy | weight 0 since | bt since (full) | bt last 20d | drawdown now | worst before pause | 60d Sharpe | paper-live since (full) | paper days | book coverage |
|---|---|---|---|---|---|---|---|---|---|
| agri_event | 2026-11-02 | -11,755 | -112,720 | -155,285 | -149,745 | -2.22 | -6,350 | 3 | 100% |
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
| agri_event | +9,450 |
| stat_arb | +16,744 |
| all | +25,172 |
| strategy | vintages | latest | cause | commit | rows restated | net change (full size) |
|---|---|---|---|---|---|---|
| ks_branch | 2 | 20261102090932_cbbdd7664522.csv | unknown | cbbdd76 | 165 | +341,255 |
| ks_ext | 2 | 20261102090932_1a03a09367cb.csv | unknown | 1a03a09 | 91 | +31,590 |
| china_pairs | 2 | 20261102090932_51a17747e0e0.csv | unknown | 51a1774 | 44 | -46,815 |
| agri_event | 6 | 20261105091241_8f0b7b90cc1f.csv | data | 8f0b7b9 | 54 | +1,925 |
| chem_fund | 3 | 20261105091241_a98238f08285.csv | data | a98238f | 1 | -480 |
| fund_v3 | 3 | 20261105091241_0712a0472bd7.csv | data | 0712a04 | 3 | -53 |
| stat_arb | 2 | 20261105091241_9f7e9a742805.csv | unknown | 9f7e9a7 | 1 | -7,530 |
full series: data/backtest/vintages/<strategy>/; index: data/backtest/vintages/index.csv

## Data health
decision-price coverage (2026-11-05): 100% of held notional benchmarked (0 contract(s) unbenchmarked); 10 contract(s) (15%) first decided after the 0900 snap, so they straddle their own overnight leg
scale: 1 (since 2026-09-09)
regime: forward (merged weighted book) since 2026-08-31; 43 forward day(s), 8 legacy day(s)
merge weights (2026-11-05): ks_branch 0.8, fund_v3 2, china_pairs 1.5, ks_ext 0.25, chem_fund 1.5, agri_event 0, stat_arb 1
as-shipped pins: 51 live day(s) pinned; current series diverges from pins on chem_fund: 30 day(s), max 9,725 CNY, fund_v3: 47 day(s), max 22,683 CNY, 1 NEW, ks_branch: 43 day(s), max 82,125 CNY, ks_ext: 35 day(s), max 42,170 CNY, stat_arb: 43 day(s), max 9,982 CNY, china_pairs: 23 day(s), max 10,910 CNY, agri_event: 10 day(s), max 7,250 CNY; standing counts -- a divergence is announced as an alert once, the first run it appears, and kept here afterwards
inbox ks summary mtime: 2026-11-05 05:57 UTC
