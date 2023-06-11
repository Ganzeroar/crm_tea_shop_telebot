from loader import dp
from handlers.create_order.step_1_select_product import handlers
from handlers.create_order.states import MakeOrderState


async def create_route(product_id, user_id):
    dp.register_message_handler(
        handlers.start_ask_user_to_use_buttons,
        content_types=['text'],
        state=MakeOrderState.select_product
    )

    dp.register_callback_query_handler(
        handlers.select_product_handler,
        text=[f"{product_id}_{user_id}"],
        state=MakeOrderState.select_product
    )


def create_routes():
    dp.register_callback_query_handler(
        handlers.select_product_next_page,
        text=["next_page"],
        state=MakeOrderState.select_product
    )

    dp.register_callback_query_handler(
        handlers.select_product_previous_page,
        text=["previous_page"],
        state=MakeOrderState.select_product
    )
