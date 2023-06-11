from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from handlers.create_order.step_1_select_product import routes


async def create_products_keyboard(user_id, info_about_products):
    inline_keyboard_array = []
    existing_products = info_about_products.get('results')
    for product in existing_products:
        product_button = [
            InlineKeyboardButton(
                text=product.get('name'),
                callback_data=f"{product.get('id')}_{user_id}",
            )
        ]
        inline_keyboard_array.append(product_button)

        await routes.create_route(product.get('id'), user_id)
    if info_about_products.get('next'):
        next_button = [
            InlineKeyboardButton(
                text='Следующая страница',
                callback_data="next_page",
            )
        ]
        inline_keyboard_array.append(next_button)
    if info_about_products.get('previous'):
        next_button = [
            InlineKeyboardButton(
                text='Предыдущая страница',
                callback_data="previous_page",
            )
        ]
        inline_keyboard_array.append(next_button)

    return InlineKeyboardMarkup(
        inline_keyboard=inline_keyboard_array,
    )
