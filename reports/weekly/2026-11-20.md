# Weekly performance - week of 2026-11-16   (5 trading day(s), 2026-11-16 .. 2026-11-20)

- NOTE: 2026-11-20 is PROVISIONAL (16:00 close mark; re-marked to settlement by the next daily run)
- NOTE: backtest row pending on 2026-11-20: expected excludes that sleeve

## Summary
- Book: live net +272,882 (gross +279,645 vs backtest expected +200,742, gap +78,903); prior week net +320,530.
- Strategies: best fund_v3 +219,550, worst fpe -50,745.
- Vs backtest: furthest below fund_v3 -43,418, furthest above ks_ext +35,965.
- Sectors: best ferrous +142,360, worst oilseeds -61,210.
- Products: best i +58,450, cu +58,000, hc +56,790; worst AP -53,330, pp -41,525, a -41,030.
- Live-to-date: net +864,796 over 62 days, Sharpe 3.85, max DD -330,281, drawdown now +0.

## Book (CNY)
|  | week | prior week | 4 weeks | live-to-date |
|---|---|---|---|---|
| live_gross | +279,645 | +327,115 | +315,825 | +918,460 |
| expected | +200,742 | +322,017 | +219,025 | +843,651 |
| gap | +78,903 | +5,098 | +96,800 | +74,809 |
| exec_cost | +13,555 | -3,540 | +78,190 | +94,075 |
| fees | +6,836 | +6,621 | +25,560 | +64,860 |
| live_net | +272,882 | +320,530 | +296,965 | +864,796 |
gap = live gross - expected (scale x weighted as-shipped backtest); exec_cost and fees are costs (+ = paid).

## Strategies (live attributed gross, CNY, worst week first)
| strategy | week | week expected | week gap | prior week | 4 weeks | live-to-date | weight |
|---|---|---|---|---|---|---|---|
| fpe | -50,745 | -67,007 | +16,262 | +51,113 | +368 | +368 | 0.1 |
| stat_arb | -22,355 | -31,650 | +7,545 | -1,975 | -28,975 | +37,488 | 1 |
| ks_outright | -17,825 | -23,538 | +5,712 | +23,345 | +5,520 | +5,520 | 0.5 |
| chem_fund | -13,298 | -28,965 | +15,668 | -57,878 | -50,812 | -46,670 | 1.5 |
| agri_event | +0 | +0 | +0 | +0 | -71,170 | -152,798 | 0 |
| china_pairs | +27,668 | +35,272 | -7,605 | +9,922 | +40,290 | +32,013 | 1.5 |
| ks_branch | +41,296 | +29,344 | +11,952 | +92,788 | +75,976 | +165,655 | 0.8 |
| ks_ext | +60,282 | +24,318 | +35,965 | -11,068 | +42,235 | +117,365 | 0.25 |
| fund_v3 | +219,550 | +262,968 | -43,418 | +196,200 | +272,410 | +671,495 | 2 |
| trading/other | +35,072 | +0 | +35,072 | +24,667 | +29,984 | +88,023 | - |
| total | +279,645 | +200,742 | +78,903 | +327,115 | +315,825 | +918,460 | |
holdings attribution from the daily report: previous-day weighted book x scale x settlement move; `trading/other` is the rest of live gross (fills vs settlement on rebalances, lot rounding) so the column foots; its expected is 0, so its gap is its P&L.  A sleeve-day whose backtest row is pending is left out of expected and gap (as in the daily report).

## Sectors (live gross, CNY, worst week first)
| sector | week | prior week | 4 weeks | live-to-date | best product (week) | worst product (week) |
|---|---|---|---|---|---|---|
| oilseeds | -61,210 | +38,670 | -208,240 | -174,000 | p +27,760 | a -41,030 |
| petchem | -24,010 | -30,675 | -130,340 | +46,575 | v +45,435 | pp -41,525 |
| energy | -1,630 | +19,230 | +14,470 | -26,010 | pg +37,220 | fu -30,940 |
| chem/build | -110 | +21,615 | +55,395 | +99,135 | SA +13,480 | FG -24,980 |
| softs | +3,260 | +34,435 | -9,410 | +35,345 | sp +16,880 | AP -53,330 |
| grains/live | +45,090 | +26,210 | +38,500 | +172,580 | cs +31,850 | lh +6,480 |
| financial | +53,280 | +3,480 | +46,680 | +68,220 | IH +36,120 | IF +17,160 |
| nonferrous | +122,615 | +178,170 | +320,005 | +496,690 | cu +58,000 | sn -13,470 |
| ferrous | +142,360 | +35,980 | +188,765 | +199,925 | i +58,450 | ss -4,150 |
| total | +279,645 | +327,115 | +315,825 | +918,460 | | |

### Sector x strategy, this week (attributed gross, CNY)
| sector | ks_branch | fund_v3 | china_pairs | ks_ext | chem_fund | stat_arb | fpe | ks_outright | trading |
|---|---|---|---|---|---|---|---|---|---|
| oilseeds | +10,432 | -45,100 | +13,695 | +0 | +0 | -37,790 | -3,303 | +1,400 | -544 |
| petchem | -1,032 | +20,460 | +5,452 | +35 | -23,812 | +6,325 | +0 | -26,190 | -5,248 |
| energy | -2,376 | +20,880 | +0 | +558 | -19,215 | +5,710 | +0 | -5,995 | -1,192 |
| chem/build | -6,720 | +2,240 | +0 | +15 | +16,230 | -9,900 | +0 | -2,960 | +985 |
| softs | +26,996 | -9,850 | +4,238 | +350 | +13,500 | +14,185 | -46,040 | -1,328 | +1,209 |
| grains/live | +15,848 | +21,420 | -1,185 | +0 | +0 | -440 | +497 | +9,165 | -215 |
| financial | +0 | +0 | +0 | +46,230 | +0 | +0 | +0 | +0 | +7,050 |
| nonferrous | -35,900 | +181,360 | -4,462 | +13,095 | +0 | +10,360 | -51,721 | +4,210 | +5,673 |
| ferrous | +34,048 | +28,140 | +9,930 | +0 | +0 | -10,805 | +49,822 | +3,872 | +27,353 |

## Products: 5 worst and 5 best this week (live gross, CNY)
| product | week | prior week | 4 weeks | live-to-date | sector | main driver (week) |
|---|---|---|---|---|---|---|
| AP | -53,330 | +33,420 | -19,910 | -19,910 | softs | fpe (-52,747) |
| pp | -41,525 | -27,670 | -119,540 | -122,870 | petchem | china_pairs (-31,890) |
| a | -41,030 | +5,530 | -89,980 | -37,240 | oilseeds | stat_arb (-12,240) |
| y | -35,530 | +7,230 | -117,430 | -143,090 | oilseeds | china_pairs (-35,175) |
| fu | -30,940 | +6,540 | +5,130 | +32,910 | energy | stat_arb (-11,490) |
| i | +58,450 | +21,650 | +52,400 | +65,450 | ferrous | fund_v3 (+25,900) |
| cu | +58,000 | +7,950 | +98,000 | +72,400 | nonferrous | fund_v3 (+100,300) |
| hc | +56,790 | +22,490 | +93,070 | -68,570 | ferrous | china_pairs (+61,350) |
| v | +45,435 | -2,985 | +55,870 | +62,235 | petchem | fund_v3 (+16,090) |
| ni | +39,820 | +3,300 | +29,410 | +9,880 | nonferrous | fund_v3 (+31,760) |
main driver = the strategy with the largest contribution in the product's direction this week. Daily detail: reports/daily/.

