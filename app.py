#! /usr/bin/env python
# -*- coding: utf-8 -*-

import logging
import sys
import time

from aiogram import executor, types

from configurations.config import DEBUG
from loader import dp
# from services.db_functions import delete_all_data_in_users_chat_id


async def set_default_commands(dp):
    await dp.bot.set_my_commands([
        types.BotCommand('start', 'Start bot'),
        types.BotCommand('help', 'Start bot'),
    ])


async def on_startup(dispatcher):
    await set_default_commands(dispatcher)


async def dev_on_startup(dispatcher):
    # await delete_all_data_in_users_chat_id()
    await set_default_commands(dispatcher)


def dev_run_local():
    executor.start_polling(dp, on_startup=dev_on_startup, skip_updates=True)


logging.basicConfig(
    level=logging.INFO,
    filename='telebot.log',
    filemode='a',
    format='TIME - %(asctime)s\nLEVEL - %(levelname)s\nNAME -- %(name)s\nMESSAGE - %(message)s\n',
)

if DEBUG:
    root = logging.getLogger()
    stream_handler = logging.StreamHandler(sys.stdout)
    stream_handler.setLevel(logging.INFO)
    formatter = logging.Formatter('TIME - %(asctime)s | LEVEL - %(levelname)s | NAME -- %(name)s | MESSAGE - %(message)s')
    stream_handler.setFormatter(formatter)
    root.addHandler(stream_handler)

if __name__ == '__main__':
    while True:
        try:
            executor.start_polling(dp, on_startup=on_startup, skip_updates=True)
        except Exception as e:
            time.sleep(5)
            logging.error(e)
