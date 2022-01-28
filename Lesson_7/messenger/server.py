import sys
import select
import time
from socket import socket, AF_INET, SOCK_STREAM
from Lesson_7.messenger.common import get_message, send_message
from Lesson_7.log.log_config import log, logger
from Lesson_7.messenger.settings import ACTION, ACCOUNT_NAME, PRESENCE, TIME, USER, RESPONSE, ERROR, PORT_DEFAULT, \
    NUMBER_OF_CONNECTIONS, MESSAGE, SENDER

sys.path.append('../')


@log
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


@log
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


@log
def ip_address_verify_func(argv):
    try:
        if '-a' in argv:
            ip_address = argv[argv.index('-a') + 1]
            logger.info(f'Выбран IP адрес {ip_address}')
        return ip_address
    except IndexError as err:
        logger.error(f'{err} - После параметра \'a\'- необходимо указать ip адрес для входящих подключений')
        exit(1)


def process_client_message(param, messages, client_with_message):
    pass


@log
def start_server(ip_address, port):
    logger.info(f'Попытка запуска сервера {ip_address}:{port}')
    transport = socket(AF_INET, SOCK_STREAM)
    transport.bind((ip_address, port))
    transport.settimeout(0.3)
    transport.listen(NUMBER_OF_CONNECTIONS)

    clients = []
    messages = []

    while True:

        try:
            logger.info(f"Сервер успешно запущен, ожидает подключения клиентов")
            client, client_address = transport.accept()

        except OSError:
            pass

        else:
            logger.error(f'Установлено соединение с {client_address}')
            clients.append(client)

        recv_data_list = []
        send_data_list = []
        err_list = []

        try:
            if clients:
                recv_data_list, send_data_list, err_list = select.select(clients, clients, [], 0)
        except OSError:
            pass

        if recv_data_list:
            for client_with_message in recv_data_list:
                try:
                    process_client_message(get_message(client_with_message), messages, client_with_message)
                except:
                    logger.info(f'Клиент {client_with_message.getpeername()} отключился от сервера')
                    clients.remove(client_with_message)

        if messages and send_data_list:
            messages = {
                ACTION: MESSAGE,
                SENDER: messages[0][0],
                TIME: time.time(),
                MESSAGES_TEXT: messages[0][1]
            }
            del messages[0]

            for waiting_client in send_data_list:
                try:
                    send_message(waiting_client, messages)
                except:
                    logger.info(f'Клиент {waiting_client.getpeername()} отключился от сервера')
                    waiting_client.close()
                    clients.remove(waiting_client)


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
