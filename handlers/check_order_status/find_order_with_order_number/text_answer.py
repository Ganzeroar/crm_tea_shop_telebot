from services import api

find_order_with_order_number = 'Введите номер заказа'

order_number_wrong = 'Пожалуйста, введите номер заказа используя только цифры'


async def create_answer_text(message):
    order_id = message
    order_info = await api.make_request_for_check_order_status(order_id)
    current_status_id = order_info.get('status')


    status_name = await api.make_request_for_name_order_status(current_status_id)
    if status_name == []:
        answer_text = 'Заказ с таким номером не найден. Проверьте правильность ввода и попробуйте снова'

        return answer_text

    elif not status_name == []:
        answer_text = status_name.get('name')
        if answer_text == 'В работе':
            answer_text = f'Ваш заказ № {order_id} сейчас находится в обработке! Примерная дата передачи посылки курьеру завтра. При смене статуса заказа мы Вас уведомим и позвоним.'
        elif answer_text == 'Передан курьеру':
            answer_text = f'Ваш заказ № {order_id} передан курьеру. В течение дня он позвонит Вам для согласования времени доставки.'

        return answer_text