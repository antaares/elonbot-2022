from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

CONFIRM = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="To‘g‘ri"),
            KeyboardButton(text="Noto‘g‘ri")
        ]
    ],
    resize_keyboard= True
)

