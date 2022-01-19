import logging
import os.path

# Настройка формата вывода сообщения лога
formatter = logging.Formatter("%(asctime)s - %(levelname)-8s - %(module)-8s - %(message)s ")

# Установка уровня логирования
level_handler = logging.DEBUG
Level_logging = logging.DEBUG


# Создание директории если отсутствует
def create_dir():
    storage_name = '../log/log_storage'
    if not os.path.exists(storage_name):
        os.mkdir(storage_name)
    return storage_name
