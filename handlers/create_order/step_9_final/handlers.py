from services import api, db_functions
from handlers import handlers
from handlers.create_order.step_9_final import text_answer

async def start_final(message, state):
    user_data = await state.get_data()
    user_name = user_data.get('name')
    user_surname = user_data.get('surname')
    user_phone = user_data.get('phone')
    user_city = user_data.get('city')
    telegram_user_id = message.from_user.id

    client_data = await api.make_request_for_create_client(user_name, user_surname, user_phone, user_city, telegram_user_id)
    new_client_id = client_data.get('id')
        
    quantity = user_data.get('quantity')
    product_info = await db_functions.get_product_info(message.from_user.id)
    product_info_arr = []
    for product_and_quantity in product_info:
        proudct_id = product_and_quantity[1]
        proudct_quantity = product_and_quantity[0]
        product_info_arr.append(
            {
                'product': proudct_id,
                'quantity': proudct_quantity,
            },
        )
    print(product_info)
    destination_address = user_data.get('destination_address')
    response = await api.make_request_for_create_order(product_info_arr, new_client_id, destination_address)
    
    order_id = response.get('id')
    
    answer_text = f'Номер вашего заказа - {order_id}'
    await message.answer(answer_text)
    
    answer_text = text_answer.final_form_text
    await message.answer(answer_text)

    await db_functions.delete_order_info(message)
    await state.finish()

    await handlers.start_main_menu(message)