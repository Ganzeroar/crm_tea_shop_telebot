from loader import dp
from handlers.check_order_status.find_order_with_phone.states import CheckOrderWithPhoneState

def create_routes():
    from handlers.check_order_status.find_order_with_phone import handlers
    dp.register_callback_query_handler(
        handlers.find_order_with_phone_handler,
        text =['find_order_with_phone', 'find_another_order_with_phone'],
    )

    from handlers.check_order_status.find_order_with_phone import handlers
    dp.register_message_handler(
        handlers.find_order_handler,
        content_types=['text'],
        state=CheckOrderWithPhoneState.waiting_for_phone,
    )