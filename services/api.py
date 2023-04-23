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



async def make_request_for_chat_id() -> str:
    async with ClientSession() as session:
        url = f'{config.URL_PATH_TO_CRM}/chats?tenantUrl={config.TENANT_URL}'
        initial_data = {
            'phone_number': '',
        }
        async with session.post(url=url, json=initial_data) as response:
            response_data = await response.json()
            return response_data.get('chat_id')