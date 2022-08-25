from data.config import how_member
from aiogram import types
from aiogram.dispatcher.filters import BoundFilter

from loader import db








class NotYet(BoundFilter):
    async def check(self, message: types.Message) -> bool:
        id = message.from_user.id
        count = db.count_adding_users(id=id)
        if count >= how_member:
            return True
        return False
