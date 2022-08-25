from aiogram.types import chat
from data.config import CHANNELS
from aiogram import types
from aiogram.dispatcher.filters import BoundFilter

from loader import bot 

class IsMember(BoundFilter):
    async def check(self, message: types.Message) -> bool:
        status = await bot.get_chat_member(CHANNELS[0], message.from_user.id)
        all_status = ['creator','administrator','member']
        return not (status.status in all_status)




# class IsAdmin(BoundFilter):
#     async def isAdmin(self, message: types.Message) -> bool:
#         chat_id = message.chat.id
#         if chat_id in ADMINS:
#             return True
#         return False