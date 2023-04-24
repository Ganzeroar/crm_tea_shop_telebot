from loader import dp
from handlers.create_order import states


def create_routes():
    from handlers.create_order.step_3_select_quantity import handlers
    dp.register_message_handler(
        handlers.select_quantity_handler,
        content_types=['text'],
        state=states.MakeOrderState.quantity,
    )