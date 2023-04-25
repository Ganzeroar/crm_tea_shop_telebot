import os

from aiogram.types import CallbackQuery, Message
from aiogram.dispatcher import FSMContext

from handlers.check_order_status.find_order_with_phone import keyboards, text_answer
from handlers.check_order_status.find_order_with_phone.states import CheckOrderWithPhoneState
from handlers import keyboards as main_keyboard
from handlers import handlers as main_menu_handler

async def find_order_with_phone_handler(call: CallbackQuery, state: FSMContext):
    await CheckOrderWithPhoneState.waiting_for_phone.set()

    answer_text = text_answer.find_order_with_phone
    answer_keyboard = await keyboards.get_find_order_with_phone()
    await call.message.answer(answer_text, reply_markup=answer_keyboard)

async def find_order_handler(message: Message, state: FSMContext):
    await state.finish()
    if not (len(message.text)) < 7 and message.text.isdigit():
        answer_text = text_answer.phone_number_wrong
        answer_keyboard = await keyboards.get_after_find_order_keyboard
        await message.answer(answer_text ,reply_markup=answer_keyboard)

    print(message.text)