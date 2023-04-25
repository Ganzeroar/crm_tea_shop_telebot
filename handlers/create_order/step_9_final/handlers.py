from services import api, db_functions
from handlers import handlers

async def start_final(message, state):
    user_data = await state.get_data()
    user_name = user_data.get('name')
    user_surname = user_data.get('surname')
    user_phone = user_data.get('phone')
    user_city = user_data.get('city')

    client_data = await api.make_request_for_create_client(user_name, user_surname, user_phone, user_city)
    new_client_id = client_data.get('id')
        
    quantity = user_data.get('quantity')
    product_id = await db_functions.get_product_id(message.from_user.id)

    response = await api.make_request_for_create_order(quantity, product_id, new_client_id)
    
    order_id = response.get('id')
    
    answer_text = f'Номер вашего заказа - {order_id}'
    await message.answer(answer_text)
    
    answer_text = 'Спасибо за обращение! Ваш заказ уже в работе. Мы вам сообщим, когда заказ перейдёт курьеру.'
    await message.answer(answer_text)

    await db_functions.delete_order_info(message)
    await state.finish()

    await handlers.start_main_menu(message)