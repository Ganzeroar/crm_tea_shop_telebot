from loader import dp
from handlers.create_order.step_6_city import handlers
from handlers.create_order.states import MakeOrderState


async def create_route(city_id, user_id):
    dp.register_callback_query_handler(
        handlers.city_handler,
        text=[f"{city_id}_{user_id}"],
        state=MakeOrderState.city
    )