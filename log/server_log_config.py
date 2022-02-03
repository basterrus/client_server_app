import os
from log.log_config import formatter, create_dir, level_handler, Level_logging, logger
import logging.handlers

storage_name = create_dir()

filename = os.path.join(storage_name, 'server.log')
fh = logging.handlers.TimedRotatingFileHandler(filename, encoding='utf-8', when='D', interval=1, backupCount=7)
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

