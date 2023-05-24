from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from handlers.create_order.step_0_select_type import routes


async def create_product_types_keyboard(user_id, existing_product_types):
    inline_keyboard_array = []
    for product_type in existing_product_types:
        product_type_button = [
            InlineKeyboardButton(
                text=product_type.get('name'),
                callback_data=f"{product_type.get('id')}_{user_id}",
            )
        ]
        inline_keyboard_array.append(product_type_button)

        await routes.create_route(product_type.get('id'), user_id)

    return InlineKeyboardMarkup(
        inline_keyboard=inline_keyboard_array,
    )
