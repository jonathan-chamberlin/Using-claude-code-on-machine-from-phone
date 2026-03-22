#!/usr/bin/env bash
set -euo pipefail

TAILSCALE="/Applications/Tailscale.app/Contents/MacOS/Tailscale"
SCRIPT_DIR="$(cd "$(dirname "$0")/.." && pwd)"
LOG="$SCRIPT_DIR/logs/tailscale.log"
TIMESTAMP=$(date '+%Y-%m-%d %H:%M:%S')

mkdir -p "$(dirname "$LOG")"

TS_STATUS=$("$TAILSCALE" status 2>&1 || true)
TS_IP=$("$TAILSCALE" ip -4 2>/dev/null || echo "unavailable")
SSHD_STATUS=$(ssh -o ConnectTimeout=2 -o BatchMode=yes -o StrictHostKeyChecking=no "$TS_IP" "true" 2>/dev/null && echo "reachable" || echo "unreachable")

echo "[$TIMESTAMP] tailscale_ip=$TS_IP sshd=$SSHD_STATUS"
echo "[$TIMESTAMP] tailscale_ip=$TS_IP sshd=$SSHD_STATUS" >> "$LOG"

if [ "$SSHD_STATUS" = "unreachable" ]; then
    echo "WARNING: SSH not reachable on Tailscale IP"
fi

if [ "$TS_IP" = "unavailable" ]; then
    echo "WARNING: Tailscale not connected"
fi
