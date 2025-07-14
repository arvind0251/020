import asyncio, logging
from datetime import datetime
from zoneinfo import ZoneInfo

from aiogram import Bot, Dispatcher
from aiogram.enums import ParseMode

import config
from router_private import router as priv_router, user_pairs, push_signal
from router_group  import router as grp_router, broadcast as group_broadcast

logging.basicConfig(level=logging.INFO)

bot = Bot(token=config.BOT_TOKEN, parse_mode=ParseMode.HTML)
dp  = Dispatcher()
dp.include_router(priv_router)
dp.include_router(grp_router)

def ist_now():
    return datetime.now(ZoneInfo(config.TIMEZONE)).strftime("%H:%M:%S")

async def scheduler():
    while True:
        # private chats
        for chat_id, pair in list(user_pairs.items()):
            try: await push_signal(bot, chat_id, pair)
            except Exception as e: logging.exception("Private signal: %s", e)
        # group broadcast
        try: await group_broadcast(bot)
        except Exception as e: logging.exception("Broadcast: %s", e)
        await asyncio.sleep(60)

async def on_startup():
    asyncio.create_task(scheduler())
    logging.info("Scheduler started %s", ist_now())

async def main():
    dp.startup.register(on_startup)
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
