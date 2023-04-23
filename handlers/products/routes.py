from loader import dp


def create_routes():
    from handlers.products import handlers
    dp.register_callback_query_handler(
        handlers.start_products,
        text=['products'],
    )
    
