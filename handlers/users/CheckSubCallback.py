from aiogram import types
import data

from loader import dp, bot
# from handlers.users.start import bot_start
from keyboards.inline.to_group import BUTTON_TO_GROUP

@dp.callback_query_handler(text="Checksub")
async def checkCallUser(query: types.CallbackQuery):
    User = query.from_user
    status = await bot.get_chat_member(data.config.CHANNELS[0],User.id)
    all_status = ['creator','administrator','member']
    if status.status in all_status:
        await query.answer(text="malades", cache_time=0)
        await bot.delete_message(User.id, query.message.message_id)
        await bot.send_message(User.id, "Kanallarga azoligingiz tasdiqlandi...\n\n✅✅✅")
        await bot.send_message(User.id, "Iltimos Guruhimizga yangi foydalanuvchilarni taklif qiling!",
        reply_markup=BUTTON_TO_GROUP)
    else:
        await query.answer(text="Iltimos kanallarga azo bolmagunizcha bot ishlamaydi...",
        show_alert=True, cache_time=0)