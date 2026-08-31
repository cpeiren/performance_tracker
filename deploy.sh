#!/usr/bin/env bash
# Push tracker CODE changes from this repo to CME-Server2 (data flows the
# other way, via daily_publish.sh).  Fails loudly: any scp error aborts,
# and the deployed files are checksum-verified against the local tree
# (2026-08-31: a silent scp failure printed "deployed" with stale code on
# the box).
set -euo pipefail
cd "$(dirname "$0")"
scp -q config.py run_daily.sh README.md .gitignore CME-Server2:performance_tracker/
scp -q tracker/*.py CME-Server2:performance_tracker/tracker/
local_sum=$(md5sum config.py run_daily.sh tracker/*.py | awk '{print $1}' | sort | md5sum | awk '{print $1}')
remote_sum=$(ssh CME-Server2 'cd performance_tracker && md5sum config.py run_daily.sh tracker/*.py' | awk '{print $1}' | sort | md5sum | awk '{print $1}')
if [ "$local_sum" != "$remote_sum" ]; then
    echo "DEPLOY FAILED: checksum mismatch after copy (local $local_sum, box $remote_sum)" >&2
    exit 1
fi
echo "deployed code to CME-Server2:performance_tracker (verified $local_sum)"
