# config.py  (hard‑coded version)

# ─── Telegram & Bot settings ─────────────────────────────────────────
BOT_TOKEN = "7864815464:AAGiwjulKLxnDP9MuaVhhQZ8fhoPRz3uv2Q"     # ← यहाँ अपना BotFather token भरें
GROUP_ID  = -1002711451967                # ← group / channel numeric ID

# जो‑जो пары (symbols) चाहिए—लिस्ट में लिखें
ALL_PAIRS = [
    # --- Majors (7) ---
    "EUR/USD", "GBP/USD", "USD/JPY", "USD/CHF",
    "AUD/USD", "NZD/USD", "USD/CAD",

    # --- Popular Crosses (20) ---
    "EUR/GBP", "EUR/JPY", "EUR/CHF", "EUR/AUD", "EUR/CAD",
    "GBP/JPY", "GBP/CHF", "GBP/AUD", "GBP/CAD",
    "AUD/JPY", "AUD/NZD", "AUD/CHF", "AUD/CAD",
    "NZD/JPY", "NZD/CHF", "NZD/CAD",
    "CAD/JPY", "CAD/CHF",
    "CHF/JPY",

    # --- Crypto spot (10) ---
    "BTC/USD", "ETH/USD", "BNB/USD", "SOL/USD", "XRP/USD",
    "ADA/USD", "DOGE/USD", "DOT/USD", "LTC/USD", "SHIB/USD",
]

# ─── Data‑feed (TwelveData) ──────────────────────────────────────────
TD_API_KEY = "d1q6pipr01qrh89og8e0d1q6pipr01qrh89og8eg"    # फ्री टियर key भी चलेगी

# ─── Misc ────────────────────────────────────────────────────────────
TIMEZONE = "Asia/Kolkata"                 # टाइम‑स्टैम्प IST में

# बस! बाकी कोड इस फाइल के वैरिएबल्स सीधे पढ़ेगा।
