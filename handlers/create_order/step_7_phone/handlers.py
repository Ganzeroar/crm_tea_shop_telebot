from handlers.create_order.states import MakeOrderState
from handlers.create_order.step_8_destination_address import handlers as step_8_handlers
from phonenumbers import carrier, phonenumberutil, parse as phonenumbers_parse
from handlers.create_order.step_7_phone import text_answer

async def start_phone(call):
    await MakeOrderState.next()
    answer_text = text_answer.enter_phone
    await call.message.answer(answer_text)

async def is_phone_valid(phone):
    if '+7' in phone:
        phone = phone.replace('+7', '8', 1)
    if not phone.isdigit():
        return False
    try:
        is_phone = carrier._is_mobile(phonenumberutil.is_valid_number(phonenumbers_parse(phone, 'KZ')))
    except phonenumberutil.NumberParseException:
        return False
    return is_phone

async def phone_handler(message, state):
    if not await is_phone_valid(message.text):
        answer_text = text_answer.incorrect_phone
        await message.answer(answer_text)
    else:
        await state.update_data(phone=message.text)

        await step_8_handlers.start_destination_address(message)
