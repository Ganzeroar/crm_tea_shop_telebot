from services import api, db_functions
from handlers import handlers
from handlers.create_order.step_9_final import text_answer

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

    products_id_from_crm = await api.make_request_for_create_products(quantity, product_id)

    products_id_from_crm = [products_id_from_crm.get('id')]
    
    destination_address = user_data.get('destination_address')
    response = await api.make_request_for_create_order(products_id_from_crm, new_client_id, destination_address)
    
    order_id = response.get('id')
    
    answer_text = f'Номер вашего заказа - {order_id}'
    await message.answer(answer_text)
    
    answer_text = text_answer.final_form_text
    await message.answer(answer_text)

    await db_functions.delete_order_info(message)
    await state.finish()

    await handlers.start_main_menu(message)