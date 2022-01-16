port = int(input('enter port'))

if 1024 <= port <= 65535:
    print('OK')
else:
    raise ValueError
