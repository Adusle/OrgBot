from aiogram import Router, F , types, Bot
from data_base.bd import get_users_id, add_user
from keyboards import *
from aiogram.types import Message
from aiogram.fsm.context import FSMContext
from aiogram.types import ReplyKeyboardRemove
from aiogram.filters import Command , CommandObject, CommandStart
from utils.states import UserRegistration

router = Router()

@router.message(CommandStart())
async def cmd_start(message: types.Message, state: FSMContext):
    await message.answer("Добро пожаловать\n Для того, чтобы пользоваться ботом необходимо пройти регистрацию\n Введите ваше имя или же название группы, либо отвественно если, это парное выступление\n")
    await state.set_state(UserRegistration.name)


@router.message(UserRegistration.name)
async def add_user_name(message: types.Message, state: FSMContext):
    await state.update_data(name=message.text)
    user_telegram_id = message.from_user.id
    info = get_users_id(user_telegram_id)
    if info == None:                        
        add_user(user_telegram_id,message.text)
    await message.answer("Регистрация прошла успешно", reply_markup=keyboard.kb)
    await state.clear()
    
"""
@router.message(Command("info"))
async def cmd_start(message: types.Message, state: FSMContext):
    await message.answer("Что он может? Да нихуя собственно", reply_markup=ReplyKeyboardRemove())
  """  
"""
@router.message(F.text)
async def keyboard_us(message: types.Message, state: FSMContext):
    if message.text == "Список мероприятий":
        await message.answer("Мероприятия", reply_markup=keyboard.eventlist)
    if message.text == "Назад":
        await message.answer("Ты кент", reply_markup=keyboard.kb)
"""