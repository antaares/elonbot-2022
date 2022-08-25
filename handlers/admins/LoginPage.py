from aiogram import types

from loader import dp, db, bot

from filters.isAdmin import IsAdmin
from filters.privateChat import IsPrivate

from keyboards.default.adminKeys import ADMIN_MENU

@dp.message_handler(IsPrivate(), IsAdmin(), commands=['dastur'])
async def send_welcome(message: types.Message):
    text = "Assalomu alaykum, siz admin paneldasiz..."
    await message.answer(text=text, reply_markup=ADMIN_MENU)