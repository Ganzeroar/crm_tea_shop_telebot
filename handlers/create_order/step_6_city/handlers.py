from aiogram.types import Message
from handlers.create_order.states import MakeOrderState
from handlers.create_order.step_7_phone import handlers as step_7_handlers
from services import api
from handlers.create_order.step_6_city import keyboards, text_answer


async def start_city(message):
    await MakeOrderState.next()

    user_id = message.from_user.id
    existing_cities = await api.make_request_for_cities()

    answer_text = text_answer.choose_city
    answer_keyboard = await keyboards.create_cities_keyboard(user_id, existing_cities)
    await message.answer(answer_text, reply_markup=answer_keyboard)


async def city_handler(call, state):
    button_data = call.data
    city_id = button_data.split('_')[0]

    await state.update_data(city=city_id)

    await step_7_handlers.start_phone(call)

async def start_ask_user_to_use_buttons(message: Message):
    answer_text = text_answer.ask_user_to_use_buttons

    await message.answer(answer_text)