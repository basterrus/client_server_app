# Настройки сервера
PORT_DEFAULT = 7777
IP_ADDRESS_DEFAULT = '127.0.0.1'
NUMBER_OF_CONNECTIONS = 5
MAX_PACKAGE_LENGTH = 1024
ENCODING = 'UTF-8'

# JIM - ключи:
ACTION = 'action'
TIME = 'time'
USER = 'user'
ACCOUNT_NAME = 'account_name'
SENDER = 'sender'
DESTINATION = 'to'

# ACTIONS
PRESENCE = 'presence'
RESPONSE = 'response'
ERROR = 'error'
MESSAGE = 'message'
MESSAGES_TEXT = 'mess_text'
MESSAGE_TEXT = 'mess_text'
EXIT = 'exit'

RESPONSE_200 = {RESPONSE: 200}
# 400
RESPONSE_400 = {
    RESPONSE: 400,
    ERROR: None
}
