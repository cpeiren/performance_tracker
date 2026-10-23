# Performance tracker - 2026-10-23   (reconciled through 2026-10-23)

## ALERTS
- WEIGHTS 2026-10-09: day's own merge weights not shipped yet -- carried forward from an earlier day.
- WEIGHTS 2026-10-16: day's own merge weights not shipped yet -- carried forward from an earlier day.
- WEIGHTS 2026-10-22: day's own merge weights not shipped yet -- carried forward from an earlier day.
- BT PENDING 2026-10-23: no mature backtest row for stat_arb (nonzero weight) -- day reconciled WITHOUT that sleeve's expected; its live P&L sits in bt_pending_live, not resid, until the rows ship.
- WEIGHTS CHANGE on 2026-09-01: ks_ext: 0.0->0.25.
- WEIGHTS CHANGE on 2026-09-02: stat_arb: 1.0->0.0.
- WEIGHTS CHANGE on 2026-09-03: stat_arb: 0.0->1.0.
- MISSING LIVE DAY 2026-08-28: trading day with a backtest row but no daily_pnl/state file; excluded from the bridge, expected pnl held in the missing-day bucket.
- SCALE 2026-08-28: no usable run record; previous scale carried forward.
- SCALE 2026-09-25: no usable run record; previous scale carried forward.
- SCALE CHANGE on 2026-08-27: now 0.2.
- SCALE CHANGE on 2026-09-01: now 0.5.
- SCALE CHANGE on 2026-09-09: now 1.
- BACKTEST REVISED: agri_event -- 2 mature row(s) changed since last run (net -600 CNY, largest 2026-02-25 +9705 -> +9055; first 2026-02-25, last 2026-03-09). Regeneration upstream; baseline re-set.
- SLIPPAGE 2026-10-23: 2 unbenchmarked leg(s), -20 CNY exec cost without a shipped decision price.
- RESIDUAL 2026-08-27: -17267 CNY vs trailing median |resid| 2062, offset by neither neighbour (2026-08-26 +3749, 2026-08-31 -17348) -- attribution quality changed. (A break-out that a neighbouring day mirrors is the backtest/live day-window straddle and is not alerted.)
- RESIDUAL 2026-08-31: -17348 CNY vs trailing median |resid| 2277, offset by neither neighbour (2026-08-27 -17267, 2026-09-01 -8190) -- attribution quality changed. (A break-out that a neighbouring day mirrors is the backtest/live day-window straddle and is not alerted.)
- RESIDUAL 2026-09-01: -8190 CNY vs trailing median |resid| 2492, offset by neither neighbour (2026-08-31 -17348, 2026-09-02 -30063) -- attribution quality changed. (A break-out that a neighbouring day mirrors is the backtest/live day-window straddle and is not alerted.)
- RESIDUAL 2026-09-02: -30063 CNY vs trailing median |resid| 3121, offset by neither neighbour (2026-09-01 -8190, 2026-09-03 -29049) -- attribution quality changed. (A break-out that a neighbouring day mirrors is the backtest/live day-window straddle and is not alerted.)
- RESIDUAL 2026-09-03: -29049 CNY vs trailing median |resid| 3941, offset by neither neighbour (2026-09-02 -30063, 2026-09-04 -5584) -- attribution quality changed. (A break-out that a neighbouring day mirrors is the backtest/live day-window straddle and is not alerted.)
- RESIDUAL 2026-09-16: -103509 CNY vs trailing median |resid| 22936, offset by neither neighbour (2026-09-15 -28634, 2026-09-17 +23811) -- attribution quality changed. (A break-out that a neighbouring day mirrors is the backtest/live day-window straddle and is not alerted.)

## Latest reconciled day (2026-10-23, forward regime, PROVISIONAL: marked at the 16:00 close, re-marked to settlement after the next capture)
live gross -33,965 | expected (1 x bt -27,565) = -27,565 | gap -6,400
  exec_cost -330 (slip -310, unbench -20) | marking -33,020 | bookdiff +2,340 (carry +9,800, new -7,460) | intraday +0 | offbook +0 (0 contract(s)) | residual +19,458 (live re-marked to first decision, vs the previous backtest row)
  PARTIAL: no backtest row yet for stat_arb -- expected excludes it; its live P&L +4,493 is held out of resid
  fees +647 | broker residual +0 -> live net -34,612

## Cumulative bridge (live since 2026-08-18, 42 reconciled days, 1 with a sleeve's backtest pending)
| expected | -exec | +marking | +bookdiff | +intraday | +offbook | +bt pending | +resid | = live gross | -fees | +broker_resid | = live net |
|---|---|---|---|---|---|---|---|---|---|---|---|
| +610,553 | -15,885 | -2,970 | +90,252 | -2,108 | -50 | +4,493 | -104,060 | +580,225 | -39,300 | +4,495 | +545,420 |
missing live days excluded: 2026-08-28 (expected +4,849 held in bucket)

## Stats (daily CNY pnl)
| window | days | total | sharpe | mdd | hit |
|---|---|---|---|---|---|
| live net live-to-date | 42 | +545,420 | 3.61 | -330,281 | 60% |
| live net last-20d | 20 | +296,618 | 3.83 | -111,994 | 60% | (small sample)
| live net 2026-YTD | 42 | +545,420 | 3.61 | -330,281 | 60% |
| bt scaled live-to-date | 42 | +610,553 | 4.07 | -342,266 | 69% |
| bt scaled last-20d | 20 | +309,147 | 4.18 | -149,776 | 65% | (small sample)
| bt scaled 2026-YTD | 42 | +610,553 | 4.07 | -342,266 | 69% |

## Slippage (+ = cost; bps vs benchmarked notional)
| day | lots | notional M | slip total | drift | exec | bps | unbench legs | unbench CNY |
|---|---|---|---|---|---|---|---|---|
| 2026-10-12 | 306 | 13.1 | +615 | +618 | -2 | +0.47 | 1 | -15 |
| 2026-10-13 | 400 | 17.5 | +1,545 | +1,368 | +178 | +0.91 | 3 | -105 |
| 2026-10-14 | 483 | 23.2 | +5,880 | +5,285 | +595 | +2.85 | 6 | +1,205 |
| 2026-10-15 | 343 | 17.6 | +7,540 | +6,830 | +710 | +5.20 | 8 | +350 |
| 2026-10-16 | 295 | 15.6 | +1,280 | +558 | +722 | +0.85 | 3 | +35 |
| 2026-10-19 | 384 | 24.3 | -6,565 | -7,905 | +1,340 | -2.70 | 0 | +0 |
| 2026-10-20 | 476 | 30.2 | -7,010 | -8,490 | +1,480 | -2.49 | 6 | +145 |
| 2026-10-21 | 342 | 21.4 | +3,385 | +2,920 | +465 | +2.04 | 6 | +270 |
| 2026-10-22 | 408 | 18.0 | +1,025 | +60 | +965 | +0.58 | 2 | +30 |
| 2026-10-23 | 345 | 14.2 | -310 | -1,435 | +1,125 | -0.23 | 2 | -20 |
| live window (42d) | 15123 | 936.0 | +2,170 | -40,782 | +42,952 | +0.03 | 223 | +13,715 |
exec-only bps over the window: +0.50; benchmark coverage 92% of traded notional

| product | days | lots | notional M | drift | exec (incl. unbench) | all-in | bps |
|---|---|---|---|---|---|---|---|
| IH | 25 | 104 | 87.1 | -28,890 | +5,190 | -23,700 | -2.72 |
| IF | 13 | 56 | 73.5 | -23,700 | +3,000 | -20,700 | -2.81 |
| CY | 31 | 242 | 26.8 | +11,000 | +4,275 | +15,275 | +5.69 |
| bu | 35 | 387 | 18.6 | -12,385 | +1,465 | -10,920 | -5.87 |
| FG | 41 | 737 | 13.5 | +5,450 | +2,610 | +8,060 | +5.96 |
| pg | 22 | 36 | 4.8 | +7,710 | +210 | +7,920 | +16.38 |
| SF | 38 | 371 | 11.2 | +7,240 | +575 | +7,815 | +6.97 |
| rb | 35 | 1052 | 32.7 | +9,860 | -2,910 | +6,950 | +2.12 |
| PF | 33 | 192 | 7.9 | -6,780 | +570 | -6,210 | -7.82 |
| y | 36 | 245 | 21.9 | +3,990 | +2,120 | +6,110 | +2.79 |
| cs | 40 | 854 | 21.4 | +1,245 | +4,610 | +5,855 | +2.73 |
| ru | 25 | 82 | 15.9 | +6,025 | -250 | +5,775 | +3.64 |
| hc | 36 | 1249 | 41.5 | -9,640 | +4,440 | -5,200 | -1.25 |
| a | 38 | 498 | 26.2 | +2,495 | +2,530 | +5,025 | +1.92 |
| SA | 38 | 499 | 10.2 | +3,540 | +760 | +4,300 | +4.22 |
| other (34) | - | 8519 | 522.6 | -17,942 | +27,472 | +9,530 | +0.18 |
| all products | - | 15123 | 936.0 | -40,782 | +56,668 | +15,885 | +0.17 |
ranked by |all-in| over the live window (all-in = drift + exec = the bridge's exec_cost by product); product bps are vs traded notional

## Per strategy
| strategy | live? | bt 2026 pnl (full) | bt scaled+weighted (live window) | live attributed | note |
|---|---|---|---|---|---|
| Calendar main pool (branch) | yes | +830,280 | +135,637 | +328,693 | forward w=0.8 |
| Fundamental factor | yes | +841,364 | +417,225 | +321,554 | forward w=2 |
| Cross-product pairs | yes | +112,000 | +11,678 | -43,650 | forward w=1.5 |
| Calendar extended pool | yes | +397,635 | -1,928 | +83,772 | forward w=0.25 |
| Chemical fundamental | yes | +455,705 | +40,346 | -48,806 | forward w=1.5 |
| Agriculture event-driven | yes | +99,110 | -40,778 | -73,511 | forward w=1 |
| Factor-neutral stat arb | yes | +343,707 | +48,374 | -53,332 | forward w=1 |
| shared bucket | - | - | - | +62,900 | legacy multi-holder / forward offsetting (split refused, not a cost) |
| neither bucket (no target) | - | - | - | +2,605 | named by no book that day or the day before |
forward-day attribution is pro-rated by weighted full-size lots; legacy days remain exclusive-holder. A contract the day's own books do not name resolves against the previous same-regime day, so a roll-out's exit P&L is charged to whoever held it.

## Live P&L by strategy, last 10 reconciled days (attributed gross CNY)
| day | ks_branch | fund_v3 | china_pairs | ks_ext | chem_fund | agri_event | stat_arb | shared | neither | total |
|---|---|---|---|---|---|---|---|---|---|---|
| 2026-10-12 | +63,246 | +27,008 | +4,425 | +9,007 | -10,069 | +5,000 | +10,563 | +3,375 | +0 | +112,555 |
| 2026-10-13 | +38,061 | +17,581 | -7,062 | +3,387 | +16,875 | +1,064 | +8,773 | +4,410 | +0 | +83,090 |
| 2026-10-14 | +6,623 | +12,054 | -6,499 | +14,223 | +4,998 | +2,429 | +5,836 | +9,195 | +0 | +48,860 |
| 2026-10-15 | +3,186 | -33,709 | +15,924 | +20,056 | -561 | -19,940 | -5,537 | +425 | +0 | -20,155 |
| 2026-10-16 | +9,168 | -13,010 | +8,080 | +3,561 | +894 | -9,252 | -6,757 | -3,020 | +765 | -9,570 |
| 2026-10-19 | +12,920 | +34,833 | -10,092 | +12,667 | -8,809 | -13,690 | +6,759 | -5,495 | +0 | +29,095 |
| 2026-10-20 | -4,132 | +3,630 | +12,432 | +5,076 | -12,713 | -4,150 | -10,662 | +3,520 | +0 | -7,000 |
| 2026-10-21 | -8,066 | +33,024 | -3,404 | -932 | -3,412 | +10,931 | +9,829 | +1,240 | +0 | +39,210 |
| 2026-10-22 | +15,638 | +2,987 | +8,858 | -941 | +3,220 | -5,947 | -1,414 | -6,100 | +1,170 | +17,470 |
| 2026-10-23 | -28,386 | +17,131 | +12,873 | -2,971 | +3,827 | -11,142 | +4,493 | -29,790 | +0 | -33,965 |
| sum | +108,259 | +101,530 | +35,536 | +63,134 | -5,750 | -44,696 | +21,883 | -22,240 | +1,935 | +259,590 |
forward days pro-rate each contract's live P&L by weighted full-size lots; total foots to live gross. Live-window sums: 'Per strategy' above; full series: data/per_strategy_daily.csv (attributed)

## Per strategy gap by day, last 10 reconciled days (live attributed - expected, CNY)
| day | ks_branch | fund_v3 | china_pairs | ks_ext | chem_fund | agri_event | stat_arb | total |
|---|---|---|---|---|---|---|---|---|
| 2026-10-12 | +19,954 | -4,423 | +9,892 | +6,639 | -9,611 | -14,085 | -10,105 | -1,738 |
| 2026-10-13 | -45,299 | +34,613 | -10,025 | -5,502 | +3,188 | +804 | -7,499 | -29,719 |
| 2026-10-14 | +17,247 | +3,007 | +1,188 | +2,748 | -19,377 | +1,764 | +4,164 | +10,741 |
| 2026-10-15 | -36,414 | -9,456 | -2,623 | +17,955 | +7,351 | +1,570 | -9,674 | -31,290 |
| 2026-10-16 | +5,352 | +10,099 | +1,525 | -15,697 | +5,349 | -1,412 | +901 | +6,117 |
| 2026-10-19 | +13,512 | -1,464 | -2,299 | +14,484 | -9,964 | -10,260 | -949 | +3,059 |
| 2026-10-20 | +12,332 | +4,765 | +9,395 | +2,383 | -12,803 | +4,770 | +5,621 | +26,461 |
| 2026-10-21 | -4,810 | +12,753 | +1,561 | -2,126 | -600 | +4,511 | +4,283 | +15,572 |
| 2026-10-22 | +35,150 | -18,945 | +3,226 | -302 | +1,652 | -9,177 | -4,527 | +7,077 |
| 2026-10-23 | -16,230 | +21,914 | +3,356 | +1,038 | -2,878 | +11,698 | - | +18,898 |
| sum | +795 | +52,863 | +15,196 | +21,619 | -37,693 | -9,816 | -17,785 | +25,179 |
full series: data/per_strategy_daily.csv (day, strategy, expected, attributed, gap); a strategy's daily total foots to expected - live_gross once the shared and neither buckets are added. '-' = that sleeve's backtest row has not shipped yet (BT PENDING).

## Live P&L by product, last 10 reconciled days (gross CNY, worst first)
| product | 10-12 | 10-13 | 10-14 | 10-15 | 10-16 | 10-19 | 10-20 | 10-21 | 10-22 | 10-23 | 10d sum | live window |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| SA | -19,320 | -18,180 | -22,440 | -12,380 | +840 | +11,140 | -6,740 | +5,740 | -16,300 | +29,260 | -48,380 | -44,700 |
| CY | -550 | -475 | +9,425 | -3,800 | -5,750 | -14,100 | -5,225 | +75 | -3,875 | +50 | -24,225 | -21,825 |
| m | +880 | -1,120 | -2,930 | -4,010 | +2,480 | -570 | -8,680 | +840 | -6,140 | -4,300 | -23,550 | -18,150 |
| OI | +4,960 | -1,320 | +3,720 | -17,010 | +4,280 | +2,100 | +790 | -2,780 | -1,310 | -12,120 | -18,690 | -30,810 |
| cu | -3,900 | -1,200 | +900 | -4,200 | -1,200 | -900 | -3,600 | +3,300 | -3,000 | -4,500 | -18,300 | -28,600 |
| rb | -10,500 | +4,880 | -1,380 | +1,600 | +430 | -1,510 | -2,940 | +5,940 | -10,050 | -3,080 | -16,610 | +129,320 |
| cs | -2,150 | +820 | +2,100 | +1,520 | +2,570 | +10,650 | -5,780 | +9,980 | -670 | -32,840 | -13,800 | +125,780 |
| ru | +12,400 | -3,750 | -8,250 | -9,950 | +2,350 | -1,500 | -150 | -3,900 | +900 | +900 | -10,950 | +10,400 |
| zn | +4,800 | -4,125 | -2,000 | -4,600 | -4,800 | +6,200 | -1,650 | +200 | +2,300 | -6,925 | -10,600 | +10,200 |
| b | -3,250 | +3,720 | +2,090 | -4,360 | -4,570 | +2,760 | -1,000 | -4,120 | -4,370 | +5,640 | -7,460 | +2,870 |
| y | +3,540 | +4,250 | -1,730 | +5,090 | +1,060 | -880 | -3,410 | -800 | -2,170 | -10,040 | -5,090 | -34,490 |
| TA | -4,020 | +580 | +1,900 | -730 | -1,530 | +2,900 | -430 | +2,460 | -950 | -4,980 | -4,800 | +29,990 |
| pp | -190 | +9,920 | +7,690 | -660 | +4,430 | +630 | -4,005 | -11,800 | -2,460 | -7,320 | -3,765 | -6,060 |
| l | -100 | +2,930 | +11,900 | -7,120 | +6,315 | -785 | -1,295 | +185 | -1,280 | -14,265 | -3,515 | +17,685 |
| i | +350 | -4,200 | -3,600 | -2,050 | +1,200 | -1,100 | +1,150 | +300 | +9,400 | -2,900 | -1,450 | +9,550 |
| other (24) | +56,265 | +9,035 | +14,970 | -21,970 | +6,960 | -4,425 | -1,175 | -300 | +34,375 | +25,460 | +119,195 | +281,640 |
| pb | +2,925 | +9,025 | +7,500 | +1,475 | -175 | -775 | +425 | -525 | -300 | -650 | +18,925 | +29,975 |
| CF | +9,125 | -1,150 | +3,500 | +1,100 | -600 | -7,625 | +1,075 | +13,325 | +1,250 | +800 | +20,800 | -44,150 |
| SH | +990 | +6,660 | +4,140 | +4,320 | +4,020 | +3,420 | -270 | +1,350 | -1,260 | -2,190 | +21,180 | +35,220 |
| hc | +15,150 | -9,710 | -4,590 | +1,130 | -1,590 | +3,390 | +2,130 | -1,440 | +7,230 | +9,490 | +21,190 | -161,690 |
| lh | +8,640 | +7,200 | +3,840 | +4,160 | +0 | +0 | +0 | +0 | +0 | +0 | +23,840 | +24,000 |
| sp | +3,100 | +3,280 | +2,760 | +2,460 | -1,200 | +4,620 | +5,500 | +2,920 | +1,400 | +2,600 | +27,440 | +34,420 |
| IH | +3,300 | -1,620 | +2,880 | +8,520 | -1,440 | +12,780 | +5,160 | +1,860 | -1,200 | +900 | +31,140 | +63,720 |
| FG | +12,560 | +7,260 | +4,820 | +2,640 | -4,420 | -1,940 | +10,120 | +1,140 | +7,520 | -7,320 | +32,380 | +63,380 |
| bu | +6,350 | +9,180 | +6,620 | +11,020 | +6,170 | -960 | -600 | +3,510 | -520 | +6,290 | +47,060 | -38,100 |
| al | +11,200 | +51,200 | +5,025 | +27,650 | -25,400 | +5,575 | +13,600 | +11,750 | +8,950 | -1,925 | +107,625 | +140,650 |
| all products | +112,555 | +83,090 | +48,860 | -20,155 | -9,570 | +29,095 | -7,000 | +39,210 | +17,470 | -33,965 | +259,590 | +580,225 |
executor total_pnl (holding + trading, settlement-to-settlement once the next capture lands, before fees) summed by product root; 'all products' foots to live gross. Full series: data/product_daily.csv

## Data health
decision-price coverage (2026-10-23): 100% of held notional benchmarked (1 contract(s) unbenchmarked); 10 contract(s) (19%) first decided after the 0900 snap, so they straddle their own overnight leg
scale: 1 (since 2026-09-09)
regime: forward (merged weighted book) since 2026-08-31; 34 forward day(s), 8 legacy day(s)
merge weights (2026-10-23): ks_branch 0.8, fund_v3 2, china_pairs 1.5, ks_ext 0.25, chem_fund 1.5, agri_event 1, stat_arb 1
as-shipped pins: 42 live day(s) pinned; current series diverges from pins on fund_v3: 32 day(s), max 22,683 CNY, ks_branch: 27 day(s), max 33,735 CNY, ks_ext: 29 day(s), max 42,170 CNY, stat_arb: 27 day(s), max 10,347 CNY, china_pairs: 17 day(s), max 2,120 CNY, agri_event: 5 day(s), max 5,680 CNY, chem_fund: 8 day(s), max 3,740 CNY; standing counts -- a divergence is announced as an alert once, the first run it appears, and kept here afterwards
inbox ks summary mtime: 2026-10-23 05:53 UTC
