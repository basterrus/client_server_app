"""
Создать текстовый файл test_file.txt, заполнить его тремя строками: «сетевое программирование», «сокет», «декоратор».
Проверить кодировку созданного файла (исходить из того, что вам априори неизвестна кодировка этого файла!).
Затем открыть этот файл и вывести его содержимое на печать. ВАЖНО: файл должен быть открыт без ошибок вне зависимости
от того, в какой кодировке он был создан!
"""
import chardet


def create_file(words):

    # На каждой итерации открываем файл и дозаписываем в конец новое слово

    for word in words:
        with open('test_file.txt', 'a') as file:
            file.write(f'{word}\n')
    print(f'Файл успешно создан, данные записаны!\n')

    # Открываем файл для определения кодировки текста в нем

    with open('test_file.txt', 'rb') as file:
        src = file.read()
        type_encod = chardet.detect(src)['encoding']
        print(f'Данные в файле записаны в кодировке "{type_encod}"\n')
        return type_encod


def open_file(type_encod):
    # Открываем файл в переменную src и выводим содержимое файла в определенной в функции create_file кодировке

    with open('test_file.txt', 'r', encoding=type_encod) as file:
        src = file.read()
        print(src)


if __name__ == '__main__':
    words = ['сетевое программирование', 'сокет', 'декоратор']
    open_file(create_file(words))
