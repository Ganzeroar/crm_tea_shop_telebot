import os

from aiogram.types import CallbackQuery, Message

from handlers.check_order_status import keyboards, text_answer


async def start_check_order_status(call: CallbackQuery):
    answer_text = text_answer.check_order_status
    answer_keyboard = await keyboards.get_check_order_status_keyboard()
    await call.message.answer(answer_text, reply_markup=answer_keyboard)
