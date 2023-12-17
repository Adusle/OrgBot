from aiogram.fsm.state import StatesGroup, State

class AdminRegistration(StatesGroup):
    name = State()

class AdminEv(StatesGroup):
    ev = State()
    rem= State()

class UserRegistration(StatesGroup):
    name = State()

class UserEv(StatesGroup):
    ev = State()
