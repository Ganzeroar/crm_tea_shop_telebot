from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton


from handlers.create_order.step_4_another_product_or_go_next import text_keyboard


async def get_another_product_or_go_next_keyboard():
    return InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton(
                    text=text_keyboard.select_another_product,
                    callback_data='select_another_product',
                ),
            ],
            [
                InlineKeyboardButton(
                    text=text_keyboard.go_next,
                    callback_data='go_next',
                ),
            ],
        ],
    )
