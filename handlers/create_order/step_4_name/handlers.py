from handlers.create_order.states import MakeOrderState
from handlers.create_order.step_5_surname import handlers as step_5_handlers

async def start_name(message):
    await MakeOrderState.next()
    answer_text = 'Введите Имя'
    await message.answer(answer_text)


async def is_first_name_valid(first_name):
    return first_name.isalpha()


async def first_name_handler(message, state):
    if not await is_first_name_valid(message.text):
        answer_text = 'Имя невалидно'
        await message.answer(answer_text)
    else:
        await state.update_data(name=message.text)
        await step_5_handlers.start_surname(message)