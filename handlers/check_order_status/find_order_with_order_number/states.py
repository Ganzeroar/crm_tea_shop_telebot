from aiogram.dispatcher.filters.state import State, StatesGroup

class CheckOrderWithNumberState(StatesGroup):
    waiting_for_order_number = State()