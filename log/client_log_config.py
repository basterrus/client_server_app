import logging
import os.path
from log.log_config import formatter, create_dir, level_handler, Level_logging, logger

storage_name = create_dir()

filename = os.path.join(storage_name, 'client.log')
fh = logging.FileHandler(filename, encoding='utf-8')
fh.setLevel(level_handler)
fh.setFormatter(formatter)
logger.addHandler(fh)
logger.setLevel(Level_logging)

if __name__ == '__main__':
    console = logging.StreamHandler()
    console.setLevel(logging.DEBUG)
    console.setFormatter(formatter)
    logger.addHandler(console)
    logger.info('Тестовый запуск логирования')
