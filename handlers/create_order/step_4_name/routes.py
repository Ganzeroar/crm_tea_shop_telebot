from loader import dp
from handlers.create_order import states


def create_routes():
    from handlers.create_order.step_4_name import handlers
    dp.register_message_handler(
        handlers.first_name_handler,
        content_types=['text'],
        state=states.MakeOrderState.name,
    )