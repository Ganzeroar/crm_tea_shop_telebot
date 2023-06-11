from aiogram.types import CallbackQuery, Message
from aiogram.dispatcher import FSMContext
from handlers.create_order.step_0_select_type import handlers
from handlers.create_order import text_answer, keyboards
from handlers.handlers import start_main_menu
from services import db_functions


async def create_order(call: CallbackQuery):
    answer_text = text_answer.info_about_create_order
    answer_keyboard = await keyboards.get_return_to_main_menu_reply_keyboard()
    await call.message.answer(answer_text, reply_markup=answer_keyboard)

    await handlers.start_select_type(call)


async def return_to_main_menu(message: Message, state: FSMContext):
    await db_functions.delete_order_info(message)

    await state.finish()

    await start_main_menu(message)
