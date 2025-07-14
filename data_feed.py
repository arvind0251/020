"""Live data‑feed module (Finnhub).

अगर FINNHUB_API_KEY गायब हो या rate‑limit हिट हो जाए तो
फंक्शन random demo candles लौटाता है ताकि बोट बाकी काम करता रहे।
"""

import pandas as pd
import aiohttp
from datetime import datetime, timedelta
import random, time
from config import FINNHUB_API_KEY   # ←  config.py में यह key जोड़ें

BASE_URL = "https://finnhub.io/api/v1/forex/candle"
_RESOLUTION = {"1m": "1", "5m": "5"}   # Finnhub uses numbers for minutes

# ────────────────────────────────────────────────────────────────
def _pair_to_symbol(pair: str) -> str:
    """
    Forex: 'EUR/USD' -> 'OANDA:EUR_USD'
    Crypto: 'BTC/USD' -> 'BINANCE:BTCUSDT'
    """
    base, quote = pair.upper().split("/")
    if base in {"BTC","ETH","BNB","SOL","XRP","ADA","DOGE","DOT","LTC","SHIB"}:
        return f"BINANCE:{base}USDT"
    return f"OANDA:{base}_{quote}"

# ────────────────────────────────────────────────────────────────
async def get_live_candles(pair: str, timeframe: str = "1m", limit: int = 200):
    """
    Return DataFrame with columns:
    ['datetime','open','high','low','close','volume'] oldest → newest
    """
    if not FINNHUB_API_KEY:
        return _demo_candles(limit)

    end_ts   = int(time.time())
    start_ts = end_ts - limit * 60

    params = {
        "symbol": _pair_to_symbol(pair),
        "resolution": _RESOLUTION.get(timeframe, "1"),
        "from": start_ts,
        "to":   end_ts,
        "token": FINNHUB_API_KEY,
    }

    async with aiohttp.ClientSession() as sess:
        try:
            async with sess.get(BASE_URL, params=params, timeout=8) as r:
                js = await r.json()
            if js.get("s") != "ok":
                raise ValueError(js.get("error", "invalid response"))
        except Exception as e:
            print("Finnhub error → demo data:", e)
            return _demo_candles(limit)

    df = pd.DataFrame({
        "datetime": pd.to_datetime(js["t"], unit="s"),
        "open":  js["o"],
        "high":  js["h"],
        "low":   js["l"],
        "close": js["c"],
        "volume": js.get("v", [0]*len(js["c"]))
    })

    return df.tail(limit)

# ────────────────────────────────────────────────────────────────
def _demo_candles(limit: int):
    """Random candles so the rest of the bot keeps running offline."""
    now = datetime.utcnow()
    closes = [random.uniform(1, 2) for _ in range(limit)]
    highs  = [c + random.uniform(0, .01) for c in closes]
    lows   = [c - random.uniform(0, .01) for c in closes]
    return pd.DataFrame({
        "datetime": [now - timedelta(minutes=i) for i in range(limit)][::-1],
        "open": closes,
        "high": highs,
        "low":  lows,
        "close": closes,
        "volume": [0] * limit,
    })
