import asyncio
import logging
from aiogram import Bot, Dispatcher


from app.config import APP_NAME, telegram_bot_token
from app.handlers.common import router as command_router
from app.handlers.bot_message import router as massage_router
from app.handlers.bot_photo import router as photo_router
from app.handlers.call_back_handler import router as callback_router



async def main():
    logging.basicConfig(level=logging.INFO)
    bot = Bot(token=telegram_bot_token)
    dp = Dispatcher()

    dp.include_router(command_router)
    dp.include_router(massage_router)
    dp.include_router(photo_router)
    dp.include_router(callback_router_router)

    await dp.start_polling(bot)

if __name__ == '__main__':
    asyncio.run(main())







#print(f" приложение {APP_NAME} стартовало!")
# запрос по API
#print(f" приложение {APP_NAME} стартовало!")
#print(f" приложение {APP_NAME} стартовало!")
#print(f" приложение {APP_NAME} стартовало!")

