#!/usr/bin/env bash
# Weekly summary on CME-Server2 (Saturday cron, owner installs).
# Reads only what run_daily.sh already wrote under data/; writes
# reports/weekly/<Friday>.md + reports/latest_weekly.md.  Safe to rerun.
set -u
cd "$(dirname "$0")"
PY="$HOME/miniforge3/bin/python"
exec "$PY" -m tracker.weekly "$@"
