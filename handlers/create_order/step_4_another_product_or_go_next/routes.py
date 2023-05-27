from loader import dp
from handlers.create_order.states import MakeOrderState


def create_routes():
    from handlers.create_order.step_4_another_product_or_go_next import handlers
    dp.register_callback_query_handler(
        handlers.select_another_product_handler,
        text=['select_another_product'],
        state=MakeOrderState.another_product_or_go_next,
    )

    dp.register_callback_query_handler(
        handlers.go_next_handler,
        text=['go_next'],
        state=MakeOrderState.another_product_or_go_next,
    )
