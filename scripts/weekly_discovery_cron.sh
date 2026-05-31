#!/bin/bash
# launchd entrypoint for the weekly tool discovery.
# Invoked every Sunday by ~/Library/LaunchAgents/com.kitoolnavigator.weekly-discovery.plist
#
# It runs a single headless `claude` agent against the WEEKLY_DISCOVERY.md
# runbook. That agent runs the weekly-tool-discovery workflow, then the
# deterministic seed/capture/cover/deploy/commit tail, and self-corrects blocked
# screenshots. All output is logged.

set -uo pipefail

REPO="/Users/astoeckl/Documents/tool navigator"
cd "$REPO" || { echo "repo not found: $REPO"; exit 1; }

# launchd starts with a minimal environment — restore what the toolchain needs.
export HOME="/Users/astoeckl"
export PATH="/opt/homebrew/bin:/opt/homebrew/opt/python@3.13/libexec/bin:/usr/local/bin:/usr/bin:/bin:/usr/sbin:/sbin:$HOME/.claude/local:$PATH"

mkdir -p scripts/logs
STAMP=$(date '+%Y%m%d_%H%M%S')
LOG="scripts/logs/weekly_${STAMP}.log"

{
  echo "================================================================"
  echo "Weekly tool discovery — started $(date)"
  echo "claude: $(command -v claude)  |  node: $(command -v node)  |  python3: $(command -v python3)"
  echo "================================================================"

  claude -p "$(cat scripts/WEEKLY_DISCOVERY.md)" \
    --dangerously-skip-permissions \
    --max-turns 240 \
    --add-dir "$REPO"
  RC=$?

  echo "================================================================"
  echo "Weekly tool discovery — finished $(date) (claude rc=$RC)"
  echo "================================================================"
} >> "$LOG" 2>&1

# keep only the 12 most recent run logs
ls -1t scripts/logs/weekly_*.log 2>/dev/null | tail -n +13 | xargs rm -f 2>/dev/null || true
