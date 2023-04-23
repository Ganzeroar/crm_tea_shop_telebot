from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from loader import dp
from handlers.products import handlers


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

        dp.register_callback_query_handler(
            handlers.one_product,
            text=[f"{product.get('id')}_{user_id}"],
        )

    return InlineKeyboardMarkup(
        inline_keyboard=inline_keyboard_array,
    )

async def get_product_answer_keyboard():
    pass