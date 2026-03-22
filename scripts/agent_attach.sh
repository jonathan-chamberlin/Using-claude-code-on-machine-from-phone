#!/usr/bin/env bash
SESSION="${1:?Usage: agent_attach.sh <session_name>}"
tmux attach-session -t "$SESSION"
