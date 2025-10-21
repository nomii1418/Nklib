#!/bin/bash
# Start script for Telegram bot

set -e

echo "🤖 Starting Telegram Bot..."

# Install dependencies if needed
if [ ! -d "venv" ]; then
    python3 -m venv venv
    source venv/bin/activate
    pip install -r bot/requirements.txt
else
    source venv/bin/activate
fi

# Start bot
cd bot
exec python telegram_bot.py
