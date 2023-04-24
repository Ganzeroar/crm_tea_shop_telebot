from loader import dp
from handlers.create_order.step_1_select_product import handlers
from handlers.create_order.states import MakeOrderState


async def create_route(product_id, user_id):
    dp.register_callback_query_handler(
        handlers.select_product_handler,
        text=[f"{product_id}_{user_id}"],
        state=MakeOrderState.select_product
    )