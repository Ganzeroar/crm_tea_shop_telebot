from aiogram.types import CallbackQuery

from handlers.products import text_answer, keyboards
from services import api

async def start_products(call: CallbackQuery):
    user_id = call.from_user.id

    existing_products = await api.make_request_products()

    answer_text = text_answer.products
    answer_keyboard = await keyboards.create_products_keyboard(user_id, existing_products)
    await call.message.answer(answer_text, reply_markup=answer_keyboard)


async def one_product(call: CallbackQuery):
    button_data = call.data
    product_id = button_data.split('_')[0]
    product_info = await api.make_request_for_product_info(product_id)
    product_name = product_info.get('name')
    product_description = product_info.get('description')
    product_price = product_info.get('price')
    product_quantity = product_info.get('quantity')
    product_unit = product_info.get('unit')
    product_type_id = product_info.get('product_type')
    
    product_type_info = await api.make_request_for_product_type_info(product_type_id)
    product_type = product_type_info.get('type_name')
    
    answer_message = f'Название: {product_name}\nТип: {product_type}\nОписание: {product_description}\nЕдиница измерения: {product_unit}\nДоступное количество: {product_quantity}\nЦена: {product_price}'
    answer_keyboard = keyboards.get_product_answer_keyboard()
    await call.message.answer(answer_message), reply_markup=answer_keyboard)
    
    