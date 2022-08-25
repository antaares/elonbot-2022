from aiogram.types import ContentType, Message
from aiogram.types.message import ContentTypes

from loader import dp, bot, db

from filters import IsGroup

@dp.message_handler(IsGroup(), content_types=ContentType.NEW_CHAT_MEMBERS)
async def newMemberHandling(message: Message):
    user = message.from_user
    users = len(message.new_chat_members)
    db.new_chat(user.id, user.full_name, count=users)