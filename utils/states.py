from aiogram.fsm.state import StatesGroup, State

class AdminRegistration(StatesGroup):
    first_name = State()
    second_name = State()
    