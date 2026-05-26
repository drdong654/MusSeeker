import asyncio

from aiogram import Bot, Dispatcher

from handlers.commands import router as commands_router
from handlers.download import router as download_router
from config import TOKEN

dp = Dispatcher()
dp.include_router(commands_router)
dp.include_router(download_router)


async def main():
    bot = Bot(token=TOKEN)
    await dp.start_polling(bot)


if __name__ == "__main__":
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print("Бот остановлен...")
