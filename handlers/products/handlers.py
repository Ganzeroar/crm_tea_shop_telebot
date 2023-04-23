from aiogram.types import CallbackQuery

from handlers.products import text_answer, keyboards
from services import api

async def start_products(call: CallbackQuery):
    existing_products = await api.make_request_products()
    print(213123)
    print(existing_products)
    answer_text = text_answer.products
    answer_keyboard = await keyboards.create_products_keyboard(existing_products)
    await call.message.answer(answer_text, reply_markup=answer_keyboard)

