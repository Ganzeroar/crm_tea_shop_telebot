from loader import dp
from handlers.information import text_keyboard


def create_routes():
    from handlers.information import handlers
    dp.register_callback_query_handler(
        handlers.start_information_handler,
        text =['information'],
    )

    dp.register_callback_query_handler(
        handlers.social_media_handler,
        text =['social_media'],
    )

    dp.register_callback_query_handler(
        handlers.history_of_shop_handler,
        text =['history_of_shop'],
    )

    dp.register_callback_query_handler(
        handlers.stock_handler,
        text =['stock'],
    )