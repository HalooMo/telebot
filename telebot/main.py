from aiogram import Bot, Dispatcher
from aiogram.enums.parse_mode import ParseMode
from aiogram.fsm.storage.memory import MemoryStorage
import logging
from aiogram.utils.chat_action import ChatActionMiddleware

import config
from handlers import router

import asyncio


async def main():
    bot = Bot(token=config.TOKEN, parse_mode=ParseMode.HTML)
    dp = Dispatcher(storage=MemoryStorage())
    dp.message.middleware(ChatActionMiddleware())
    dp.include_router(router)
    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot, allowed_updates=dp.resolve_used_update_types())


if __name__ == "__main__":
    asyncio.run(main())
    logging.basicConfig(level=logging.INFO)

