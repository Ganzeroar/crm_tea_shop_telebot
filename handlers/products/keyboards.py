from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

# from handlers.products import text
# from handlers import keyboards as main_keyboards


async def create_products_keyboard(existing_products):
    inline_keyboard_array = []
    for product in existing_products:
        product_button = [
            InlineKeyboardButton(
                text=product.get('name'),
                callback_data=f"{product.get('name')}_{product.get('id')}",
            )
        ]
        inline_keyboard_array.append(product_button)
    print(inline_keyboard_array)
    return InlineKeyboardMarkup(
        inline_keyboard=inline_keyboard_array,
    )

