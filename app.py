#! /usr/bin/env python
# -*- coding: utf-8 -*-

import asyncio
import logging
import sys
import time
from aiohttp import web

from aiogram import executor, types

from configurations.config import DEBUG
from loader import dp, bot

# from services.db_functions import delete_all_data_in_users_chat_id


async def set_default_commands(dp):
    await dp.bot.set_my_commands([
        types.BotCommand('start', 'Start bot'),
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

async def start_polling():
    await set_default_commands(dp)
    await dp.start_polling()


# async def 

routes = web.RouteTableDef()

@routes.post('/status_was_updated')
async def hello(request):
    print(request)
    data = await request.json()
    status = data['status']
    telegram_user_id = data['telegram_user_id']
    await send_message_to_user_about_status_change(telegram_user_id, status) 
    print(dir(request))
    return web.Response(text="Hello, world")


async def send_message_to_user_about_status_change(user_id, status):
    answer_text = f'Статус вашего заказа поменялся на: {status}'
    await bot.send_message(user_id, answer_text)


app = web.Application()
app.add_routes(routes)

async def run_aiohttp_server():
    runner = web.AppRunner(app)
    await runner.setup()
    site = web.TCPSite(runner, '127.0.0.1', 8080)
    await site.start()


async def create_task_group():
    await asyncio.gather(
        start_polling(),
        run_aiohttp_server(),
    )

if __name__ == '__main__':
    asyncio.new_event_loop().run_until_complete(create_task_group())
