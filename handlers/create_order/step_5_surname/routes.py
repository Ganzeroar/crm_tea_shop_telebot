from loader import dp
from handlers.create_order import states


def create_routes():
    from handlers.create_order.step_5_surname import handlers
    dp.register_message_handler(
        handlers.surname_handler,
        content_types=['text'],
        state=states.MakeOrderState.surname,
    )