import asyncio

from services import db_functions

if __name__ == '__main__':
    asyncio.run(db_functions.create_order_info_table())
    asyncio.run(db_functions.create_chat_information_table())
