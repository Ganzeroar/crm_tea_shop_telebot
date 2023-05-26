from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton


from handlers import text_keyboard


async def get_main_keyboard():
    return InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton(
                    text=text_keyboard.create_order,
                    callback_data='create_order',
                ),
            ],
            [
                InlineKeyboardButton(
                    text=text_keyboard.check_order_status,
                    callback_data='check_order_status',
                ),
            ],
            [
                InlineKeyboardButton(
                    text=text_keyboard.information,
                    callback_data='information',
                ),
            ],
            [
                InlineKeyboardButton(
                    text=text_keyboard.contacts,
                    callback_data='contacts',
                ),
            ],
        ],
    )


async def get_return_to_main_menu_keyboard_button():
    return [
        InlineKeyboardButton(
            text=text_keyboard.return_to_main_menu,
            callback_data='main_menu',
        ),
    ]


async def get_return_to_main_menu_keyboard():
    return InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton(
                    text=text_keyboard.return_to_main_menu,
                    callback_data='main_menu',
                ),
            ],
        ],
    )