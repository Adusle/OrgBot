from aiogram import Router, F , types
from data_base.bd import get_users_id, add_user
from keyboards import *
from aiogram.types import Message
from aiogram.fsm.context import FSMContext
from aiogram.types import ReplyKeyboardRemove
from aiogram.filters import Command , CommandObject, CommandStart

router = Router()

@router.message(CommandStart())
async def cmd_start(message: types.Message, state: FSMContext):
    
    user_telegram_id = message.from_user.id
    username = message.from_user.username   #Получаем айди и имя пользователя
    info = get_users_id(user_telegram_id)
    if info == None:                        #Проверяем есть ли пользователь в БД
        add_user(user_telegram_id,username)
    
    await message.answer("Ты кент", reply_markup=keyboard.kb)

@router.message(Command("info"))
async def cmd_start(message: types.Message, state: FSMContext):
    await message.answer("Что он может? Да нихуя собственно", reply_markup=ReplyKeyboardRemove())

@router.message(F.text)
async def keyboard_us(message: types.Message, state: FSMContext):
    if message.text == "Список мероприятий":
        await message.answer("Мероприятия", reply_markup=keyboard.eventlist)
    if message.text == "Назад":
        await message.answer("Ты кент", reply_markup=keyboard.kb)
