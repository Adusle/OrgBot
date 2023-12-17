from aiogram.fsm.state import StatesGroup, State

class Admin(StatesGroup):
    ev = State()
    rem= State()
    red = State()
    an = State()

class User(StatesGroup):
    name = State()
    ev = State()
