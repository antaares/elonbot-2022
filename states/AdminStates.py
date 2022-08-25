from aiogram.dispatcher.filters.state import StatesGroup, State


class FullAdmin(StatesGroup):
    getMessage = State()
    Choice = State()
    confirm = State()
    StackEnd = State()

class Comment(StatesGroup):
    GetComment = State()