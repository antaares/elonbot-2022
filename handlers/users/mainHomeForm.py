import asyncio
from aiogram import types
from aiogram.types import message
from keyboards.default.cancel_keys import CANCEL
from keyboards.default.mainHomeKeys import CONFIRM
from keyboards.default.mainMenu import MAIN_MENU
from states.menuStates import MainHome
from aiogram.dispatcher.filters import Text, state
from aiogram.dispatcher import FSMContext

from loader import dp, bot, db
from filters import IsPrivate

from data.config import ADMIN_GROUP, ADMINS, how_member

from keyboards.inline.mainHomeKeys import ADMIN_CONFIRM, YES_AND_NO
from keyboards.inline.to_group import BUTTON_TO_GROUP
from utils.photograph import upload_photo





TEXT = {
    'start': ("Assalomu alaykum, Kop qavatli uylar boyicha reklama bolimiga xush kelibsiz!!!\n"
        "Iltimos arizangiz qabul qilinishi uchun barcha talablarni togri bajaring...\n"
        "Formani bekor qilish uchun /cancel buyrug'ini bering...\n\n\n"
        "Binodagi jami qavatlar sonini kiriting:"),
    'floor': "Qaysi qavatda turasiz?",
    'rooms': "Uydagi xonalar sonini kiriting:",
    'things': "Uyning jihozlari bormi?",
    'cost': 'Uyga qanday narx taklif qilasiz?',
    'phone': 'Boglanish uchun bitta telefon raqam qoldiring:',
    'city': 'Qaysi shaharda yashaysiz?',
    'photo': "Iltimos uyning bir dona suratini yuboring",
    'holat': "Uyning holati qanday?",
}












@dp.message_handler(IsPrivate(),Text(equals="🏬 Kop qavatli uylar"), state="*")
async def startHomeForm(message: types.Message, state: FSMContext):
    id = message.chat.id
    count = db.count_adding_users(id=id)
    if count<how_member and id not in ADMINS:
        warning = f"Iltimos botdan to‘liq foydalanish uchun guruhimizga kamida {how_member - count} ta odam qo‘shgan bo‘lishingiz shart!!!"
        await message.answer(text=warning, reply_markup=BUTTON_TO_GROUP)
        await state.finish()
        return
    ##
    text = TEXT['start']
    await message.answer(text=text, reply_markup=CANCEL)
    await MainHome.totalFloor.set()

@dp.message_handler(state=MainHome.totalFloor)
async def getTotalFloor(message: types.Message, state: FSMContext):
    data = message.text
    await state.update_data({'floor':data})
    await message.answer(TEXT['floor'])
    await MainHome.currentFloor.set()
    await bot.delete_message(message.chat.id, message.message_id-1)
    await message.delete()


@dp.message_handler(state=MainHome.currentFloor)
async def getCurrentFloor(message: types.Message, state: FSMContext):
    data = message.text
    await state.update_data(current = data)
    await message.answer(TEXT['rooms'])
    await MainHome.countRooms.set()
    await bot.delete_message(message.chat.id, message.message_id-1)
    await message.delete()
    


@dp.message_handler(state=MainHome.countRooms)
async def getCountRooms(message: types.Message, state: FSMContext):
    data = message.text
    await state.update_data(rooms = data)
    await message.answer(TEXT['things'], reply_markup=YES_AND_NO)
    await MainHome.homeThings.set()
    await bot.delete_message(message.chat.id, message.message_id-1)
    await message.delete()


@dp.message_handler(state=MainHome.homeState)
async def getHomeState(message: types.Message, state: FSMContext):
    data = message.text
    await state.update_data(homestate = data)
    await message.answer(TEXT['cost'])
    await MainHome.homeCost.set()
    await bot.delete_message(message.chat.id, message.message_id-1)
    await message.delete()


@dp.message_handler(state=MainHome.homeCost)
async def getHomeCost(message: types.Message, state: FSMContext):
    data = message.text
    await state.update_data(cost = data)
    await message.answer(TEXT['phone'])
    await MainHome.homePhoneNumber.set()
    await bot.delete_message(message.chat.id, message.message_id-1)
    await message.delete()

@dp.message_handler(state=MainHome.homePhoneNumber)
async def getHomeNumber(message: types.Message, state: FSMContext):
    data = message.text
    await state.update_data(number = data)
    await message.answer(TEXT['city'])
    await MainHome.address.set()
    await bot.delete_message(message.chat.id, message.message_id-1)
    await message.delete()

@dp.message_handler(state=MainHome.address)
async def getAddress(message: types.Message, state: FSMContext):
    data = "#" + message.text.replace(" ", " #")
    await state.update_data(address = data)
    await message.answer(TEXT['photo'])
    await MainHome.getHomePhoto.set()
    await bot.delete_message(message.chat.id, message.message_id-1)
    await message.delete()



@dp.message_handler(content_types='photo', state=MainHome.getHomePhoto)
async def getPhoto(message: types.Message, state: FSMContext):
    photo = message.photo[-1]
    link = await upload_photo(photo = photo)
    await state.update_data(photo = link)
    await bot.delete_message(message.chat.id, message.message_id-1)
    await message.delete()
    await confirmation(message, state)






@dp.message_handler(state=MainHome.UserConfirm)
async def userConfirm(message: types.Message, state: FSMContext):
    data = message.text
    if data == "To‘g‘ri":
        data = await state.get_data()
        await bot.copy_message(ADMIN_GROUP, message.chat.id, data['msg_id'], reply_markup=ADMIN_CONFIRM(message.from_user.id))
        await state.finish()
    else:
        await bot.delete_message(message.chat.id, message.message_id-2)
        await bot.delete_message(message.chat.id, message.message_id-1)
        await message.delete()
        await state.finish()
    await bot.send_message(chat_id=message.chat.id, text="Kerakli bo'limni tanlang!", reply_markup=MAIN_MENU)
    












# callbacks
@dp.callback_query_handler(state=MainHome.homeThings)
async def getHomeThings(query: types.CallbackQuery, state: FSMContext):
    data = query.data
    await state.update_data(things = data)
    await bot.send_message(chat_id=query.message.chat.id, text=TEXT['holat'])
    await MainHome.homeState.set()
    await bot.delete_message(query.message.chat.id, query.message.message_id)




async def returnDatas(state: FSMContext):
    data = await state.get_data()
    floors = data['floor']
    current = data['current']
    rooms = data['rooms']
    things = data['things']
    homestate = data['homestate']
    cost = data['cost']
    number = data['number']
    address = data['address']
    text = f"#{address} #uy\n"\
    f"Jami qavatlar: {floors}\n"\
    f"Nechanchi qavat: {current}\n"\
    f"Xonalar soni: {rooms}\n"\
    f"Uydagi jihozlar: {things}\n"\
    f"Uyning holati: {homestate}\n"\
    f"Taklif qilingan narx: {cost}\n"\
    f"Boglanish uchun raqam: {number}\n"\
    f"Uyning manzili: {address}\n"
    return text





async def confirmation(message: types.Message, state: FSMContext):
    await message.answer("Siz yuborgan ma'lumotlar togri ekanligiga ishonchingiz komilmi?")
    data = await state.get_data()
    photo = data['photo']
    text = await returnDatas(state)
    ##
    await asyncio.sleep(0.5)
    msg = await message.answer_photo(
        photo=photo,
        caption=text, 
        reply_markup = CONFIRM)
    ##
    await MainHome.UserConfirm.set()
    msg_id = msg.message_id
    await state.update_data(msg_id = msg_id)
    