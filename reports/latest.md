# Performance tracker - 2026-11-20   (reconciled through 2026-11-20)

## ALERTS
- WEIGHTS 2026-10-09: day's own merge weights not shipped yet -- carried forward from an earlier day.
- WEIGHTS 2026-10-16: day's own merge weights not shipped yet -- carried forward from an earlier day.
- WEIGHTS 2026-10-22: day's own merge weights not shipped yet -- carried forward from an earlier day.
- BT PENDING 2026-11-20: no mature backtest row for stat_arb (nonzero weight) -- day reconciled WITHOUT that sleeve's expected; its live P&L sits in bt_pending_live, not resid, until the rows ship.
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
- SLIPPAGE 2026-11-20: 2 unbenchmarked leg(s), -25 CNY exec cost without a shipped decision price.
- RESIDUAL 2026-08-27: -17267 CNY vs trailing median |resid| 2062, offset by neither neighbour (2026-08-26 +3749, 2026-08-31 -17348) -- attribution quality changed. (A break-out that a neighbouring day mirrors is the backtest/live day-window straddle and is not alerted.)
- RESIDUAL 2026-08-31: -17348 CNY vs trailing median |resid| 2277, offset by neither neighbour (2026-08-27 -17267, 2026-09-01 -8190) -- attribution quality changed. (A break-out that a neighbouring day mirrors is the backtest/live day-window straddle and is not alerted.)
- RESIDUAL 2026-09-01: -8190 CNY vs trailing median |resid| 2492, offset by neither neighbour (2026-08-31 -17348, 2026-09-02 -30063) -- attribution quality changed. (A break-out that a neighbouring day mirrors is the backtest/live day-window straddle and is not alerted.)
- RESIDUAL 2026-09-02: -30063 CNY vs trailing median |resid| 3121, offset by neither neighbour (2026-09-01 -8190, 2026-09-03 -29049) -- attribution quality changed. (A break-out that a neighbouring day mirrors is the backtest/live day-window straddle and is not alerted.)
- RESIDUAL 2026-09-03: -29049 CNY vs trailing median |resid| 3941, offset by neither neighbour (2026-09-02 -30063, 2026-09-04 -5584) -- attribution quality changed. (A break-out that a neighbouring day mirrors is the backtest/live day-window straddle and is not alerted.)
- RESIDUAL 2026-09-16: -103509 CNY vs trailing median |resid| 22936, offset by neither neighbour (2026-09-15 -28634, 2026-09-17 +23811) -- attribution quality changed. (A break-out that a neighbouring day mirrors is the backtest/live day-window straddle and is not alerted.)
- RESIDUAL 2026-10-26: +29017 CNY vs trailing median |resid| 7638, offset by neither neighbour (2026-10-23 +7825, 2026-10-27 +81673) -- attribution quality changed. (A break-out that a neighbouring day mirrors is the backtest/live day-window straddle and is not alerted.)
- RESIDUAL 2026-10-27: +81673 CNY vs trailing median |resid| 9046, offset by neither neighbour (2026-10-26 +29017, 2026-10-28 +2573) -- attribution quality changed. (A break-out that a neighbouring day mirrors is the backtest/live day-window straddle and is not alerted.)

## Latest reconciled day (2026-11-20, forward regime, PROVISIONAL: marked at the 16:00 close, re-marked to settlement after the next capture)
live gross +22,065 | expected (1 x bt -55,473) = -55,473 | gap +77,538
  exec_cost +18,380 (slip +18,405, unbench -25) | marking +91,805 | bookdiff +0 (carry +0, new +0) | intraday +0 | offbook +0 (0 contract(s)) | residual +2,363 (live re-marked to first decision, vs the previous backtest row)
  PARTIAL: no backtest row yet for stat_arb -- expected excludes it; its live P&L +1,750 is held out of resid
  fees +1,397 | broker residual +0 -> live net +20,668

## Cumulative bridge (live since 2026-08-18, 62 reconciled days, 1 with a sleeve's backtest pending)
| expected | -exec | +marking | +bookdiff | +intraday | +offbook | +bt pending | +resid | = live gross | -fees | +broker_resid | = live net |
|---|---|---|---|---|---|---|---|---|---|---|---|
| +843,651 | -94,075 | +99,705 | +90,047 | -6,568 | -50 | +1,750 | -16,000 | +918,460 | -64,860 | +11,197 | +864,796 |
missing live days excluded: 2026-08-28 (expected +4,849 held in bucket)

## Stats (daily CNY pnl)
| window | days | total | sharpe | mdd | hit |
|---|---|---|---|---|---|
| live net live-to-date | 62 | +864,796 | 3.85 | -330,281 | 60% |
| live net last-20d | 20 | +296,965 | 3.90 | -308,840 | 60% | (small sample)
| live net 2026-YTD | 62 | +864,796 | 3.85 | -330,281 | 60% |
| bt scaled live-to-date | 62 | +843,651 | 3.37 | -381,526 | 66% |
| bt scaled last-20d | 20 | +219,025 | 2.19 | -373,759 | 60% | (small sample)
| bt scaled 2026-YTD | 62 | +843,651 | 3.37 | -381,526 | 66% |

## Slippage (+ = cost; bps vs benchmarked notional)
| day | lots | notional M | slip total | drift | exec | bps | unbench legs | unbench CNY |
|---|---|---|---|---|---|---|---|---|
| 2026-11-09 | 519 | 27.4 | -5,690 | -6,638 | +948 | -2.09 | 1 | -30 |
| 2026-11-10 | 484 | 26.2 | +1,890 | +445 | +1,445 | +0.75 | 2 | +118 |
| 2026-11-11 | 445 | 37.7 | -5,640 | -6,922 | +1,282 | -1.52 | 3 | +50 |
| 2026-11-12 | 508 | 31.3 | +3,550 | +2,372 | +1,178 | +1.15 | 2 | -100 |
| 2026-11-13 | 504 | 35.5 | +2,085 | -325 | +2,410 | +0.62 | 5 | +228 |
| 2026-11-16 | 540 | 42.9 | +14,910 | +13,128 | +1,782 | +3.92 | 8 | +28 |
| 2026-11-17 | 436 | 22.5 | -3,665 | -7,090 | +3,425 | -1.67 | 4 | -48 |
| 2026-11-18 | 689 | 27.1 | -5,590 | -6,510 | +920 | -2.45 | 3 | +1,895 |
| 2026-11-19 | 504 | 26.6 | -12,410 | -12,082 | -328 | -4.71 | 2 | +55 |
| 2026-11-20 | 485 | 23.4 | +18,405 | +17,610 | +795 | +7.95 | 2 | -25 |
| live window (62d) | 24568 | 1504.4 | +76,305 | +1,650 | +74,655 | +0.54 | 282 | +17,770 |
exec-only bps over the window: +0.53; benchmark coverage 93% of traded notional

| product | days | lots | notional M | drift | exec (incl. unbench) | all-in | bps |
|---|---|---|---|---|---|---|---|
| IH | 40 | 162 | 134.4 | -27,840 | +5,880 | -21,960 | -1.63 |
| pg | 31 | 60 | 8.0 | +21,570 | +150 | +21,720 | +27.25 |
| IF | 25 | 86 | 109.3 | -20,340 | +3,300 | -17,040 | -1.56 |
| CY | 46 | 346 | 37.9 | +10,838 | +6,088 | +16,925 | +4.47 |
| rb | 51 | 2031 | 62.1 | +13,680 | +2,295 | +15,975 | +2.57 |
| al | 49 | 750 | 86.9 | +12,625 | +2,975 | +15,600 | +1.80 |
| y | 52 | 376 | 33.2 | +11,675 | +2,465 | +14,140 | +4.26 |
| hc | 54 | 2065 | 67.3 | -18,255 | +5,715 | -12,540 | -1.86 |
| bu | 54 | 619 | 29.1 | -13,750 | +1,545 | -12,205 | -4.20 |
| SA | 58 | 995 | 19.9 | +8,000 | +3,860 | +11,860 | +5.95 |
| SF | 55 | 592 | 17.6 | +8,865 | +980 | +9,845 | +5.58 |
| FG | 61 | 1213 | 21.9 | +1,270 | +7,070 | +8,340 | +3.81 |
| zn | 47 | 505 | 65.3 | -9,850 | +1,588 | -8,262 | -1.27 |
| pb | 50 | 1102 | 88.3 | +2,812 | +5,162 | +7,975 | +0.90 |
| a | 57 | 681 | 35.8 | +4,010 | +3,455 | +7,465 | +2.09 |
| other (39) | - | 12985 | 687.6 | -3,660 | +39,898 | +36,238 | +0.53 |
| all products | - | 24568 | 1504.4 | +1,650 | +92,425 | +94,075 | +0.63 |
ranked by |all-in| over the live window (all-in = drift + exec = the bridge's exec_cost by product); product bps are vs traded notional

## Per strategy
| strategy | live? | bt 2026 pnl (full) | bt scaled+weighted (live window) | live attributed | note |
|---|---|---|---|---|---|
| Calendar main pool (branch) | yes | +1,175,765 | +138,468 | +165,655 | forward w=0.8 |
| Fundamental factor | yes | +995,846 | +724,745 | +671,495 | forward w=2 |
| Cross-product pairs | yes | +100,965 | +65,348 | +32,013 | forward w=1.5 |
| Calendar extended pool | yes | +597,550 | +40,153 | +117,365 | forward w=0.25 |
| Chemical fundamental | yes | +484,135 | +5,283 | -46,670 | forward w=1.5 |
| Agriculture event-driven | no | -25,435 | -111,243 | -152,798 | forward w=0 (parked) |
| Factor-neutral stat arb | yes | +307,336 | +1,209 | +37,488 | forward w=1 |
| Fund pipeline ensemble | yes | +1,978,210 | -18,858 | +368 | forward w=0.1 |
| Outright trend + basis | yes | +512,520 | -1,455 | +5,520 | forward w=0.5 |
| shared bucket | - | - | - | +3,575 | legacy days only: a contract both per-source books held |
| neither bucket (no target) | - | - | - | +2,585 | named by no book that day or the day before |
| trading bucket | - | - | - | +81,863 | forward days: live P&L minus the strategies' holdings (fills vs settlement on rebalances, lot rounding, scale changes) |
forward days: each strategy is its own previous-day weighted book x scale x the settlement-to-settlement move (holdings); legacy days remain exclusive-holder. The gap tables (attributed - expected) therefore exclude execution, which sits in trading.

## Live P&L by strategy, last 10 reconciled days (attributed gross CNY)
| day | ks_branch | fund_v3 | china_pairs | ks_ext | chem_fund | agri_event | stat_arb | fpe | ks_outright | shared | neither | trading | total |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 2026-11-09 | -224 | +21,420 | +11,745 | -3,271 | -4,425 | +0 | -745 | +0 | +0 | +0 | +0 | +4,255 | +28,755 |
| 2026-11-10 | +10,060 | +60,290 | -5,542 | +4,261 | -39,090 | +0 | -8,585 | +0 | +0 | +0 | +0 | +1,881 | +23,275 |
| 2026-11-11 | -48 | +81,680 | +7,920 | -1,788 | -14,685 | +0 | +7,710 | +0 | +0 | +0 | +0 | +7,396 | +88,185 |
| 2026-11-12 | +57,280 | +15,540 | -5,798 | -3,425 | +975 | +0 | -5,505 | +30,757 | +8,365 | +0 | +255 | -1,640 | +96,805 |
| 2026-11-13 | +25,720 | +17,270 | +1,598 | -6,845 | -652 | +0 | +5,150 | +20,356 | +14,980 | +0 | +0 | +12,519 | +90,095 |
| 2026-11-16 | +42,372 | +44,060 | -4,905 | +3,780 | +9,698 | +0 | -9,495 | +21,178 | +3,188 | +0 | +0 | -7,000 | +102,875 |
| 2026-11-17 | +40,840 | +8,880 | -6,218 | -1,909 | -3,375 | +0 | -13,180 | +12,305 | -15,038 | +0 | +0 | +3,059 | +25,365 |
| 2026-11-18 | -42,252 | +43,890 | +8,482 | +6,179 | -2,985 | +0 | +4,010 | +14,961 | -5,422 | +0 | +0 | +14,027 | +40,890 |
| 2026-11-19 | +1,716 | +131,140 | +22,200 | +7,641 | -17,880 | +0 | -5,440 | -58,952 | -6,205 | +0 | +0 | +14,230 | +88,450 |
| 2026-11-20 | -1,380 | -8,420 | +8,108 | +44,591 | +1,245 | +0 | +1,750 | -40,236 | +5,652 | +0 | +0 | +10,755 | +22,065 |
| sum | +134,084 | +415,750 | +37,590 | +49,215 | -71,175 | +0 | -24,330 | +368 | +5,520 | +0 | +255 | +59,483 | +606,760 |
forward days: previous-day weighted book x scale x settlement move per strategy, the rest in trading; total foots to live gross. Live-window sums: 'Per strategy' above; full series: data/per_strategy_daily.csv (attributed)

## Per strategy gap by day, last 10 reconciled days (live attributed - expected, CNY)
| day | ks_branch | fund_v3 | china_pairs | ks_ext | chem_fund | agri_event | stat_arb | fpe | ks_outright | total |
|---|---|---|---|---|---|---|---|---|---|---|
| 2026-11-09 | -3,548 | +39,923 | -5,205 | +4,985 | +3,098 | +0 | -4,969 | +0 | +0 | +34,284 |
| 2026-11-10 | -18,696 | +40,476 | +870 | -1,682 | -10,462 | +0 | -3,516 | +0 | +0 | +6,989 |
| 2026-11-11 | +13,352 | -41,720 | +892 | -9,048 | -22,582 | +0 | -5,842 | +0 | +0 | -64,948 |
| 2026-11-12 | +26,396 | +1,299 | +390 | -855 | +18,465 | +0 | +840 | +17,117 | +5,348 | +69,000 |
| 2026-11-13 | -40,452 | +8,720 | +2,962 | -7,659 | -14,955 | +0 | +4,729 | -14,154 | -4,085 | -64,893 |
| 2026-11-16 | +32,344 | -15,894 | -248 | +2,479 | +13,995 | +0 | -12,710 | +440 | +1,990 | +22,396 |
| 2026-11-17 | -26,696 | -22,456 | -5,460 | -224 | +4,868 | +0 | +8,546 | -7,176 | -252 | -48,850 |
| 2026-11-18 | -1,864 | +30,364 | +8,272 | +3,881 | -11,250 | +0 | +875 | +887 | +5,092 | +36,258 |
| 2026-11-19 | +11,768 | -56,964 | -1,770 | -1,804 | +13,560 | +0 | +10,834 | -837 | -7,542 | -32,755 |
| 2026-11-20 | -3,600 | +21,533 | -8,400 | +31,632 | -5,505 | +0 | - | +22,948 | +6,425 | +65,034 |
| sum | -10,996 | +5,281 | -7,695 | +21,706 | -10,770 | +0 | -1,214 | +19,226 | +6,975 | +22,513 |
full series: data/per_strategy_daily.csv (day, strategy, expected, attributed, gap); a strategy's daily total foots to expected - live_gross once the shared, neither and trading buckets are added. '-' = that sleeve's backtest row has not shipped yet (BT PENDING).

## Live P&L by product, last 10 reconciled days (gross CNY, worst first)
| product | 11-09 | 11-10 | 11-11 | 11-12 | 11-13 | 11-16 | 11-17 | 11-18 | 11-19 | 11-20 | 10d sum | live window |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| pp | -11,905 | -37,895 | -560 | +9,640 | +13,050 | -85 | -12,865 | -10,520 | -22,405 | +4,350 | -69,195 | -122,870 |
| a | +5,480 | +1,700 | +3,830 | +140 | -5,620 | -23,390 | -8,070 | -1,250 | +3,870 | -12,190 | -35,500 | -37,240 |
| eb | -2,700 | -6,390 | +745 | +2,810 | +5,685 | +2,310 | -12,620 | -8,020 | -5,980 | -4,180 | -28,340 | -1,010 |
| y | -7,260 | -1,200 | +8,330 | +4,870 | +2,490 | +1,830 | -16,100 | -9,510 | -8,910 | -2,840 | -28,300 | -143,090 |
| fu | +3,490 | -2,650 | -2,080 | +2,360 | +5,420 | +5,710 | -21,360 | -70 | -5,340 | -9,880 | -24,400 | +32,910 |
| AP | +0 | +0 | +3,320 | +17,200 | +12,900 | -7,460 | -5,520 | +930 | -28,180 | -13,100 | -19,910 | -19,910 |
| c | +2,470 | -13,550 | -5,180 | -2,210 | -4,200 | +1,030 | +1,790 | +1,170 | +1,830 | +940 | -15,910 | -31,460 |
| TA | +4,200 | -10,140 | +140 | +930 | +2,300 | +180 | -3,060 | -2,350 | +1,840 | -7,870 | -13,830 | -82,510 |
| SF | -2,330 | -4,940 | -670 | +1,720 | -6,230 | -3,820 | +8,830 | +420 | +3,090 | -6,080 | -10,010 | +25,740 |
| sn | -1,300 | -60 | -2,960 | +3,300 | +5,590 | +8,270 | +10,890 | -5,320 | -3,760 | -23,550 | -8,900 | +26,090 |
| bu | +1,450 | -3,480 | -2,270 | +890 | +820 | +240 | -4,090 | -1,790 | -540 | +780 | -7,990 | -47,290 |
| OI | +7,690 | +260 | -7,840 | +2,180 | +3,960 | -470 | -9,660 | +2,370 | -3,540 | -2,160 | -7,210 | -33,620 |
| br | +1,150 | -2,350 | -400 | -950 | -3,200 | -4,400 | +4,450 | +1,800 | +650 | -3,400 | -6,650 | -21,575 |
| MA | -1,850 | -4,400 | +1,240 | +1,950 | +2,220 | +1,350 | -910 | -1,560 | -5,040 | +2,520 | -4,480 | +6,010 |
| eg | -1,340 | +3,920 | -1,800 | -3,920 | -3,870 | +370 | -660 | +2,880 | -800 | +1,190 | -4,030 | +46,500 |
| other (29) | +1,580 | +4,055 | +34,600 | -1,630 | +13,570 | -980 | -48,720 | +79,435 | +97,480 | +41,310 | +220,700 | +550,215 |
| l | +3,770 | +16,200 | +1,975 | -745 | -1,780 | +170 | +6,185 | +3,060 | -5,725 | +840 | +23,950 | +68,435 |
| IH | -360 | -1,620 | -720 | -60 | +1,080 | +960 | -3,120 | +5,040 | +3,780 | +29,460 | +34,440 | +112,320 |
| v | +5,370 | +15,230 | -5,025 | -5,640 | -12,920 | -6,025 | +15,170 | +11,315 | +19,040 | +5,935 | +42,450 | +62,235 |
| ni | -1,020 | +3,290 | +5,880 | -4,020 | -830 | +10,800 | +5,010 | -22,400 | +26,870 | +19,540 | +43,120 | +9,880 |
| pg | +3,480 | +8,740 | -260 | +400 | +140 | -3,080 | +13,420 | +2,440 | +13,360 | +11,080 | +49,720 | -3,240 |
| cu | -2,400 | -5,300 | +8,600 | +1,150 | +5,900 | +23,800 | +2,300 | +18,200 | +21,600 | -7,900 | +65,950 | +72,400 |
| hc | +5,630 | +7,780 | +1,710 | +9,190 | -1,820 | +11,350 | +47,900 | +12,830 | -6,590 | -8,700 | +79,280 | -68,570 |
| i | +4,000 | -3,550 | +5,100 | +8,750 | +7,350 | +40,900 | +34,300 | +2,700 | -9,050 | -10,400 | +80,100 | +65,450 |
| cs | -11,790 | +23,800 | +22,430 | +8,100 | +9,940 | +5,590 | +7,700 | +1,990 | +5,300 | +11,270 | +84,330 | +177,160 |
| al | +23,250 | +35,825 | +20,050 | +40,400 | +38,150 | +37,725 | +14,175 | -42,900 | -4,400 | +5,100 | +167,375 | +275,500 |
| all products | +28,755 | +23,275 | +88,185 | +96,805 | +90,095 | +102,875 | +25,365 | +40,890 | +88,450 | +22,065 | +606,760 | +918,460 |
executor total_pnl (holding + trading, settlement-to-settlement once the next capture lands, before fees) summed by product root; 'all products' foots to live gross. Full series: data/product_daily.csv

## Worst (strategy, product) cells, last 10 reconciled days (attributed gross CNY)
| strategy | product | 11-09 | 11-10 | 11-11 | 11-12 | 11-13 | 11-16 | 11-17 | 11-18 | 11-19 | 11-20 | sum |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| china_pairs | rb | -1,290 | -3,870 | +6,120 | -9,600 | +2,400 | -13,200 | -52,800 | -13,650 | +20,475 | +8,880 | -56,535 |
| china_pairs | pp | -2,362 | -30,772 | -742 | +7,155 | +8,032 | +270 | -15,060 | -5,460 | -13,860 | +2,220 | -50,580 |
| fpe | sn | +0 | +0 | +0 | +858 | +99 | -2,500 | +1,782 | -7,820 | -11,308 | -13,145 | -32,034 |
| china_pairs | y | -4,920 | -240 | +6,600 | +5,280 | +720 | +1,155 | -13,545 | -10,440 | -9,180 | -3,165 | -27,735 |
| stat_arb | l | -1,365 | -7,275 | -850 | +630 | +2,250 | +480 | -7,110 | -2,910 | -13,455 | +2,860 | -26,745 |
| fund_v3 | eb | -5,850 | -9,570 | +1,020 | +3,810 | +6,390 | +3,080 | -8,970 | -6,780 | -3,910 | -3,450 | -24,230 |
| chem_fund | pp | -4,762 | -16,830 | +1,530 | +3,330 | +7,110 | +2,175 | -2,640 | -3,788 | -10,778 | +1,492 | -23,160 |
| fpe | AP | +0 | +0 | +0 | +17,028 | +12,771 | -7,372 | -5,589 | +1,312 | -28,260 | -12,838 | -22,948 |
| fund_v3 | c | +2,000 | -11,520 | -4,980 | -1,260 | -3,020 | +120 | -1,280 | +920 | -280 | -3,540 | -22,840 |
| fund_v3 | p | -4,600 | -1,620 | +6,920 | +4,960 | +1,760 | +3,440 | -9,940 | -10,040 | -9,240 | -3,400 | -21,760 |
| fund_v3 | SR | +3,160 | +3,620 | +1,680 | -440 | -760 | -4,080 | -14,000 | +22,360 | -11,280 | -17,220 | -16,960 |
| stat_arb | ss | +175 | -7,175 | -2,550 | -600 | +400 | -525 | -125 | +4,875 | -6,625 | -4,125 | -16,275 |
| chem_fund | bu | -4,050 | -8,115 | -3,720 | +2,820 | +5,370 | +600 | -7,095 | -780 | -885 | +270 | -15,585 |
| stat_arb | p | -3,700 | -2,640 | +8,460 | +1,490 | +1,890 | +340 | -4,350 | -1,740 | -9,840 | -4,720 | -14,810 |
| ks_branch | cu | +0 | +0 | +0 | +0 | +3,120 | +3,720 | +4,440 | -6,120 | -6,840 | -12,440 | -14,120 |
same holdings split as 'Live P&L by strategy'; summing a strategy's products reproduces its row there (trading / neither included as their own strategy). Full series: data/strategy_product_daily.csv

## Paper strategies (weight 0 in the forward book: tracked, not traded)
| strategy | weight 0 since | bt since (full) | bt last 20d | drawdown now | worst before pause | 60d Sharpe | paper-live since (full) | paper days | book coverage |
|---|---|---|---|---|---|---|---|---|---|
| agri_event | 2026-11-02 | -69,025 | -132,400 | -211,355 | -148,545 | -2.77 | -60,690 | 14 | 100% |
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
| agri_event | 15 | 20261120091424_8f0b7b90cc1f.csv | data | 8f0b7b9 | 4 | -475 |
full series: data/backtest/vintages/<strategy>/; index: data/backtest/vintages/index.csv

## Data health
decision-price coverage (2026-11-20): 100% of held notional benchmarked (0 contract(s) unbenchmarked); 14 contract(s) (21%) first decided after the 0900 snap, so they straddle their own overnight leg
scale: 1 (since 2026-09-09)
regime: forward (merged weighted book) since 2026-08-31; 54 forward day(s), 8 legacy day(s)
merge weights (2026-11-20): ks_branch 0.8, fund_v3 2, china_pairs 1.5, ks_ext 0.25, chem_fund 1.5, agri_event 0, stat_arb 1, fpe 0.1, ks_outright 0.5
as-shipped pins: 62 live day(s) pinned; current series diverges from pins on chem_fund: 30 day(s), max 9,725 CNY, fund_v3: 53 day(s), max 22,683 CNY, ks_branch: 43 day(s), max 82,125 CNY, ks_ext: 35 day(s), max 42,170 CNY, stat_arb: 45 day(s), max 9,982 CNY, china_pairs: 23 day(s), max 10,910 CNY, agri_event: 12 day(s), max 7,250 CNY; standing counts -- a divergence is announced as an alert once, the first run it appears, and kept here afterwards
inbox ks summary mtime: 2026-11-20 05:57 UTC
