from loader import dp
from handlers.create_order.step_2_check_product_information import handlers
from handlers.create_order.states import MakeOrderState

def create_routes():
    dp.register_callback_query_handler(
        handlers.check_product_information_handler,
        text=['make_order'],
        state=MakeOrderState.check_product_information,
    )