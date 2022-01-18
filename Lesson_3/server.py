import sys

sys.path.append('../lesson_3/')

from socket import socket, AF_INET, SOCK_STREAM
from sys import argv
import settings
from common import *


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

    except IndexError:
        print('"IndexError:" После параметра -\'p\' необходимо указать номер порта! ')
        exit(1)
    except ValueError:
        print('"ValueError:" Значение для порта должно быть в диапазоне от 1024 до 65535.')
        exit(1)


def ip_address_verify_func(argv):
    try:
        if '-a' in argv:
            ip_address = argv[argv.index('-a') + 1]
        return ip_address
    except IndexError:
        print('После параметра \'a\'- необходимо указать ip адрес для входящих подключений')
        exit(1)


def start_server(ip_address, port):
    transport = socket(AF_INET, SOCK_STREAM)
    transport.bind((ip_address, port))
    transport.listen(NUMBER_OF_CONNECTIONS)

    while True:
        client, client_address = transport.accept()
        try:
            message_from_cient = get_message(client)
            response = client_message_handler(message_from_cient)
            send_message(client, response)
            client.close()
        except (ValueError, json.JSONDecodeError):
            print('Принято некорретное сообщение от клиента.')
            client.close()


def main():
    args = sys.argv
    port = port_verify_func(args)
    ip_address = ip_address_verify_func(args)
    start_server(ip_address, port)


if __name__ == '__main__':
    main()
    # start_server('127.0.0.1', 8080)
