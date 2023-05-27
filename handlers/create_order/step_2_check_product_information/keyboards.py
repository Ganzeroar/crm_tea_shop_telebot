from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from handlers.create_order.step_2_check_product_information import text_keyboard
from handlers import keyboards as main_keyboards


async def get_product_answer_keyboard(is_at_least_one_item_selected, product_quantity):
    print(is_at_least_one_item_selected)
    print(product_quantity)
    if is_at_least_one_item_selected and product_quantity != 'Нет в наличии':
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
                        text=text_keyboard.continue_main_order,
                        callback_data='continue_main_order',
                    ),
                ],
                [
                    InlineKeyboardButton(
                        text=text_keyboard.return_to_select_product_type,
                        callback_data='return_to_select_product_type',
                    ),
                ],
            ],
        )
    elif is_at_least_one_item_selected and product_quantity == 'Нет в наличии':
        return InlineKeyboardMarkup(
            inline_keyboard=[
                [
                    InlineKeyboardButton(
                        text=text_keyboard.continue_main_order,
                        callback_data='continue_main_order',
                    ),
                ],
                [
                    InlineKeyboardButton(
                        text=text_keyboard.return_to_select_product_type,
                        callback_data='return_to_select_product_type',
                    ),
                ],
            ],
        )
    elif not is_at_least_one_item_selected and product_quantity != 'Нет в наличии':
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
                        text=text_keyboard.return_to_select_product_type,
                        callback_data='return_to_select_product_type',
                    ),
                ],
            ],
        )    
    elif not is_at_least_one_item_selected and product_quantity == 'Нет в наличии':
        return InlineKeyboardMarkup(
            inline_keyboard=[
                [   
                    InlineKeyboardButton(
                        text=text_keyboard.return_to_select_product_type,
                        callback_data='return_to_select_product_type',
                    ),
                ],
            ],
        )