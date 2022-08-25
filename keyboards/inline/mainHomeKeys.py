from typing import Text
from aiogram.types import InlineKeyboardMarkup,InlineKeyboardButton

YES_AND_NO = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="Bor", callback_data='Bor'),
            InlineKeyboardButton(text="Yoq", callback_data='Yoq')
        ]
    ]
)
def ADMIN_CONFIRM(user):
    ADMIN_CONFIRM = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="Tasdiqlansin", callback_data=f"confirm|{user}"),
            InlineKeyboardButton(text="Qaytarilsin", callback_data=f"inconfirm|{user}")
        ]
        ]
    )
    return ADMIN_CONFIRM