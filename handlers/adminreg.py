from aiogram import Router,F ,types
from aiogram.types import Message
from aiogram.filters import Filter, Command
from aiogram.fsm.context import FSMContext
from aiogram.filters import Command, StateFilter
from aiogram.fsm.context import FSMContext
from utils.states import AdminRegistration

router = Router()

@router.message(Command("hel"))
async def add_admin_name(message: types.Message, state: FSMContext):
    await state.set_state(AdminRegistration.first_name)
    await message.answer("Введите имя организатор")


    
