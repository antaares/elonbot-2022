from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandStart
from filters.privateChat import IsPrivate
from filters.isMember import IsMember
from keyboards.default.mainMenu import MAIN_MENU
from keyboards.inline.to_group import BUTTON_TO_GROUP
from loader import dp, db, bot

from keyboards.inline.startButtons import SUBSCRIBE

from data.config import how_member

@dp.message_handler(IsPrivate(), IsMember(), CommandStart(), state="*")
async def bot_start(message: types.Message):
    await message.answer(f"Salom, {message.from_user.full_name}!")
    await message.answer("Iltimos kanallarga azo boling", reply_markup=SUBSCRIBE)
    try:
        db.add_user(
            id=message.from_user.id,
            name=message.from_user.full_name,
            language=message.from_user.language_code
            )
    except Exception as error:
       print(error)

@dp.message_handler(IsPrivate(), CommandStart(), state="*")
async def bot_start(message: types.Message):
    await message.answer(f"Salom, {message.from_user.full_name}!")
    text = "Kerakli bo'limni tanlang!!!"
    await message.answer(text=text, reply_markup=MAIN_MENU)
    try:
        db.add_user(
            id=message.from_user.id,
            name=message.from_user.full_name,
            language=message.from_user.language_code
            )
    except Exception as error:
       print(error)
    