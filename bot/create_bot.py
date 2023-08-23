from aiogram import Bot
from aiogram.dispatcher import Dispatcher
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.contrib.fsm_storage.memory import MemoryStorage

storage = MemoryStorage()

class Search(StatesGroup):
    track = State()
    album = State()
    artist = State()

bot = Bot(token='5637666298:AAF7bA-2por37ctVOpjQ2J16jMKIeGGNKXw')
dp = Dispatcher(bot, storage=storage)