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
