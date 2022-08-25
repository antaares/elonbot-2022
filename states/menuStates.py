from aiogram.dispatcher.filters.state import StatesGroup, State


class MainAuto(StatesGroup):
    model = State()
    position = State()
    manuYear = State() # manufactured year
    carColor = State()
    carState = State()
    distance = State()
    transBox = State()
    carCost = State()
    phoneNumber = State()
    carCity = State()
    address = State()
    carPhoto = State()
    UserConfirm = State()

class MainSmartphone(StatesGroup):
    mdoel = State()
    totalMemory = State()
    documents = State()
    defaultBox = State()
    phoneState = State()
    phoneCost = State()
    phoneNumber = State()
    address = State()
    getPhonePhoto = State()
    UserConfirm = State()


class MainHouse(StatesGroup): # Hovlili uylar uchun
    totalArea = State()
    countRooms = State()
    conveniences = State() # qulayliklar
    houseState = State()
    houseCost = State()
    housePhoneNumber = State()
    address = State()
    UserConfirm = State()
    getHousePhoto = State()



class MainHome(StatesGroup): #kop qavatli uylar uchun
    totalFloor = State() # Binodagi jami qavatlar
    currentFloor = State() # sizning qavatingiz
    countRooms = State()
    homeThings = State()
    homeState = State()
    homeCost = State()
    homePhoneNumber = State()
    address = State()
    getHomePhoto = State()
    UserConfirm = State()


