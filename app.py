import sqlite3
from aiogram import executor

from loader import dp, db
import filters, handlers
#from utils import ErrorCoder
from utils.notify_admins import on_startup_notify
from utils.set_bot_commands import set_default_commands

async def on_startup(dispatcher):
    # Birlamchi komandalar (/start va /help)
    # await set_default_commands(dispatcher)
    try:
        db.create_table_users()
        db.create_group_table()
    except sqlite3.IntegrityError as error:
        pass

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True, on_startup=on_startup)
