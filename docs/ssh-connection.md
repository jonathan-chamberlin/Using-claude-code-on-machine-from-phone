# SSH Connection via Tailscale

## Connection Details

- **Tailscale IP**: 100.83.13.123
- **Username**: jonathanchamberlin
- **Auth**: SSH key only (no password)
- **Connection string**: `ssh jonathanchamberlin@100.83.13.123`

## Public Key

```
ssh-ed25519 AAAAC3NzaC1lZDI1NTE5AAAAIE4LDJbQeB7xGw1eWOtcHcIFFFQj0nOJrW64wBjpHXYQ mac-automation
```

## Setup: Blink Shell (iOS, recommended)

1. Open Blink Shell
2. Type `config` to open settings
3. Go to **Keys** > **+** > **Import from clipboard**
4. On your Mac, copy the private key: `cat ~/.ssh/id_ed25519 | pbcopy`
5. Paste into Blink Shell and save with name "mac"
6. Go to **Hosts** > **+**
   - Host: `mac`
   - Hostname: `100.83.13.123`
   - User: `jonathanchamberlin`
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
   - Hostname: `100.83.13.123`
   - Username: `jonathanchamberlin`
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
