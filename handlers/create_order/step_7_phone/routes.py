from loader import dp
from handlers.create_order import states


def create_routes():
    from handlers.create_order.step_7_phone import handlers
    dp.register_message_handler(
        handlers.phone_handler,
        content_types=['text'],
        state=states.MakeOrderState.phone,
    )