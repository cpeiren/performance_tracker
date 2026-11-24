# Performance tracker - 2026-11-23   (reconciled through 2026-11-23)

## ALERTS
- VINTAGE agri_event: 5 historical row(s) restated (net -1,250 CNY, cause data, commit 8f0b7b9) -- kept as vintages/agri_event/20261123091013_8f0b7b90cc1f.csv; the bridge keeps the as-shipped pins
- WEIGHTS 2026-10-09: day's own merge weights not shipped yet -- carried forward from an earlier day.
- WEIGHTS 2026-10-16: day's own merge weights not shipped yet -- carried forward from an earlier day.
- WEIGHTS 2026-10-22: day's own merge weights not shipped yet -- carried forward from an earlier day.
- BT PENDING 2026-11-23: no mature backtest row for stat_arb (nonzero weight) -- day reconciled WITHOUT that sleeve's expected; its live P&L sits in bt_pending_live, not resid, until the rows ship.
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
- BACKTEST REVISED: agri_event -- 3 mature row(s) changed since last run (net -325 CNY, largest 2026-05-07 -17315 -> -17715; first 2026-02-06, last 2026-05-07). Regeneration upstream; baseline re-set.
- SLIPPAGE 2026-11-23: 3 unbenchmarked leg(s), +48 CNY exec cost without a shipped decision price.
- RESIDUAL 2026-08-27: -17267 CNY vs trailing median |resid| 2062, offset by neither neighbour (2026-08-26 +3749, 2026-08-31 -17348) -- attribution quality changed. (A break-out that a neighbouring day mirrors is the backtest/live day-window straddle and is not alerted.)
- RESIDUAL 2026-08-31: -17348 CNY vs trailing median |resid| 2277, offset by neither neighbour (2026-08-27 -17267, 2026-09-01 -8190) -- attribution quality changed. (A break-out that a neighbouring day mirrors is the backtest/live day-window straddle and is not alerted.)
- RESIDUAL 2026-09-01: -8190 CNY vs trailing median |resid| 2492, offset by neither neighbour (2026-08-31 -17348, 2026-09-02 -30063) -- attribution quality changed. (A break-out that a neighbouring day mirrors is the backtest/live day-window straddle and is not alerted.)
- RESIDUAL 2026-09-02: -30063 CNY vs trailing median |resid| 3121, offset by neither neighbour (2026-09-01 -8190, 2026-09-03 -29049) -- attribution quality changed. (A break-out that a neighbouring day mirrors is the backtest/live day-window straddle and is not alerted.)
- RESIDUAL 2026-09-03: -29049 CNY vs trailing median |resid| 3941, offset by neither neighbour (2026-09-02 -30063, 2026-09-04 -5584) -- attribution quality changed. (A break-out that a neighbouring day mirrors is the backtest/live day-window straddle and is not alerted.)
- RESIDUAL 2026-09-16: -103509 CNY vs trailing median |resid| 22936, offset by neither neighbour (2026-09-15 -28634, 2026-09-17 +23811) -- attribution quality changed. (A break-out that a neighbouring day mirrors is the backtest/live day-window straddle and is not alerted.)
- RESIDUAL 2026-10-26: +29017 CNY vs trailing median |resid| 7638, offset by neither neighbour (2026-10-23 +7825, 2026-10-27 +81673) -- attribution quality changed. (A break-out that a neighbouring day mirrors is the backtest/live day-window straddle and is not alerted.)
- RESIDUAL 2026-10-27: +81673 CNY vs trailing median |resid| 9046, offset by neither neighbour (2026-10-26 +29017, 2026-10-28 +2573) -- attribution quality changed. (A break-out that a neighbouring day mirrors is the backtest/live day-window straddle and is not alerted.)

## Latest reconciled day (2026-11-23, forward regime, PROVISIONAL: marked at the 16:00 close, re-marked to settlement after the next capture)
live gross +89,025 | expected (1 x bt +122,661) = +122,661 | gap -33,636
  exec_cost -4,722 (slip -4,770, unbench +48) | marking -54,650 | bookdiff +0 (carry +0, new +0) | intraday +0 | offbook +0 (0 contract(s)) | residual +14,517 (live re-marked to first decision, vs the previous backtest row)
  PARTIAL: no backtest row yet for stat_arb -- expected excludes it; its live P&L +1,775 is held out of resid
  fees +824 | broker residual +0 -> live net +88,201

## Cumulative bridge (live since 2026-08-18, 63 reconciled days, 1 with a sleeve's backtest pending)
| expected | -exec | +marking | +bookdiff | +intraday | +offbook | +bt pending | +resid | = live gross | -fees | +broker_resid | = live net |
|---|---|---|---|---|---|---|---|---|---|---|---|
| +978,347 | -89,352 | +23,955 | +90,047 | -6,568 | -50 | +1,775 | -11,769 | +986,385 | -65,684 | +11,199 | +931,900 |
missing live days excluded: 2026-08-28 (expected +4,849 held in bucket)

## Stats (daily CNY pnl)
| window | days | total | sharpe | mdd | hit |
|---|---|---|---|---|---|
| live net live-to-date | 63 | +931,900 | 4.06 | -330,281 | 59% |
| live net last-20d | 20 | +360,973 | 4.57 | -267,933 | 55% | (small sample)
| live net 2026-YTD | 63 | +931,900 | 4.06 | -330,281 | 59% |
| bt scaled live-to-date | 63 | +978,347 | 3.80 | -381,526 | 67% |
| bt scaled last-20d | 20 | +348,548 | 3.34 | -258,267 | 60% | (small sample)
| bt scaled 2026-YTD | 63 | +978,347 | 3.80 | -381,526 | 67% |

## Slippage (+ = cost; bps vs benchmarked notional)
| day | lots | notional M | slip total | drift | exec | bps | unbench legs | unbench CNY |
|---|---|---|---|---|---|---|---|---|
| 2026-11-10 | 484 | 26.2 | +1,890 | +445 | +1,445 | +0.75 | 2 | +118 |
| 2026-11-11 | 445 | 37.7 | -5,640 | -6,922 | +1,282 | -1.52 | 3 | +50 |
| 2026-11-12 | 508 | 31.3 | +3,550 | +2,372 | +1,178 | +1.15 | 2 | -100 |
| 2026-11-13 | 504 | 35.5 | +2,085 | -325 | +2,410 | +0.62 | 5 | +228 |
| 2026-11-16 | 540 | 42.9 | +14,910 | +13,128 | +1,782 | +3.92 | 8 | +28 |
| 2026-11-17 | 436 | 22.5 | -3,665 | -7,090 | +3,425 | -1.67 | 4 | -48 |
| 2026-11-18 | 689 | 27.1 | -5,590 | -6,510 | +920 | -2.45 | 3 | +1,895 |
| 2026-11-19 | 504 | 26.6 | -12,410 | -12,082 | -328 | -4.71 | 2 | +55 |
| 2026-11-20 | 485 | 23.4 | +18,405 | +17,610 | +795 | +7.95 | 2 | -25 |
| 2026-11-23 | 297 | 17.1 | -4,770 | -4,665 | -105 | -2.83 | 3 | +48 |
| live window (63d) | 24865 | 1521.5 | +71,535 | -3,015 | +74,550 | +0.50 | 285 | +17,818 |
exec-only bps over the window: +0.52; benchmark coverage 93% of traded notional

| product | days | lots | notional M | drift | exec (incl. unbench) | all-in | bps |
|---|---|---|---|---|---|---|---|
| pg | 32 | 61 | 8.1 | +22,770 | +170 | +22,940 | +28.41 |
| IH | 41 | 164 | 136.0 | -27,630 | +5,790 | -21,840 | -1.61 |
| IF | 25 | 86 | 109.3 | -20,340 | +3,300 | -17,040 | -1.56 |
| CY | 46 | 346 | 37.9 | +10,838 | +6,088 | +16,925 | +4.47 |
| rb | 52 | 2053 | 62.8 | +14,620 | +2,245 | +16,865 | +2.69 |
| zn | 48 | 517 | 66.7 | -16,525 | +1,362 | -15,162 | -2.27 |
| al | 50 | 752 | 87.1 | +11,650 | +3,000 | +14,650 | +1.68 |
| y | 53 | 380 | 33.5 | +11,535 | +2,545 | +14,080 | +4.21 |
| hc | 55 | 2070 | 67.4 | -18,160 | +5,700 | -12,460 | -1.85 |
| bu | 55 | 624 | 29.3 | -13,790 | +1,505 | -12,285 | -4.19 |
| SA | 59 | 1010 | 20.2 | +8,430 | +3,830 | +12,260 | +6.07 |
| SF | 56 | 594 | 17.7 | +8,835 | +1,010 | +9,845 | +5.56 |
| pb | 51 | 1112 | 89.0 | +2,938 | +5,088 | +8,025 | +0.90 |
| FG | 62 | 1238 | 22.3 | +1,080 | +6,880 | +7,960 | +3.56 |
| a | 58 | 684 | 35.9 | +4,045 | +3,440 | +7,485 | +2.08 |
| other (39) | - | 13174 | 698.3 | -3,310 | +40,415 | +37,105 | +0.53 |
| all products | - | 24865 | 1521.5 | -3,015 | +92,368 | +89,352 | +0.59 |
ranked by |all-in| over the live window (all-in = drift + exec = the bridge's exec_cost by product); product bps are vs traded notional

## Per strategy
| strategy | live? | bt 2026 pnl (full) | bt scaled+weighted (live window) | live attributed | note |
|---|---|---|---|---|---|
| Calendar main pool (branch) | yes | +1,225,500 | +178,256 | +212,831 | forward w=0.8 |
| Fundamental factor | yes | +1,001,296 | +735,646 | +695,195 | forward w=2 |
| Cross-product pairs | yes | +95,430 | +57,046 | +29,433 | forward w=1.5 |
| Calendar extended pool | yes | +767,230 | +82,573 | +108,395 | forward w=0.25 |
| Chemical fundamental | yes | +488,005 | +11,088 | -47,517 | forward w=1.5 |
| Agriculture event-driven | no | -36,205 | -111,243 | -152,798 | forward w=0 (parked) |
| Factor-neutral stat arb | yes | +319,371 | +13,244 | +41,728 | forward w=1 |
| Fund pipeline ensemble | yes | +2,293,856 | +12,707 | +43,398 | forward w=0.1 |
| Outright trend + basis | yes | +513,490 | -970 | -4,465 | forward w=0.5 |
| shared bucket | - | - | - | +3,575 | legacy days only: a contract both per-source books held |
| neither bucket (no target) | - | - | - | +3,050 | named by no book that day or the day before |
| trading bucket | - | - | - | +53,560 | forward days: live P&L minus the strategies' holdings (fills vs settlement on rebalances, lot rounding, scale changes) |
forward days: each strategy is its own previous-day weighted book x scale x the settlement-to-settlement move (holdings); legacy days remain exclusive-holder. The gap tables (attributed - expected) therefore exclude execution, which sits in trading.

## Live P&L by strategy, last 10 reconciled days (attributed gross CNY)
| day | ks_branch | fund_v3 | china_pairs | ks_ext | chem_fund | agri_event | stat_arb | fpe | ks_outright | shared | neither | trading | total |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 2026-11-10 | +10,060 | +60,290 | -5,542 | +4,261 | -39,090 | +0 | -8,585 | +0 | +0 | +0 | +0 | +1,881 | +23,275 |
| 2026-11-11 | -48 | +81,680 | +7,920 | -1,788 | -14,685 | +0 | +7,710 | +0 | +0 | +0 | +0 | +7,396 | +88,185 |
| 2026-11-12 | +57,280 | +15,540 | -5,798 | -3,425 | +975 | +0 | -5,505 | +30,757 | +8,365 | +0 | +255 | -1,640 | +96,805 |
| 2026-11-13 | +25,720 | +17,270 | +1,598 | -6,845 | -652 | +0 | +5,150 | +20,356 | +14,980 | +0 | +0 | +12,519 | +90,095 |
| 2026-11-16 | +42,372 | +44,060 | -4,905 | +3,780 | +9,698 | +0 | -9,495 | +21,178 | +3,188 | +0 | +0 | -7,000 | +102,875 |
| 2026-11-17 | +40,840 | +8,880 | -6,218 | -1,909 | -3,375 | +0 | -13,180 | +12,305 | -15,038 | +0 | +0 | +3,059 | +25,365 |
| 2026-11-18 | -42,252 | +43,890 | +8,482 | +6,179 | -2,985 | +0 | +4,010 | +14,961 | -5,422 | +0 | +0 | +14,027 | +40,890 |
| 2026-11-19 | +1,716 | +131,140 | +22,200 | +7,641 | -17,880 | +0 | -5,440 | -58,952 | -6,205 | +0 | +0 | +14,230 | +88,450 |
| 2026-11-20 | +10,400 | -24,460 | +11,348 | +35,759 | +1,958 | +0 | +4,215 | -37,628 | +3,755 | +0 | +0 | -4,381 | +965 |
| 2026-11-23 | +35,396 | +39,740 | -5,820 | -137 | -1,560 | +0 | +1,775 | +40,422 | -8,087 | +0 | +465 | -13,168 | +89,025 |
| sum | +181,484 | +418,030 | +23,265 | +43,516 | -67,598 | +0 | -19,345 | +43,398 | -4,465 | +0 | +720 | +26,925 | +645,930 |
forward days: previous-day weighted book x scale x settlement move per strategy, the rest in trading; total foots to live gross. Live-window sums: 'Per strategy' above; full series: data/per_strategy_daily.csv (attributed)

## Per strategy gap by day, last 10 reconciled days (live attributed - expected, CNY)
| day | ks_branch | fund_v3 | china_pairs | ks_ext | chem_fund | agri_event | stat_arb | fpe | ks_outright | total |
|---|---|---|---|---|---|---|---|---|---|---|
| 2026-11-10 | -18,696 | +40,476 | +870 | -1,682 | -10,462 | +0 | -3,516 | +0 | +0 | +6,989 |
| 2026-11-11 | +13,352 | -41,720 | +892 | -9,048 | -22,582 | +0 | -5,842 | +0 | +0 | -64,948 |
| 2026-11-12 | +26,396 | +1,299 | +390 | -855 | +18,465 | +0 | +840 | +17,117 | +5,348 | +69,000 |
| 2026-11-13 | -40,452 | +8,720 | +2,962 | -7,659 | -14,955 | +0 | +4,729 | -14,154 | -4,085 | -64,893 |
| 2026-11-16 | +32,344 | -15,894 | -248 | +2,479 | +13,995 | +0 | -12,710 | +440 | +1,990 | +22,396 |
| 2026-11-17 | -26,696 | -22,456 | -5,460 | -224 | +4,868 | +0 | +8,546 | -7,176 | -252 | -48,850 |
| 2026-11-18 | -1,864 | +30,364 | +8,272 | +3,881 | -11,250 | +0 | +875 | +887 | +5,092 | +36,258 |
| 2026-11-19 | +11,768 | -56,964 | -1,770 | -1,804 | +13,560 | +0 | +10,834 | -837 | -7,542 | -32,755 |
| 2026-11-20 | +8,180 | +5,493 | -5,160 | +22,800 | -4,792 | +0 | -7,820 | +25,556 | +4,528 | +48,784 |
| 2026-11-23 | -4,392 | +28,839 | +2,482 | -42,557 | -7,365 | +0 | - | +8,857 | -8,572 | -22,708 |
| sum | -60 | -21,842 | +3,232 | -34,669 | -20,520 | +0 | -4,065 | +30,691 | -3,495 | -50,728 |
full series: data/per_strategy_daily.csv (day, strategy, expected, attributed, gap); a strategy's daily total foots to expected - live_gross once the shared, neither and trading buckets are added. '-' = that sleeve's backtest row has not shipped yet (BT PENDING).

## Live P&L by product, last 10 reconciled days (gross CNY, worst first)
| product | 11-10 | 11-11 | 11-12 | 11-13 | 11-16 | 11-17 | 11-18 | 11-19 | 11-20 | 11-23 | 10d sum | live window |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| pp | -37,895 | -560 | +9,640 | +13,050 | -85 | -12,865 | -10,520 | -22,405 | +7,430 | -20,920 | -75,130 | -140,710 |
| a | +1,700 | +3,830 | +140 | -5,620 | -23,390 | -8,070 | -1,250 | +3,870 | -8,990 | +1,890 | -35,890 | -32,150 |
| eb | -6,390 | +745 | +2,810 | +5,685 | +2,310 | -12,620 | -8,020 | -5,980 | -2,370 | -10,620 | -34,450 | -9,820 |
| fu | -2,650 | -2,080 | +2,360 | +5,420 | +5,710 | -21,360 | -70 | -5,340 | -7,860 | -3,470 | -29,340 | +31,460 |
| y | -1,200 | +8,330 | +4,870 | +2,490 | +1,830 | -16,100 | -9,510 | -8,910 | -2,840 | +80 | -20,960 | -143,010 |
| c | -13,550 | -5,180 | -2,210 | -4,200 | +1,030 | +1,790 | +1,170 | +1,830 | -250 | -1,140 | -20,710 | -33,790 |
| OI | +260 | -7,840 | +2,180 | +3,960 | -470 | -9,660 | +2,370 | -3,540 | +1,000 | -1,640 | -13,380 | -32,100 |
| TA | -10,140 | +140 | +930 | +2,300 | +180 | -3,060 | -2,350 | +1,840 | -5,570 | +4,460 | -11,270 | -75,750 |
| MA | -4,400 | +1,240 | +1,950 | +2,220 | +1,350 | -910 | -1,560 | -5,040 | +1,300 | -3,220 | -7,070 | +1,570 |
| SF | -4,940 | -670 | +1,720 | -6,230 | -3,820 | +8,830 | +420 | +3,090 | -5,260 | +1,280 | -5,580 | +27,840 |
| eg | +3,920 | -1,800 | -3,920 | -3,870 | +370 | -660 | +2,880 | -800 | +190 | -1,190 | -4,880 | +44,310 |
| lh | +0 | -880 | -240 | -2,480 | +80 | +4,160 | +2,240 | +560 | -480 | -7,840 | -4,880 | +19,120 |
| bu | -3,480 | -2,270 | +890 | +820 | +240 | -4,090 | -1,790 | -540 | +1,940 | +3,430 | -4,850 | -42,700 |
| sn | -60 | -2,960 | +3,300 | +5,590 | +8,270 | +10,890 | -5,320 | -3,760 | -19,540 | +1,120 | -2,470 | +31,220 |
| RM | +1,210 | -1,990 | -110 | -960 | +790 | +1,700 | -740 | +10 | +520 | -1,610 | -1,180 | +16,750 |
| other (29) | +13,845 | +38,765 | +11,625 | +26,055 | -9,540 | -51,915 | +80,475 | +59,980 | +9,015 | +24,150 | +202,455 | +492,625 |
| IH | -1,620 | -720 | -60 | +1,080 | +960 | -3,120 | +5,040 | +3,780 | +25,140 | -240 | +30,240 | +107,760 |
| pb | +2,850 | +3,600 | +2,600 | -1,125 | -4,000 | +2,450 | +3,250 | +3,675 | +10,450 | +14,000 | +37,750 | +71,225 |
| ni | +3,290 | +5,880 | -4,020 | -830 | +10,800 | +5,010 | -22,400 | +26,870 | +18,860 | -1,150 | +42,310 | +8,050 |
| v | +15,230 | -5,025 | -5,640 | -12,920 | -6,025 | +15,170 | +11,315 | +19,040 | +2,630 | +12,025 | +45,800 | +70,955 |
| pg | +8,740 | -260 | +400 | +140 | -3,080 | +13,420 | +2,440 | +13,360 | +4,200 | +14,000 | +53,360 | +3,880 |
| cu | -5,300 | +8,600 | +1,150 | +5,900 | +23,800 | +2,300 | +18,200 | +21,600 | -7,700 | -12,000 | +56,550 | +60,600 |
| i | -3,550 | +5,100 | +8,750 | +7,350 | +40,900 | +34,300 | +2,700 | -9,050 | -23,450 | +9,500 | +72,550 | +61,900 |
| hc | +7,780 | +1,710 | +9,190 | -1,820 | +11,350 | +47,900 | +12,830 | -6,590 | -5,010 | +2,430 | +79,770 | -62,450 |
| cs | +23,800 | +22,430 | +8,100 | +9,940 | +5,590 | +7,700 | +1,990 | +5,300 | +5,310 | +11,750 | +101,910 | +182,950 |
| al | +35,825 | +20,050 | +40,400 | +38,150 | +37,725 | +14,175 | -42,900 | -4,400 | +2,300 | +53,950 | +195,275 | +326,650 |
| all products | +23,275 | +88,185 | +96,805 | +90,095 | +102,875 | +25,365 | +40,890 | +88,450 | +965 | +89,025 | +645,930 | +986,385 |
executor total_pnl (holding + trading, settlement-to-settlement once the next capture lands, before fees) summed by product root; 'all products' foots to live gross. Full series: data/product_daily.csv

## Worst (strategy, product) cells, last 10 reconciled days (attributed gross CNY)
| strategy | product | 11-10 | 11-11 | 11-12 | 11-13 | 11-16 | 11-17 | 11-18 | 11-19 | 11-20 | 11-23 | sum |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| china_pairs | pp | -30,772 | -742 | +7,155 | +8,032 | +270 | -15,060 | -5,460 | -13,860 | +4,620 | -15,600 | -61,418 |
| china_pairs | rb | -3,870 | +6,120 | -9,600 | +2,400 | -13,200 | -52,800 | -13,650 | +20,475 | +15,540 | +3,675 | -44,910 |
| fund_v3 | SR | +3,620 | +1,680 | -440 | -760 | -4,080 | -14,000 | +22,360 | -11,280 | -19,920 | -9,520 | -32,340 |
| stat_arb | l | -7,275 | -850 | +630 | +2,250 | +480 | -7,110 | -2,910 | -13,455 | +4,095 | -7,930 | -32,075 |
| ks_branch | cu | +0 | +0 | +0 | +3,120 | +3,720 | +4,440 | -6,120 | -6,840 | -3,320 | -26,080 | -31,080 |
| fund_v3 | c | -11,520 | -4,980 | -1,260 | -3,020 | +120 | -1,280 | +920 | -280 | -2,200 | -5,920 | -29,420 |
| fpe | sn | +0 | +0 | +858 | +99 | -2,500 | +1,782 | -7,820 | -11,308 | -11,550 | +1,973 | -28,466 |
| fund_v3 | eb | -9,570 | +1,020 | +3,810 | +6,390 | +3,080 | -8,970 | -6,780 | -3,910 | -2,160 | -8,620 | -25,710 |
| chem_fund | pp | -16,830 | +1,530 | +3,330 | +7,110 | +2,175 | -2,640 | -3,788 | -10,778 | +3,232 | -7,665 | -24,322 |
| china_pairs | y | -240 | +6,600 | +5,280 | +720 | +1,155 | -13,545 | -10,440 | -9,180 | -2,355 | -510 | -22,515 |
| fund_v3 | p | -1,620 | +6,920 | +4,960 | +1,760 | +3,440 | -9,940 | -10,040 | -9,240 | -840 | -7,320 | -21,920 |
| stat_arb | ss | -7,175 | -2,550 | -600 | +400 | -525 | -125 | +4,875 | -6,625 | -3,125 | -2,125 | -17,575 |
| fund_v3 | FG | -13,320 | +4,120 | -1,280 | +15,560 | -4,480 | -12,960 | +8,320 | +4,200 | -7,600 | -9,920 | -17,360 |
| trading | cu | +0 | +2,100 | -1,010 | +730 | +385 | +395 | -5,710 | +3,140 | -14,280 | -2,030 | -16,280 |
| stat_arb | p | -2,640 | +8,460 | +1,490 | +1,890 | +340 | -4,350 | -1,740 | -9,840 | -1,920 | -6,200 | -14,510 |
same holdings split as 'Live P&L by strategy'; summing a strategy's products reproduces its row there (trading / neither included as their own strategy). Full series: data/strategy_product_daily.csv

## Paper strategies (weight 0 in the forward book: tracked, not traded)
| strategy | weight 0 since | bt since (full) | bt last 20d | drawdown now | worst before pause | 60d Sharpe | paper-live since (full) | paper days | book coverage |
|---|---|---|---|---|---|---|---|---|---|
| agri_event | 2026-11-02 | -78,545 | -140,555 | -221,800 | -149,470 | -3.24 | -74,930 | 15 | 100% |
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
| agri_event | +9,725 |
| stat_arb | +12,379 |
| all | +20,853 |
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
| agri_event | 16 | 20261123091013_8f0b7b90cc1f.csv | data | 8f0b7b9 | 5 | -1,250 |
full series: data/backtest/vintages/<strategy>/; index: data/backtest/vintages/index.csv

## Data health
decision-price coverage (2026-11-23): 100% of held notional benchmarked (0 contract(s) unbenchmarked); 14 contract(s) (20%) first decided after the 0900 snap, so they straddle their own overnight leg
scale: 1 (since 2026-09-09)
regime: forward (merged weighted book) since 2026-08-31; 55 forward day(s), 8 legacy day(s)
merge weights (2026-11-23): ks_branch 0.8, fund_v3 2, china_pairs 1.5, ks_ext 0.25, chem_fund 1.5, agri_event 0, stat_arb 1, fpe 0.1, ks_outright 0.5
as-shipped pins: 63 live day(s) pinned; current series diverges from pins on chem_fund: 30 day(s), max 9,725 CNY, fund_v3: 53 day(s), max 22,683 CNY, ks_branch: 43 day(s), max 82,125 CNY, ks_ext: 35 day(s), max 42,170 CNY, stat_arb: 45 day(s), max 9,982 CNY, china_pairs: 23 day(s), max 10,910 CNY, agri_event: 11 day(s), max 7,250 CNY; standing counts -- a divergence is announced as an alert once, the first run it appears, and kept here afterwards
inbox ks summary mtime: 2026-11-23 05:57 UTC
