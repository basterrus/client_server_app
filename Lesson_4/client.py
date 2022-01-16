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


def main(account_name):
    try:
        address = argv[4]
        port = int(argv[2])
        if 1024 > port > 65535:
            raise ValueError
    except IndexError:
        address = IP_ADDRESS_DEFAULT
        port = PORT_DEFAULT
    except ValueError:
        print('Может быть указано только число в диапазоне от 1024 до 65535.')
        exit(1)

    transport = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    transport.connect((address, port))
    message_to_server = create_presence(account_name)
    send_message(transport, message_to_server)
    try:
        answer = process_ans(get_message(transport))
        print(answer)
    except (ValueError, json.JSONDecodeError):
        print('Не удалось декодировать сообщение сервера.')


if __name__ == '__main__':
    # main("User")
    main("User")
