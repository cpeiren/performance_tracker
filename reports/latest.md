# Performance tracker - 2026-11-24   (reconciled through 2026-11-24)

## ALERTS
- VINTAGE agri_event: 3 historical row(s) restated (net +1,325 CNY, cause data, commit 8f0b7b9) -- kept as vintages/agri_event/20261124091333_8f0b7b90cc1f.csv; the bridge keeps the as-shipped pins
- WEIGHTS 2026-10-09: day's own merge weights not shipped yet -- carried forward from an earlier day.
- WEIGHTS 2026-10-16: day's own merge weights not shipped yet -- carried forward from an earlier day.
- WEIGHTS 2026-10-22: day's own merge weights not shipped yet -- carried forward from an earlier day.
- BT PENDING 2026-11-24: no mature backtest row for stat_arb (nonzero weight) -- day reconciled WITHOUT that sleeve's expected; its live P&L sits in bt_pending_live, not resid, until the rows ship.
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
- BACKTEST REVISED: agri_event -- 1 mature row(s) changed since last run (net +400 CNY, largest 2026-05-07 -17715 -> -17315; first 2026-05-07, last 2026-05-07). Regeneration upstream; baseline re-set.
- SLIPPAGE 2026-11-24: 5 unbenchmarked leg(s), -85 CNY exec cost without a shipped decision price.
- RESIDUAL 2026-08-27: -17267 CNY vs trailing median |resid| 2062, offset by neither neighbour (2026-08-26 +3749, 2026-08-31 -17348) -- attribution quality changed. (A break-out that a neighbouring day mirrors is the backtest/live day-window straddle and is not alerted.)
- RESIDUAL 2026-08-31: -17348 CNY vs trailing median |resid| 2277, offset by neither neighbour (2026-08-27 -17267, 2026-09-01 -8190) -- attribution quality changed. (A break-out that a neighbouring day mirrors is the backtest/live day-window straddle and is not alerted.)
- RESIDUAL 2026-09-01: -8190 CNY vs trailing median |resid| 2492, offset by neither neighbour (2026-08-31 -17348, 2026-09-02 -30063) -- attribution quality changed. (A break-out that a neighbouring day mirrors is the backtest/live day-window straddle and is not alerted.)
- RESIDUAL 2026-09-02: -30063 CNY vs trailing median |resid| 3121, offset by neither neighbour (2026-09-01 -8190, 2026-09-03 -29049) -- attribution quality changed. (A break-out that a neighbouring day mirrors is the backtest/live day-window straddle and is not alerted.)
- RESIDUAL 2026-09-03: -29049 CNY vs trailing median |resid| 3941, offset by neither neighbour (2026-09-02 -30063, 2026-09-04 -5584) -- attribution quality changed. (A break-out that a neighbouring day mirrors is the backtest/live day-window straddle and is not alerted.)
- RESIDUAL 2026-09-16: -103509 CNY vs trailing median |resid| 22936, offset by neither neighbour (2026-09-15 -28634, 2026-09-17 +23811) -- attribution quality changed. (A break-out that a neighbouring day mirrors is the backtest/live day-window straddle and is not alerted.)
- RESIDUAL 2026-10-26: +29017 CNY vs trailing median |resid| 7638, offset by neither neighbour (2026-10-23 +7825, 2026-10-27 +81673) -- attribution quality changed. (A break-out that a neighbouring day mirrors is the backtest/live day-window straddle and is not alerted.)
- RESIDUAL 2026-10-27: +81673 CNY vs trailing median |resid| 9046, offset by neither neighbour (2026-10-26 +29017, 2026-10-28 +2573) -- attribution quality changed. (A break-out that a neighbouring day mirrors is the backtest/live day-window straddle and is not alerted.)
- KS CROSS-CHECK: shipped ks_branch series differs from inbox summary on 1 date(s), max |diff| 28635 CNY (first: 2026-11-23).

## Latest reconciled day (2026-11-24, forward regime, PROVISIONAL: marked at the 16:00 close, re-marked to settlement after the next capture)
live gross +71,145 | expected (1 x bt +50,167) = +50,167 | gap +20,978
  exec_cost -9,450 (slip -9,365, unbench -85) | marking -18,500 | bookdiff -150 (carry +0, new -150) | intraday +0 | offbook +0 (0 contract(s)) | residual +48,548 (live re-marked to first decision, vs the previous backtest row)
  PARTIAL: no backtest row yet for stat_arb -- expected excludes it; its live P&L -18,370 is held out of resid
  fees +878 | broker residual +0 -> live net +70,267

## Cumulative bridge (live since 2026-08-18, 64 reconciled days, 1 with a sleeve's backtest pending)
| expected | -exec | +marking | +bookdiff | +intraday | +offbook | +bt pending | +resid | = live gross | -fees | +broker_resid | = live net |
|---|---|---|---|---|---|---|---|---|---|---|---|
| +1,027,298 | -79,902 | -23,375 | +89,897 | -6,568 | -50 | -18,370 | +39,771 | +1,028,700 | -66,563 | +11,201 | +973,338 |
missing live days excluded: 2026-08-28 (expected +4,849 held in bucket)

## Stats (daily CNY pnl)
| window | days | total | sharpe | mdd | hit |
|---|---|---|---|---|---|
| live net live-to-date | 64 | +973,338 | 4.22 | -330,281 | 59% |
| live net last-20d | 20 | +443,318 | 5.79 | -230,008 | 60% | (small sample)
| live net 2026-YTD | 64 | +973,338 | 4.22 | -330,281 | 59% |
| bt scaled live-to-date | 64 | +1,027,298 | 3.95 | -381,526 | 67% |
| bt scaled last-20d | 20 | +512,991 | 5.30 | -246,994 | 65% | (small sample)
| bt scaled 2026-YTD | 64 | +1,027,298 | 3.95 | -381,526 | 67% |

## Slippage (+ = cost; bps vs benchmarked notional)
| day | lots | notional M | slip total | drift | exec | bps | unbench legs | unbench CNY |
|---|---|---|---|---|---|---|---|---|
| 2026-11-11 | 445 | 37.7 | -5,640 | -6,922 | +1,282 | -1.52 | 3 | +50 |
| 2026-11-12 | 508 | 31.3 | +3,550 | +2,372 | +1,178 | +1.15 | 2 | -100 |
| 2026-11-13 | 504 | 35.5 | +2,085 | -325 | +2,410 | +0.62 | 5 | +228 |
| 2026-11-16 | 540 | 42.9 | +14,910 | +13,128 | +1,782 | +3.92 | 8 | +28 |
| 2026-11-17 | 436 | 22.5 | -3,665 | -7,090 | +3,425 | -1.67 | 4 | -48 |
| 2026-11-18 | 689 | 27.1 | -5,590 | -6,510 | +920 | -2.45 | 3 | +1,895 |
| 2026-11-19 | 504 | 26.6 | -12,410 | -12,082 | -328 | -4.71 | 2 | +55 |
| 2026-11-20 | 485 | 23.4 | +18,405 | +17,610 | +795 | +7.95 | 2 | -25 |
| 2026-11-23 | 297 | 17.1 | -4,770 | -4,665 | -105 | -2.83 | 3 | +48 |
| 2026-11-24 | 287 | 23.9 | -9,365 | -9,605 | +240 | -4.23 | 5 | -85 |
| live window (64d) | 25152 | 1545.5 | +62,170 | -12,620 | +74,790 | +0.43 | 290 | +17,732 |
exec-only bps over the window: +0.52; benchmark coverage 93% of traded notional

| product | days | lots | notional M | drift | exec (incl. unbench) | all-in | bps |
|---|---|---|---|---|---|---|---|
| IF | 26 | 87 | 110.5 | -28,680 | +3,240 | -25,440 | -2.30 |
| pg | 33 | 62 | 8.2 | +23,420 | +180 | +23,600 | +28.85 |
| IH | 42 | 172 | 142.5 | -28,050 | +5,490 | -22,560 | -1.58 |
| al | 51 | 757 | 87.6 | +16,412 | +3,238 | +19,650 | +2.24 |
| rb | 53 | 2056 | 62.9 | +14,635 | +2,250 | +16,885 | +2.69 |
| CY | 47 | 350 | 38.3 | +9,288 | +6,038 | +15,325 | +4.00 |
| zn | 48 | 517 | 66.7 | -16,525 | +1,362 | -15,162 | -2.27 |
| bu | 56 | 631 | 29.6 | -14,820 | +1,485 | -13,335 | -4.51 |
| hc | 56 | 2082 | 67.8 | -18,140 | +5,760 | -12,380 | -1.83 |
| SA | 60 | 1020 | 20.4 | +8,070 | +3,830 | +11,900 | +5.83 |
| y | 54 | 386 | 34.0 | +9,345 | +2,495 | +11,840 | +3.49 |
| SF | 57 | 595 | 17.7 | +8,710 | +1,005 | +9,715 | +5.48 |
| pb | 52 | 1161 | 92.8 | +3,812 | +5,062 | +8,875 | +0.96 |
| FG | 63 | 1242 | 22.4 | +1,240 | +6,900 | +8,140 | +3.63 |
| a | 59 | 689 | 36.2 | +3,670 | +3,465 | +7,135 | +1.97 |
| other (39) | - | 13345 | 708.0 | -5,008 | +40,722 | +35,715 | +0.50 |
| all products | - | 25152 | 1545.5 | -12,620 | +92,522 | +79,902 | +0.52 |
ranked by |all-in| over the live window (all-in = drift + exec = the bridge's exec_cost by product); product bps are vs traded notional

## Per strategy
| strategy | live? | bt 2026 pnl (full) | bt scaled+weighted (live window) | live attributed | note |
|---|---|---|---|---|---|
| Calendar main pool (branch) | yes | +1,279,260 | +198,356 | +243,879 | forward w=0.8 |
| Fundamental factor | yes | +1,020,316 | +773,686 | +734,785 | forward w=2 |
| Cross-product pairs | yes | +101,000 | +65,401 | +25,248 | forward w=1.5 |
| Calendar extended pool | yes | +694,200 | +64,316 | +118,702 | forward w=0.25 |
| Chemical fundamental | yes | +487,355 | +10,113 | -45,732 | forward w=1.5 |
| Agriculture event-driven | no | -30,830 | -111,243 | -152,798 | forward w=0 (parked) |
| Factor-neutral stat arb | yes | +318,155 | +12,028 | +22,934 | forward w=1 |
| Fund pipeline ensemble | yes | +2,375,001 | +20,821 | +24,447 | forward w=0.1 |
| Outright trend + basis | yes | +503,070 | -6,180 | -5,922 | forward w=0.5 |
| shared bucket | - | - | - | +3,575 | legacy days only: a contract both per-source books held |
| neither bucket (no target) | - | - | - | +3,050 | named by no book that day or the day before |
| trading bucket | - | - | - | +56,532 | forward days: live P&L minus the strategies' holdings (fills vs settlement on rebalances, lot rounding, scale changes) |
forward days: each strategy is its own previous-day weighted book x scale x the settlement-to-settlement move (holdings); legacy days remain exclusive-holder. The gap tables (attributed - expected) therefore exclude execution, which sits in trading.

## Live P&L by strategy, last 10 reconciled days (attributed gross CNY)
| day | ks_branch | fund_v3 | china_pairs | ks_ext | chem_fund | agri_event | stat_arb | fpe | ks_outright | shared | neither | trading | total |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 2026-11-11 | -48 | +81,680 | +7,920 | -1,788 | -14,685 | +0 | +7,710 | +0 | +0 | +0 | +0 | +7,396 | +88,185 |
| 2026-11-12 | +57,280 | +15,540 | -5,798 | -3,425 | +975 | +0 | -5,505 | +30,757 | +8,365 | +0 | +255 | -1,640 | +96,805 |
| 2026-11-13 | +25,720 | +17,270 | +1,598 | -6,845 | -652 | +0 | +5,150 | +20,356 | +14,980 | +0 | +0 | +12,519 | +90,095 |
| 2026-11-16 | +42,372 | +44,060 | -4,905 | +3,780 | +9,698 | +0 | -9,495 | +21,178 | +3,188 | +0 | +0 | -7,000 | +102,875 |
| 2026-11-17 | +40,840 | +8,880 | -6,218 | -1,909 | -3,375 | +0 | -13,180 | +12,305 | -15,038 | +0 | +0 | +3,059 | +25,365 |
| 2026-11-18 | -42,252 | +43,890 | +8,482 | +6,179 | -2,985 | +0 | +4,010 | +14,961 | -5,422 | +0 | +0 | +14,027 | +40,890 |
| 2026-11-19 | +1,716 | +131,140 | +22,200 | +7,641 | -17,880 | +0 | -5,440 | -58,952 | -6,205 | +0 | +0 | +14,230 | +88,450 |
| 2026-11-20 | +10,400 | -24,460 | +11,348 | +35,759 | +1,958 | +0 | +4,215 | -37,628 | +3,755 | +0 | +0 | -4,381 | +965 |
| 2026-11-23 | +6,956 | +40,930 | -5,108 | -9,127 | -382 | +0 | +1,350 | +27,163 | +175 | +0 | +465 | -2,227 | +60,195 |
| 2026-11-24 | +59,488 | +38,400 | -4,898 | +19,297 | +608 | +0 | -18,370 | -5,692 | -9,720 | +0 | +0 | -7,968 | +71,145 |
| sum | +202,472 | +397,330 | +24,622 | +49,562 | -26,722 | +0 | -29,555 | +24,447 | -5,922 | +0 | +720 | +28,016 | +664,970 |
forward days: previous-day weighted book x scale x settlement move per strategy, the rest in trading; total foots to live gross. Live-window sums: 'Per strategy' above; full series: data/per_strategy_daily.csv (attributed)

## Per strategy gap by day, last 10 reconciled days (live attributed - expected, CNY)
| day | ks_branch | fund_v3 | china_pairs | ks_ext | chem_fund | agri_event | stat_arb | fpe | ks_outright | total |
|---|---|---|---|---|---|---|---|---|---|---|
| 2026-11-11 | +13,352 | -41,720 | +892 | -9,048 | -22,582 | +0 | -5,842 | +0 | +0 | -64,948 |
| 2026-11-12 | +26,396 | +1,299 | +390 | -855 | +18,465 | +0 | +840 | +17,117 | +5,348 | +69,000 |
| 2026-11-13 | -40,452 | +8,720 | +2,962 | -7,659 | -14,955 | +0 | +4,729 | -14,154 | -4,085 | -64,893 |
| 2026-11-16 | +32,344 | -15,894 | -248 | +2,479 | +13,995 | +0 | -12,710 | +440 | +1,990 | +22,396 |
| 2026-11-17 | -26,696 | -22,456 | -5,460 | -224 | +4,868 | +0 | +8,546 | -7,176 | -252 | -48,850 |
| 2026-11-18 | -1,864 | +30,364 | +8,272 | +3,881 | -11,250 | +0 | +875 | +887 | +5,092 | +36,258 |
| 2026-11-19 | +11,768 | -56,964 | -1,770 | -1,804 | +13,560 | +0 | +10,834 | -837 | -7,542 | -32,755 |
| 2026-11-20 | +8,180 | +5,493 | -5,160 | +22,800 | -4,792 | +0 | -7,820 | +25,556 | +4,528 | +48,784 |
| 2026-11-23 | -32,832 | +30,029 | +3,195 | -51,547 | -6,188 | +0 | +2,566 | -4,402 | -310 | -59,488 |
| 2026-11-24 | +39,388 | +360 | -13,252 | +37,555 | +1,582 | +0 | - | -13,806 | -4,510 | +47,317 |
| sum | +29,584 | -60,769 | -10,178 | -4,421 | -7,298 | +0 | +2,018 | +3,626 | +258 | -47,180 |
full series: data/per_strategy_daily.csv (day, strategy, expected, attributed, gap); a strategy's daily total foots to expected - live_gross once the shared, neither and trading buckets are added. '-' = that sleeve's backtest row has not shipped yet (BT PENDING).

## Live P&L by product, last 10 reconciled days (gross CNY, worst first)
| product | 11-11 | 11-12 | 11-13 | 11-16 | 11-17 | 11-18 | 11-19 | 11-20 | 11-23 | 11-24 | 10d sum | live window |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| a | +3,830 | +140 | -5,620 | -23,390 | -8,070 | -1,250 | +3,870 | -8,990 | -290 | +730 | -39,040 | -33,600 |
| pp | -560 | +9,640 | +13,050 | -85 | -12,865 | -10,520 | -22,405 | +7,430 | -15,085 | -5,645 | -37,045 | -140,520 |
| fu | -2,080 | +2,360 | +5,420 | +5,710 | -21,360 | -70 | -5,340 | -7,860 | -4,630 | -3,370 | -31,220 | +26,930 |
| eb | +745 | +2,810 | +5,685 | +2,310 | -12,620 | -8,020 | -5,980 | -2,370 | -8,030 | -3,980 | -29,450 | -11,210 |
| y | +8,330 | +4,870 | +2,490 | +1,830 | -16,100 | -9,510 | -8,910 | -2,840 | -20 | +3,160 | -16,700 | -139,950 |
| sp | -5,860 | +2,020 | +760 | +5,880 | -5,400 | +60 | +9,920 | +1,520 | -1,940 | -18,640 | -11,680 | +21,680 |
| eg | -1,800 | -3,920 | -3,870 | +370 | -660 | +2,880 | -800 | +190 | +520 | -2,620 | -9,710 | +43,400 |
| c | -5,180 | -2,210 | -4,200 | +1,030 | +1,790 | +1,170 | +1,830 | -250 | -4,380 | +2,620 | -7,780 | -34,410 |
| m | -7,690 | +6,060 | -3,220 | +670 | +8,660 | -1,500 | -4,230 | -1,470 | -3,200 | -320 | -6,240 | +3,630 |
| SF | -670 | +1,720 | -6,230 | -3,820 | +8,830 | +420 | +3,090 | -5,260 | +3,590 | -7,160 | -5,490 | +22,990 |
| jm | +0 | +0 | +0 | +0 | -2,520 | +30,450 | +10,560 | -24,420 | +2,310 | -20,790 | -4,410 | -4,410 |
| RM | -1,990 | -110 | -960 | +790 | +1,700 | -740 | +10 | +520 | -700 | -2,790 | -4,270 | +14,870 |
| TA | +140 | +930 | +2,300 | +180 | -3,060 | -2,350 | +1,840 | -5,570 | +1,220 | +640 | -3,730 | -78,350 |
| lh | -880 | -240 | -2,480 | +80 | +4,160 | +2,240 | +560 | -480 | -4,800 | -1,760 | -3,600 | +20,400 |
| OI | -7,840 | +2,180 | +3,960 | -470 | -9,660 | +2,370 | -3,540 | +1,000 | -1,840 | +10,370 | -3,470 | -21,930 |
| other (29) | +38,710 | +2,445 | +23,885 | -14,425 | -26,315 | +25,390 | +64,190 | +28,235 | +23,340 | +39,825 | +205,280 | +429,410 |
| IH | -720 | -60 | +1,080 | +960 | -3,120 | +5,040 | +3,780 | +25,140 | -6,960 | +5,940 | +31,080 | +106,980 |
| SR | +4,590 | +1,600 | +340 | +2,170 | -5,280 | +28,720 | -10,760 | -8,520 | -2,120 | +27,800 | +38,540 | +112,120 |
| pb | +3,600 | +2,600 | -1,125 | -4,000 | +2,450 | +3,250 | +3,675 | +10,450 | +12,300 | +10,425 | +43,625 | +79,950 |
| ni | +5,880 | -4,020 | -830 | +10,800 | +5,010 | -22,400 | +26,870 | +18,860 | +1,960 | +2,630 | +44,760 | +13,790 |
| pg | -260 | +400 | +140 | -3,080 | +13,420 | +2,440 | +13,360 | +4,200 | +19,440 | -3,460 | +46,600 | +5,860 |
| i | +5,100 | +8,750 | +7,350 | +40,900 | +34,300 | +2,700 | -9,050 | -23,450 | +15,200 | -19,550 | +62,250 | +48,050 |
| cu | +8,600 | +1,150 | +5,900 | +23,800 | +2,300 | +18,200 | +21,600 | -7,700 | -9,700 | +7,800 | +71,950 | +70,700 |
| hc | +1,710 | +9,190 | -1,820 | +11,350 | +47,900 | +12,830 | -6,590 | -5,010 | -6,030 | +10,100 | +73,630 | -60,810 |
| cs | +22,430 | +8,100 | +9,940 | +5,590 | +7,700 | +1,990 | +5,300 | +5,310 | +14,940 | +9,340 | +90,640 | +195,480 |
| al | +20,050 | +40,400 | +38,150 | +37,725 | +14,175 | -42,900 | -4,400 | +2,300 | +35,100 | +29,850 | +170,450 | +337,650 |
| all products | +88,185 | +96,805 | +90,095 | +102,875 | +25,365 | +40,890 | +88,450 | +965 | +60,195 | +71,145 | +664,970 | +1,028,700 |
executor total_pnl (holding + trading, settlement-to-settlement once the next capture lands, before fees) summed by product root; 'all products' foots to live gross. Full series: data/product_daily.csv

## Worst (strategy, product) cells, last 10 reconciled days (attributed gross CNY)
| strategy | product | 11-11 | 11-12 | 11-13 | 11-16 | 11-17 | 11-18 | 11-19 | 11-20 | 11-23 | 11-24 | sum |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| china_pairs | rb | +6,120 | -9,600 | +2,400 | -13,200 | -52,800 | -13,650 | +20,475 | +15,540 | +8,925 | -17,850 | -53,640 |
| china_pairs | pp | -742 | +7,155 | +8,032 | +270 | -15,060 | -5,460 | -13,860 | +4,620 | -10,920 | -6,720 | -32,685 |
| ks_branch | cu | +0 | +0 | +3,120 | +3,720 | +4,440 | -6,120 | -6,840 | -3,320 | -24,320 | -1,160 | -30,480 |
| stat_arb | l | -850 | +630 | +2,250 | +480 | -7,110 | -2,910 | -13,455 | +4,095 | -5,135 | -7,050 | -29,055 |
| fpe | sn | +0 | +858 | +99 | -2,500 | +1,782 | -7,820 | -11,308 | -11,550 | -1,076 | +4,338 | -27,177 |
| china_pairs | y | +6,600 | +5,280 | +720 | +1,155 | -13,545 | -10,440 | -9,180 | -2,355 | -615 | +1,140 | -21,240 |
| fund_v3 | c | -4,980 | -1,260 | -3,020 | +120 | -1,280 | +920 | -280 | -2,200 | -6,460 | -120 | -18,560 |
| fund_v3 | eb | +1,020 | +3,810 | +6,390 | +3,080 | -8,970 | -6,780 | -3,910 | -2,160 | -6,560 | -3,250 | -17,330 |
| fund_v3 | p | +6,920 | +4,960 | +1,760 | +3,440 | -9,940 | -10,040 | -9,240 | -840 | -7,160 | +3,480 | -16,660 |
| stat_arb | fu | +530 | -1,120 | -750 | +1,160 | -5,790 | -230 | -2,160 | -2,820 | -2,060 | -2,220 | -15,460 |
| ks_branch | a | +3,016 | -1,512 | -2,392 | -7,472 | -1,920 | -352 | +224 | -896 | -480 | -48 | -11,832 |
| stat_arb | a | +800 | +540 | -1,380 | -7,320 | -3,050 | -300 | +1,380 | -2,200 | +0 | -40 | -11,570 |
| stat_arb | ss | -2,550 | -600 | +400 | -525 | -125 | +4,875 | -6,625 | -3,125 | -2,250 | -500 | -11,025 |
| fund_v3 | OI | -3,280 | -3,260 | +1,840 | +180 | -4,800 | -120 | +0 | -560 | +280 | -1,020 | -10,740 |
| fpe | cu | +0 | +1,260 | +1,050 | +9,595 | -1,235 | +14,630 | -20,700 | -9,900 | -5,250 | +40 | -10,510 |
same holdings split as 'Live P&L by strategy'; summing a strategy's products reproduces its row there (trading / neither included as their own strategy). Full series: data/strategy_product_daily.csv

## Paper strategies (weight 0 in the forward book: tracked, not traded)
| strategy | weight 0 since | bt since (full) | bt last 20d | drawdown now | worst before pause | 60d Sharpe | paper-live since (full) | paper days | book coverage |
|---|---|---|---|---|---|---|---|---|---|
| agri_event | 2026-11-02 | -74,495 | -88,620 | -216,825 | -148,545 | -3.50 | -68,210 | 16 | 100% |
paper-live = the strategy's own pinned full-size book of D-1 x the settlement-to-settlement move of D, priced like the live attribution, on contracts the day's state capture marks (coverage). Re-entry: owner's call, at an attended morning merge; reweighting is Execution/weights_forward.json + weights_changelog.csv.

## Backtest vintages (full series kept on every restatement)
expected on the CURRENT series minus expected on the as-shipped pins, live window, weighted CNY (the bridge uses the pins):
| strategy | restated |
|---|---|
| ks_branch | +65,633 |
| fund_v3 | -42,249 |
| china_pairs | -24,878 |
| ks_ext | +6,911 |
| chem_fund | -6,668 |
| agri_event | +10,650 |
| stat_arb | +12,379 |
| all | +21,778 |
| strategy | vintages | latest | cause | commit | rows restated | net change (full size) |
|---|---|---|---|---|---|---|
| ks_branch | 2 | 20261102090932_cbbdd7664522.csv | unknown | cbbdd76 | 165 | +341,255 |
| ks_ext | 2 | 20261102090932_1a03a09367cb.csv | unknown | 1a03a09 | 91 | +31,590 |
| china_pairs | 2 | 20261102090932_51a17747e0e0.csv | unknown | 51a1774 | 44 | -46,815 |
| ks_outright | 1 | 20261111091151_49ac2cfb3881.csv | first | 49ac2cf | 0 | +0 |
| fpe | 1 | 20261111091151_01eab32dfcbf.csv | first | 01eab32 | 0 | +0 |
| stat_arb | 4 | 20261116091117_9f7e9a742805.csv | data | 9f7e9a7 | 3 | -3,932 |
| chem_fund | 4 | 20261117091502_f7a9729c0604.csv | code | f7a9729 | 1 | +170 |
| fund_v3 | 7 | 20261118090511_0712a0472bd7.csv | data | 0712a04 | 1 | +1,950 |
| agri_event | 17 | 20261124091333_8f0b7b90cc1f.csv | data | 8f0b7b9 | 3 | +1,325 |
full series: data/backtest/vintages/<strategy>/; index: data/backtest/vintages/index.csv

## Data health
decision-price coverage (2026-11-24): 100% of held notional benchmarked (0 contract(s) unbenchmarked); 14 contract(s) (16%) first decided after the 0900 snap, so they straddle their own overnight leg
scale: 1 (since 2026-09-09)
regime: forward (merged weighted book) since 2026-08-31; 56 forward day(s), 8 legacy day(s)
merge weights (2026-11-24): ks_branch 0.8, fund_v3 2, china_pairs 1.5, ks_ext 0.25, chem_fund 1.5, agri_event 0, stat_arb 1, fpe 0.1, ks_outright 0.5
as-shipped pins: 64 live day(s) pinned; current series diverges from pins on chem_fund: 30 day(s), max 9,725 CNY, fund_v3: 53 day(s), max 22,683 CNY, ks_branch: 43 day(s), max 82,125 CNY, ks_ext: 35 day(s), max 42,170 CNY, stat_arb: 45 day(s), max 9,982 CNY, china_pairs: 23 day(s), max 10,910 CNY, agri_event: 12 day(s), max 7,250 CNY; standing counts -- a divergence is announced as an alert once, the first run it appears, and kept here afterwards
inbox ks summary mtime: 2026-11-23 05:57 UTC
