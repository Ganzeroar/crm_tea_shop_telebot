from aiogram.types import CallbackQuery, Message

from handlers.create_order.states import MakeOrderState
from handlers.create_order.step_0_select_type import keyboards, text_answer
from handlers.create_order.step_1_select_product import handlers as step_1_handlers
from services import api


async def start_select_type(call: CallbackQuery):
    await MakeOrderState.select_product_type.set()

    user_id = call.from_user.id

    existing_types = await api.make_request_for_product_types()

    answer_text = text_answer.product_types
    answer_keyboard = await keyboards.create_product_types_keyboard(user_id, existing_types)
    await call.message.answer(answer_text, reply_markup=answer_keyboard, )


async def select_product_type_handler(call: CallbackQuery):
    button_data = call.data
    product_id = button_data.split('_')[0]

    await step_1_handlers.start_select_product(call, product_id)


async def start_ask_user_to_use_buttons(message: Message):
    answer_text = text_answer.ask_user_to_use_buttons

    await message.answer(answer_text)
