from loader import dp
from handlers import text_keyboard


def create_routes():
    from handlers import handlers
    dp.register_message_handler(
        handlers.start_main_menu,
        commands=['start'],
    )
    
    from handlers.create_order import routes as create_order_routes
    create_order_routes.create_routes()

    dp.register_message_handler(
        handlers.start_ask_user_to_use_buttons,
        content_types=['text'],
    )

    dp.register_callback_query_handler(
        handlers.start_main_menu_from_callback,
        text=['main_menu'],
    )

    from handlers.information import routes
    routes.create_routes()

    from handlers.contacts import routes
    routes.create_routes()

    from handlers.check_order_status import routes
    routes.create_routes()
