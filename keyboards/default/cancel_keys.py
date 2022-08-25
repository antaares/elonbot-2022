from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

CANCEL = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="/cancel")
        ]
    ],
    selective=True,
    resize_keyboard=True
)