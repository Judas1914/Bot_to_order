# Для бота
from aiogram import *
from aiogram.types import InlineKeyboardButton
from aiogram.dispatcher import Dispatcher
import aiogram.utils.markdown as md
from aiogram import Bot, Dispatcher, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Text
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.types import ParseMode
from aiogram.utils import executor

import asyncio

# Стандарт
import re
import configparser
import time
import json
import os
from os import path

# Конвентор в CVS
import pandas as pd

BASE_JSON_FILEPATH = 'settings/user_data.json'

settings_file = "settings"
config = configparser.ConfigParser()
config.read('settings/settings.ini')

def config_update():
    with open(settings_file, 'w') as fl:
        config.write(fl)
    config.read(settings_file)

def check_n_load_json(json_file_path):
    """
    Проверяет указанный путь на наличие файла и выгружает данные если они есть
    """
    if os.path.exists(json_file_path):
        with open(json_file_path, 'r', encoding='utf-8') as fl:
            json_data = json.load(fl)
    else:
        json_data = {}
        with open(json_file_path, 'w', encoding='utf-8') as fl:
            json.dump(json_data, fl, ensure_ascii=False)
    return json_data


###################

API_TOKEN = config['Telegram_Admin']['token']
bot = Bot(token=API_TOKEN)

# For example use simple MemoryStorage for Dispatcher.
storage = MemoryStorage()
dp = Dispatcher(bot, storage=storage)

