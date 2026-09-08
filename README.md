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
  ~/cnexec/inbox/{ks,fundamental,forward}/ (dated books, snap prices, ks
  backtest summary).
- Backtest: incoming/payload_* shipped by
  ensemble_analysis/scripts/ship_backtest_pnl (7 strategies, 2026, full-size,
  plus the forward merge weights and per-source component books).

Regimes (detected per day from the run records, never by date):
- LEGACY (live start 2026-08-18 .. 2026-08-28): the account traded the ks +
  fundamental per-source books unweighted; expected = scale x (ks + fund).
- FORWARD (2026-08-31 on): the account trades ONE merged book of all 7
  signals, weighted upstream (Execution/weights_forward.json); expected =
  scale x sum_i w_i x bt_i, the ideal book is the shipped forward book, and
  per-strategy live attribution is PRO-RATED by weighted full-size lots
  (ill-conditioned splits -- near-offsetting weighted lots -- go to shared).
  Weights and component books are pinned per day, first write wins.

The bridge (account-level, gross):
  live_gross = scale x bt_gross - exec_cost + marking + bookdiff + intraday
               + residual
  live_net   = live_gross - fees + broker_residual
Missing live days accrue into a sticky bucket and are excluded from cum sums.
As-shipped basis: each live day's backtest inputs are PINNED (data/state.json
bt_pinned) once the day matures; upstream history regenerations (model
updates) never rewrite already-reconciled days -- divergence is alerted once
and counted in Data health.
Alerts (top of every report): missing days, stale inbox, scale changes,
merge weight changes, missing forward/component books, backtest history
revisions, unbenchmarked slippage, broker diffs, residual blowouts, ship
staleness, ks cross-check.
- BACKTEST REVISED compares every mature row (date < series max) against the
  values stored at the previous run (state.json backtest_mature_rows), so it
  fires only when a value actually moved; dates carried by the pins are left
  to the BT REVISED vs PINS alert.  (Until 2026-09-02 it hashed the whole
  stable region, which grows daily, so it fired for all seven books every day.)
- Window alignment (2026-09-08): a backtest row D is 09:00(D)->09:00(D+1),
  a live day is settle(D-1)->settle(D).  The marking term benchmarks at each
  contract's FIRST decision price of the day, so live re-marked is
  09:00(D-1)->09:00(D), and live day D is bridged against backtest row D-1
  (config.BT_ROW_LAG; stat_arb's ledger already books on the realisation
  date, lag 0).  Before this the bench was the last decision (1330) and the
  row was D: every overnight leg sat in the residual with one sign on D and
  its mirror on D+1, and the 2026-09-04 weekend leg alone was -85.8k.
- RESIDUAL still excuses a break-out that a neighbouring day mirrors
  (contracts first decided after 09:00, or with no decision price, straddle
  their own leg); the latest day is judged once the next one reconciles.

Tests: `python -m pytest tests/` (pure functions only; nothing touches the
box).

Optional cron on the box (owner installs; report generation only -- publish
still happens from the local session):
  15 9 * * 1-5 cd $HOME/performance_tracker && ./run_daily.sh >> run.log 2>&1
