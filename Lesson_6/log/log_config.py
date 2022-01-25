import inspect
import logging
import os.path
from functools import wraps
# Настройка формата вывода сообщения лога
formatter = logging.Formatter("%(asctime)s - %(levelname)-8s - %(module)-8s - %(message)s ")

client_logger = logging.getLogger('client')
server_logger = logging.getLogger('server')


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
    def call(*args, **kwargs):
        outer_func = inspect.stack()[1][3]
        server_logger.debug(f'Function "{func.__name__}" is called into "{outer_func}"')
        client_logger.debug(f'Function "{func.__name__}" is called into "{outer_func}"')
        return func(*args, **kwargs)

    return call
