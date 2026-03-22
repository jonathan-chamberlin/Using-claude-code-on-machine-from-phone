#!/usr/bin/env bash
set -euo pipefail

export PATH="$HOME/.local/bin:/opt/homebrew/bin:$PATH"

TASK="${1:?Usage: agent_run.sh \"<task>\" [session_name]}"
SESSION="${2:-agent-$(date +%s)}"
LOG_DIR="/Users/jonathanchamberlin/repos/mac-automation/logs/agent_sessions"
LOG_FILE="${LOG_DIR}/${SESSION}.log"

mkdir -p "$LOG_DIR"

tmux new-session -d -s "$SESSION" \
  "claude -p $(printf '%q' "$TASK") --allowedTools 'Bash(*),Edit(*),Read(*),Write(*)' --verbose --output-format stream-json > '${LOG_FILE}' 2>&1"

echo "$SESSION"
