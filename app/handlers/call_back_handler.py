from aiogram import Router, types, F
from aiogram.filters.command import Command
from aiogram.utils import callback_answer

from app.keyboards.reply import main_menu_keyboard, help_menu_keyboard
from app.keyboards.inline import demo_inline_keyboard


FAQ_ANSWERS = {
    "price": "бАЗОВАЯ ВЕРСИЯ БЕСПЛАТНО",
    "support": "Пока используйте кнопку связаться",
    "privacy": "Мы не храним данные",
    "features": "Много что умеет"
}


router = Router()


@router.callback_query(F.data == "demo_ask_gpt")
async def ask_gpt_callback(callback: types.CallbackQuery):
    action = callback.data

    await callback.answer("Вы выбрали gpt")   #всплывающее уведомление
    await callback.message.answer("Вы нажали gpt")   #сообщение

@router.callback_query(F.data == "demo_ask_yandex")
async def ask_gpt_callback(callback: types.CallbackQuery):
    action = callback.data

    await callback.answer("Вы выбрали yandex")   #всплывающее уведомление
    await callback.message.answer("Вы нажали yandex")  # сообщение

@router.callback_query(F.data.startswith("faq_"))
async def on_faq_callback(callback: types.CallbackQuery):
    data = callback.data
    await callback.answer()

    if data == "faq_price":
        await callback.message.answer(FAQ_ANSWERS.get("price"))
    elif data == "faq_support":
        await callback.message.answer(FAQ_ANSWERS.get("support"))
    elif data == "faq_privacy":
        await callback.message.answer(FAQ_ANSWERS.get("privacy"))
    elif data == "faq_features":
        await callback.message.answer(FAQ_ANSWERS.get("features"))

