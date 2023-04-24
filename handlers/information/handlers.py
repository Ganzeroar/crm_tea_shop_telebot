import os

from aiogram.types import CallbackQuery, Message
from handlers.information import keyboards, text_answer

async def start_information_handler(call: CallbackQuery):
    answer_text = text_answer.information
    answer_keyboard = await keyboards.get_information_keyboard()
    await call.message.answer(answer_text, reply_markup=answer_keyboard)

async def social_media_handler(call: CallbackQuery):
    answer_text = text_answer.social_media
    answer_keyboard = await keyboards.get_information_keyboard()
    await call.message.answer(answer_text, reply_markup=answer_keyboard)

async def history_of_shop_handler(call: CallbackQuery):
    answer_text = text_answer.history_of_shop
    answer_keyboard = await keyboards.get_information_keyboard()
    await call.message.answer(answer_text, reply_markup=answer_keyboard)

async def stock_handler(call: CallbackQuery):
    answer_text = text_answer.stock
    answer_keyboard = await keyboards.get_information_keyboard()
    await call.message.answer(answer_text, reply_markup=answer_keyboard)