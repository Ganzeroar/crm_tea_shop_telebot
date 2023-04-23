from environs import Env

env = Env()
env.read_env()

DEBUG = env.bool('DEBUG')

BOT_TOKEN = env.str('BOT_TOKEN')

APP_ID = env.str('APP_ID')
SUB_DOMAIN = env.str('SUB_DOMAIN')
TENANT_URL = env.str('TENANT_URL')

DATABASE = env.str('DATABASE')
DB_USER = env.str('DB_USER')
PASSWORD = env.str('PASSWORD')
HOST = env.str('HOST')
PORT = env.str('PORT')
OPTIONS = env.str('OPTIONS')

URL_PATH_TO_CRM = env.str('URL_PATH_TO_CRM')

