from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from handlers.create_order.step_2_check_product_information import text_keyboard
from handlers import keyboards as main_keyboards



async def get_product_answer_keyboard():
    return InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton(
                    text=text_keyboard.make_order,
                    callback_data='make_order',
                ),
            ],
            await main_keyboards.get_return_to_main_menu_keyboard_button(),
        ],
    )