import asyncio
import logging
import os
from handlers import adminreg, user_commands, admin_commands
from aiogram import Bot, Dispatcher
from dotenv import load_dotenv
from data_base.bd import *
from data_base.admindb import *

load_dotenv(
create_table()
create_admin_table()

logging.basicConfig(level=logging.INFO)


async def main():
    bot = Bot("6765186512:AAGKXrz_2gXWZYXti6zVc5_B2hcZZUCwHy8")
    dp = Dispatcher()

    logging.basicConfig(level=logging.INFO)

    dp.include_router(admin_commands.router)
    dp.include_router(adminreg.router)
    dp.include_router(user_commands.router)



    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
