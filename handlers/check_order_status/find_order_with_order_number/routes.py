from loader import dp
from handlers.check_order_status.find_order_with_order_number.states import CheckOrderWithNumberState

def create_routes():
    from handlers.check_order_status.find_order_with_order_number import handlers
    dp.register_callback_query_handler(
        handlers.start_find_order_with_order_number_handler,
        text =['find_order_with_order_number', 'find_another_order_with_order_number'],
    )

    from handlers.check_order_status.find_order_with_order_number import handlers
    dp.register_message_handler(
        handlers.find_order_handler,
        content_types=['text'],
        state=CheckOrderWithNumberState.waiting_for_order_number,
    )