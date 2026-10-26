# Performance tracker - 2026-10-26   (reconciled through 2026-10-26)

## ALERTS
- WEIGHTS 2026-10-09: day's own merge weights not shipped yet -- carried forward from an earlier day.
- WEIGHTS 2026-10-16: day's own merge weights not shipped yet -- carried forward from an earlier day.
- WEIGHTS 2026-10-22: day's own merge weights not shipped yet -- carried forward from an earlier day.
- BT PENDING 2026-10-26: no mature backtest row for stat_arb (nonzero weight) -- day reconciled WITHOUT that sleeve's expected; its live P&L sits in bt_pending_live, not resid, until the rows ship.
- WEIGHTS CHANGE on 2026-09-01: ks_ext: 0.0->0.25.
- WEIGHTS CHANGE on 2026-09-02: stat_arb: 1.0->0.0.
- WEIGHTS CHANGE on 2026-09-03: stat_arb: 0.0->1.0.
- BT REVISED vs PINS: fund_v3 current history differs from pinned as-shipped values on 8 new live-window day(s) (max |diff| 22683 CNY, first 2026-09-29); the bridge keeps the pins.
- MISSING LIVE DAY 2026-08-28: trading day with a backtest row but no daily_pnl/state file; excluded from the bridge, expected pnl held in the missing-day bucket.
- SCALE 2026-08-28: no usable run record; previous scale carried forward.
- SCALE 2026-09-25: no usable run record; previous scale carried forward.
- SCALE CHANGE on 2026-08-27: now 0.2.
- SCALE CHANGE on 2026-09-01: now 0.5.
- SCALE CHANGE on 2026-09-09: now 1.
- BACKTEST REVISED: agri_event -- 2 mature row(s) changed since last run (net +600 CNY, largest 2026-02-25 +9055 -> +9705; first 2026-02-25, last 2026-03-09). Regeneration upstream; baseline re-set.
- SLIPPAGE 2026-10-26: 1 unbenchmarked leg(s), +105 CNY exec cost without a shipped decision price.
- RESIDUAL 2026-08-27: -17267 CNY vs trailing median |resid| 2062, offset by neither neighbour (2026-08-26 +3749, 2026-08-31 -17348) -- attribution quality changed. (A break-out that a neighbouring day mirrors is the backtest/live day-window straddle and is not alerted.)
- RESIDUAL 2026-08-31: -17348 CNY vs trailing median |resid| 2277, offset by neither neighbour (2026-08-27 -17267, 2026-09-01 -8190) -- attribution quality changed. (A break-out that a neighbouring day mirrors is the backtest/live day-window straddle and is not alerted.)
- RESIDUAL 2026-09-01: -8190 CNY vs trailing median |resid| 2492, offset by neither neighbour (2026-08-31 -17348, 2026-09-02 -30063) -- attribution quality changed. (A break-out that a neighbouring day mirrors is the backtest/live day-window straddle and is not alerted.)
- RESIDUAL 2026-09-02: -30063 CNY vs trailing median |resid| 3121, offset by neither neighbour (2026-09-01 -8190, 2026-09-03 -29049) -- attribution quality changed. (A break-out that a neighbouring day mirrors is the backtest/live day-window straddle and is not alerted.)
- RESIDUAL 2026-09-03: -29049 CNY vs trailing median |resid| 3941, offset by neither neighbour (2026-09-02 -30063, 2026-09-04 -5584) -- attribution quality changed. (A break-out that a neighbouring day mirrors is the backtest/live day-window straddle and is not alerted.)
- RESIDUAL 2026-09-16: -103509 CNY vs trailing median |resid| 22936, offset by neither neighbour (2026-09-15 -28634, 2026-09-17 +23811) -- attribution quality changed. (A break-out that a neighbouring day mirrors is the backtest/live day-window straddle and is not alerted.)

## Latest reconciled day (2026-10-26, forward regime, PROVISIONAL: marked at the 16:00 close, re-marked to settlement after the next capture)
live gross -24,960 | expected (1 x bt +11,109) = +11,109 | gap -36,069
  exec_cost +3,235 (slip +3,130, unbench +105) | marking -56,315 | bookdiff +0 (carry +0, new +0) | intraday +0 | offbook +0 (0 contract(s)) | residual +27,222 (live re-marked to first decision, vs the previous backtest row)
  PARTIAL: no backtest row yet for stat_arb -- expected excludes it; its live P&L -3,742 is held out of resid
  fees +942 | broker residual +0 -> live net -25,902

## Cumulative bridge (live since 2026-08-18, 43 reconciled days, 1 with a sleeve's backtest pending)
| expected | -exec | +marking | +bookdiff | +intraday | +offbook | +bt pending | +resid | = live gross | -fees | +broker_resid | = live net |
|---|---|---|---|---|---|---|---|---|---|---|---|
| +636,288 | -19,120 | -35,375 | +90,252 | -2,108 | -50 | -3,742 | -88,470 | +577,675 | -40,242 | +4,496 | +541,929 |
missing live days excluded: 2026-08-28 (expected +4,849 held in bucket)

## Stats (daily CNY pnl)
| window | days | total | sharpe | mdd | hit |
|---|---|---|---|---|---|
| live net live-to-date | 43 | +541,929 | 3.55 | -330,281 | 58% |
| live net last-20d | 20 | +397,614 | 5.77 | -57,748 | 60% | (small sample)
| live net 2026-YTD | 43 | +541,929 | 3.55 | -330,281 | 58% |
| bt scaled live-to-date | 43 | +636,288 | 4.21 | -342,266 | 70% |
| bt scaled last-20d | 20 | +395,235 | 5.67 | -36,981 | 70% | (small sample)
| bt scaled 2026-YTD | 43 | +636,288 | 4.21 | -342,266 | 70% |

## Slippage (+ = cost; bps vs benchmarked notional)
| day | lots | notional M | slip total | drift | exec | bps | unbench legs | unbench CNY |
|---|---|---|---|---|---|---|---|---|
| 2026-10-13 | 400 | 17.5 | +1,545 | +1,368 | +178 | +0.91 | 3 | -105 |
| 2026-10-14 | 483 | 23.2 | +5,880 | +5,285 | +595 | +2.85 | 6 | +1,205 |
| 2026-10-15 | 343 | 17.6 | +7,540 | +6,830 | +710 | +5.20 | 8 | +350 |
| 2026-10-16 | 295 | 15.6 | +1,280 | +558 | +722 | +0.85 | 3 | +35 |
| 2026-10-19 | 384 | 24.3 | -6,565 | -7,905 | +1,340 | -2.70 | 0 | +0 |
| 2026-10-20 | 476 | 30.2 | -7,010 | -8,490 | +1,480 | -2.49 | 6 | +145 |
| 2026-10-21 | 342 | 21.4 | +3,385 | +2,920 | +465 | +2.04 | 6 | +270 |
| 2026-10-22 | 408 | 18.0 | +1,025 | +60 | +965 | +0.58 | 2 | +30 |
| 2026-10-23 | 345 | 14.2 | -310 | -1,435 | +1,125 | -0.23 | 2 | -20 |
| 2026-10-26 | 423 | 16.9 | +3,130 | +2,752 | +378 | +1.86 | 1 | +105 |
| live window (43d) | 15546 | 952.9 | +5,300 | -38,030 | +43,330 | +0.06 | 224 | +13,820 |
exec-only bps over the window: +0.49; benchmark coverage 92% of traded notional

| product | days | lots | notional M | drift | exec (incl. unbench) | all-in | bps |
|---|---|---|---|---|---|---|---|
| IH | 25 | 104 | 87.1 | -28,890 | +5,190 | -23,700 | -2.72 |
| IF | 13 | 56 | 73.5 | -23,700 | +3,000 | -20,700 | -2.81 |
| CY | 32 | 246 | 27.3 | +11,175 | +4,300 | +15,475 | +5.67 |
| rb | 36 | 1118 | 34.7 | +15,470 | -3,240 | +12,230 | +3.52 |
| hc | 37 | 1332 | 44.1 | -16,505 | +4,285 | -12,220 | -2.77 |
| bu | 36 | 404 | 19.4 | -12,350 | +1,570 | -10,780 | -5.56 |
| FG | 42 | 746 | 13.7 | +5,600 | +2,520 | +8,120 | +5.94 |
| SF | 39 | 376 | 11.4 | +7,475 | +570 | +8,045 | +7.08 |
| pg | 22 | 36 | 4.8 | +7,710 | +210 | +7,920 | +16.38 |
| a | 39 | 506 | 26.6 | +4,185 | +2,780 | +6,965 | +2.61 |
| y | 37 | 246 | 22.0 | +4,110 | +2,120 | +6,230 | +2.83 |
| PF | 34 | 197 | 8.1 | -6,785 | +565 | -6,220 | -7.63 |
| ru | 25 | 82 | 15.9 | +6,025 | -250 | +5,775 | +3.64 |
| cs | 41 | 892 | 22.4 | +1,050 | +4,515 | +5,565 | +2.49 |
| SR | 38 | 667 | 36.4 | +2,245 | +1,840 | +4,085 | +1.12 |
| other (34) | - | 8538 | 505.4 | -14,845 | +27,175 | +12,330 | +0.24 |
| all products | - | 15546 | 952.9 | -38,030 | +57,150 | +19,120 | +0.20 |
ranked by |all-in| over the live window (all-in = drift + exec = the bridge's exec_cost by product); product bps are vs traded notional

## Per strategy
| strategy | live? | bt 2026 pnl (full) | bt scaled+weighted (live window) | live attributed | note |
|---|---|---|---|---|---|
| Calendar main pool (branch) | yes | +851,115 | +152,305 | +341,554 | forward w=0.8 |
| Fundamental factor | yes | +831,850 | +396,211 | +295,331 | forward w=2 |
| Cross-product pairs | yes | +114,450 | +15,353 | -57,678 | forward w=1.5 |
| Calendar extended pool | yes | +410,970 | +1,406 | +96,438 | forward w=0.25 |
| Chemical fundamental | yes | +463,200 | +51,588 | -38,386 | forward w=1.5 |
| Agriculture event-driven | yes | +97,420 | -43,068 | -77,894 | forward w=1 |
| Factor-neutral stat arb | yes | +357,827 | +62,494 | -57,580 | forward w=1 |
| shared bucket | - | - | - | +73,285 | legacy multi-holder / forward offsetting (split refused, not a cost) |
| neither bucket (no target) | - | - | - | +2,605 | named by no book that day or the day before |
forward-day attribution is pro-rated by weighted full-size lots; legacy days remain exclusive-holder. A contract the day's own books do not name resolves against the previous same-regime day, so a roll-out's exit P&L is charged to whoever held it.

## Live P&L by strategy, last 10 reconciled days (attributed gross CNY)
| day | ks_branch | fund_v3 | china_pairs | ks_ext | chem_fund | agri_event | stat_arb | shared | neither | total |
|---|---|---|---|---|---|---|---|---|---|---|
| 2026-10-13 | +38,061 | +17,581 | -7,062 | +3,387 | +16,875 | +1,064 | +8,773 | +4,410 | +0 | +83,090 |
| 2026-10-14 | +6,623 | +12,054 | -6,499 | +14,223 | +4,998 | +2,429 | +5,836 | +9,195 | +0 | +48,860 |
| 2026-10-15 | +3,186 | -33,709 | +15,924 | +20,056 | -561 | -19,940 | -5,537 | +425 | +0 | -20,155 |
| 2026-10-16 | +9,168 | -13,010 | +8,080 | +3,561 | +894 | -9,252 | -6,757 | -3,020 | +765 | -9,570 |
| 2026-10-19 | +12,920 | +34,833 | -10,092 | +12,667 | -8,809 | -13,690 | +6,759 | -5,495 | +0 | +29,095 |
| 2026-10-20 | -4,132 | +3,630 | +12,432 | +5,076 | -12,713 | -4,150 | -10,662 | +3,520 | +0 | -7,000 |
| 2026-10-21 | -8,066 | +33,024 | -3,404 | -932 | -3,412 | +10,931 | +9,829 | +1,240 | +0 | +39,210 |
| 2026-10-22 | +15,638 | +2,987 | +8,858 | -941 | +3,220 | -5,947 | -1,414 | -6,100 | +1,170 | +17,470 |
| 2026-10-23 | +82 | +21,160 | +5,507 | -3,654 | -891 | -9,641 | +3,986 | -28,105 | +0 | -11,555 |
| 2026-10-26 | -15,607 | -30,252 | -6,662 | +13,349 | +15,139 | -5,884 | -3,742 | +8,700 | +0 | -24,960 |
| sum | +57,874 | +48,299 | +17,083 | +66,793 | +14,739 | -54,079 | +7,072 | -15,230 | +1,935 | +144,485 |
forward days pro-rate each contract's live P&L by weighted full-size lots; total foots to live gross. Live-window sums: 'Per strategy' above; full series: data/per_strategy_daily.csv (attributed)

## Per strategy gap by day, last 10 reconciled days (live attributed - expected, CNY)
| day | ks_branch | fund_v3 | china_pairs | ks_ext | chem_fund | agri_event | stat_arb | total |
|---|---|---|---|---|---|---|---|---|
| 2026-10-13 | -45,299 | +34,613 | -10,025 | -5,502 | +3,188 | +804 | -7,499 | -29,719 |
| 2026-10-14 | +17,247 | +3,007 | +1,188 | +2,748 | -19,377 | +1,764 | +4,164 | +10,741 |
| 2026-10-15 | -36,414 | -9,456 | -2,623 | +17,955 | +7,351 | +1,570 | -9,674 | -31,290 |
| 2026-10-16 | +5,352 | +10,099 | +1,525 | -15,697 | +5,349 | -1,412 | +901 | +6,117 |
| 2026-10-19 | +13,512 | -1,464 | -2,299 | +14,484 | -9,964 | -10,260 | -949 | +3,059 |
| 2026-10-20 | +12,332 | +4,765 | +9,395 | +2,383 | -12,803 | +4,770 | +5,621 | +26,461 |
| 2026-10-21 | -4,810 | +12,753 | +1,561 | -2,126 | -600 | +4,511 | +4,283 | +15,572 |
| 2026-10-22 | +35,150 | -18,945 | +3,226 | -302 | +1,652 | -9,177 | -4,527 | +7,077 |
| 2026-10-23 | +12,238 | +25,438 | -4,010 | +355 | -7,596 | +13,199 | -10,134 | +29,490 |
| 2026-10-26 | -32,275 | -8,732 | -10,337 | +10,015 | +3,896 | -3,594 | - | -41,028 |
| sum | -22,966 | +52,078 | -12,400 | +24,312 | -28,904 | +2,176 | -17,814 | -3,518 |
full series: data/per_strategy_daily.csv (day, strategy, expected, attributed, gap); a strategy's daily total foots to expected - live_gross once the shared and neither buckets are added. '-' = that sleeve's backtest row has not shipped yet (BT PENDING).

## Live P&L by product, last 10 reconciled days (gross CNY, worst first)
| product | 10-13 | 10-14 | 10-15 | 10-16 | 10-19 | 10-20 | 10-21 | 10-22 | 10-23 | 10-26 | 10d sum | live window |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| ru | -3,750 | -8,250 | -9,950 | +2,350 | -1,500 | -150 | -3,900 | +900 | -1,500 | -200 | -25,950 | +7,800 |
| a | +1,650 | -10,020 | -5,790 | +3,420 | -6,220 | -5,600 | +1,130 | +6,190 | +4,610 | -12,510 | -23,140 | +40,230 |
| SA | -18,180 | -22,440 | -12,380 | +840 | +11,140 | -6,740 | +5,740 | -16,300 | +11,440 | +24,400 | -22,480 | -38,120 |
| OI | -1,320 | +3,720 | -17,010 | +4,280 | +2,100 | +790 | -2,780 | -1,310 | -7,940 | -2,360 | -21,830 | -28,990 |
| m | -1,120 | -2,930 | -4,010 | +2,480 | -570 | -8,680 | +840 | -6,140 | -4,080 | +3,740 | -20,470 | -14,190 |
| p | +4,090 | -3,260 | -8,210 | -2,520 | -5,070 | -2,030 | -4,730 | -2,560 | +15,090 | -8,590 | -17,790 | +30,360 |
| l | +2,930 | +11,900 | -7,120 | +6,315 | -785 | -1,295 | +185 | -1,280 | -8,200 | -19,800 | -17,150 | +3,950 |
| CY | -475 | +9,425 | -3,800 | -5,750 | -14,100 | -5,225 | +75 | -3,875 | +1,850 | +6,500 | -15,375 | -13,525 |
| cs | +820 | +2,100 | +1,520 | +2,570 | +10,650 | -5,780 | +9,980 | -670 | -30,200 | -3,550 | -12,560 | +124,870 |
| SR | +840 | -3,880 | -3,570 | +1,530 | -2,260 | -770 | +1,930 | -2,140 | -1,680 | -1,990 | -11,990 | +68,230 |
| rb | +4,880 | -1,380 | +1,600 | +430 | -1,510 | -2,940 | +5,940 | -10,050 | -10,560 | +3,500 | -10,090 | +125,340 |
| pp | +9,920 | +7,690 | -660 | +4,430 | +630 | -4,005 | -11,800 | -2,460 | -4,590 | -8,070 | -8,915 | -11,400 |
| y | +4,250 | -1,730 | +5,090 | +1,060 | -880 | -3,410 | -800 | -2,170 | -1,210 | -8,140 | -7,940 | -33,800 |
| cu | -1,200 | +900 | -4,200 | -1,200 | -900 | -3,600 | +3,300 | -3,000 | -1,500 | +3,600 | -7,800 | -22,000 |
| j | +200 | +150 | -850 | +200 | -3,300 | -1,450 | +1,750 | -2,550 | +250 | -550 | -6,150 | +4,050 |
| other (24) | -590 | +26,510 | -10,000 | +600 | +18,240 | +2,710 | +9,475 | +45,645 | +7,200 | +265 | +100,055 | -12,050 |
| eg | -1,090 | +6,040 | -1,040 | -2,950 | +6,940 | +3,500 | +540 | -1,960 | +1,120 | +3,640 | +14,740 | +7,070 |
| lh | +7,200 | +3,840 | +4,160 | +0 | +0 | +0 | +0 | +0 | +0 | +0 | +15,200 | +24,000 |
| MA | +1,060 | +4,920 | -3,490 | -6,200 | -780 | -3,840 | -3,050 | +3,270 | +3,670 | +20,000 | +15,560 | +21,610 |
| RM | -5,350 | -4,050 | +5,790 | +5,010 | -2,030 | +7,310 | +4,730 | +2,080 | +840 | +1,590 | +15,920 | +12,690 |
| pb | +9,025 | +7,500 | +1,475 | -175 | -775 | +425 | -525 | -300 | -150 | +1,400 | +17,900 | +31,875 |
| FG | +7,260 | +4,820 | +2,640 | -4,420 | -1,940 | +10,120 | +1,140 | +7,520 | +3,720 | -7,140 | +23,720 | +67,280 |
| sp | +3,280 | +2,760 | +2,460 | -1,200 | +4,620 | +5,500 | +2,920 | +1,400 | +3,440 | +3,400 | +28,580 | +38,660 |
| IH | -1,620 | +2,880 | +8,520 | -1,440 | +12,780 | +5,160 | +1,860 | -1,200 | -1,200 | +3,600 | +29,340 | +65,220 |
| bu | +9,180 | +6,620 | +11,020 | +6,170 | -960 | -600 | +3,510 | -520 | +5,450 | -6,520 | +33,350 | -45,460 |
| al | +51,200 | +5,025 | +27,650 | -25,400 | +5,575 | +13,600 | +11,750 | +8,950 | +2,575 | -21,175 | +79,750 | +123,975 |
| all products | +83,090 | +48,860 | -20,155 | -9,570 | +29,095 | -7,000 | +39,210 | +17,470 | -11,555 | -24,960 | +144,485 | +577,675 |
executor total_pnl (holding + trading, settlement-to-settlement once the next capture lands, before fees) summed by product root; 'all products' foots to live gross. Full series: data/product_daily.csv

## Data health
decision-price coverage (2026-10-26): 100% of held notional benchmarked (1 contract(s) unbenchmarked); 10 contract(s) (18%) first decided after the 0900 snap, so they straddle their own overnight leg
scale: 1 (since 2026-09-09)
regime: forward (merged weighted book) since 2026-08-31; 35 forward day(s), 8 legacy day(s)
merge weights (2026-10-26): ks_branch 0.8, fund_v3 2, china_pairs 1.5, ks_ext 0.25, chem_fund 1.5, agri_event 1, stat_arb 1
as-shipped pins: 43 live day(s) pinned; current series diverges from pins on fund_v3: 40 day(s), max 22,683 CNY, 8 NEW, ks_branch: 27 day(s), max 33,735 CNY, ks_ext: 29 day(s), max 42,170 CNY, stat_arb: 27 day(s), max 10,347 CNY, china_pairs: 17 day(s), max 2,120 CNY, agri_event: 5 day(s), max 5,680 CNY, chem_fund: 8 day(s), max 3,740 CNY; standing counts -- a divergence is announced as an alert once, the first run it appears, and kept here afterwards
inbox ks summary mtime: 2026-10-26 05:53 UTC
