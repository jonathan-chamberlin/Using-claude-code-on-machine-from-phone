# SSH Connection via Tailscale

## Connection Details

- **Tailscale IP**: see `TAILSCALE_IP` in `.env`
- **Username**: see `MAC_USER` in `.env`
- **Auth**: SSH key only (no password)
- **Connection string**: `ssh $MAC_USER@$TAILSCALE_IP`

## Setup: Blink Shell (iOS, recommended)

1. Open Blink Shell
2. Type `config` to open settings
3. Go to **Keys** > **+** > **Import from clipboard**
4. On your Mac, copy the private key: `cat ~/.ssh/id_ed25519 | pbcopy`
5. Paste into Blink Shell and save with name "mac"
6. Go to **Hosts** > **+**
   - Host: `mac`
   - Hostname: (your Tailscale IP from `.env`)
   - User: (your username from `.env`)
   - Key: select "mac"
   - Port: 22
7. Save. Connect by typing `ssh mac` in Blink

## Setup: Termius (iOS, free tier)

1. Open Termius
2. Go to **Keychain** > **+** > **Key**
3. On your Mac, copy the private key: `cat ~/.ssh/id_ed25519 | pbcopy`
4. Tap **Paste from clipboard**, give it label "mac"
5. Go to **Hosts** > **+**
   - Label: `Mac`
   - Hostname: (your Tailscale IP from `.env`)
   - Username: (your username from `.env`)
   - Key: select "mac"
6. Save. Tap the host to connect.

## Attaching to tmux sessions

After connecting via SSH:

```bash
# List sessions
tmux ls

# Attach to ccgram session
tmux attach -t ccgram

# Attach to a specific window
tmux select-window -t ccgram:1
```
