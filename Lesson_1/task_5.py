"""
Выполнить пинг веб-ресурсов yandex.ru, youtube.com и преобразовать результаты из байтовового в строковый
(предварительно определив кодировку выводимых сообщений).
"""
import subprocess
import chardet
import platform


def detect_os():
    if platform.system().lower() == 'windows':
        flags = '-n'
        print('Ваша ОС - MS Windows')
    else:
        flags = '-c'

    return flags


def ping_urls(url, repeat, flags):
    args = ['ping', flags, repeat, url]
    result = subprocess.Popen(args, stdout=subprocess.PIPE)
    for count in result.stdout:
        result = chardet.detect(count)
        line = count.decode(result['encoding']).encode('utf-8')
        print(line.decode('utf-8'))


if __name__ == '__main__':
    ping_urls('yandex.ru', '4', detect_os())
    ping_urls('youtube.com', '4', detect_os())
    ping_urls('gb.ru', '4', detect_os())
