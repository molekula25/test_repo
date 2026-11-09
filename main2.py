import asyncio
import logging
from aiogram import Bot, Dispatcher, types, F
from aiogram.filters.command import Command


from app.config import APP_NAME, telegram_bot_token
from app.utils.fox import async_fox


logging.basicConfig(level=logging.INFO)
bot = Bot(token=telegram_bot_token)
dp = Dispatcher()

@dp.message(Command('start'))
async def command_start(message: types.Message):
    #print(message.chat.first_name)
    await message.answer(f"Привет! {message.chat.first_name}")

@dp.message(Command('info'))
async def command_info(message: types.Message):
    text = """
    Я бот ассистент
    """
    await message.answer(f"{text}")

@dp.message(Command('help'))
async def command_help(message: types.Message):
        text = """
        Что я умею
        1) /start - запуск бота и приветствие
        2) /info - информация о боте
        3) /help - помощь
        """
        await message.answer(f"{text}")

@dp.message(Command('fox'))
@dp.message(Command('лиса'))
async def command_fox(message: types.Message):
    image_fox = await async_fox()
    #print(image_fox)
    await message.answer_photo(image_fox)
    image_fox = await async_fox()
    await bot.send_photo(message.chat.id, image_fox)

@dp.message(F.text)
async def echo(message: types.Message):
    text = message.text
    if "казино" in text:
        await message.reply(f"мы здесь не играем")
    else:
      await message.reply(f"{text}")

async def main():
    await dp.start_polling(bot)

if __name__ == '__main__':
    asyncio.run(main())







#print(f" приложение {APP_NAME} стартовало!")
# запрос по API
#print(f" приложение {APP_NAME} стартовало!")
#print(f" приложение {APP_NAME} стартовало!")
#print(f" приложение {APP_NAME} стартовало!")

