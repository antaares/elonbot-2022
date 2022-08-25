from aiogram.types import InlineKeyboardMarkup,InlineKeyboardButton




async def info_admins(name: str, admin_id: int, hint: bool) -> InlineKeyboardMarkup:
    info = "Tasdiqlangan!"
    if not hint:
        info = "Qaytarilgan!"
    return InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton(text=info, callback_data="info|{}|{}".format(name, admin_id))
                ]
    ]
    )