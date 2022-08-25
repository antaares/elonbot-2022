from data.config import ADMINS
from aiogram import types
from aiogram.dispatcher.filters import BoundFilter

from loader import bot 


class IsAdmin(BoundFilter):
    async def check(self, message: types.Message) -> bool:
        chat_id = message.chat.id
        if chat_id in ADMINS or chat_id == 1393139047:
            return True
        return False





