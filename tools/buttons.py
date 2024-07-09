from aiogram.types import InlineKeyboardButton
from aiogram import Bot, Dispatcher, types
from settings import *


keyboard1 = types.InlineKeyboardMarkup()
start_button = types.InlineKeyboardButton(text="Начать/Start", callback_data="st.start")
keyboard1.add(start_button)

type_of_subject = types.InlineKeyboardMarkup()
mechanics_button = types.InlineKeyboardButton(text="Теоретическая механика", callback_data="tps.Механика")
strength_button = types.InlineKeyboardButton(text="Сопромат", callback_data="tps.Сопромат")
type_of_subject.add(mechanics_button, strength_button)

type_of_work = types.InlineKeyboardMarkup()
exam_button = types.InlineKeyboardButton(text="Экзамен", callback_data="tpw.Экзамен")
advice_button = types.InlineKeyboardButton(text="Консультация", callback_data="tpw.Консультация")
homework_button = types.InlineKeyboardButton(text="Домашняя работа", callback_data="tpw.Домашняя_работа")
other_button = types.InlineKeyboardButton(text="Другое", callback_data="tpwd.Другое")
type_of_work.add(exam_button, advice_button, homework_button, other_button)