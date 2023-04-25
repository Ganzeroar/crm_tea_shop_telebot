from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

from handlers.check_order_status.find_order_with_order_number import text_keyboard
from handlers import keyboards as main_keyboards

async def get_find_order_with_number():
    return InlineKeyboardMarkup(
        inline_keyboard=[
            await main_keyboards.get_return_to_main_menu_keyboard_button()
        ],
    )

async def get_after_find_order_keyboard():
    return InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton(
                    text=text_keyboard.find_another_order_with_order_number,
                    callback_data='find_another_order_with_order_number',
                ),
            ],
            await main_keyboards.get_return_to_main_menu_keyboard_button(),
        ],
    )