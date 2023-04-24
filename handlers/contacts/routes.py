from loader import dp
from handlers import text_keyboard


def create_routes():
    from handlers.contacts import handlers
    dp.register_callback_query_handler(
        handlers.start_contacts_handler,
        text =['contacts'],
    )

    dp.register_callback_query_handler(
        handlers.almaty_handler,
        text =['almaty'],
    )

    dp.register_callback_query_handler(
        handlers.astana_handler,
        text =['astana'],
    )

    dp.register_callback_query_handler(
        handlers.shymkent_handler,
        text =['shymkent'],
    )