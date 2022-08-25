from aiogram import types
from aiogram.dispatcher.filters import Text
from aiogram.dispatcher import FSMContext
from keyboards.default.mainMenu import MAIN_MENU
from keyboards.inline.to_group import BUTTON_TO_GROUP

from loader import dp, bot, db
from filters import IsPrivate

from data.config import how_member, ADMINS



MARKUP = BUTTON_TO_GROUP

@dp.message_handler(IsPrivate(), commands=['cancel'], state="*")
async def CancelDef(message: types.Message, state: FSMContext):
    id = message.chat.id
    count = db.count_adding_users(id=id)
    if count == 0 and id not in ADMINS:
        text = f"Iltimos botdan to‘liq foydalanish uchun guruhimizga kamida {how_member} ta odam qoshgan bolishingiz shart!!!"
        await message.answer(text=text, reply_markup=MARKUP)
        return
    elif count < how_member and id not in ADMINS:
        text = f"ILtimos botdan to‘liq foydalanish uchun guruhimizga yana {how_member-count} ta odam qoshishingiz kerak!!!"
        await message.answer(text=text, reply_markup=MARKUP)
        return
    await state.finish()
    await message.answer("Siz bosh menudasiz!!!", reply_markup=MAIN_MENU)