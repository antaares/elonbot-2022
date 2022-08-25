# Bu script birorta user kanaldan chiqib ketib, botdan foydalanganda bunga yo'l qo'ymaydi...



from aiogram import types
from aiogram.dispatcher.storage import FSMContext
from handlers.users.start import bot_start
from keyboards.inline.startButtons import SUBSCRIBE

from loader import dp, db
from filters import IsPrivate, IsMember


@dp.message_handler(IsMember(), IsPrivate(), state="*")
async def UserNotSub(message: types.Message, state: FSMContext):
    await state.finish()
    await message.answer("Assalomu alaykum, siz kanallarimizni tark etgansiz, iltimos botdan toliq "
    "foydalanish uchun Kanalimizga obuna boling va uni tark etmang...")
    await message.answer("Iltimos kanallarga azo boling", reply_markup = SUBSCRIBE)
    try:
        db.add_user(
            id=message.from_user.id,
            name=message.from_user.full_name,
            language=message.from_user.language_code
            )
    except Exception as error:
       print(error)
