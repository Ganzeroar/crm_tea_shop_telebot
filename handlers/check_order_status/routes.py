from loader import dp
from handlers.check_order_status import text_keyboard


def create_routes():
    from handlers.check_order_status import handlers
    dp.register_callback_query_handler(
        handlers.start_check_order_status,
        text =['check_order_status'],
    )

    from handlers.check_order_status.find_order_with_order_number import routes
    routes.create_routes()
    from handlers.check_order_status.find_order_with_phone import routes
    routes.create_routes()