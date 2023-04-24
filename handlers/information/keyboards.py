from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton


from handlers import keyboards as main_keyboards
from handlers.information import text_keyboard


async def get_information_keyboard():
    return InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton(
                    text=text_keyboard.social_media,
                    callback_data='social_media',
                ),
            ],
            [
                InlineKeyboardButton(
                    text=text_keyboard.history_of_shop,
                    callback_data='history_of_shop',
                ),
            ],
            [
                InlineKeyboardButton(
                    text=text_keyboard.stock,
                    callback_data='stock',
                ),
            ],
            await main_keyboards.get_return_to_main_menu_keyboard_button()
        ],
    )

