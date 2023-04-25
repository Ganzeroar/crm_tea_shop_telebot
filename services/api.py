from aiohttp import ClientSession

from configurations import config


async def make_request_products() -> str:
    async with ClientSession() as session:
        url = f'{config.URL_PATH_TO_CRM}/products'
        async with session.get(url=url) as response:
            response_data = await response.json()
            return response_data


async def make_request_for_product_info(product_id) -> str:
    async with ClientSession() as session:
        url = f'{config.URL_PATH_TO_CRM}/products/{product_id}'
        async with session.get(url=url) as response:
            response_data = await response.json()
            return response_data


async def make_request_for_product_type_info(product_type_id) -> str:
    async with ClientSession() as session:
        url = f'{config.URL_PATH_TO_CRM}/product_type/{product_type_id}'
        async with session.get(url=url) as response:
            response_data = await response.json()
            return response_data


async def make_request_for_cities() -> str:
    async with ClientSession() as session:
        url = f'{config.URL_PATH_TO_CRM}/cities'
        async with session.get(url=url) as response:
            response_data = await response.json()
            return response_data


async def make_request_for_create_client(name, surname, phone, user_city) -> str:
    async with ClientSession() as session:
        url = f'{config.URL_PATH_TO_CRM}/clients'
        request_data = {
            'name': name,
            'surname': surname,
            'phone': phone,
            'city': user_city,
        }
        async with session.post(url=url, json=request_data) as response:
            response_data = await response.json()
            return response_data


async def make_request_for_create_products(quantity, product_id) -> str:
    async with ClientSession() as session:
        url = f'{config.URL_PATH_TO_CRM}/create_products'
        request_data = {
            'product': product_id,
            'quantity': quantity,
        }
        async with session.post(url=url, json=request_data) as response:
            response_data = await response.json()
            print('make_request_for_create_products')
            print(response_data)
            return response_data



async def make_request_for_create_order(quantity, product_id, client_id) -> str:
    async with ClientSession() as session:
        url = f'{config.URL_PATH_TO_CRM}/orders'
        request_data = {
            'product': product_id,
            'client': client_id,
        }
        async with session.post(url=url, json=request_data) as response:
            response_data = await response.json()
            print('make_request_for_create_order')
            print(response_data)
            return response_data
