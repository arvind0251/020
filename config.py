# config.py  (hard‑coded version)

# ─── Telegram & Bot settings ────────────────────────────────────────
BOT_TOKEN = "7864815464:AAGiwjulKLxnDP9MuaVhhQZ8fhoPRz3uv2Q"   # ← BotFather token
GROUP_ID  = -1002711451967                                     # ← group / channel ID

# ─── Pairs list ────────────────────────────────────────────────────
ALL_PAIRS = [
    # --- Majors (7) ---
    "EUR/USD", "GBP/USD", "USD/JPY", "USD/CHF",
    "AUD/USD", "NZD/USD", "USD/CAD",

    # --- Popular Crosses (20) ---
    "EUR/GBP", "EUR/JPY", "EUR/CHF", "EUR/AUD", "EUR/CAD",
    "GBP/JPY", "GBP/CHF", "GBP/AUD", "GBP/CAD",
    "AUD/JPY", "AUD/NZD", "AUD/CHF", "AUD/CAD",
    "NZD/JPY", "NZD/CHF", "NZD/CAD",
    "CAD/JPY", "CAD/CHF", "CHF/JPY",

    # --- Crypto spot (10) ---
    "BTC/USD", "ETH/USD", "BNB/USD", "SOL/USD", "XRP/USD",
    "ADA/USD", "DOGE/USD", "DOT/USD", "LTC/USD", "SHIB/USD",
]

# ─── Data‑feed (Finnhub) ───────────────────────────────────────────
FINNHUB_API_KEY = "d1q6pipr01qrh89og8e0d1q6pipr01qrh89og8eg"  # ← your Finnhub key

# (अगर TwelveData अब इस्तेमाल नहीं कर रहे तो None छोड़ दें)
TD_API_KEY = None

# ─── Misc ──────────────────────────────────────────────────────────
TIMEZONE = "Asia/Kolkata"    # timestamps in IST
