import os

from aiogram.types import CallbackQuery, Message

from handlers import keyboards, text_answer


async def start_main_menu(message: Message):
    answer_text = text_answer.main_menu
    answer_keyboard = await keyboards.get_main_keyboard()
    await message.answer(answer_text, reply_markup=answer_keyboard)

async def start_ask_user_to_use_buttons(message: Message):
    answer_text = text_answer.ask_user_to_use_buttons
    await message.answer(answer_text)

async def start_main_menu_from_callback(call: CallbackQuery):
    answer_text = text_answer.main_menu
    answer_keyboard = await keyboards.get_main_keyboard()
    await call.message.answer(answer_text, reply_markup=answer_keyboard)