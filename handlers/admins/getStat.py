from aiogram import types
from aiogram.dispatcher.filters import Text
from loader import dp, db, bot

from filters.isAdmin import IsAdmin
from filters.privateChat import IsPrivate

from keyboards.default.adminKeys import ADMIN_MENU

@dp.message_handler(IsPrivate(), IsAdmin(), Text(equals="📈Statistika📉"), state="*")
async def SendStat(message: types.Message):
    users = db.count_users()
    text = f"Foydalanuvchilar: {users} ta"
    await message.answer(text=text)