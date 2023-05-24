from aiogram.types import CallbackQuery

from handlers.create_order.step_0_select_type import handlers


async def create_order(call: CallbackQuery):
    await handlers.start_select_type(call)
