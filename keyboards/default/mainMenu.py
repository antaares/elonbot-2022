from aiogram.types import ReplyKeyboardMarkup, KeyboardButton


MAIN_MENU = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="🚔Avtomobil"),
            KeyboardButton(text="📱Smartphone")
        ],
        [
            KeyboardButton(text="🏡Hovlili uylar"),
            KeyboardButton(text="🏬 Kop qavatli uylar")
        ],
        [
            KeyboardButton(text="Boshqa turdagi e'lonlar")
        ]
    ],
    resize_keyboard=True,
    selective=True
)