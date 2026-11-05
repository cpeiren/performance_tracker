#!/usr/bin/env bash
# LOCAL publish step (Git Bash, Windows): pull the tracker's state + reports
# off CME-Server2 into this repo and push to GitHub with local credentials.
# The box never holds git credentials.
#
# The fetch is ONE tar stream into a temp file, integrity-checked before the
# working tree is touched, so a dropped connection leaves the clone untouched.
# (Per-file `scp -r` of ~460 files over the ~60 KB/s route took 20+ min, and
# when it died mid-transfer on 2026-11-05 it left a half-updated tree.)
set -u
cd "$(dirname "$0")"

archive=$(mktemp) || exit 1
trap 'rm -f "$archive"' EXIT

ssh -o BatchMode=yes -o ServerAliveInterval=30 CME-Server2 \
    'tar czf - -C performance_tracker data reports' > "$archive" \
    || { echo "PUBLISH FAILED: fetch from CME-Server2 did not complete" >&2; exit 1; }
gzip -t "$archive" \
    || { echo "PUBLISH FAILED: fetched archive is truncated" >&2; exit 1; }
tar xzf "$archive" \
    || { echo "PUBLISH FAILED: extract failed" >&2; exit 1; }

git add data/ reports/
if git diff --cached --quiet; then
    echo "publish: nothing new"
    exit 0
fi
# Name the commit after the data, not the wall clock: the publish date runs a
# day ahead of the reconciled date and has been misread as a stale snapshot.
asof=$(sed -n '1s/.*reconciled through \([0-9-]*\).*/\1/p' reports/latest.md)
git commit -qm "tracker: ${asof:-$(date -u +%F)} report" && git push -q \
    && echo "published" \
    || { echo "PUBLISH FAILED: commit or push did not complete" >&2; exit 1; }
