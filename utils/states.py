from aiogram.fsm.state import StatesGroup, State

class AdminEv(StatesGroup):
    name = State()

class UserRegistration(StatesGroup):
    name = State()
    event_number = State()
    
