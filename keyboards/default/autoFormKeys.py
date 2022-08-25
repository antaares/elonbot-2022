from aiogram.types import ReplyKeyboardMarkup, KeyboardButton


CONTACT = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="kontakt ulashish", request_contact=True)
        ]
    ]
)