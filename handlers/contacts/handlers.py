import os

from aiogram.types import CallbackQuery

from handlers.contacts import keyboards, text_answer


async def start_contacts_handler(call: CallbackQuery):
    answer_text = text_answer.contacts
    answer_keyboard = await keyboards.get_contacts_keyboard()
    await call.message.answer(answer_text, reply_markup=answer_keyboard)

async def astana_handler(call: CallbackQuery):
    answer_text = text_answer.astana
    answer_keyboard = await keyboards.get_contacts_keyboard()
    await call.message.answer(answer_text, reply_markup=answer_keyboard)

async def almaty_handler(call: CallbackQuery):
    answer_text = text_answer.almaty
    answer_keyboard = await keyboards.get_contacts_keyboard()
    await call.message.answer(answer_text, reply_markup=answer_keyboard)

async def shymkent_handler(call: CallbackQuery):
    answer_text = text_answer.shymkent
    answer_keyboard = await keyboards.get_contacts_keyboard()
    await call.message.answer(answer_text, reply_markup=answer_keyboard)