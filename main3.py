import asyncio
import logging
from logging import info

from aiogram import Bot, Dispatcher
from aiogram.fsm.storage.memory import MemoryStorage


from app.config import APP_NAME, telegram_bot_token
from app.handlers.routers import root_router
from app.front.bot_entrypoint import setup_logging, logger




async def main():

    if not telegram_bot_token:
        raise RuntimeError('Не найден telegram_bot_token')

    #logging.basicConfig(level=logging.INFO)
    setup_logging()
    logger.info('Бот запущен')

    bot = Bot(token=telegram_bot_token)

    storage = MemoryStorage()

    dp = Dispatcher(storage=storage)

    dp.include_router(root_router)

    try:
        logger.info('Запуск long polling')
        await dp.start_polling(bot)
    except Exception as e:
        logger.exception(f"Неожиданная ошибка{e}")
    finally:
        logger.info('Остановка бота')
if __name__ == '__main__':
    asyncio.run(main())







#print(f" приложение {APP_NAME} стартовало!")
# запрос по API
#print(f" приложение {APP_NAME} стартовало!")
#print(f" приложение {APP_NAME} стартовало!")
#print(f" приложение {APP_NAME} стартовало!")

