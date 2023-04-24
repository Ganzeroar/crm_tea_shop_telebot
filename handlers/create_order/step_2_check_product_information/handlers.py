from aiogram.types import CallbackQuery

from handlers.create_order.states import MakeOrderState
from handlers.create_order.step_2_check_product_information import keyboards
from handlers.create_order.step_3_select_quantity import handlers as step_3_handles
from services import api


async def start_check_product_informaton(call: CallbackQuery, product_info):
    await MakeOrderState.next()

    product_name = product_info.get('name')
    product_description = product_info.get('description')
    product_price = product_info.get('price')
    product_unit = product_info.get('unit')
    product_quantity = product_info.get('quantity')

    product_type_id = product_info.get('product_type')
    product_type_info = await api.make_request_for_product_type_info(product_type_id)
    product_type = product_type_info.get('name')

    answer_message = f'Название: {product_name}\nТип: {product_type}\nОписание: {product_description}\nЕдиница измерения: {product_unit}\nДоступное количество: {product_quantity}\nЦена: {product_price}'
    answer_keyboard = await keyboards.get_product_answer_keyboard()
    await call.message.answer(answer_message, reply_markup=answer_keyboard)
    
async def check_product_information_handler(call:CallbackQuery):
    await step_3_handles.start_select_quantity(call)