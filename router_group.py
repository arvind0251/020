from aiogram import Router
from datetime import datetime
from zoneinfo import ZoneInfo

from config import GROUP_ID, ALL_PAIRS, TIMEZONE
from data_feed import get_live_candles
from signal_engine import generate_signal

router = Router()

def ist_now():
    return datetime.now(ZoneInfo(TIMEZONE)).strftime("%H:%M:%S | %d‑%b‑%Y")

async def broadcast(bot):
    lines = [f"🕗 <b>{ist_now()}</b>"]
    for pair in ALL_PAIRS:
        df1 = await get_live_candles(pair, "1m", 200)
        df5 = await get_live_candles(pair, "5m", 200)
        sig = generate_signal(df1, df5)
        if sig:
            arrow = "🔺 BUY" if sig['dir']=="BUY" else "🔻 SELL"
            lines.append(f"{pair}  {arrow}  (1 min, {sig['acc']} %)")
    if len(lines) > 1:
        await bot.send_message(GROUP_ID, "\n".join(lines))
