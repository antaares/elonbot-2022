import asyncio
from aiogram.bot.bot import Bot
from aiogram.dispatcher.filters import Text
from aiogram import types
from aiogram.dispatcher.storage import FSMContext


from loader import dp, db, bot

from filters.privateChat import IsPrivate
from filters.isAdmin import IsAdmin
from states.AdminStates import FullAdmin


from keyboards.default.adminKeys import ADMIN_MENU, CHOICE, BACK, CONFIRM
from utils.db_api.sqlite import Database


@dp.message_handler(IsPrivate(), IsAdmin(), Text(equals="📤Xabar yuborish📬"), state="*")
async def startForm(message: types.Message, state: FSMContext):
    text = "Ho‘sh, demak boshladik, menga barcha foydalanuvchilarga yubormoqchi bo‘lgan xabaringizni yuboring:"
    await message.answer(text=text, reply_markup=BACK)
    await FullAdmin.getMessage.set()

@dp.message_handler(content_types=types.ContentType.ANY, state=FullAdmin.getMessage)
async def get_message(message: types.Message, state: FSMContext):
    text = message.text
    if text == "Bekor qilish":
        await message.answer(text="Assalomu alaykum, siz admin paneldasiz...", reply_markup=ADMIN_MENU)
        return
    msg_id = message.message_id
    chat_id = message.chat.id
    await state.update_data({'msg':msg_id})
    await state.update_data({'chat':chat_id})
    await message.answer(text="Qaysi usulda yuboramiz?", reply_markup=CHOICE)
    await FullAdmin.Choice.set()


@dp.message_handler(state=FullAdmin.Choice)
async def choiceMethod(message: types.Message, state: FSMContext):
    text = message.text
    if text == "Bekor qilish":
        await message.answer(text="Assalomu alaykum, siz admin paneldasiz...", reply_markup=ADMIN_MENU)
        return
    method = message.text
    await state.update_data({"method":method})
    data = await state.get_data()
    msg_id = data.get('msg')
    await bot.send_message(chat_id= message.chat.id, text="Shu xabarni yuboramizmi?",
    reply_to_message_id=msg_id, reply_markup=CONFIRM)
    await FullAdmin.confirm.set()


@dp.message_handler(state=FullAdmin.confirm)
async def Sending(message: types.Message, state: FSMContext):
    text = message.text
    if text == "Yuborish":
        data = await state.get_data()
        method = data.get('method')
        chat = data.get('chat')
        if method == "Forward Message":
            count = await SEND_FORWARD(db, bot, state)
            send_text = f"Tayyor, sizning xabaringiz {count} ta foydalanuvchiga yetkazildi..."
            await bot.send_message(chat_id=chat, text=send_text, reply_markup=ADMIN_MENU)
        else:
            count = await SEND_COPY(db, bot, state)
            send_text = f"Tayyor, sizning xabaringiz {count} ta foydalanuvchiga yetkazildi..."
            await bot.send_message(chat_id=chat, text=send_text, reply_markup=ADMIN_MENU)
    else:
        await message.answer(text="Assalomu alaykum, siz admin paneldasiz...", reply_markup=ADMIN_MENU)
    await state.finish()










async def SEND_COPY(db: Database, bot: Bot, state: FSMContext):
    users = db.all()
    data = await state.get_data()
    chat = data.get('chat')
    msg = data.get('msg')
    count = 0
    for user in users:
        try:
            await bot.copy_message(chat_id=user, from_chat_id=chat, message_id=msg)
            count += 1
            await asyncio.sleep(0.3)
        except Exception as e:
            print(e)
    return count


async def SEND_FORWARD(db: Database, bot: Bot, state: FSMContext):
    users = db.all()
    data = await state.get_data()
    chat = data.get('chat')
    msg = data.get('msg')
    count = 0
    for user in users:
        try:
            await bot.forward_message(chat_id=user, from_chat_id=chat, message_id=msg)
            count += 1
            await asyncio.sleep(0.3)
        except Exception as e:
            print(e)
    return count