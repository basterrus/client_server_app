import sys
import logging
from socket import socket, AF_INET, SOCK_STREAM
from sys import argv
import settings
from common import *
import Lesson_5.log.server_log_config

logger = logging.getLogger('server')


def client_message_handler(message):
    if ACTION in message and message[ACTION] == PRESENCE and TIME in message and USER in message and message[USER][
        ACCOUNT_NAME] == 'User':
        return {
            RESPONSE: 200,
        }
    else:
        return {
            RESPONSE: 400,
            ERROR: 'Bad Request'
        }


def port_verify_func(argv):
    try:
        if '-p' in argv:
            port = int(argv[argv.index('-p') + 1])

        else:
            port = PORT_DEFAULT

        if 1024 <= port <= 65535:
            return port
        else:
            raise ValueError

    except IndexError as err:
        logger.error(f'{err} - После параметра -\'p\' необходимо указать номер порта! ')
        exit(1)
    except ValueError as err:
        logger.error(f'{err} - Значение для порта должно быть в диапазоне от 1024 до 65535.')
        exit(1)


def ip_address_verify_func(argv):
    try:
        if '-a' in argv:
            ip_address = argv[argv.index('-a') + 1]
            logger.info(f'Выбран IP адрес {ip_address}')
        return ip_address
    except IndexError as err:
        logger.error(f'{err} - После параметра \'a\'- необходимо указать ip адрес для входящих подключений')
        exit(1)


def start_server(ip_address, port):
    logger.info(f'Попытка запуска сервера {ip_address}:{port}')
    transport = socket(AF_INET, SOCK_STREAM)
    transport.bind((ip_address, port))
    transport.listen(NUMBER_OF_CONNECTIONS)

    while True:
        logger.info(f"Сервер успешно запущен, ожидает подключения клиентов")
        client, client_address = transport.accept()
        try:
            message_from_cient = get_message(client)
            logger.info(f'Получено сообщение от клиента - {message_from_cient}')
            response = client_message_handler(message_from_cient)
            logger.info('Сообщение декодировано и обработано')
            send_message(client, response)
            logger.info('Сообщение клиенту отправлено')
            client.close()
        except json.JSONDecodeError as err:
            logger.error(f'{err}: Принято некорретное сообщение от клиента.')
            client.close()


def main():
    args = sys.argv
    port = port_verify_func(args)
    logger.info(f"Выбран порт {port}")
    ip_address = ip_address_verify_func(args)
    logger.info(f"Выбран IP адрес сервера {ip_address}")
    logger.info(f"Запуск сервера с параметрами {ip_address}:{port}")
    start_server(ip_address, port)


if __name__ == '__main__':
    main()
