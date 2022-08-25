from aiogram.types import InlineKeyboardMarkup,InlineKeyboardButton
SUBSCRIBE = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(text="Channel", url="https://t.me/AioBotTest")],
        [InlineKeyboardButton(text="Check", callback_data="Checksub")]
    ]
)