import asyncio

from services import db_functions

if __name__ == '__main__':
    asyncio.run(db_functions.create_language_table())
    asyncio.run(db_functions.create_chat_information_table())
    asyncio.run(db_functions.create_user_actions_log_table())
    asyncio.run(db_functions.create_job_evaluation_table())
