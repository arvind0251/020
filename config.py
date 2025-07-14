# config.py  (hard‑coded version)

# ─── Telegram & Bot settings ─────────────────────────────────────────
BOT_TOKEN = "YOUR_TELEGRAM_BOT_TOKEN"     # ← यहाँ अपना BotFather token भरें
GROUP_ID  = -1001234567890                # ← group / channel numeric ID

# जो‑जो пары (symbols) चाहिए—लिस्ट में लिखें
ALL_PAIRS = [
    "EUR/USD",
    "GBP/JPY",
    "BTC/USD",
]

# ─── Data‑feed (TwelveData) ──────────────────────────────────────────
TD_API_KEY = "YOUR_TWELVEDATA_API_KEY"    # फ्री टियर key भी चलेगी

# ─── Misc ────────────────────────────────────────────────────────────
TIMEZONE = "Asia/Kolkata"                 # टाइम‑स्टैम्प IST में

# बस! बाकी कोड इस फाइल के वैरिएबल्स सीधे पढ़ेगा।
