from aiogram import Router,F ,types
from aiogram.types import Message
from aiogram.filters import Filter, Command
from aiogram.fsm.context import FSMContext
from aiogram.filters import Command, StateFilter
from aiogram.fsm.context import FSMContext
from data_base.admindb import check_admin, add_admin
from utils.states import AdminEv
from data_base.eventbd import *

router = Router()

#Чет надо будет сделать с роутерами, по папкам их распихать, иначе их просто дохуя блять
@router.message(Command("halt"))
async def cmd_start(message: types.Message):
        user_telegram_id = message.from_user.id
        username = message.from_user.username   #Получаем айди и имя пользователя
        await message.answer("Ты уже в системе, даун")
        info = check_admin(user_telegram_id)
        if info == None:                        #Проверяем есть ли пользователь в БД
            add_admin(user_telegram_id,username)
            await message.answer("Добро пожаловать, даун")

@router.message(F.text.lower() == "мероприятие")
async def cmd_start(message: types.Message, state: FSMContext):
    await state.set_state(AdminEv.name)
    await message.answer("Введите название выступления")

@router.message(AdminEv.name)
async def cmd_start(message: types.Message, state: FSMContext):
    await state.update_data(name=message.text)
    await message.answer("Выступление добавлено")
    add_performance(message.text)
    await state.clear()


@router.message(F.text.lower() == "список регистрации")
async def cmd_start(message: types.Message):
    pass

@router.message(F.text.lower() == "редактировать мероприятие ")
async def cmd_start(message: types.Message):
    pass

@router.message(F.text.lower() == "добавить позицию")
async def cmd_start(message: types.Message):
    pass

@router.message(F.text.lower() == "удалить позицию")
async def cmd_start(message: types.Message):
    pass

@router.message(F.text.lower() == "поменять местами позиции")
async def cmd_start(message: types.Message):
    pass
