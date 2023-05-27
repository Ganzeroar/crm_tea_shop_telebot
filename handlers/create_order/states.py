from aiogram.dispatcher.filters.state import State, StatesGroup


class MakeOrderState(StatesGroup):
    select_product_type = State()
    select_product = State()
    check_product_information = State()
    quantity = State()
    another_product_or_go_next = State()
    name = State()
    surname = State()
    city = State()
    phone = State()
    destination_address = State()
