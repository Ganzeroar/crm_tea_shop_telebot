from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from handlers.create_order.step_6_city import handlers, routes


async def create_cities_keyboard(user_id, existing_cities):
    inline_keyboard_array = []
    for city in existing_cities:
        city_button = [
            InlineKeyboardButton(
                text=city.get('name'),
                callback_data=f"{city.get('id')}_{user_id}",
            )
        ]
        inline_keyboard_array.append(city_button)

        await routes.create_route(city.get('id'), user_id)

    return InlineKeyboardMarkup(
        inline_keyboard=inline_keyboard_array,
    )
