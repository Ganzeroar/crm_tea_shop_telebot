import os

from aiogram.types import CallbackQuery, Message

from handlers import keyboards, text_answer


async def start_main_menu(message: Message):
    answer_text = text_answer.main_menu
    answer_keyboard = await keyboards.get_main_keyboard()
    await message.answer(answer_text, reply_markup=answer_keyboard)