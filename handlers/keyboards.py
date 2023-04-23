from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton


from handlers import text_keyboard


async def get_main_keyboard():
    return InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton(
                    text=text_keyboard.products,
                    callback_data='products',
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
                    text=text_keyboard.contact_the_operator,
                    callback_data='contact_the_operator',
                ),
            ],
            [
                InlineKeyboardButton(
                    text=text_keyboard.sweepstakes_and_promotions,
                    callback_data='sweepstakes_and_promotions',
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

