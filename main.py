import asyncio
import logging
from aiogram import Bot, Dispatcher, types
from aiogram.filters.command import Command


from app.config import APP_NAME, telegram_bot_token


logging.basicConfig(level=logging.INFO)
bot = Bot(token=telegram_bot_token)
dp = Dispatcher()

@dp.message(Command('start'))
async def command_start(message: types.Message):
    await message.answer("Привет!")

async def main():
    await dp.start_polling(bot)

if __name__ == '__main__':
    asyncio.run(main())







#print(f" приложение {APP_NAME} стартовало!")
# запрос по API
#print(f" приложение {APP_NAME} стартовало!")
#print(f" приложение {APP_NAME} стартовало!")
#print(f" приложение {APP_NAME} стартовало!")

