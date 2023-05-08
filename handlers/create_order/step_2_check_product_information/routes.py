from loader import dp
from handlers.create_order.step_2_check_product_information import handlers
from handlers.create_order.states import MakeOrderState

def create_routes():
    dp.register_message_handler(
        handlers.start_ask_user_to_use_buttons,
        content_types=['text'],
        state=MakeOrderState.check_product_information
    )

    dp.register_callback_query_handler(
        handlers.check_product_information_handler,
        text=['make_order'],
        state=MakeOrderState.check_product_information,
    )

    dp.register_callback_query_handler(
        handlers.return_to_main_menu_handler,
        text=['main_menu'],
        state=MakeOrderState.check_product_information,
    )