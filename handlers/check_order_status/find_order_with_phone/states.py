from aiogram.dispatcher.filters.state import State, StatesGroup

class CheckOrderWithPhoneState(StatesGroup):
    waiting_for_phone = State()