"""Live data‑feed module.

If TD_API_KEY is missing or the API limit is hit, the function
falls back to random demo candles so the rest of the bot still works.
"""

import pandas as pd
import aiohttp
from datetime import datetime, timedelta
import random
from config import TD_API_KEY

BASE_URL = "https://api.twelvedata.com/time_series"
_INTERVAL = {"1m": "1min", "5m": "5min"}

def _pair_to_symbol(pair: str) -> str:
    return pair.strip().upper()  # e.g., "EUR/USD" → "EUR/USD"

async def _fetch(session: aiohttp.ClientSession, params: dict):
    async with session.get(BASE_URL, params=params, timeout=10) as r:
        r.raise_for_status()
        return await r.json()

async def get_live_candles(pair: str, timeframe: str = "1m", limit: int = 200):
    """Return DataFrame[open,high,low,close,volume,datetime] oldest→newest."""
    if TD_API_KEY is None:
        return _demo_candles(limit)

    params = {
        "symbol": _pair_to_symbol(pair),
        "interval": _INTERVAL.get(timeframe, "1min"),
        "outputsize": str(limit),
        "apikey": TD_API_KEY,
        "format": "JSON",
    }
    async with aiohttp.ClientSession() as sess:
        try:
            js = await _fetch(sess, params)
            vals = js.get("values")
            if not vals:
                raise ValueError(js.get("message", "no data"))
        except Exception as e:
            print("TwelveData error → demo data:", e)
            return _demo_candles(limit)

    df = pd.DataFrame(vals[::-1])               # oldest first
    df.rename(columns={"datetime": "datetime"}, inplace=True)
    df["datetime"] = pd.to_datetime(df["datetime"])
    df[["open", "high", "low", "close", "volume"]
        ] = df[["open", "high", "low", "close", "volume"]].astype(float)
    return df.tail(limit)

def _demo_candles(limit: int):
    now = datetime.utcnow()
    closes = [random.uniform(1, 2) for _ in range(limit)]
    highs = [c + random.uniform(0, .01) for c in closes]
    lows  = [c - random.uniform(0, .01) for c in closes]
    return pd.DataFrame({
        "datetime": [now - timedelta(minutes=i) for i in range(limit)][::-1],
        "open": closes, "high": highs, "low": lows,
        "close": closes, "volume": [0]*limit
    })
