"""Configuration for Quotex Telegram Bot (TwelveData edition).

Environment variables you must set:
  BOT_TOKEN   – Telegram bot token
  GROUP_ID    – Channel / group numeric ID, e.g. -1001234567890
  ALL_PAIRS   – Comma list: "EUR/USD,GBP/JPY,BTC/USD"
  TD_API_KEY  – TwelveData API key (free tier works)
"""

import os

BOT_TOKEN: str = os.getenv("BOT_TOKEN", "")
if not BOT_TOKEN:
    raise RuntimeError("Please set BOT_TOKEN.")

GROUP_ID: int = int(os.getenv("GROUP_ID", "-1001234567890"))

ALL_PAIRS = [s.strip() for s in os.getenv(
    "ALL_PAIRS", "EUR/USD,GBP/JPY,BTC/USD").split(",")]

TD_API_KEY: str | None = os.getenv("TD_API_KEY")  # may be None in demo mode

TIMEZONE = "Asia/Kolkata"
