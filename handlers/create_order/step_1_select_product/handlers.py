from aiogram.types import CallbackQuery

from handlers.create_order.states import MakeOrderState
from handlers.create_order.step_1_select_product import keyboards, text_answer
from handlers.create_order.step_2_check_product_information import handlers as step_2_handlers
from services import api, db_functions


async def start_select_product(call: CallbackQuery):
    await MakeOrderState.select_product.set()

    user_id = call.from_user.id

    existing_products = await api.make_request_products()

    answer_text = text_answer.products
    answer_keyboard = await keyboards.create_products_keyboard(user_id, existing_products)
    await call.message.answer(answer_text, reply_markup=answer_keyboard)


async def select_product_handler(call: CallbackQuery):
    button_data = call.data
    product_id = button_data.split('_')[0]

    product_info = await api.make_request_for_product_info(product_id)
    product_quantity = product_info.get('quantity')

    await db_functions.create_order_info_data(call.from_user.id, product_id, product_quantity)
    
    await step_2_handlers.start_check_product_informaton(call, product_info)
