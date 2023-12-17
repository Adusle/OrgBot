from aiogram import types
from aiogram.types import ReplyKeyboardRemove, \
    ReplyKeyboardMarkup, KeyboardButton, \
    InlineKeyboardMarkup, InlineKeyboardButton
button = [[KeyboardButton(text='Мероприятие')],
          [KeyboardButton(text='Пожаловаться')]]
kb = types.ReplyKeyboardMarkup(keyboard=button,resize_keyboard=True)

ev = [[KeyboardButton(text='Зарегистрироваться')],
          [KeyboardButton(text='Назад')]]
event = types.ReplyKeyboardMarkup(keyboard=ev,resize_keyboard=True)

adminbutton = [[KeyboardButton(text='Мероприятие админ')]]

adminkeyboard = types.ReplyKeyboardMarkup(keyboard=adminbutton, resize_keyboard=True)

adminbutton2 = [[KeyboardButton(text='Добавить позицию')],
                [KeyboardButton(text='Удалить позицию')],
                [KeyboardButton(text='Поменять местами позиции')],
                [KeyboardButton(text='Оповестить')]]
adminkeyboard2 = types.ReplyKeyboardMarkup(keyboard=adminbutton2, resize_keyboard=True)
