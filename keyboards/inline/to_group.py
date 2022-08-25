from aiogram.types import InlineKeyboardMarkup,InlineKeyboardButton
from data.config import GROUP_LINK
BUTTON_TO_GROUP = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="Guruhga o‘ting", url=GROUP_LINK)
            ],
    [InlineKeyboardButton(text="Tekshirish", callback_data="checkcount")]]
)