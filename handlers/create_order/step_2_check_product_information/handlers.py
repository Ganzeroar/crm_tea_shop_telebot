from aiogram.types import CallbackQuery, Message
from aiogram.dispatcher import FSMContext

from handlers.create_order.states import MakeOrderState
from handlers.create_order.step_2_check_product_information import keyboards, text_answer
from handlers.create_order.step_3_select_quantity import handlers as step_3_handles
from services import api, db_functions
from handlers.create_order.step_0_select_type import handlers as step_1_handlers
from handlers.create_order.step_4_name import handlers as step_4_name_handlers

async def start_check_product_informaton(call: CallbackQuery, product_info, state):
    await MakeOrderState.next()

    product_name = product_info.get('name')
    product_description = product_info.get('description')
    product_price = product_info.get('price')

    product_unit_id = product_info.get('unit')
    product_unit_info = await api.make_request_for_product_unit_info(product_unit_id)
    product_unit = product_unit_info.get('unit')

    product_quantity = product_info.get('quantity')
    if product_quantity == 0:
        product_quantity = 'Нет в наличии'

    product_type_id = product_info.get('product_type')
    product_type_info = await api.make_request_for_product_type_info(product_type_id)
    product_type = product_type_info.get('name')

    answer_message = f'Название: {product_name}\nТип: {product_type}\nОписание: {product_description}\nЕдиница измерения: {product_unit}\nДоступное количество: {product_quantity}\nЦена: {product_price}'
    
    user_data = await state.get_data()
    is_at_least_one_item_selected = user_data.get('is_at_least_one_item_selected')
    answer_keyboard = await keyboards.get_product_answer_keyboard(is_at_least_one_item_selected, product_quantity)
    await call.message.answer(answer_message, reply_markup=answer_keyboard)
    
async def check_product_information_handler(call: CallbackQuery):
    await step_3_handles.start_select_quantity(call)


async def continue_main_order(call: CallbackQuery, state):
    user_data = await state.get_data()
    current_product_id = user_data.get('current_product')
    await db_functions.delete_one_product_from_order(call.message, current_product_id)

    await step_4_name_handlers.start_name(call.message)

async def return_to_select_product_type(call: CallbackQuery, state: FSMContext):
    user_data = await state.get_data()
    current_product_id = user_data.get('current_product')
    await db_functions.delete_one_product_from_order(call.message, current_product_id)
    await step_1_handlers.start_select_type(call)

async def start_ask_user_to_use_buttons(message: Message):
    answer_text = text_answer.ask_user_to_use_buttons

    await message.answer(answer_text)