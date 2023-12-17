from aiogram import Router, F , types
from data_base.bd import get_users_id, add_user
from keyboards import *
from aiogram.types import Message
from aiogram.fsm.context import FSMContext
from aiogram.types import ReplyKeyboardRemove
from aiogram.filters import Command , CommandObject, CommandStart
from utils.states import User
from data_base.eventbd import add_username, print_list, add_user_id

router = Router()

@router.message(CommandStart())
async def cmd_start(message: types.Message, state: FSMContext):
    await message.answer("Добро пожаловать\n Для того, чтобы пользоваться ботом необходимо пройти регистрацию\n Введите ваше имя или же название группы, либо отвественно если, это парное выступление\n")
    await state.set_state(User.name)


@router.message(User.name)
async def add_user_name(message: types.Message, state: FSMContext):
    await state.update_data(name=message.text)
    user_telegram_id = message.from_user.id
    info = get_users_id(user_telegram_id)
    if info == None:
        add_user(user_telegram_id,message.text)
    await message.answer("Регистрация прошла успешно", reply_markup=keyboard.kb)
    await state.clear()


@router.message(Command("info"))
async def cmd_start(message: types.Message, state: FSMContext):
    await message.answer("Что он может? Да нихуя собственно", reply_markup=ReplyKeyboardRemove())

@router.message(F.text.lower()=="мероприятие")
async def keyboard_us(message: types.Message):
    await message.answer("Список выступлений", reply_markup=keyboard.event)
    data = print_list()
    result_message = ""
    for row in data:
        id_value, event_value, username_value = row
        result_message += f"Порядок: {id_value}, Название: {event_value} Выступает: {username_value}\n"
    result_message = result_message.replace("None", "Участие не подтвердил ")
    await message.answer(text=result_message)

@router.message(F.text.lower()=="зарегистрироваться")
async def keyboard_us(message: types.Message, state: FSMContext):
    await state.set_state(User.ev)
    await message.answer("Выберите номер выступления", reply_markup=keyboard.event)

@router.message(User.ev)
async def keyboard_us(message: types.Message, state: FSMContext):
    await state.update_data(ev=message.text)
    username = message.from_user.id
    await message.answer("Вы зарегистрировались", reply_markup=keyboard.event)
    print(message.text, username)
    add_user_id(message.text, username)
    add_username(username)
    await state.clear()

@router.message(F.text.lower()=="назад")
async def keyboard_us(message: types.Message):
    await message.answer("Ты кент", reply_markup=keyboard.kb)

