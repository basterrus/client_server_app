import subprocess
import sys
from subprocess import Popen, CREATE_NEW_CONSOLE

word = ''
client_list = []

while True:
    user_input_chat_quantity = int(input(f"Сколько клиентов запустить? "))

    if user_input_chat_quantity == 0:
        exit(1)
    elif user_input_chat_quantity == 1:
        word = "клиент"
    elif 2 < user_input_chat_quantity <= 4:
        word = "клиента"
    else:
        word = "клиентов"

    user_input_chat_actions = input(f"Введите (s) для запуска {user_input_chat_quantity} {word},\n"
                                    f"Введите (x) для закрытия всех окон,\n"
                                    f"Введите (q) для выхода\n")

    if user_input_chat_actions == 'q':
        break
    elif user_input_chat_actions == 's':
        client_list.append(subprocess.Popen('python server.py',
                                            creationflags=subprocess.CREATE_NEW_CONSOLE))
        for i in range(1):
            client_list.append(subprocess.Popen('python client.py -m send',
                                                creationflags=subprocess.CREATE_NEW_CONSOLE))
        for i in range(1):
            client_list.append(subprocess.Popen('python client.py -m listen',
                                                creationflags=subprocess.CREATE_NEW_CONSOLE))
    elif user_input_chat_actions == 'x':
        while client_list:
            working = client_list.pop()
            working.kill()
