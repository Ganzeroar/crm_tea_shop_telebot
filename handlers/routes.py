from loader import dp
from handlers import text_keyboard


def create_routes():
    from handlers import handlers
    dp.register_message_handler(
        handlers.start_main_menu,
        commands=['start'],
    )
    
    from handlers.create_order import routes as products_routes
    products_routes.create_routes()