from aiogram.types import ReplyKeyboardMarkup, KeyboardButton


ADMIN_MENU = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="📈Statistika📉"),
            KeyboardButton(text="📤Xabar yuborish📬")
        ]
    ],
    resize_keyboard=True
)

BACK = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="Bekor qilish")
        ]
    ],
    resize_keyboard=True
)


CHOICE = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="Forward Message"),
            KeyboardButton(text="Copy Message")
        ],
        [
            KeyboardButton(text="Bekor qilish")
        ]
    ],
    resize_keyboard=True
)


CONFIRM = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="Yuborish"),
            KeyboardButton(text="Bekor qilish")
        ]
    ],
    resize_keyboard=True
)