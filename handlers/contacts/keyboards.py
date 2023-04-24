from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton


from handlers.contacts import text_keyboard
from handlers import keyboards as main_keyboards


async def get_contacts_keyboard():
    return InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton(
                    text=text_keyboard.almaty,
                    callback_data='almaty',
                ),
            ],
            [
                InlineKeyboardButton(
                    text=text_keyboard.astana,
                    callback_data='astana',
                ),
            ],
            [
                InlineKeyboardButton(
                    text=text_keyboard.shymkent,
                    callback_data='shymkent',
                ),
            ],
            await main_keyboards.get_return_to_main_menu_keyboard_button()
        ],
    )
