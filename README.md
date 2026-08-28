# performance_tracker

Backtest-vs-live performance tracker for the co-shipped book on CME-Server2
(pyexec, environment prod_yingxi). Self-contained: reads cnexec DATA files
only, imports no cnexec code.

This local repo is the CANONICAL git repo (remote: cpeiren/performance_tracker,
private). CME-Server2 holds a plain-file deployment with NO git credentials --
github.com HTTPS is blocked from the box and we deliberately keep no key there.
Data flows box -> local -> GitHub via daily_publish.sh.

Daily flow (driven by the local daily Claude session, see
ensemble_analysis/STRATEGY_HEALTH_CHECK.md section M):
1. Local: ensemble_analysis/scripts/ship_backtest_pnl.py ships the 7
   backtest series (2026, full-size) to CME-Server2:performance_tracker/incoming/.
2. Box:   ssh CME-Server2 'cd performance_tracker && ./run_daily.sh'
   -- ingest (sha256-validated) -> recompute the full live-vs-backtest bridge
   (tracker/reconcile.py holds the exact accounting identity) -> write
   reports/daily/<D>.md + .png (and latest.md / latest.png). Idempotent.
3. Local: ./daily_publish.sh -- scp data/ + reports/ off the box into this
   repo, commit, push with local credentials.

Code changes: edit here, then ./deploy.sh to push code files to the box.

Inputs (on the box):
- Live: ~/cnexec/pnl/{daily_summary.csv,daily_pnl_<D>.csv,state_<D>.json},
  ~/cnexec/analysis/exec_summary.csv, ~/cnexec/pyexec_runs/detail/<D>.jsonl,
  ~/cnexec/inbox/{ks,fundamental}/ (dated books, snap prices, ks backtest
  summary).
- Backtest: incoming/payload_* shipped by
  ensemble_analysis/scripts/ship_backtest_pnl (7 strategies, 2026, full-size).

The bridge (account-level, gross):
  live_gross = scale x bt_gross - exec_cost + marking + bookdiff + residual
               + broker_basis
  live_net   = live_gross - fees + broker_residual
Missing live days accrue into a sticky bucket and are excluded from cum sums.
Alerts (top of every report): missing days, stale inbox, scale changes,
backtest history revisions, unbenchmarked slippage, broker diffs, residual
blowouts, ship staleness, ks cross-check.

Optional cron on the box (owner installs; report generation only -- publish
still happens from the local session):
  15 9 * * 1-5 cd $HOME/performance_tracker && ./run_daily.sh >> run.log 2>&1
