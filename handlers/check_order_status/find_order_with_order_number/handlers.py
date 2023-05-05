from aiogram.types import CallbackQuery, Message
from aiogram.dispatcher import FSMContext

from handlers.check_order_status.find_order_with_order_number import keyboards, text_answer
from handlers.check_order_status.find_order_with_order_number.states import CheckOrderWithNumberState
from handlers.handlers import start_main_menu_from_callback


async def start_find_order_with_order_number_handler(call: CallbackQuery, state: FSMContext):
    await CheckOrderWithNumberState.waiting_for_order_number.set()

    answer_text = text_answer.find_order_with_order_number
    answer_keyboard = await keyboards.get_find_order_with_number()
    await call.message.answer(answer_text, reply_markup=answer_keyboard)


async def find_order_handler(message: Message, state: FSMContext):
    if not message.text.isdigit():
        answer_text = text_answer.order_number_wrong
        answer_keyboard = await keyboards.get_after_find_order_keyboard()
        await message.answer(answer_text, reply_markup=answer_keyboard)
        return

    answer_text = await text_answer.create_answer_text(message.text)
    answer_keyboard = await keyboards.get_after_find_order_keyboard()

    await message.answer(answer_text, reply_markup=answer_keyboard)

    await state.finish()


async def return_to_main_menu_handler(call: CallbackQuery, state: FSMContext):
    await state.finish()

    await start_main_menu_from_callback(call)