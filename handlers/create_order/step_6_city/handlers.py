from handlers.create_order.states import MakeOrderState
from handlers.create_order.step_7_phone import handlers as step_7_handlers
from services import api
from handlers.create_order.step_6_city import keyboards


async def start_city(message):
    await MakeOrderState.next()

    user_id = message.from_user.id
    existing_cities = await api.make_request_for_cities()

    answer_text = 'Выберите город'
    answer_keyboard = await keyboards.create_cities_keyboard(user_id, existing_cities)
    await message.answer(answer_text, reply_markup=answer_keyboard)


async def city_handler(call, state):
    await state.update_data(city=call.message.text)

    await step_7_handlers.start_phone(call)