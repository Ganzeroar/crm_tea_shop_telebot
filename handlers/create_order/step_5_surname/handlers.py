from handlers.create_order.states import MakeOrderState
from handlers.create_order.step_6_city import handlers as step_6_handlers

async def start_surname(message):
    await MakeOrderState.next()
    answer_text = 'Введите фамилию'
    await message.answer(answer_text)


async def is_surname_valid(surname):
    return surname.isalpha()


async def surname_handler(message, state):
    if not await is_surname_valid(message.text):
        answer_text = 'Фамилия невалидно'
        await message.answer(answer_text)
    else:
        await state.update_data(surname=message.text)

        await step_6_handlers.start_city(message)

