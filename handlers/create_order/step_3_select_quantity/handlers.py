from aiogram.types import CallbackQuery

from handlers.create_order.states import MakeOrderState
from services import db_functions
from handlers.create_order.step_4_name import handlers as step_4_handlers
from handlers.create_order.step_3_select_quantity import text_answer


async def start_select_quantity(call: CallbackQuery):
    await MakeOrderState.next()
    answer_text = text_answer.enter_quantity
    await call.message.answer(answer_text)


async def select_quantity_handler(message, state):
    product_quantity = await db_functions.get_product_quantity(message.from_user.id)

    user_order_quantity = message.text

    if user_order_quantity.isalpha():
        answer_text = text_answer.incorrect_quantity
        await message.answer(answer_text)
        return

    elif int(product_quantity) - int(user_order_quantity) < 0:
        answer_text = text_answer.wrong_count_of_product
        await message.answer(answer_text)
        return


    await state.update_data(quantity=message.text)
    await step_4_handlers.start_name(message)
