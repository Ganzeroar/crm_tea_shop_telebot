from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton, ReplyKeyboardMarkup, KeyboardButton
from handlers.create_order import handlers, text_keyboard



async def get_product_answer_keyboard():
    return InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton(
                    text=text_keyboard.make_order,
                    callback_data='make_order',
                ),
            ],
            [
                InlineKeyboardButton(
                    text=text_keyboard.return_to_main_menu,
                    callback_data='return_to_main_menu_from_products',
                ),
            ],
        ],
    )


async def get_return_to_main_menu_reply_keyboard():
    return ReplyKeyboardMarkup(
        resize_keyboard=True,
        keyboard=[
            [
                KeyboardButton(
                    text=text_keyboard.back_to_main_menu,
                ),
            ],
        ],
    )