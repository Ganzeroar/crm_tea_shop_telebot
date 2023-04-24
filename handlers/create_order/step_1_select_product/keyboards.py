from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from handlers.create_order.step_1_select_product import routes


async def create_products_keyboard(user_id, existing_products):
    inline_keyboard_array = []
    for product in existing_products:
        product_button = [
            InlineKeyboardButton(
                text=product.get('name'),
                callback_data=f"{product.get('id')}_{user_id}",
            )
        ]
        inline_keyboard_array.append(product_button)

        await routes.create_route(product.get('id'), user_id)

    return InlineKeyboardMarkup(
        inline_keyboard=inline_keyboard_array,
    )
