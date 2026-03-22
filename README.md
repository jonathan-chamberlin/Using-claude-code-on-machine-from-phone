# mac-automation

Remote Claude Code control from Telegram via [ccgram](https://github.com/alexei-led/ccgram). Each Telegram forum topic maps 1:1 to a tmux window running a Claude Code session. Includes tmux helper scripts for local session management and a launchd plist for auto-starting the bot on login.

## Setup

1. Install ccgram: `uv tool install ccgram`
2. Configure `~/.ccgram/.env` with `TELEGRAM_BOT_TOKEN`, `ALLOWED_USERS`, and `CCGRAM_GROUP_ID`
3. Install Claude Code hooks: `ccgram hook --install`
4. Load launchd plist: `launchctl load ~/Library/LaunchAgents/com.user.telegrambot.plist`

## Scripts

- `scripts/agent_run.sh` — Launch Claude in a detached tmux session with JSON logging
- `scripts/agent_status.sh` — List active tmux sessions
- `scripts/agent_attach.sh` — Attach to a session by name
