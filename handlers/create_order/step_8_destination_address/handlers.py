from handlers.create_order.states import MakeOrderState
from handlers.create_order.step_9_final import handlers as step_9_handlers
from handlers.create_order.step_8_destination_address import text_answer

async def start_destination_address(message):
    await MakeOrderState.next()
    answer_text = text_answer.enter_adress
    await message.answer(answer_text)

async def is_destination_address_valid(destination_address):
    return len(destination_address) <= 100

async def destination_address_handler(message, state):
    if not await is_destination_address_valid(message.text):
        answer_text = text_answer.incorrect_adress
        await message.answer(answer_text)
    else:
        await state.update_data(destination_address=message.text)
        await step_9_handlers.start_final(message, state)
