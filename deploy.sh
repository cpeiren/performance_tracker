#!/usr/bin/env bash
# Push tracker CODE changes from this repo to CME-Server2 (data flows the
# other way, via daily_publish.sh).
set -u
cd "$(dirname "$0")"
scp -q config.py run_daily.sh README.md .gitignore CME-Server2:performance_tracker/
scp -q tracker/*.py CME-Server2:performance_tracker/tracker/
echo "deployed code to CME-Server2:performance_tracker"
