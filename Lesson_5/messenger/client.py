import logging
import sys
from sys import argv
import socket
import time
from common import *
import Lesson_5.log.client_log_config
logger = logging.getLogger('client')

def create_presence(account_name):
    out = {
        ACTION: PRESENCE,
        TIME: time.time(),
        USER: {
            ACCOUNT_NAME: account_name
        }
    }
    return out


def process_ans(message):
    if RESPONSE in message:
        if message[RESPONSE] == 200:
            return '200 : OK'
        elif message[RESPONSE] == 400:
            return f'400 : {message[ERROR]}'
    raise ValueError


def ip_address_verify_func(argv):
    try:
        if '-a' in argv:
            ip_address = argv[argv.index('-a') + 1]
            return ip_address
        else:
            raise IndexError
    except IndexError:
        logger.error('Не указан адрес для подключения к серверу')
        exit(1)


def port_verify_func(argv):
    try:
        if '-p' in argv:
            port = int(argv[argv.index('-p') + 1])
            return port
        else:
            port = PORT_DEFAULT

        if 1024 <= port <= 65535:
            return port
        else:
            raise ValueError

    except IndexError:
        logger.error('"IndexError:" После параметра -\'p\' необходимо указать номер порта! ')
        exit(1)
    except ValueError:
        logger.error('"ValueError:" Значение для порта должно быть в диапазоне от 1024 до 65535.')
        exit(1)


def connect_server(account_name, ip_address, port):
    transport = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    logger.info('Запуск клиента, попытка подключения к серверу')
    transport.connect((ip_address, port))
    logger.info(f'Успешное подключение к серверу {ip_address}:{port}')
    message_to_server = create_presence(account_name)
    logger.info(f'Подготовка к передаче данных {account_name}')
    send_message(transport, message_to_server)
    logger.info(f'Сообщение отправлено {message_to_server}')
    try:
        answer = process_ans(get_message(transport))
        logger.info(f'Ответ от сервера {answer}')
        print(answer)
        return answer
    except (ValueError, json.JSONDecodeError):
        logger.error('Не удалось декодировать сообщение сервера.')


def main(account_name, argv):
    port = port_verify_func(argv)
    logger.info(f"Выбран порт {port}")
    ip_address = ip_address_verify_func(argv)
    logger.info(f"Выбран IP адрес сервера {ip_address}")
    logger.info(f"Запуск сервера с параметрами {ip_address}:{port}")
    connect_server(account_name, ip_address, port)


if __name__ == '__main__':
    main("User", argv)
    # main("Guest", argv)

