from aiogram.types import InlineKeyboardMarkup,InlineKeyboardButton

DEVICE_DOCS = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="Bor", callback_data="bor"),
            InlineKeyboardButton(text="Yo‘q", callback_data="yoq")
        ]
    ]
)

DEVICE_BOX = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="Bor", callback_data="bor"),
            InlineKeyboardButton(text="Yo‘q", callback_data="yoq")
        ]
    ]
)