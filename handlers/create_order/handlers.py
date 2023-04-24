from aiogram.types import CallbackQuery

from handlers.create_order.step_1_select_product import handlers


async def create_order(call: CallbackQuery):
    await handlers.start_select_product(call)




