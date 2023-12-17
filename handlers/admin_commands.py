from aiogram import Router,F ,types, Bot
from aiogram.types import Message
from aiogram.filters import Filter, Command
from aiogram.fsm.context import FSMContext
from aiogram.filters import Command, StateFilter
from aiogram.fsm.context import FSMContext
from data_base.admindb import check_admin, add_admin
from utils.states import Admin
from data_base.eventbd import *
from keyboards import keyboard

router = Router()

#Чет надо будет сделать с роутерами, по папкам их распихать, иначе их просто дохуя блять
@router.message(Command("halt"))#сделать парольную секретную фразу для админа
async def cmd_start(message: types.Message):
        user_telegram_id = message.from_user.id
        username = message.from_user.username   #Получаем айди и имя пользователя
        info = check_admin(user_telegram_id)
        if info == None:                        #Проверяем есть ли пользователь в БД
            add_admin(user_telegram_id,username)
            await message.answer("Добро пожаловать, даун", reply_markup=keyboard.adminkeyboard)
        else:
            await message.answer("Ты уже в системе, даун", reply_markup=keyboard.adminkeyboard)

@router.message(F.text.lower() == "мероприятие админ")
async def cmd_start(message: types.Message):
    await message.answer("Список выступлений", reply_markup=keyboard.adminkeyboard2)
    data = print_list()
    result_message = ""
    for row in data:
        id_value, event_value, username_value = row
        result_message += f"Порядок: {id_value}, Название: {event_value} Выступает: {username_value}\n"
    result_message = result_message.replace("None", "Участие не подтвердил ")
    await message.answer(text=result_message)

@router.message(F.text.lower() == "добавить позицию")
async def cmd_start(message: types.Message, state: FSMContext):
    await state.set_state(Admin.ev)
    await message.answer("Введите название выступления")

@router.message(Admin.ev)
async def cmd_start(message: types.Message, state: FSMContext):
    await state.update_data(ev=message.text)
    await message.answer("Выступление добавлено")
    add_performance(message.text)
    await state.clear()

@router.message(F.text.lower() == "удалить позицию")
async def cmd_start(message: types.Message, state: FSMContext):
    await state.set_state(Admin.rem)
    await message.answer("Выберите номер выступления")

@router.message(Admin.rem)
async def cmd_start(message: types.Message, state: FSMContext):
    await state.update_data(rem=message.text)
    remove_performance(message.text)
    await message.answer("Выступление удалено")
    await state.clear()

@router.message(F.text.lower() == "поменять местами позиции")
async def cmd_start(message: types.Message, state: FSMContext):
    await state.set_state(Admin.red)
    await message.answer("Введите номера позиций")

@router.message(Admin.red)
async def cmd_start(message: types.Message, state: FSMContext):
    await state.update_data(red=message.text)
    s = message.text
    replace(s[0], s[2:])
    await message.answer("Изменения внесены")
    await state.clear()


@router.message(F.text.lower() == "вернуться")
async def cmd_start(message: types.Message):
    await message.answer("Ты уже в системе, даун", reply_markup=keyboard.adminkeyboard)

@router.message(F.text.lower() == "оповестить")
async def cmd_start(message: types.Message):
    await message.answer("Оповестить всех или уведомить артиста?", reply_markup=keyboard.adminkeyboard3)

@router.message(F.text.lower() == "оповестить всех")
async def cmd_start(message: types.Message, bot:Bot):
    l = get_performance_username_id()
    for username, id in l:
        await bot.send_message(chat_id=id, text=f"Расписание изменилось, прошу ознакомиться, {username}", reply_markup=keyboard.adminkeyboard2)

@router.message(F.text.lower() == "Уведомить артиста")
async def cmd_start(message: types.Message, state: FSMContext, bot:Bot):
    await state.set_state(Admin.an)
    
