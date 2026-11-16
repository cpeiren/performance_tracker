# Weekly performance - week of 2026-11-09   (5 trading day(s), 2026-11-09 .. 2026-11-13)

- NOTE: 2026-11-13 is PROVISIONAL (16:00 close mark; re-marked to settlement by the next daily run)
- NOTE: backtest row pending on 2026-11-13: expected excludes that sleeve

## Summary
- Book: live net +349,077 (gross +355,665 vs backtest expected +321,142, gap +34,523); prior week net -39,951.
- Strategies: best fund_v3 +177,260, worst chem_fund -46,838.
- Vs backtest: furthest below ks_branch -15,704, furthest above fund_v3 +29,779.
- Sectors: best nonferrous +189,360, worst petchem -28,935.
- Products: best al +155,075, cs +42,520, AP +33,820; worst c -25,520, v -15,040, pp -14,530.
- Live-to-date: net +620,462 over 57 days, Sharpe 2.95, max DD -330,281, drawdown now +0.

## Book (CNY)
|  | week | prior week | 4 weeks | live-to-date |
|---|---|---|---|---|
| live_gross | +355,665 | -33,425 | +131,950 | +667,365 |
| expected | +321,142 | +35,359 | +36,739 | +642,035 |
| gap | +34,523 | -68,784 | +95,211 | +25,330 |
| exec_cost | -3,540 | +36,065 | +55,585 | +80,520 |
| fees | +6,621 | +6,545 | +23,072 | +58,025 |
| live_net | +349,077 | -39,951 | +115,513 | +620,462 |
gap = live gross - expected (scale x weighted as-shipped backtest); exec_cost and fees are costs (+ = paid).

## Strategies (live attributed gross, CNY, worst week first)
| strategy | week | week expected | week gap | prior week | 4 weeks | live-to-date | weight |
|---|---|---|---|---|---|---|---|
| chem_fund | -46,838 | -31,440 | -15,398 | -5,918 | -34,042 | -22,332 | 1.5 |
| ks_ext | -8,376 | +3,191 | -11,568 | -26,206 | -9,957 | +59,774 | 0.25 |
| stat_arb | -3,280 | +5,930 | -13,055 | +30,550 | +5,800 | +58,538 | 1 |
| agri_event | +0 | +0 | +0 | -3,995 | -97,420 | -152,798 | 0 |
| china_pairs | +13,920 | +10,012 | +3,908 | +17,258 | +21,135 | +8,343 | 1.5 |
| ks_outright | +33,660 | +22,082 | +11,578 | +0 | +33,660 | +33,660 | 0.5 |
| fpe | +54,836 | +48,149 | +6,687 | +0 | +54,836 | +54,836 | 0.1 |
| ks_branch | +100,032 | +115,736 | -15,704 | -31,308 | +6,344 | +131,603 | 0.8 |
| fund_v3 | +177,260 | +147,481 | +29,779 | -1,050 | +103,200 | +433,005 | 2 |
| trading/other | +34,451 | +0 | +34,451 | -12,756 | +48,395 | +62,736 | - |
| total | +355,665 | +321,142 | +34,523 | -33,425 | +131,950 | +667,365 | |
holdings attribution from the daily report: previous-day weighted book x scale x settlement move; `trading/other` is the rest of live gross (fills vs settlement on rebalances, lot rounding) so the column foots; its expected is 0, so its gap is its P&L.  A sleeve-day whose backtest row is pending is left out of expected and gap (as in the daily report).

## Sectors (live gross, CNY, worst week first)
| sector | week | prior week | 4 weeks | live-to-date | best product (week) | worst product (week) |
|---|---|---|---|---|---|---|
| petchem | -28,935 | -49,090 | -129,440 | +72,325 | l +16,005 | v -15,040 |
| financial | +3,480 | -30,840 | +5,640 | +14,940 | IF +5,880 | IH -2,400 |
| grains/live | +13,000 | -21,740 | -29,370 | +114,280 | cs +42,520 | c -25,520 |
| energy | +27,250 | +43,100 | +31,320 | -16,360 | fu +17,140 | bu -2,250 |
| chem/build | +27,315 | -4,380 | +88,935 | +104,945 | FG +28,140 | SA -5,380 |
| softs | +39,180 | -1,750 | -18,115 | +36,830 | AP +33,820 | ru -10,200 |
| oilseeds | +40,880 | -17,930 | -169,610 | -110,580 | b +15,980 | p -4,290 |
| ferrous | +44,135 | +32,885 | +103,320 | +65,720 | hc +22,730 | SF -12,410 |
| nonferrous | +189,360 | +16,320 | +249,270 | +385,265 | al +155,075 | si -500 |
| total | +355,665 | -33,425 | +131,950 | +667,365 | | |

### Sector x strategy, this week (attributed gross, CNY)
| sector | ks_branch | fund_v3 | china_pairs | ks_ext | chem_fund | stat_arb | fpe | ks_outright | trading | neither |
|---|---|---|---|---|---|---|---|---|---|---|
| petchem | -25,232 | -6,740 | +6,788 | +2,100 | -13,102 | -29,780 | +0 | +19,650 | +17,127 | +255 |
| financial | +0 | +0 | +0 | -8,280 | +0 | +0 | +0 | +0 | +11,760 | +0 |
| grains/live | -8,128 | +32,680 | +1,185 | +0 | +0 | -3,040 | +540 | -1,785 | -8,452 | +0 |
| energy | -744 | +13,840 | +0 | +708 | +345 | -1,050 | +0 | +7,590 | +6,562 | +0 |
| chem/build | +12,176 | +10,740 | +0 | +0 | -19,470 | +18,900 | +0 | +5,610 | -641 | +0 |
| softs | -5,048 | +16,180 | -1,238 | -788 | -14,610 | +10,260 | +30,824 | +4,088 | -488 | +0 |
| oilseeds | +22,448 | +10,840 | -9,780 | +0 | +0 | +10,640 | +4,973 | -675 | +2,434 | +0 |
| ferrous | +22,108 | +20,940 | +16,965 | +0 | +0 | -12,970 | +965 | +2,210 | -6,083 | +0 |
| nonferrous | +82,452 | +78,780 | +0 | -2,116 | +0 | +3,760 | +17,534 | -3,028 | +11,978 | +0 |

## Products: 5 worst and 5 best this week (live gross, CNY)
| product | week | prior week | 4 weeks | live-to-date | sector | main driver (week) |
|---|---|---|---|---|---|---|
| c | -25,520 | +3,670 | -16,280 | -41,070 | grains/live | fund_v3 (-16,060) |
| v | -15,040 | +29,950 | -2,230 | +4,745 | petchem | stat_arb (-8,815) |
| pp | -14,530 | -33,985 | -87,100 | -68,205 | petchem | ks_branch (-14,640) |
| SF | -12,410 | +19,750 | +5,400 | +23,340 | ferrous | fund_v3 (-10,940) |
| ru | -10,200 | -5,800 | -30,450 | -16,300 | softs | chem_fund (-13,950) |
| al | +155,075 | -8,675 | +160,500 | +263,200 | nonferrous | fund_v3 (+65,850) |
| cs | +42,520 | -25,410 | -9,090 | +135,350 | grains/live | fund_v3 (+48,740) |
| AP | +33,820 | +0 | +33,820 | +33,820 | softs | fpe (+30,195) |
| FG | +28,140 | -10,900 | +46,680 | +100,540 | chem/build | stat_arb (+16,480) |
| hc | +22,730 | +7,650 | +57,370 | -125,120 | ferrous | china_pairs (+20,805) |
main driver = the strategy with the largest contribution in the product's direction this week. Daily detail: reports/daily/.

