import inspect
import logging
import os.path
import sys
import traceback
from functools import wraps

# Настройка формата вывода сообщения лога
formatter = logging.Formatter("%(asctime)s - %(levelname)-8s - %(module)-8s - %(message)s ")

client_logger = logging.getLogger('client')
server_logger = logging.getLogger('server')

if sys.argv[0].find('client.py') == -1:
    LOGGER = logging.getLogger('server')
else:
    LOGGER = logging.getLogger('client')

# Установка уровня логирования
level_handler = logging.DEBUG
Level_logging = logging.DEBUG


# Создание директории если отсутствует
def create_dir():
    storage_name = '../log/log_storage'
    if not os.path.exists(storage_name):
        os.mkdir(storage_name)
    return storage_name


def log(func):
    @wraps(func)
    def log_saver(*args, **kwargs):
        ret = func(*args, **kwargs)
        LOGGER.debug(f'Была вызвана функция {func.__name__} c параметрами {args}, {kwargs}. '
                     f'Вызов из модуля {func.__module__}.'
                     f'Вызов из функции {traceback.format_stack()[0].strip().split()[-1]}.'
                     f'Вызов из функции {inspect.stack()[1][3]}')
        return ret

    return log_saver

