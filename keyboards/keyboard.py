from aiogram import types
from aiogram.types import ReplyKeyboardRemove, \
    ReplyKeyboardMarkup, KeyboardButton, \
    InlineKeyboardMarkup, InlineKeyboardButton
button = [[KeyboardButton(text='Список мероприятий')],
          [KeyboardButton(text='Узнать расписание')],
          [KeyboardButton(text='Пожаловаться')]]
kb = types.ReplyKeyboardMarkup(keyboard=button,resize_keyboard=True)

event = [[KeyboardButton(text='Мероприятие')],
            [KeyboardButton(text='Назад')]]
eventlist = types.ReplyKeyboardMarkup(keyboard=event,resize_keyboard=True)

reg = [[KeyboardButton(text='Регистрация')],
          [KeyboardButton(text='Пожаловаться')],
            [KeyboardButton(text='Назад')]]
regreport = types.ReplyKeyboardMarkup(keyboard=reg,resize_keyboard=True)
