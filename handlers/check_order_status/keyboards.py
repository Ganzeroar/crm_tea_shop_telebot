from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton


from handlers import keyboards as main_keyboards
from handlers.check_order_status import text_keyboard


async def get_check_order_status_keyboard():
    return InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton(
                    text=text_keyboard.find_order_with_order_number,
                    callback_data='find_order_with_order_number',
                ),
            ],
            await main_keyboards.get_return_to_main_menu_keyboard_button()
        ],
    )
