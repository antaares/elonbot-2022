from aiogram import types
from aiogram.dispatcher.storage import FSMContext

from data.config import how_member

from loader import dp, bot, db 
from keyboards.default.mainMenu import MAIN_MENU

@dp.callback_query_handler(text="checkcount")
async def checkCount(query: types.CallbackQuery, state: FSMContext):
    MSG = query.message
    id = query.from_user.id
    count = db.count_adding_users(id=id)
    if count == 0:
        text = f"Iltimos botdan to‘liq foydalanish uchun guruhimizga kamida {how_member} ta odam qo‘shgan bo‘lishingiz shart!!!"
        await query.answer(text=text, show_alert=True, cache_time=0)
        return
    elif count < how_member:
        text = f"ILtimos botdan to‘liq foydalanish uchun guruhimizga yana {how_member-count} ta odam qo‘shishingiz kerak!!!"
        await query.answer(text=text, show_alert=True, cache_time=0)
        return
    await MSG.delete()
    await state.finish()
    await bot.send_message(chat_id=MSG.chat.id, text="Kerakli bo'limni tanlang!", reply_markup=MAIN_MENU)



async def toMainMenu(message: types.Message):
    MSG = message
    await bot.send_message(chat_id=MSG.chat.id, text="Kerakli bo'limni tanlang!", reply_markup=MAIN_MENU)








