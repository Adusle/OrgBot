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
async def cmd_halt(message: types.Message):
        user_telegram_id = message.from_user.id
        username = message.from_user.username   #Получаем айди и имя пользователя
        info = check_admin(user_telegram_id)
        if info == None:                        #Проверяем есть ли пользователь в БД
            add_admin(user_telegram_id,username)
            await message.answer("Добро пожаловать", reply_markup=keyboard.adminkeyboard)
        else:
            await message.answer("Ты уже в системе", reply_markup=keyboard.adminkeyboard)

@router.message(F.text.lower() == "мероприятие админ")
async def event_admin(message: types.Message):
    await message.answer("Список выступлений", reply_markup=keyboard.adminkeyboard2)
    data = print_list()
    result_message = ""
    for row in data:
        id_value, event_value, username_value = row
        result_message += f"Порядок: {id_value}, Название: {event_value} Выступает: {username_value}\n"
    result_message = result_message.replace("None", "Участие не подтвердил ")
    await message.answer(text=result_message)

@router.message(F.text.lower() == "добавить позицию")
async def add_position(message: types.Message, state: FSMContext):
    await state.set_state(Admin.ev)
    await message.answer("Введите название выступления")

@router.message(Admin.ev)
async def add_position_end(message: types.Message, state: FSMContext):
    await state.update_data(ev=message.text)
    await message.answer("Выступление добавлено")
    add_performance(message.text)
    await state.clear()

@router.message(F.text.lower() == "удалить позицию")
async def delete_position(message: types.Message, state: FSMContext):
    await state.set_state(Admin.rem)
    await message.answer("Выберите номер выступления")

@router.message(Admin.rem)
async def delete_position_end(message: types.Message, state: FSMContext):
    await state.update_data(rem=message.text)
    remove_performance(message.text)
    await message.answer("Выступление удалено")
    await state.clear()

@router.message(F.text.lower() == "поменять местами позиции")
async def swap_positions(message: types.Message, state: FSMContext):
    await state.set_state(Admin.red)
    await message.answer("Введите номера позиций")

@router.message(Admin.red)
async def swap_position_end(message: types.Message, state: FSMContext):
    await state.update_data(red=message.text)
    s = message.text
    replace(s[0], s[2:])
    await message.answer("Изменения внесены")
    await state.clear()


@router.message(F.text.lower() == "вернуться")
async def back(message: types.Message):
    await message.answer("Выберите действие", reply_markup=keyboard.adminkeyboard)

@router.message(F.text.lower() == "оповестить")
async def notify(message: types.Message):
    await message.answer("Оповестить всех или уведомить артиста?", reply_markup=keyboard.adminkeyboard3)

@router.message(F.text.lower() == "оповестить всех")
async def notify_all(message: types.Message, bot:Bot):
    l = get_performance_username_id()
    for username, id in l:
        await bot.send_message(chat_id=id, text=f"Расписание изменилось, прошу ознакомиться, {username}", reply_markup=keyboard.adminkeyboard2)

@router.message(F.text.lower() == "уведомить артиста")
async def notify_one(message: types.Message, state: FSMContext):
    await message.answer("Для того чтобы уведомить артиста напишите номер выступления\n Также можно написать номер следующего выступления, чтобы артист успел подготовиться\n Пример уведомления '1 2' ")
    await message.answer("Список выступлений")
    data = print_list()
    result_message = ""
    for row in data:
        id_value, event_value, username_value = row
        result_message += f"Порядок: {id_value}, Название: {event_value} Выступает: {username_value}\n"
    result_message = result_message.replace("None", "Участие не подтвердил ")
    await message.answer(text=result_message)

    await state.set_state(Admin.an)
    
@router.message(Admin.an)
async def notify_one_end(message: types.Message, state: FSMContext, bot:Bot):
    await state.update_data(an=message.text) 
    l = message.text
    if len(l) == 3:
        number1 = get_one_username_id(int(l[0]))
        number2 = get_one_username_id(int(l[1]))
        for username1, user_id1 in number1:
            await bot.send_message(chat_id=user_id1,text=f"Выходите на сцену, {username1}")
        for username2, user_id2 in number2:
            await bot.send_message(chat_id=user_id2,text=f"Приготовьтесь, {username2}")
    else:
        only_one_number = get_one_username_id(l)
        print(only_one_number)
        username = only_one_number[0]
        user_id = only_one_number[1]
        await bot.send_message(chat_id=user_id,text=f"Выходите на сцену, {username}")
    await state.clear()
