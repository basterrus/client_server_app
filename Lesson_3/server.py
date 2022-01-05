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


def main():
    try:
        if '-p' in argv:
            port = int(argv[argv.index('-p') + 1])
        else:
            port = PORT_DEFAULT

        if 1024 > port > 65535:
            raise ValueError
    except IndexError:
        print('После параметра -\'p\' необходимо указать номер порта! ')
        exit(1)
    except ValueError:
        print('Значение для порта должно быть в диапазоне от 1024 до 65535.')
        exit(1)

    try:
        if '-a' in argv:
            ip_address = argv[argv.index('-a') + 1]
        else:
            ip_address = IP_ADDRESS_DEFAULT
    except IndexError:
        print('После параметра \'a\'- необходимо указать ip адрес для входящих подключений')
        exit(1)

    transport = socket(AF_INET, SOCK_STREAM)
    transport.bind((ip_address, port))
    transport.listen(NUMBER_OF_CONNECTIONS)

    while True:
        client, client_address = transport.accept()
        try:
            message_from_cient = get_message(client)
            print(message_from_cient)
            response = client_message_handler(message_from_cient)
            send_message(client, response)
            client.close()
        except (ValueError, json.JSONDecodeError):
            print('Принято некорретное сообщение от клиента.')
            client.close()


if __name__ == '__main__':
    main()
