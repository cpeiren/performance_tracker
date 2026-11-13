# Performance tracker - 2026-11-13   (reconciled through 2026-11-13)

## ALERTS
- VINTAGE agri_event: 24 historical row(s) restated (net +750 CNY, cause data, commit 8f0b7b9) -- kept as vintages/agri_event/20261113091334_8f0b7b90cc1f.csv; the bridge keeps the as-shipped pins
- VINTAGE stat_arb: 1 historical row(s) restated (net +16 CNY, cause data, commit 9f7e9a7) -- kept as vintages/stat_arb/20261113091334_9f7e9a742805.csv; the bridge keeps the as-shipped pins
- WEIGHTS 2026-10-09: day's own merge weights not shipped yet -- carried forward from an earlier day.
- WEIGHTS 2026-10-16: day's own merge weights not shipped yet -- carried forward from an earlier day.
- WEIGHTS 2026-10-22: day's own merge weights not shipped yet -- carried forward from an earlier day.
- BT PENDING 2026-11-13: no mature backtest row for stat_arb (nonzero weight) -- day reconciled WITHOUT that sleeve's expected; its live P&L sits in bt_pending_live, not resid, until the rows ship.
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
- BACKTEST REVISED: agri_event -- 24 mature row(s) changed since last run (net +750 CNY, largest 2026-01-06 +13690 -> +12015; first 2026-01-05, last 2026-02-05). Regeneration upstream; baseline re-set.
- SLIPPAGE 2026-11-13: 5 unbenchmarked leg(s), +228 CNY exec cost without a shipped decision price.
- RESIDUAL 2026-08-27: -17267 CNY vs trailing median |resid| 2062, offset by neither neighbour (2026-08-26 +3749, 2026-08-31 -17348) -- attribution quality changed. (A break-out that a neighbouring day mirrors is the backtest/live day-window straddle and is not alerted.)
- RESIDUAL 2026-08-31: -17348 CNY vs trailing median |resid| 2277, offset by neither neighbour (2026-08-27 -17267, 2026-09-01 -8190) -- attribution quality changed. (A break-out that a neighbouring day mirrors is the backtest/live day-window straddle and is not alerted.)
- RESIDUAL 2026-09-01: -8190 CNY vs trailing median |resid| 2492, offset by neither neighbour (2026-08-31 -17348, 2026-09-02 -30063) -- attribution quality changed. (A break-out that a neighbouring day mirrors is the backtest/live day-window straddle and is not alerted.)
- RESIDUAL 2026-09-02: -30063 CNY vs trailing median |resid| 3121, offset by neither neighbour (2026-09-01 -8190, 2026-09-03 -29049) -- attribution quality changed. (A break-out that a neighbouring day mirrors is the backtest/live day-window straddle and is not alerted.)
- RESIDUAL 2026-09-03: -29049 CNY vs trailing median |resid| 3941, offset by neither neighbour (2026-09-02 -30063, 2026-09-04 -5584) -- attribution quality changed. (A break-out that a neighbouring day mirrors is the backtest/live day-window straddle and is not alerted.)
- RESIDUAL 2026-09-16: -103509 CNY vs trailing median |resid| 22936, offset by neither neighbour (2026-09-15 -28634, 2026-09-17 +23811) -- attribution quality changed. (A break-out that a neighbouring day mirrors is the backtest/live day-window straddle and is not alerted.)
- RESIDUAL 2026-10-26: +29017 CNY vs trailing median |resid| 7638, offset by neither neighbour (2026-10-23 +7825, 2026-10-27 +81673) -- attribution quality changed. (A break-out that a neighbouring day mirrors is the backtest/live day-window straddle and is not alerted.)
- RESIDUAL 2026-10-27: +81673 CNY vs trailing median |resid| 9046, offset by neither neighbour (2026-10-26 +29017, 2026-10-28 +2573) -- attribution quality changed. (A break-out that a neighbouring day mirrors is the backtest/live day-window straddle and is not alerted.)

## Latest reconciled day (2026-11-13, forward regime, PROVISIONAL: marked at the 16:00 close, re-marked to settlement after the next capture)
live gross +118,645 | expected (1 x bt +142,027) = +142,027 | gap -23,382
  exec_cost +2,312 (slip +2,085, unbench +228) | marking -29,955 | bookdiff +0 (carry +0, new +0) | intraday +0 | offbook +0 (0 contract(s)) | residual +5,040 (live re-marked to first decision, vs the previous backtest row)
  PARTIAL: no backtest row yet for stat_arb -- expected excludes it; its live P&L +3,845 is held out of resid
  fees +1,225 | broker residual +0 -> live net +117,420

## Cumulative bridge (live since 2026-08-18, 57 reconciled days, 1 with a sleeve's backtest pending)
| expected | -exec | +marking | +bookdiff | +intraday | +offbook | +bt pending | +resid | = live gross | -fees | +broker_resid | = live net |
|---|---|---|---|---|---|---|---|---|---|---|---|
| +642,035 | -80,520 | +17,255 | +90,047 | -6,568 | -50 | +3,845 | +1,321 | +667,365 | -58,025 | +11,121 | +620,462 |
missing live days excluded: 2026-08-28 (expected +4,849 held in bucket)

## Stats (daily CNY pnl)
| window | days | total | sharpe | mdd | hit |
|---|---|---|---|---|---|
| live net live-to-date | 57 | +620,462 | 2.95 | -330,281 | 56% |
| live net last-20d | 20 | +115,513 | 1.61 | -317,945 | 50% | (small sample)
| live net 2026-YTD | 57 | +620,462 | 2.95 | -330,281 | 56% |
| bt scaled live-to-date | 57 | +642,035 | 2.80 | -381,526 | 67% |
| bt scaled last-20d | 20 | +36,739 | 0.41 | -381,526 | 60% | (small sample)
| bt scaled 2026-YTD | 57 | +642,035 | 2.80 | -381,526 | 67% |

## Slippage (+ = cost; bps vs benchmarked notional)
| day | lots | notional M | slip total | drift | exec | bps | unbench legs | unbench CNY |
|---|---|---|---|---|---|---|---|---|
| 2026-11-02 | 258 | 19.2 | +7,360 | +6,620 | +740 | +3.92 | 3 | -5 |
| 2026-11-03 | 379 | 25.3 | +7,160 | +5,542 | +1,618 | +2.94 | 2 | +2,140 |
| 2026-11-04 | 364 | 32.1 | +2,030 | +1,422 | +608 | +0.64 | 1 | +275 |
| 2026-11-05 | 462 | 30.3 | +3,350 | +942 | +2,408 | +1.15 | 4 | -45 |
| 2026-11-06 | 863 | 42.1 | +13,755 | +6,750 | +7,005 | +3.27 | 1 | +45 |
| 2026-11-09 | 519 | 27.4 | -5,690 | -6,638 | +948 | -2.09 | 1 | -30 |
| 2026-11-10 | 484 | 26.2 | +1,890 | +445 | +1,445 | +0.75 | 2 | +118 |
| 2026-11-11 | 445 | 37.7 | -5,640 | -6,922 | +1,282 | -1.52 | 3 | +50 |
| 2026-11-12 | 508 | 31.3 | +3,550 | +2,372 | +1,178 | +1.15 | 2 | -100 |
| 2026-11-13 | 504 | 35.5 | +2,085 | -325 | +2,410 | +0.62 | 5 | +228 |
| live window (57d) | 21914 | 1362.0 | +64,655 | -3,405 | +68,060 | +0.51 | 263 | +15,865 |
exec-only bps over the window: +0.54; benchmark coverage 93% of traded notional

| product | days | lots | notional M | drift | exec (incl. unbench) | all-in | bps |
|---|---|---|---|---|---|---|---|
| IH | 37 | 150 | 124.6 | -27,270 | +4,830 | -22,440 | -1.80 |
| IF | 24 | 84 | 107.0 | -20,220 | +3,120 | -17,100 | -1.60 |
| CY | 43 | 313 | 34.4 | +10,450 | +6,075 | +16,525 | +4.80 |
| pg | 28 | 48 | 6.6 | +15,040 | +220 | +15,260 | +23.28 |
| bu | 49 | 591 | 27.9 | -13,730 | +1,545 | -12,185 | -4.37 |
| y | 47 | 324 | 28.8 | +9,935 | +2,125 | +12,060 | +4.19 |
| rb | 47 | 1540 | 47.5 | +9,930 | +1,790 | +11,720 | +2.47 |
| SF | 53 | 481 | 14.4 | +9,450 | +1,035 | +10,485 | +7.29 |
| FG | 56 | 1086 | 19.6 | +3,760 | +6,360 | +10,120 | +5.16 |
| SA | 53 | 853 | 17.2 | +6,560 | +3,200 | +9,760 | +5.68 |
| SR | 51 | 1023 | 55.1 | +6,040 | +1,985 | +8,025 | +1.46 |
| PF | 48 | 334 | 13.6 | -8,600 | +795 | -7,805 | -5.73 |
| hc | 49 | 1768 | 58.0 | -11,340 | +4,930 | -6,410 | -1.10 |
| ru | 37 | 123 | 23.7 | +6,350 | -175 | +6,175 | +2.60 |
| cs | 55 | 1032 | 25.9 | +1,575 | +4,590 | +6,165 | +2.38 |
| other (38) | - | 12164 | 757.5 | -1,335 | +41,500 | +40,165 | +0.53 |
| all products | - | 21914 | 1362.0 | -3,405 | +83,925 | +80,520 | +0.59 |
ranked by |all-in| over the live window (all-in = drift + exec = the bridge's exec_cost by product); product bps are vs traded notional

## Per strategy
| strategy | live? | bt 2026 pnl (full) | bt scaled+weighted (live window) | live attributed | note |
|---|---|---|---|---|---|
| Calendar main pool (branch) | yes | +1,139,085 | +109,124 | +131,603 | forward w=0.8 |
| Fundamental factor | yes | +864,344 | +461,757 | +433,005 | forward w=2 |
| Cross-product pairs | yes | +77,450 | +30,076 | +8,343 | forward w=1.5 |
| Calendar extended pool | yes | +500,280 | +15,836 | +59,774 | forward w=0.25 |
| Chemical fundamental | yes | +503,445 | +34,248 | -22,332 | forward w=1.5 |
| Agriculture event-driven | no | +46,875 | -111,243 | -152,798 | forward w=0 (parked) |
| Factor-neutral stat arb | yes | +342,497 | +32,006 | +58,538 | forward w=1 |
| Fund pipeline ensemble | yes | +2,648,282 | +48,149 | +54,836 | forward w=0.1 |
| Outright trend + basis | yes | +559,595 | +22,082 | +33,660 | forward w=0.5 |
| shared bucket | - | - | - | +3,575 | legacy days only: a contract both per-source books held |
| neither bucket (no target) | - | - | - | +2,585 | named by no book that day or the day before |
| trading bucket | - | - | - | +56,576 | forward days: live P&L minus the strategies' holdings (fills vs settlement on rebalances, lot rounding, scale changes) |
forward days: each strategy is its own previous-day weighted book x scale x the settlement-to-settlement move (holdings); legacy days remain exclusive-holder. The gap tables (attributed - expected) therefore exclude execution, which sits in trading.

## Live P&L by strategy, last 10 reconciled days (attributed gross CNY)
| day | ks_branch | fund_v3 | china_pairs | ks_ext | chem_fund | agri_event | stat_arb | fpe | ks_outright | shared | neither | trading | total |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 2026-11-02 | +4,260 | -660 | +7,845 | -25,403 | +15,420 | -3,995 | +12,980 | +0 | +0 | +0 | +0 | -12,588 | -2,140 |
| 2026-11-03 | -9,816 | +21,940 | -8,490 | -123 | -13,485 | +0 | +1,335 | +0 | +0 | +0 | +0 | +2,793 | -5,845 |
| 2026-11-04 | +7,320 | -21,410 | -2,842 | -13,680 | +11,618 | +0 | +12,140 | +0 | +0 | +0 | +0 | +4,875 | -1,980 |
| 2026-11-05 | -33,388 | +1,260 | -532 | +8,112 | -8,992 | +0 | +12,415 | +0 | +0 | +0 | +0 | -13,885 | -35,010 |
| 2026-11-06 | +316 | -2,180 | +21,278 | +4,886 | -10,478 | +0 | -8,320 | +0 | +0 | +0 | +0 | +6,048 | +11,550 |
| 2026-11-09 | -224 | +21,420 | +11,745 | -3,271 | -4,425 | +0 | -745 | +0 | +0 | +0 | +0 | +4,255 | +28,755 |
| 2026-11-10 | +10,060 | +60,290 | -5,542 | +4,261 | -39,090 | +0 | -8,585 | +0 | +0 | +0 | +0 | +1,881 | +23,275 |
| 2026-11-11 | -48 | +81,680 | +7,920 | -1,788 | -14,685 | +0 | +7,710 | +0 | +0 | +0 | +0 | +7,396 | +88,185 |
| 2026-11-12 | +57,280 | +15,540 | -5,798 | -3,425 | +975 | +0 | -5,505 | +30,757 | +8,365 | +0 | +255 | -1,640 | +96,805 |
| 2026-11-13 | +32,964 | -1,670 | +5,595 | -4,154 | +10,388 | +0 | +3,845 | +24,079 | +25,295 | +0 | +0 | +22,303 | +118,645 |
| sum | +68,724 | +176,210 | +31,178 | -34,583 | -52,755 | -3,995 | +27,270 | +54,836 | +33,660 | +0 | +255 | +21,440 | +322,240 |
forward days: previous-day weighted book x scale x settlement move per strategy, the rest in trading; total foots to live gross. Live-window sums: 'Per strategy' above; full series: data/per_strategy_daily.csv (attributed)

## Per strategy gap by day, last 10 reconciled days (live attributed - expected, CNY)
| day | ks_branch | fund_v3 | china_pairs | ks_ext | chem_fund | agri_event | stat_arb | fpe | ks_outright | total |
|---|---|---|---|---|---|---|---|---|---|---|
| 2026-11-02 | +9,376 | +63,262 | -1,358 | -26,996 | +3,038 | -3,995 | -3,385 | +0 | +0 | +39,942 |
| 2026-11-03 | -18,168 | -12,215 | -1,110 | +13,477 | -7,695 | +0 | +3,215 | +0 | +0 | -22,496 |
| 2026-11-04 | +2,600 | -42,652 | -6,390 | -17,409 | -240 | +0 | +12,722 | +0 | +0 | -51,368 |
| 2026-11-05 | -20,828 | -38,627 | +5,752 | +2,836 | +1,545 | +0 | +26,370 | +0 | +0 | -22,951 |
| 2026-11-06 | +16,056 | +9,255 | -3,420 | +208 | -16,882 | +0 | -4,371 | +0 | +0 | +845 |
| 2026-11-09 | -3,548 | +39,923 | -5,205 | +4,985 | +3,098 | +0 | -4,969 | +0 | +0 | +34,284 |
| 2026-11-10 | -18,696 | +40,476 | +870 | -1,682 | -10,462 | +0 | -3,516 | +0 | +0 | +6,989 |
| 2026-11-11 | +13,352 | -41,720 | +892 | -9,048 | -22,582 | +0 | -5,842 | +0 | +0 | -64,948 |
| 2026-11-12 | +26,396 | +1,299 | +390 | -855 | +18,465 | +0 | +1,272 | +17,117 | +5,348 | +69,433 |
| 2026-11-13 | -33,208 | -10,199 | +6,960 | -4,968 | -3,915 | +0 | - | -10,431 | +6,230 | -49,530 |
| sum | -26,668 | +8,803 | -2,618 | -39,451 | -35,632 | -3,995 | +21,496 | +6,687 | +11,578 | -59,801 |
full series: data/per_strategy_daily.csv (day, strategy, expected, attributed, gap); a strategy's daily total foots to expected - live_gross once the shared, neither and trading buckets are added. '-' = that sleeve's backtest row has not shipped yet (BT PENDING).

## Live P&L by product, last 10 reconciled days (gross CNY, worst first)
| product | 11-02 | 11-03 | 11-04 | 11-05 | 11-06 | 11-09 | 11-10 | 11-11 | 11-12 | 11-13 | 10d sum | live window |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| TA | +6,350 | -42,080 | -9,440 | -44,250 | -5,800 | +4,200 | -10,140 | +140 | +930 | +2,660 | -97,430 | -70,890 |
| y | +8,940 | -25,520 | -29,090 | -8,710 | -12,240 | -7,260 | -1,200 | +8,330 | +4,870 | +3,470 | -58,410 | -106,580 |
| pp | +410 | -14,870 | -2,660 | -17,820 | +955 | -11,905 | -37,895 | -560 | +9,640 | +26,190 | -48,515 | -68,205 |
| eb | +7,710 | -19,680 | -5,700 | -12,610 | -3,905 | -2,700 | -6,390 | +745 | +2,810 | +7,205 | -32,515 | +29,000 |
| IF | -26,400 | +3,420 | -15,000 | +900 | -540 | +1,320 | -240 | -120 | +720 | +4,200 | -31,740 | -60,540 |
| br | +1,100 | -5,350 | -300 | -8,350 | -2,750 | +1,150 | -2,350 | -400 | -950 | -5,700 | -23,900 | -23,175 |
| c | +2,780 | +1,050 | -1,880 | +4,280 | -2,560 | +2,470 | -13,550 | -5,180 | -2,210 | -7,050 | -21,850 | -41,070 |
| MA | +11,020 | -12,150 | -3,700 | -11,620 | -5,080 | -1,850 | -4,400 | +1,240 | +1,950 | +6,180 | -18,410 | +13,610 |
| ru | +150 | +1,200 | -5,800 | -900 | -450 | +500 | -2,600 | -1,800 | -2,250 | -4,050 | -16,000 | -16,300 |
| a | +2,070 | -6,810 | -12,270 | +5,100 | -5,410 | +5,480 | +1,700 | +3,830 | +140 | -8,600 | -14,770 | +810 |
| ni | +180 | +2,470 | -410 | -10,520 | -9,800 | -1,020 | +3,290 | +5,880 | -4,020 | +820 | -13,130 | -28,290 |
| pg | +6,020 | -7,040 | -2,980 | -8,020 | -7,720 | +3,480 | +8,740 | -260 | +400 | -4,100 | -11,480 | -44,700 |
| lu | -1,380 | -3,480 | -930 | -3,220 | +210 | +1,850 | +1,140 | -1,120 | +1,510 | +720 | -4,700 | -4,560 |
| lh | +0 | +0 | +0 | +0 | +0 | +0 | +0 | -880 | -240 | -2,880 | -4,000 | +20,000 |
| j | +0 | +0 | +50 | -1,950 | +0 | +0 | +0 | +900 | -3,000 | +0 | -4,000 | +2,150 |
| other (28) | -6,975 | +81,410 | +51,215 | -18,445 | +3,245 | -11,460 | +20,525 | +61,765 | +11,780 | +36,245 | +229,305 | +632,045 |
| m | -3,810 | +90 | +5,870 | +3,880 | +6,680 | +6,660 | +12,590 | -7,690 | +6,060 | -2,960 | +27,370 | +5,280 |
| hc | -6,480 | -9,690 | +750 | +19,770 | +3,300 | +5,630 | +7,780 | +1,710 | +9,190 | -1,580 | +30,380 | -125,120 |
| cu | -1,400 | -5,000 | +19,650 | -1,600 | +11,150 | -2,400 | -5,300 | +8,600 | +1,150 | +6,450 | +31,300 | +14,950 |
| OI | +7,280 | +2,470 | -4,450 | +5,590 | +14,420 | +7,690 | +260 | -7,840 | +2,180 | +4,360 | +31,960 | -19,760 |
| AP | +0 | +0 | +0 | +0 | +0 | +0 | +0 | +3,320 | +17,200 | +13,300 | +33,820 | +33,820 |
| PF | -4,860 | +23,910 | +2,570 | +13,630 | +3,580 | -2,250 | -1,980 | -570 | +850 | +290 | +35,170 | +82,260 |
| eg | -3,220 | +13,720 | +2,050 | +26,680 | +4,990 | -1,340 | +3,920 | -1,800 | -3,920 | -2,900 | +38,180 | +44,490 |
| l | -9,825 | +12,460 | -4,500 | +14,790 | +25,555 | +3,770 | +16,200 | +1,975 | -745 | -5,195 | +54,485 | +60,490 |
| fu | +4,000 | +9,400 | +11,500 | +21,060 | +1,620 | +3,490 | -2,650 | -2,080 | +2,360 | +16,020 | +64,720 | +74,450 |
| al | +4,200 | -5,775 | +3,475 | -2,675 | -7,900 | +23,250 | +35,825 | +20,050 | +40,400 | +35,550 | +146,400 | +263,200 |
| all products | -2,140 | -5,845 | -1,980 | -35,010 | +11,550 | +28,755 | +23,275 | +88,185 | +96,805 | +118,645 | +322,240 | +667,365 |
executor total_pnl (holding + trading, settlement-to-settlement once the next capture lands, before fees) summed by product root; 'all products' foots to live gross. Full series: data/product_daily.csv

## Worst (strategy, product) cells, last 10 reconciled days (attributed gross CNY)
| strategy | product | 11-02 | 11-03 | 11-04 | 11-05 | 11-06 | 11-09 | 11-10 | 11-11 | 11-12 | 11-13 | sum |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| china_pairs | pp | +5,760 | -18,322 | -3,098 | -16,380 | -20,700 | -2,362 | -30,772 | -742 | +7,155 | +17,820 | -61,642 |
| ks_ext | IF | -23,940 | +1,590 | -15,795 | +255 | -4,635 | +1,455 | -135 | +75 | -2,580 | -2,340 | -46,050 |
| fund_v3 | eb | +6,840 | -18,620 | -6,840 | -10,980 | -4,000 | -5,850 | -9,570 | +1,020 | +3,810 | +6,690 | -37,500 |
| fund_v3 | TA | +1,600 | -17,320 | -3,100 | -11,500 | -1,240 | +0 | +1,420 | +360 | -1,140 | -3,760 | -34,680 |
| china_pairs | TA | +4,785 | -15,360 | -4,050 | -19,305 | -1,485 | +2,520 | -5,550 | -375 | +2,025 | +5,100 | -31,695 |
| china_pairs | y | +11,400 | -15,660 | -16,065 | -5,130 | -7,455 | -4,920 | -240 | +6,600 | +5,280 | +2,160 | -24,030 |
| stat_arb | pg | +6,640 | -7,040 | -2,980 | -8,020 | -5,640 | -2,440 | -6,380 | -60 | +360 | +2,100 | -23,460 |
| chem_fund | TA | +2,415 | -9,525 | -2,265 | -10,305 | -1,455 | +2,010 | -5,505 | -435 | +285 | +1,410 | -23,370 |
| ks_branch | pp | -664 | -6,564 | -1,644 | -6,552 | +7,924 | -6,280 | -6,044 | -676 | +88 | -1,728 | -22,140 |
| ks_branch | l | -2,524 | -40 | -2,064 | -7,616 | +96 | -4,568 | -2,316 | +160 | -20 | -104 | -18,996 |
| ks_branch | bu | +2,416 | -6,664 | -1,560 | -9,608 | -1,456 | +1,408 | -1,976 | -672 | +64 | +0 | -18,048 |
| chem_fund | pp | -1,162 | -2,468 | -338 | -5,692 | -5,130 | -4,762 | -16,830 | +1,530 | +3,330 | +13,770 | -17,752 |
| fund_v3 | y | +2,120 | -6,960 | -7,380 | -2,160 | -1,720 | +2,460 | -40 | +0 | -2,060 | -1,100 | -16,840 |
| fund_v3 | c | +1,920 | -100 | -1,360 | +3,340 | -2,840 | +2,000 | -11,520 | -4,980 | -1,260 | -300 | -15,100 |
| stat_arb | v | +520 | -2,190 | +0 | -3,660 | +175 | -780 | +660 | -80 | +420 | -9,035 | -13,970 |
same holdings split as 'Live P&L by strategy'; summing a strategy's products reproduces its row there (trading / neither included as their own strategy). Full series: data/strategy_product_daily.csv

## Paper strategies (weight 0 in the forward book: tracked, not traded)
| strategy | weight 0 since | bt since (full) | bt last 20d | drawdown now | worst before pause | 60d Sharpe | paper-live since (full) | paper days | book coverage |
|---|---|---|---|---|---|---|---|---|---|
| agri_event | 2026-11-02 | -2,615 | -92,455 | -146,245 | -149,845 | -2.71 | -5,235 | 9 | 100% |
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
| agri_event | +9,350 |
| stat_arb | +16,744 |
| all | +24,827 |
| strategy | vintages | latest | cause | commit | rows restated | net change (full size) |
|---|---|---|---|---|---|---|
| ks_branch | 2 | 20261102090932_cbbdd7664522.csv | unknown | cbbdd76 | 165 | +341,255 |
| ks_ext | 2 | 20261102090932_1a03a09367cb.csv | unknown | 1a03a09 | 91 | +31,590 |
| china_pairs | 2 | 20261102090932_51a17747e0e0.csv | unknown | 51a1774 | 44 | -46,815 |
| chem_fund | 3 | 20261105091241_a98238f08285.csv | data | a98238f | 1 | -480 |
| fund_v3 | 4 | 20261110091023_0712a0472bd7.csv | data | 0712a04 | 3 | -184 |
| ks_outright | 1 | 20261111091151_49ac2cfb3881.csv | first | 49ac2cf | 0 | +0 |
| fpe | 1 | 20261111091151_01eab32dfcbf.csv | first | 01eab32 | 0 | +0 |
| agri_event | 10 | 20261113091334_8f0b7b90cc1f.csv | data | 8f0b7b9 | 24 | +750 |
| stat_arb | 3 | 20261113091334_9f7e9a742805.csv | data | 9f7e9a7 | 1 | +16 |
full series: data/backtest/vintages/<strategy>/; index: data/backtest/vintages/index.csv

## Data health
decision-price coverage (2026-11-13): 100% of held notional benchmarked (0 contract(s) unbenchmarked); 15 contract(s) (13%) first decided after the 0900 snap, so they straddle their own overnight leg
scale: 1 (since 2026-09-09)
regime: forward (merged weighted book) since 2026-08-31; 49 forward day(s), 8 legacy day(s)
merge weights (2026-11-13): ks_branch 0.8, fund_v3 2, china_pairs 1.5, ks_ext 0.25, chem_fund 1.5, agri_event 0, stat_arb 1, fpe 0.1, ks_outright 0.5
as-shipped pins: 57 live day(s) pinned; current series diverges from pins on chem_fund: 30 day(s), max 9,725 CNY, fund_v3: 49 day(s), max 22,683 CNY, ks_branch: 43 day(s), max 82,125 CNY, ks_ext: 35 day(s), max 42,170 CNY, stat_arb: 43 day(s), max 9,982 CNY, china_pairs: 23 day(s), max 10,910 CNY, agri_event: 11 day(s), max 7,250 CNY; standing counts -- a divergence is announced as an alert once, the first run it appears, and kept here afterwards
inbox ks summary mtime: 2026-11-13 05:57 UTC
