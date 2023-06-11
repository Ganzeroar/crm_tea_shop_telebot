from loader import dp


def create_routes():
    from handlers.create_order import handlers
    dp.register_callback_query_handler(
        handlers.create_order,
        text=['create_order'],
    )

    dp.register_message_handler(
        handlers.return_to_main_menu,
        text=['Вернуться в главное меню'],
        state='*',
    )

    from handlers.create_order.step_1_select_product import routes as step_1_routes
    step_1_routes.create_routes()

    from handlers.create_order.step_2_check_product_information import routes as step_2_routes
    step_2_routes.create_routes()

    from handlers.create_order.step_3_select_quantity import routes as step_3_routes
    step_3_routes.create_routes()

    from handlers.create_order.step_4_another_product_or_go_next import routes as step_4_routes_1
    step_4_routes_1.create_routes()

    from handlers.create_order.step_4_name import routes as step_4_routes
    step_4_routes.create_routes()

    from handlers.create_order.step_5_surname import routes as step_5_routes
    step_5_routes.create_routes()

    from handlers.create_order.step_7_phone import routes as step_7_routes
    step_7_routes.create_routes()

    from handlers.create_order.step_8_destination_address import routes as step_8_routes
    step_8_routes.create_routes()
