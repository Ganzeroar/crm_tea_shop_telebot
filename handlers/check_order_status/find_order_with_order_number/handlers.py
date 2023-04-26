from aiogram.types import CallbackQuery, Message
from aiogram.dispatcher import FSMContext

from handlers.check_order_status.find_order_with_order_number import keyboards, text_answer
from handlers.check_order_status.find_order_with_order_number.states import CheckOrderWithNumberState
from handlers.handlers import start_main_menu_from_callback
from services import api


async def start_find_order_with_order_number_handler(call: CallbackQuery, state: FSMContext):
    await CheckOrderWithNumberState.waiting_for_order_number.set()

    answer_text = text_answer.find_order_with_order_number
    answer_keyboard = await keyboards.get_find_order_with_number()
    await call.message.answer(answer_text, reply_markup=answer_keyboard)

async def find_order_handler(message: Message, state: FSMContext):
    await state.finish()
    if not message.text.isdigit():
        answer_text = text_answer.order_number_wrong
        answer_keyboard = await keyboards.get_after_find_order_keyboard()
        await message.answer(answer_text ,reply_markup=answer_keyboard)
        return

    order_id = message.text
    order_info = await api.make_request_for_check_order_status(order_id)
    current_status_id = order_info.get('status')

    status_name = await api.make_request_for_name_order_status(current_status_id)
    answer_text = status_name.get('name')
    if answer_text == 'В работе':
        answer_text = f'Ваш заказ № {order_id} сейчас находится в обработке! Примерная дата передачи посылки курьеру завтра. При смене статуса заказа мы Вас уведомим и позвоним.'
    elif answer_text == 'Передан курьеру':
        answer_text = f'Ваш заказ № {order_id} передан курьеру. В течение дня он позвонит Вам для согласования времени доставки.'

    answer_keyboard = await keyboards.get_after_find_order_keyboard()
    await message.answer(answer_text, reply_markup=answer_keyboard)

async def return_to_main_menu_handler(call: CallbackQuery, state: FSMContext):
    await state.finish()

    await start_main_menu_from_callback(call)