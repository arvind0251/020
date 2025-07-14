from aiogram import Router, types, F
from aiogram.filters import Command
from aiogram.types import InlineKeyboardButton as Btn, InlineKeyboardMarkup as Markup
from datetime import datetime
from zoneinfo import ZoneInfo

from config import ALL_PAIRS, TIMEZONE
from data_feed import get_live_candles
from signal_engine import generate_signal

router = Router()
user_pairs: dict[int, str] = {}

def ist_now():
    return datetime.now(ZoneInfo(TIMEZONE)).strftime("%H:%M:%S | %d‑%b‑%Y")

@router.message(Command("start"))
async def start(m: types.Message):
    kb = Markup(inline_keyboard=[[Btn(text=p, callback_data=f"pair:{p}")] for p in ALL_PAIRS])
    await m.answer("👋 <b>Welcome!</b> Choose your pair:", reply_markup=kb)

@router.callback_query(F.data.startswith("pair:"))
async def set_pair(cb: types.CallbackQuery):
    pair = cb.data.split(":", 1)[1]
    user_pairs[cb.from_user.id] = pair
    await cb.answer()
    await cb.message.answer(f"✅ Pair <b>{pair}</b> selected.")

async def push_signal(bot, chat_id: int, pair: str):
    df1 = await get_live_candles(pair, "1m", 200)
    df5 = await get_live_candles(pair, "5m", 200)
    sig = generate_signal(df1, df5)
    if not sig:
        return
    arrow = "🔺 BUY" if sig['dir']=="BUY" else "🔻 SELL"
    msg = (f"🕗 <b>{ist_now()}</b>\n"
           f"Pair : <b>{pair}</b>\n"
           f"Direction : {arrow}\n"
           f"Expiry : 1 min\n"
           f"Confidence : {sig['acc']} %")
    await bot.send_message(chat_id, msg)
