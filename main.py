import logging
import sys
from aiogram import Bot, Dispatcher
import asyncio
import psycopg2

bot = Bot(token="Твой токен")
dp = Dispatcher()




async def main():

    try:
        await dp.start_polling(bot)
    except:
        print(Exception)


if __name__ == "__main__":
    try:
        logging.basicConfig(level=logging.INFO, stream=sys.stdout)
        asyncio.run(main())
    except:
        print(Exception)

