from aiogram.types import CallbackQuery, Message

from handlers.create_order.states import MakeOrderState
from handlers.create_order.step_1_select_product import keyboards, text_answer
from handlers.create_order.step_2_check_product_information import handlers as step_2_handlers
from services import api, db_functions


async def start_select_product(call: CallbackQuery, product_type_id: str, state):
    await MakeOrderState.select_product.set()

    user_id = call.from_user.id

    info_about_products = await api.make_request_for_products_of_type(product_type_id)
    await state.update_data(current_info_about_products=info_about_products)

    answer_text = text_answer.products
    answer_keyboard = await keyboards.create_products_keyboard(user_id, info_about_products)
    await call.message.answer(answer_text, reply_markup=answer_keyboard)


async def select_product_handler(call: CallbackQuery, state):
    button_data = call.data
    product_id = button_data.split('_')[0]

    await state.update_data(current_product=product_id)

    product_info = await api.make_request_for_product_info(product_id)
    product_quantity = product_info.get('quantity')

    await db_functions.create_order_info_data(call.from_user.id, product_id, product_quantity)

    await step_2_handlers.start_check_product_informaton(call, product_info, state)


async def select_product_next_page(call: CallbackQuery, state):
    user_data = await state.get_data()
    current_info_about_products = user_data.get('current_info_about_products')
    next_url = current_info_about_products.get('next')
    info_about_products = await api.make_request_for_products_of_type_using_request(next_url)
    await state.update_data(current_info_about_products=info_about_products)

    user_id = call.from_user.id
    answer_text = text_answer.products
    answer_keyboard = await keyboards.create_products_keyboard(user_id, info_about_products)
    await call.message.answer(answer_text, reply_markup=answer_keyboard)


async def select_product_previous_page(call: CallbackQuery, state):
    user_data = await state.get_data()
    current_info_about_products = user_data.get('current_info_about_products')
    previous_url = current_info_about_products.get('previous')
    info_about_products = await api.make_request_for_products_of_type_using_request(previous_url)
    await state.update_data(current_info_about_products=info_about_products)

    user_id = call.from_user.id
    answer_text = text_answer.products
    answer_keyboard = await keyboards.create_products_keyboard(user_id, info_about_products)
    await call.message.answer(answer_text, reply_markup=answer_keyboard)


async def start_ask_user_to_use_buttons(message: Message):
    answer_text = text_answer.ask_user_to_use_buttons

    await message.answer(answer_text)
