import sys

sys.path.append('../lesson_3/')

from sys import argv
import socket
import time
from common import *


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
        print('После параметра \'a\'- необходимо указать ip адрес для входящих подключений')
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
        print('"IndexError:" После параметра -\'p\' необходимо указать номер порта! ')
        exit(1)
    except ValueError:
        print('"ValueError:" Значение для порта должно быть в диапазоне от 1024 до 65535.')
        exit(1)


def connect_server(account_name, ip_address, port):
    transport = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    transport.connect((ip_address, port))
    message_to_server = create_presence(account_name)
    send_message(transport, message_to_server)
    try:
        answer = process_ans(get_message(transport))
        print(answer)
        return answer
    except (ValueError, json.JSONDecodeError):
        print('Не удалось декодировать сообщение сервера.')


def main(account_name, argv):
    port = port_verify_func(argv)
    ip_address = ip_address_verify_func(argv)
    connect_server(account_name, ip_address, port)


if __name__ == '__main__':
    # main("User", argv)
    main("Guest", argv)

