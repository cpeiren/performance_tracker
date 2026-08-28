#!/usr/bin/env bash
# LOCAL publish step (Git Bash, Windows): pull the tracker's state + reports
# off CME-Server2 into this repo and push to GitHub with local credentials.
# The box never holds git credentials.
set -u
cd "$(dirname "$0")"

scp -q -r CME-Server2:performance_tracker/data . || { echo "scp data/ failed" >&2; exit 1; }
scp -q -r CME-Server2:performance_tracker/reports . || { echo "scp reports/ failed" >&2; exit 1; }

git add data/ reports/
if git diff --cached --quiet; then
    echo "publish: nothing new"
    exit 0
fi
git commit -qm "tracker: $(date -u +%F) report" && git push -q \
    && echo "published" \
    || { echo "PUBLISH FAILED: commit or push did not complete" >&2; exit 1; }
