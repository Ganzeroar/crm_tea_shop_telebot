from loader import dp
from handlers.create_order import states


def create_routes():
    from handlers.create_order.step_8_destination_address import handlers
    dp.register_message_handler(
        handlers.destination_address_handler,
        content_types=['text'],
        state=states.MakeOrderState.destination_address,
    )