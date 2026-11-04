# Performance tracker - 2026-11-03   (reconciled through 2026-11-03)

## ALERTS
- VINTAGE agri_event: 13 historical row(s) restated (net +225 CNY, cause data, commit 8f0b7b9) -- kept as vintages/agri_event/20261103091251_8f0b7b90cc1f.csv; the bridge keeps the as-shipped pins
- WEIGHTS 2026-10-09: day's own merge weights not shipped yet -- carried forward from an earlier day.
- WEIGHTS 2026-10-16: day's own merge weights not shipped yet -- carried forward from an earlier day.
- WEIGHTS 2026-10-22: day's own merge weights not shipped yet -- carried forward from an earlier day.
- BT PENDING 2026-11-03: no mature backtest row for stat_arb (nonzero weight) -- day reconciled WITHOUT that sleeve's expected; its live P&L sits in bt_pending_live, not resid, until the rows ship.
- WEIGHTS CHANGE on 2026-09-01: ks_ext: 0.0->0.25.
- WEIGHTS CHANGE on 2026-09-02: stat_arb: 1.0->0.0.
- WEIGHTS CHANGE on 2026-09-03: stat_arb: 0.0->1.0.
- WEIGHTS CHANGE on 2026-11-02: agri_event: 1.0->0.0.
- BT REVISED vs PINS: agri_event current history differs from pinned as-shipped values on 4 new live-window day(s) (max |diff| 7250 CNY, first 2026-10-09); the bridge keeps the pins.
- MISSING LIVE DAY 2026-08-28: trading day with a backtest row but no daily_pnl/state file; excluded from the bridge, expected pnl held in the missing-day bucket.
- SCALE 2026-08-28: no usable run record; previous scale carried forward.
- SCALE 2026-09-25: no usable run record; previous scale carried forward.
- SCALE CHANGE on 2026-08-27: now 0.2.
- SCALE CHANGE on 2026-09-01: now 0.5.
- SCALE CHANGE on 2026-09-09: now 1.
- BACKTEST REVISED: agri_event -- 5 mature row(s) changed since last run (net +525 CNY, largest 2026-03-30 -15565 -> -15190; first 2026-03-30, last 2026-05-22). Regeneration upstream; baseline re-set.
- SLIPPAGE 2026-11-03: 2 unbenchmarked leg(s), +2140 CNY exec cost without a shipped decision price.
- RESIDUAL 2026-08-27: -17267 CNY vs trailing median |resid| 2062, offset by neither neighbour (2026-08-26 +3749, 2026-08-31 -17348) -- attribution quality changed. (A break-out that a neighbouring day mirrors is the backtest/live day-window straddle and is not alerted.)
- RESIDUAL 2026-08-31: -17348 CNY vs trailing median |resid| 2277, offset by neither neighbour (2026-08-27 -17267, 2026-09-01 -8190) -- attribution quality changed. (A break-out that a neighbouring day mirrors is the backtest/live day-window straddle and is not alerted.)
- RESIDUAL 2026-09-01: -8190 CNY vs trailing median |resid| 2492, offset by neither neighbour (2026-08-31 -17348, 2026-09-02 -30063) -- attribution quality changed. (A break-out that a neighbouring day mirrors is the backtest/live day-window straddle and is not alerted.)
- RESIDUAL 2026-09-02: -30063 CNY vs trailing median |resid| 3121, offset by neither neighbour (2026-09-01 -8190, 2026-09-03 -29049) -- attribution quality changed. (A break-out that a neighbouring day mirrors is the backtest/live day-window straddle and is not alerted.)
- RESIDUAL 2026-09-03: -29049 CNY vs trailing median |resid| 3941, offset by neither neighbour (2026-09-02 -30063, 2026-09-04 -5584) -- attribution quality changed. (A break-out that a neighbouring day mirrors is the backtest/live day-window straddle and is not alerted.)
- RESIDUAL 2026-09-16: -103509 CNY vs trailing median |resid| 22936, offset by neither neighbour (2026-09-15 -28634, 2026-09-17 +23811) -- attribution quality changed. (A break-out that a neighbouring day mirrors is the backtest/live day-window straddle and is not alerted.)
- RESIDUAL 2026-10-26: +29017 CNY vs trailing median |resid| 7638, offset by neither neighbour (2026-10-23 +7825, 2026-10-27 +81673) -- attribution quality changed. (A break-out that a neighbouring day mirrors is the backtest/live day-window straddle and is not alerted.)
- RESIDUAL 2026-10-27: +81673 CNY vs trailing median |resid| 9046, offset by neither neighbour (2026-10-26 +29017, 2026-10-28 +2573) -- attribution quality changed. (A break-out that a neighbouring day mirrors is the backtest/live day-window straddle and is not alerted.)

## Latest reconciled day (2026-11-03, forward regime, PROVISIONAL: marked at the 16:00 close, re-marked to settlement after the next capture)
live gross +6,565 | expected (1 x bt +15,334) = +15,334 | gap -8,769
  exec_cost +9,300 (slip +7,160, unbench +2,140) | marking +37,345 | bookdiff +4,570 (carry +4,750, new -180) | intraday +0 | offbook +0 (0 contract(s)) | residual -45,734 (live re-marked to first decision, vs the previous backtest row)
  PARTIAL: no backtest row yet for stat_arb -- expected excludes it; its live P&L +4,350 is held out of resid
  fees +1,279 | broker residual +0 -> live net +5,286

## Cumulative bridge (live since 2026-08-18, 49 reconciled days, 1 with a sleeve's backtest pending)
| expected | -exec | +marking | +bookdiff | +intraday | +offbook | +bt pending | +resid | = live gross | -fees | +broker_resid | = live net |
|---|---|---|---|---|---|---|---|---|---|---|---|
| +271,373 | -64,650 | +46,630 | +91,287 | -5,168 | -50 | +4,350 | +5,778 | +349,550 | -46,813 | +11,070 | +313,807 |
missing live days excluded: 2026-08-28 (expected +4,849 held in bucket)

## Stats (daily CNY pnl)
| window | days | total | sharpe | mdd | hit |
|---|---|---|---|---|---|
| live net live-to-date | 49 | +313,807 | 1.74 | -330,281 | 55% |
| live net last-20d | 20 | +129,632 | 1.75 | -271,511 | 50% | (small sample)
| live net 2026-YTD | 49 | +313,807 | 1.74 | -330,281 | 55% |
| bt scaled live-to-date | 49 | +271,373 | 1.40 | -381,526 | 63% |
| bt scaled last-20d | 20 | +19,386 | 0.22 | -381,526 | 55% | (small sample)
| bt scaled 2026-YTD | 49 | +271,373 | 1.40 | -381,526 | 63% |

## Slippage (+ = cost; bps vs benchmarked notional)
| day | lots | notional M | slip total | drift | exec | bps | unbench legs | unbench CNY |
|---|---|---|---|---|---|---|---|---|
| 2026-10-21 | 342 | 21.4 | +3,385 | +2,920 | +465 | +2.04 | 6 | +270 |
| 2026-10-22 | 408 | 18.0 | +1,025 | +60 | +965 | +0.58 | 2 | +30 |
| 2026-10-23 | 345 | 14.2 | -310 | -1,435 | +1,125 | -0.23 | 2 | -20 |
| 2026-10-26 | 423 | 16.9 | +3,130 | +2,752 | +378 | +1.86 | 1 | +105 |
| 2026-10-27 | 720 | 42.7 | +11,470 | +8,082 | +3,388 | +2.83 | 2 | -335 |
| 2026-10-28 | 220 | 17.2 | +7,060 | +6,922 | +138 | +4.23 | 3 | +320 |
| 2026-10-29 | 393 | 27.9 | +4,825 | +3,225 | +1,600 | +2.13 | 6 | -620 |
| 2026-10-30 | 249 | 14.1 | +6,150 | +6,185 | -35 | +4.49 | 4 | +5 |
| 2026-11-02 | 258 | 19.2 | +7,360 | +6,620 | +740 | +3.92 | 3 | -5 |
| 2026-11-03 | 379 | 25.3 | +7,160 | +5,542 | +1,618 | +2.94 | 2 | +2,140 |
| live window (49d) | 17765 | 1099.3 | +49,325 | -1,452 | +50,778 | +0.49 | 244 | +15,325 |
exec-only bps over the window: +0.50; benchmark coverage 92% of traded notional

| product | days | lots | notional M | drift | exec (incl. unbench) | all-in | bps |
|---|---|---|---|---|---|---|---|
| IH | 30 | 120 | 100.0 | -29,010 | +5,610 | -23,400 | -2.34 |
| IF | 18 | 64 | 83.0 | -21,090 | +3,030 | -18,060 | -2.18 |
| CY | 37 | 272 | 30.0 | +10,162 | +5,438 | +15,600 | +5.19 |
| rb | 39 | 1229 | 38.1 | +17,305 | -3,635 | +13,670 | +3.59 |
| hc | 41 | 1466 | 48.4 | -17,755 | +5,585 | -12,170 | -2.52 |
| bu | 42 | 433 | 20.9 | -13,400 | +1,570 | -11,830 | -5.67 |
| pg | 26 | 45 | 6.2 | +10,410 | +310 | +10,720 | +17.38 |
| FG | 48 | 907 | 16.4 | +6,150 | +4,430 | +10,580 | +6.45 |
| SF | 45 | 415 | 12.5 | +8,930 | +675 | +9,605 | +7.68 |
| y | 40 | 268 | 24.0 | +6,130 | +1,980 | +8,110 | +3.38 |
| a | 44 | 564 | 29.7 | +4,030 | +2,875 | +6,905 | +2.32 |
| PF | 40 | 241 | 10.0 | -7,270 | +720 | -6,550 | -6.55 |
| SR | 43 | 882 | 47.8 | +4,740 | +1,775 | +6,515 | +1.36 |
| cs | 47 | 937 | 23.5 | +1,415 | +4,480 | +5,895 | +2.51 |
| ru | 29 | 90 | 17.4 | +5,925 | -300 | +5,625 | +3.23 |
| other (34) | - | 9832 | 591.4 | +11,875 | +31,560 | +43,435 | +0.73 |
| all products | - | 17765 | 1099.3 | -1,452 | +66,102 | +64,650 | +0.59 |
ranked by |all-in| over the live window (all-in = drift + exec = the bridge's exec_cost by product); product bps are vs traded notional

## Per strategy
| strategy | live? | bt 2026 pnl (full) | bt scaled+weighted (live window) | live attributed | note |
|---|---|---|---|---|---|
| Calendar main pool (branch) | yes | +1,023,890 | +16,968 | +62,623 | forward w=0.8 |
| Fundamental factor | yes | +765,876 | +264,179 | +270,695 | forward w=2 |
| Cross-product pairs | yes | +56,135 | -1,897 | -22,377 | forward w=1.5 |
| Calendar extended pool | yes | +432,780 | -1,039 | +74,925 | forward w=0.25 |
| Chemical fundamental | yes | +519,255 | +57,963 | +39,993 | forward w=1.5 |
| Agriculture event-driven | no | +34,715 | -111,243 | -152,798 | forward w=0 (parked) |
| Factor-neutral stat arb | yes | +356,933 | +46,442 | +48,598 | forward w=1 |
| shared bucket | - | - | - | +3,575 | legacy days only: a contract both per-source books held |
| neither bucket (no target) | - | - | - | +2,330 | named by no book that day or the day before |
| trading bucket | - | - | - | +21,985 | forward days: live P&L minus the strategies' holdings (fills vs settlement on rebalances, lot rounding, scale changes) |
forward days: each strategy is its own previous-day weighted book x scale x the settlement-to-settlement move (holdings); legacy days remain exclusive-holder. The gap tables (attributed - expected) therefore exclude execution, which sits in trading.

## Live P&L by strategy, last 10 reconciled days (attributed gross CNY)
| day | ks_branch | fund_v3 | china_pairs | ks_ext | chem_fund | agri_event | stat_arb | shared | neither | trading | total |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 2026-10-21 | -7,536 | +34,220 | -6,472 | -1,204 | -3,150 | +10,620 | +8,660 | +0 | +0 | +4,072 | +39,210 |
| 2026-10-22 | -1,172 | +12,220 | +11,835 | -1,720 | +982 | -3,140 | -740 | +0 | +1,170 | -1,965 | +17,470 |
| 2026-10-23 | -8,796 | -9,130 | +6,262 | -2,563 | +11,032 | -19,495 | +8,845 | +0 | +0 | +2,289 | -11,555 |
| 2026-10-26 | -240 | -4,570 | +2,258 | +11,030 | +17,498 | -9,650 | -10,845 | +0 | +0 | -1,445 | +4,035 |
| 2026-10-27 | +35,236 | -2,240 | -9,068 | +6,356 | +9,218 | -37,080 | -20,025 | +0 | +0 | -21,217 | -38,820 |
| 2026-10-28 | +4,048 | -15,440 | -5,362 | -7,313 | -2,760 | -10,980 | -2,965 | +0 | +0 | -2,938 | -43,710 |
| 2026-10-29 | -49,776 | -53,440 | -825 | +6,281 | -6,968 | -18,070 | -15,165 | +0 | +0 | -8,983 | -146,945 |
| 2026-10-30 | -16,068 | -66,600 | -1,560 | +2,871 | +9,292 | +8,605 | +13,805 | +0 | -275 | +17,859 | -32,070 |
| 2026-11-02 | +4,260 | -660 | +7,845 | -25,403 | +15,420 | -3,995 | +12,980 | +0 | +0 | -12,588 | -2,140 |
| 2026-11-03 | -4,516 | +14,560 | -7,388 | +5,971 | -5,850 | +0 | +4,350 | +0 | +0 | -563 | +6,565 |
| sum | -44,560 | -91,080 | -2,475 | -5,691 | +44,715 | -83,185 | -1,100 | +0 | +895 | -25,479 | -207,960 |
forward days: previous-day weighted book x scale x settlement move per strategy, the rest in trading; total foots to live gross. Live-window sums: 'Per strategy' above; full series: data/per_strategy_daily.csv (attributed)

## Per strategy gap by day, last 10 reconciled days (live attributed - expected, CNY)
| day | ks_branch | fund_v3 | china_pairs | ks_ext | chem_fund | agri_event | stat_arb | total |
|---|---|---|---|---|---|---|---|---|
| 2026-10-21 | -4,280 | +13,949 | -1,508 | -2,398 | -338 | +4,200 | +3,114 | +12,740 |
| 2026-10-22 | +18,340 | -9,712 | +6,202 | -1,081 | -585 | -6,370 | -3,852 | +2,942 |
| 2026-10-23 | +3,360 | -4,852 | -3,255 | +1,446 | +4,328 | +3,345 | -5,275 | -904 |
| 2026-10-26 | -16,908 | +16,537 | -1,418 | +7,696 | +6,255 | -7,360 | -4,496 | +307 |
| 2026-10-27 | +83,988 | -3,013 | +4,755 | +3,094 | -12,608 | +9,880 | +11,794 | +97,890 |
| 2026-10-28 | -13,640 | +4,387 | -210 | -11,386 | +10,568 | -8,470 | -10,748 | -29,499 |
| 2026-10-29 | +31,404 | -1,601 | +480 | +7,169 | +7,665 | +585 | +3,032 | +48,734 |
| 2026-10-30 | +9,708 | -35,219 | -2,768 | -241 | +3,375 | +8,655 | -2,361 | -18,851 |
| 2026-11-02 | +9,376 | +63,262 | -1,358 | -26,996 | +3,038 | -3,995 | -3,385 | +39,942 |
| 2026-11-03 | -12,868 | -19,192 | -8 | +19,571 | -60 | +0 | - | -12,556 |
| sum | +108,480 | +24,546 | +915 | -3,126 | +21,638 | +470 | -12,177 | +140,746 |
full series: data/per_strategy_daily.csv (day, strategy, expected, attributed, gap); a strategy's daily total foots to expected - live_gross once the shared, neither and trading buckets are added. '-' = that sleeve's backtest row has not shipped yet (BT PENDING).

## Live P&L by product, last 10 reconciled days (gross CNY, worst first)
| product | 10-21 | 10-22 | 10-23 | 10-26 | 10-27 | 10-28 | 10-29 | 10-30 | 11-02 | 11-03 | 10d sum | live window |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| y | -800 | -2,170 | -1,210 | -9,590 | +840 | -3,550 | -7,880 | -2,330 | +8,940 | -31,850 | -49,600 | -71,080 |
| p | -4,730 | -2,560 | +15,090 | +1,810 | -35,990 | -8,710 | -22,970 | -5,410 | +4,090 | +10,320 | -49,060 | -17,910 |
| pp | -11,800 | -2,460 | -4,590 | -2,380 | -6,235 | -1,165 | -8,380 | +1,800 | +410 | -13,310 | -48,110 | -32,590 |
| cs | +9,980 | -670 | -30,200 | -50 | +860 | -3,860 | -10,540 | +3,410 | -10,770 | -1,290 | -43,130 | +106,180 |
| CF | +13,325 | +1,250 | -3,750 | -3,100 | -22,400 | -14,350 | -7,350 | +6,175 | -2,700 | -6,200 | -39,100 | -98,625 |
| l | +185 | -1,280 | -8,200 | -14,180 | -1,470 | +4,735 | -9,445 | +2,615 | -9,825 | -920 | -37,785 | -4,740 |
| a | +1,130 | +6,190 | +4,610 | -11,510 | -2,340 | -2,580 | -16,320 | -4,410 | +2,070 | -9,160 | -32,320 | +8,490 |
| TA | +2,460 | -950 | -3,880 | -6,270 | +2,620 | +290 | +1,770 | -2,960 | +6,350 | -31,690 | -32,260 | +1,200 |
| OI | -2,780 | -1,310 | -7,940 | -1,930 | -3,800 | +340 | -10,220 | -9,480 | +7,280 | +4,750 | -25,090 | -39,690 |
| eb | +190 | -2,210 | +835 | +2,335 | -1,505 | -2,215 | -5,445 | -190 | +7,710 | -20,030 | -20,525 | +49,195 |
| b | -4,120 | -4,370 | +4,440 | -310 | -5,420 | +5,350 | -8,470 | -410 | -670 | -1,900 | -15,880 | -10,160 |
| IF | -3,000 | -900 | -1,500 | +5,400 | -1,080 | -5,040 | +2,880 | +9,120 | -26,400 | +6,360 | -14,160 | -48,840 |
| v | -915 | +95 | -90 | -4,755 | +2,505 | -7,400 | -4,440 | -2,440 | +1,815 | +1,465 | -14,160 | -6,885 |
| m | +840 | -6,140 | -4,080 | +100 | -1,320 | +2,110 | -6,330 | +1,280 | -3,810 | +3,200 | -14,150 | -22,700 |
| fu | +3,770 | +360 | -9,800 | -5,750 | -2,570 | -360 | -10,780 | +1,410 | +4,000 | +6,300 | -13,420 | +20,030 |
| other (24) | +9,825 | +24,170 | +37,975 | +2,495 | -16,765 | -29,230 | -11,965 | -6,320 | -22,520 | +29,600 | +17,265 | +213,215 |
| sp | +2,920 | +1,400 | +3,440 | +5,000 | +7,160 | +3,880 | +1,340 | -16,700 | +2,940 | +2,720 | +14,100 | +41,600 |
| rb | +5,940 | -10,050 | -10,560 | +3,780 | +3,890 | -9,760 | -15,710 | +6,930 | +17,080 | +23,240 | +14,780 | +151,290 |
| c | +1,110 | +7,610 | +3,300 | -1,270 | -1,130 | +3,630 | +90 | -2,200 | +2,780 | +1,320 | +15,240 | -15,120 |
| CY | +75 | -3,875 | +1,850 | +1,800 | +12,200 | +4,800 | +6,800 | -14,450 | -1,100 | +9,025 | +17,125 | -950 |
| zn | +200 | +2,300 | -9,775 | +12,975 | +3,000 | +1,400 | +850 | -250 | -150 | +7,550 | +18,100 | +32,725 |
| FG | +1,140 | +7,520 | +3,720 | -5,700 | +18,640 | +1,060 | -2,300 | -2,820 | +6,160 | -5,180 | +22,240 | +84,280 |
| ss | +8,275 | +21,550 | -4,850 | -2,025 | -7,950 | -525 | -850 | +2,500 | +900 | +7,075 | +24,100 | +2,875 |
| cu | +3,300 | -3,000 | -1,500 | +2,700 | +1,900 | +3,550 | +3,600 | -2,500 | -1,400 | +17,600 | +24,250 | -150 |
| SA | +5,740 | -16,300 | +11,440 | +20,000 | +11,760 | +11,360 | -7,140 | +180 | -6,340 | +3,660 | +34,360 | -29,040 |
| MA | -3,050 | +3,270 | +3,670 | +14,460 | +5,780 | +2,530 | +2,260 | +5,380 | +11,020 | -6,090 | +39,230 | +36,950 |
| all products | +39,210 | +17,470 | -11,555 | +4,035 | -38,820 | -43,710 | -146,945 | -32,070 | -2,140 | +6,565 | -207,960 | +349,550 |
executor total_pnl (holding + trading, settlement-to-settlement once the next capture lands, before fees) summed by product root; 'all products' foots to live gross. Full series: data/product_daily.csv

## Worst (strategy, product) cells, last 10 reconciled days (attributed gross CNY)
| strategy | product | 10-21 | 10-22 | 10-23 | 10-26 | 10-27 | 10-28 | 10-29 | 10-30 | 11-02 | 11-03 | sum |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| china_pairs | l | +1,688 | -150 | -12,900 | -17,752 | -5,100 | -4,650 | -10,425 | -11,715 | -12,045 | +7,425 | -65,625 |
| fund_v3 | cs | +4,600 | +4,320 | -26,840 | -1,200 | +640 | -3,400 | -10,780 | +2,720 | -11,120 | -1,580 | -42,640 |
| fund_v3 | pp | +2,520 | +80 | -10,160 | -16,240 | -5,160 | -5,080 | -4,720 | -5,360 | -5,120 | +7,880 | -41,360 |
| ks_branch | y | -144 | -2,304 | -2,592 | -8,904 | -1,400 | -3,672 | -6,808 | -2,320 | +6,032 | -8,080 | -30,192 |
| ks_branch | OI | -3,800 | -2,800 | -6,600 | -1,584 | -5,672 | -440 | -9,096 | -7,176 | +5,656 | +4,504 | -27,008 |
| ks_branch | pp | -8,124 | -2,120 | -4,176 | -7,540 | -1,540 | +3,636 | -3,568 | +4,864 | -664 | -5,188 | -24,420 |
| fund_v3 | CF | +200 | +3,600 | +0 | -5,800 | -17,600 | -2,700 | -2,700 | +2,700 | -1,050 | -1,050 | -24,400 |
| fund_v3 | p | +4,060 | -2,060 | +2,000 | +1,840 | -19,280 | -3,280 | -8,720 | -160 | +4,660 | -2,640 | -23,580 |
| fund_v3 | pg | +0 | +0 | +0 | -9,280 | -8,120 | +1,520 | -1,120 | -5,000 | +0 | +0 | -22,000 |
| agri_event | SR | +3,680 | -3,040 | -2,240 | -2,240 | -13,280 | +1,760 | -1,760 | -320 | -3,520 | +0 | -20,960 |
| stat_arb | SH | -930 | -5,130 | -1,980 | -6,750 | -6,600 | -2,070 | -720 | +5,400 | -5,250 | +3,840 | -20,190 |
| ks_ext | IF | -2,850 | -855 | -1,425 | +5,670 | -630 | -4,830 | +2,625 | -405 | -23,940 | +6,930 | -19,710 |
| agri_event | p | +8,190 | -3,150 | -1,080 | +2,340 | -21,150 | -4,140 | -11,160 | +2,250 | +8,550 | +0 | -19,350 |
| stat_arb | p | -910 | +0 | +0 | +1,040 | -11,750 | -2,760 | -7,440 | +250 | +3,800 | -920 | -18,690 |
| fund_v3 | FG | +640 | +5,400 | +1,400 | -3,360 | +6,160 | -8,400 | -3,920 | -10,840 | +800 | -6,480 | -18,600 |
same holdings split as 'Live P&L by strategy'; summing a strategy's products reproduces its row there (trading / neither included as their own strategy). Full series: data/strategy_product_daily.csv

## Paper strategies (weight 0 in the forward book: tracked, not traded)
| strategy | weight 0 since | bt since (full) | bt last 20d | drawdown now | worst before pause | 60d Sharpe | paper-live since (full) | paper days | book coverage |
|---|---|---|---|---|---|---|---|---|---|
| agri_event | 2026-11-02 | -7,800 | -96,720 | -154,005 | -152,420 | -1.97 | -3,560 | 1 | 100% |
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
| agri_event | +6,775 |
| stat_arb | +16,744 |
| all | +22,894 |
| strategy | vintages | latest | cause | commit | rows restated | net change (full size) |
|---|---|---|---|---|---|---|
| fund_v3 | 1 | 20261029084152_nocommit.csv | baseline | - | 0 | +0 |
| stat_arb | 1 | 20261029084152_nocommit.csv | baseline | - | 0 | +0 |
| ks_branch | 2 | 20261102090932_cbbdd7664522.csv | unknown | cbbdd76 | 165 | +341,255 |
| ks_ext | 2 | 20261102090932_1a03a09367cb.csv | unknown | 1a03a09 | 91 | +31,590 |
| china_pairs | 2 | 20261102090932_51a17747e0e0.csv | unknown | 51a1774 | 44 | -46,815 |
| chem_fund | 2 | 20261102090932_a98238f08285.csv | unknown | a98238f | 120 | +51,865 |
| agri_event | 4 | 20261103091251_8f0b7b90cc1f.csv | data | 8f0b7b9 | 13 | +225 |
full series: data/backtest/vintages/<strategy>/; index: data/backtest/vintages/index.csv

## Data health
decision-price coverage (2026-11-03): 100% of held notional benchmarked (0 contract(s) unbenchmarked); 10 contract(s) (16%) first decided after the 0900 snap, so they straddle their own overnight leg
scale: 1 (since 2026-09-09)
regime: forward (merged weighted book) since 2026-08-31; 41 forward day(s), 8 legacy day(s)
merge weights (2026-11-03): ks_branch 0.8, fund_v3 2, china_pairs 1.5, ks_ext 0.25, chem_fund 1.5, agri_event 0, stat_arb 1
as-shipped pins: 49 live day(s) pinned; current series diverges from pins on chem_fund: 30 day(s), max 9,725 CNY, fund_v3: 43 day(s), max 22,683 CNY, ks_branch: 43 day(s), max 82,125 CNY, ks_ext: 35 day(s), max 42,170 CNY, stat_arb: 43 day(s), max 9,982 CNY, china_pairs: 23 day(s), max 10,910 CNY, agri_event: 19 day(s), max 7,250 CNY, 4 NEW; standing counts -- a divergence is announced as an alert once, the first run it appears, and kept here afterwards
inbox ks summary mtime: 2026-11-03 05:53 UTC
