from aiogram.types import InlineKeyboardMarkup,InlineKeyboardButton
SUBSCRIBE = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(text="Channel", url="https://t.me/elonlartahtasi")],
        [InlineKeyboardButton(text="Check", callback_data="Checksub")]
    ]
)