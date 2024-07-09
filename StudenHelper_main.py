import logging
from tools import *
from settings import *

bot.user_data = check_n_load_json(BASE_JSON_FILEPATH)

logging.basicConfig(level=logging.INFO)

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
