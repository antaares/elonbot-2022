from aiogram.dispatcher.filters import Text
from aiogram import types
from aiogram.types.inline_keyboard import InlineKeyboardButton
from filters.privateChat import IsPrivate

from loader import dp 
MARKUP = types.InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton("Admin", url="https://t.me/SirojiddinXolxodjayev")
        ]
    ]
)

@dp.message_handler(IsPrivate(), Text(equals="Boshqa turdagi e'lonlar"))
async def otherAdver(message: types.Message):
    text = "Boshqa turdagi e'lonlar uchun admin bilan bog‘laning."
    await message.answer(text=text, reply_markup=MARKUP)