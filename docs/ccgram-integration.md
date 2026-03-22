# ccgram + SSH: Two Remote Access Modes

## When to use what

**Telegram via ccgram** — fire and forget
- Send a task from your phone, get notified when done
- Quick status checks, log reads, session kills
- Works great for autonomous tasks that don't need babysitting
- No SSH key needed, works from any device with Telegram

**SSH via Tailscale** — interactive intervention
- When an agent gets stuck and needs manual debugging
- When you need a full terminal (vim, git, interactive commands)
- When you want to watch Claude work in real-time
- When you need to run commands ccgram can't handle

## SSH workflow for stuck agents

1. Connect from your phone terminal app:
   ```
   ssh jonathanchamberlin@100.83.13.123
   ```

2. List what's running:
   ```
   tmux ls
   ```

3. Attach to the ccgram session:
   ```
   tmux attach -t ccgram
   ```

4. Switch to the stuck window:
   ```
   Ctrl-b, then window number (1, 2, 3...)
   ```
   Or list windows: `Ctrl-b, w`

5. You're now looking at the same Claude Code TUI that ccgram controls. You can type directly, approve permissions, or Ctrl-C to kill a stuck process.

6. Detach when done (leave it running):
   ```
   Ctrl-b, d
   ```

## Both at once

You can use Telegram and SSH simultaneously. ccgram sends keystrokes to tmux — if you're also attached via SSH, you'll see them appear in real-time. Useful for watching what the bot is doing while on a call.
