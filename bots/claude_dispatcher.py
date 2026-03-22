#!/usr/bin/env python3
"""Telegram bot that dispatches Claude agent tasks via tmux."""

import os
import subprocess
from pathlib import Path

from dotenv import load_dotenv
from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, filters

BASE_DIR = Path(__file__).resolve().parent.parent
AGENT_RUN = BASE_DIR / "scripts" / "agent_run.sh"
LOG_DIR = BASE_DIR / "logs" / "agent_sessions"

load_dotenv(BASE_DIR / ".env")

BOT_TOKEN = os.environ["BOT_TOKEN"]
ALLOWED_IDS = {int(uid.strip()) for uid in os.environ["MY_USER_ID"].split(",") if uid.strip()}


def is_allowed(update: Update) -> bool:
    return update.effective_user and update.effective_user.id in ALLOWED_IDS


async def handle_task(update: Update, context) -> None:
    if not is_allowed(update):
        return
    task = update.message.text
    result = subprocess.run(
        [str(AGENT_RUN), task],
        capture_output=True, text=True, timeout=10,
    )
    session_name = result.stdout.strip()
    if result.returncode == 0 and session_name:
        await update.message.reply_text(f"Started session: {session_name}")
    else:
        await update.message.reply_text(f"Failed to start:\n{result.stderr.strip()}")


async def cmd_status(update: Update, context) -> None:
    if not is_allowed(update):
        return
    result = subprocess.run(["tmux", "ls"], capture_output=True, text=True)
    output = result.stdout.strip() or result.stderr.strip() or "No active sessions."
    await update.message.reply_text(output)


async def cmd_log(update: Update, context) -> None:
    if not is_allowed(update):
        return
    if not context.args:
        await update.message.reply_text("Usage: /log <session_name>")
        return
    session = context.args[0]
    log_file = LOG_DIR / f"{session}.log"
    if not log_file.exists():
        await update.message.reply_text(f"No log found for session: {session}")
        return
    result = subprocess.run(
        ["tail", "-50", str(log_file)],
        capture_output=True, text=True,
    )
    text = result.stdout.strip() or "(empty log)"
    # Telegram messages max 4096 chars
    if len(text) > 4000:
        text = text[-4000:]
    await update.message.reply_text(text)


async def cmd_kill(update: Update, context) -> None:
    if not is_allowed(update):
        return
    if not context.args:
        await update.message.reply_text("Usage: /kill <session_name>")
        return
    session = context.args[0]
    result = subprocess.run(
        ["tmux", "kill-session", "-t", session],
        capture_output=True, text=True,
    )
    if result.returncode == 0:
        await update.message.reply_text(f"Killed session: {session}")
    else:
        await update.message.reply_text(f"Error: {result.stderr.strip()}")


def main() -> None:
    app = Application.builder().token(BOT_TOKEN).build()
    app.add_handler(CommandHandler("status", cmd_status))
    app.add_handler(CommandHandler("log", cmd_log))
    app.add_handler(CommandHandler("kill", cmd_kill))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_task))
    app.run_polling()


if __name__ == "__main__":
    main()
