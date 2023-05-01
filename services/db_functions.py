import datetime

import sqlite3
from aiogram.types import Message


async def get_connection_to_db():
    return sqlite3.connect("test.db")


# ORDER INFO 
async def create_order_info_table():
    conn = await get_connection_to_db()
    cursor = conn.cursor()
    cursor.execute(
        """CREATE TABLE order_info (id integer PRIMARY KEY, telegram_user_id int8 NOT NULL, product_id int8 NOT NULL, product_quantity int8 NOT NULL)""",
    )
    conn.commit()


async def create_order_info_data(telegram_user_id, product_id, product_quantity):
    conn = await get_connection_to_db()
    cursor = conn.cursor()
    cursor.execute(
        'INSERT INTO order_info (telegram_user_id, product_id, product_quantity) VALUES (%s, %s, %s);',
        [telegram_user_id, product_id, product_quantity],
    )
    conn.commit()


async def get_product_quantity(telegram_user_id):
    conn = await get_connection_to_db()
    cursor = conn.cursor()
    cursor.execute(
        'SELECT product_quantity FROM order_info WHERE telegram_user_id = (%s);',
        [telegram_user_id],
    )
    user_data = cursor.fetchone()
    return user_data[0]


async def get_product_id(telegram_user_id):
    conn = await get_connection_to_db()
    cursor = conn.cursor()
    cursor.execute(
        'SELECT product_id FROM order_info WHERE telegram_user_id = (%s);',
        [telegram_user_id],
    )
    user_data = cursor.fetchone()
    return user_data[0]


async def delete_order_info(message: Message):
    user_id = message.from_user.id

    conn = await get_connection_to_db()
    cursor = conn.cursor()
    cursor.execute(
        'DELETE FROM order_info WHERE telegram_user_id = (%s);',
        [user_id],
    )
    conn.commit()

# CHAT INFORMATION

async def create_chat_information_table():
    conn = await get_connection_to_db()
    cursor = conn.cursor()
    cursor.execute(
        """CREATE TABLE chat_information (id integer PRIMARY KEY, chat_id varchar NOT NULL, telegram_user_id int8 NOT NULL, chat_session_state varchar NOT NULL)""",
    )
    conn.commit()


async def update_chat_session_state(chat_id, chat_session_state):
    conn = await get_connection_to_db()
    cursor = conn.cursor()
    cursor.execute(
        'UPDATE chat_information SET chat_session_state = (%s) WHERE chat_id = (%s);',
        [chat_session_state, chat_id],
    )
    conn.commit()


async def get_chat_session_state(chat_id):
    conn = await get_connection_to_db()
    cursor = conn.cursor()
    cursor.execute(
        'SELECT chat_session_state FROM chat_information WHERE chat_id = (%s);',
        [chat_id],
    )
    user_data = cursor.fetchone()
    return user_data[0]


async def delete_users_chat_id_from_chat_information(message: Message):
    user_id = message.from_user.id

    conn = await get_connection_to_db()
    cursor = conn.cursor()
    cursor.execute(
        'DELETE FROM chat_information WHERE telegram_user_id = (%s);',
        [user_id],
    )
    conn.commit()


async def delete_all_data_in_users_chat_id():
    conn = await get_connection_to_db()
    cursor = conn.cursor()
    cursor.execute(
        'DELETE FROM chat_information;',
    )
    conn.commit()


async def create_chat_information_data(chat_id, telegram_user_id, session_state):
    conn = await get_connection_to_db()
    cursor = conn.cursor()
    cursor.execute(
        'INSERT INTO chat_information (chat_id, telegram_user_id, chat_session_state) VALUES (%s, %s, %s);',
        [chat_id, telegram_user_id, session_state],
    )
    conn.commit()


async def get_user_chat_id_from_chat_information(message: Message) -> str:
    user_id = message.from_user.id

    conn = await get_connection_to_db()
    cursor = conn.cursor()
    cursor.execute(
        'SELECT chat_id FROM chat_information WHERE telegram_user_id = (%s);',
        [user_id],
    )
    user_data = cursor.fetchone()
    if user_data is None:
        return None
    return user_data[0]


async def get_telegram_user_id_using_chat_id(chat_id: int) -> str:
    conn = await get_connection_to_db()
    cursor = conn.cursor()
    cursor.execute(
        'SELECT telegram_user_id FROM chat_information WHERE chat_id = (%s);',
        [chat_id],
    )
    user_data = cursor.fetchone()
    if user_data is None:
        return None
    return user_data[0]