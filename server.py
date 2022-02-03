import sys
import select
import time
import socket
from pkg.common import get_message, send_message
from log.log_config import log, logger
from pkg.settings import ACTION, ACCOUNT_NAME, PRESENCE, TIME, USER, RESPONSE, ERROR, PORT_DEFAULT, \
    NUMBER_OF_CONNECTIONS, MESSAGE, SENDER, RESPONSE_200, RESPONSE_400, DESTINATION, MESSAGE_TEXT, EXIT, MESSAGES_TEXT

sys.path.append('/')


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
    global ip_address
    try:
        if '-a' in argv:
            ip_address = argv[argv.index('-a') + 1]
            logger.info(f'Выбран IP адрес {ip_address}')
        return ip_address
    except IndexError as err:
        logger.error(f'{err} - После параметра \'a\'- необходимо указать ip адрес для входящих подключений')
        exit(1)


@log
def process_client_message(message, messages_list, client, clients, names):
    logger.debug(f'Разбор сообщения от клиента : {message}')

    if ACTION in message and message[ACTION] == PRESENCE and TIME in message and USER in message:
        if message[USER][ACCOUNT_NAME] not in names.keys():
            names[message[USER][ACCOUNT_NAME]] = client
            send_message(client, RESPONSE_200)
        else:
            response = RESPONSE_400
            response[ERROR] = 'Данное имя уже занято'
            send_message(client, response)
            clients.remove(client)
            client.close()
        return
    elif ACTION in message and message[ACTION] == MESSAGE and DESTINATION in message and TIME in message and SENDER \
            in message and MESSAGE_TEXT in message:
        messages_list.append(message)
        return
    elif ACTION in message and message[ACTION] == EXIT and ACCOUNT_NAME in message:
        clients.remove(names[message[ACCOUNT_NAME]])
        names[message[ACCOUNT_NAME]].close()
        del names[message[ACCOUNT_NAME]]
        return
    else:
        response = RESPONSE_400
        response[ERROR] = 'Не корректный запрос!'
        send_message(client, response)
        return


@log
def process_message(message, names, listen_socks):
    if message[DESTINATION] in names and names[message[DESTINATION]] in listen_socks:
        send_message(names[message[DESTINATION]], message)
        logger.info(f'Отправлено сообщение пользователю {message[DESTINATION]} '
                    f'от пользователя {message[SENDER]}.')
    elif message[DESTINATION] in names and names[message[DESTINATION]] not in listen_socks:
        raise ConnectionError
    else:
        logger.error(
            f'Пользователь {message[DESTINATION]} не зарегистрирован на сервере, '
            f'отправка сообщения невозможна.')


@log
def start_server(ip_address, port):
    logger.info(f'Попытка запуска сервера {ip_address}:{port}')
    transport = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    transport.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    transport.bind((ip_address, port))
    transport.settimeout(0.5)

    clients = []
    messages = []
    names = dict()

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
                    process_client_message(get_message(client_with_message),
                                           messages, client_with_message, clients, names)
                except Exception:
                    logger.info(f'Клиент {client_with_message.getpeername()} '
                                f'отключился от сервера.')
                    clients.remove(client_with_message)

        for i in messages:
            try:
                process_message(i, names, send_data_list)
            except Exception:
                logger.info(f'Связь с клиентом с именем {i[DESTINATION]} была потеряна')
                clients.remove(names[i[DESTINATION]])
                del names[i[DESTINATION]]
        messages.clear()


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
