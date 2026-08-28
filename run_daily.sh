#!/usr/bin/env bash
# Daily tracker run on CME-Server2: ingest -> reconcile -> report.
# Idempotent; safe to rerun any number of times per day.
# PUBLISHING happens from the owner's LOCAL daily session (daily_publish.sh
# in the repo), which pulls data/ + reports/ off this box and pushes to
# GitHub -- this box holds no git credentials by design.
set -u
cd "$(dirname "$0")"
PY="$HOME/miniforge3/bin/python"
exec "$PY" -m tracker.main "$@"
