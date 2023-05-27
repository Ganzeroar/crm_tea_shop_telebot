from aiogram.types import CallbackQuery, Message

from handlers.create_order.states import MakeOrderState
from services import db_functions
from handlers.create_order.step_4_name import handlers as step_4_handlers
from handlers.create_order.step_4_another_product_or_go_next import text_answer, keyboards
from handlers.create_order.step_0_select_type import handlers as step_1_handlers

async def start_another_product_or_go_next(message: Message, state):
    await MakeOrderState.next()
    await state.update_data(is_at_least_one_item_selected=True)

    answer_text = text_answer.another_product_or_go_next
    answer_keyboard = await keyboards.get_another_product_or_go_next_keyboard()
    await message.answer(answer_text, reply_markup=answer_keyboard)


async def select_another_product_handler(call: CallbackQuery):
    await step_1_handlers.start_select_type(call)


async def go_next_handler(call: CallbackQuery):
    await step_4_handlers.start_name(call.message)
