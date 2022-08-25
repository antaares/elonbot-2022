from aiogram import Dispatcher
from filters.isAdmin import IsAdmin
from filters.notYetUsers import NotYet

from loader import dp
from .admins import AdminFilter
from .groups import IsGroup
from .privateChat import IsPrivate
from .isMember import IsMember


if __name__ == "filters":
    dp.filters_factory.bind(AdminFilter)
    dp.filters_factory.bind(IsGroup)
    dp.filters_factory.bind(IsPrivate)
    dp.filters_factory.bind(IsMember)
    dp.filters_factory.bind(IsAdmin)
    dp.filters_factory.bind(NotYet)
