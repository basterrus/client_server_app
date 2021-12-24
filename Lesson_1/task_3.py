"""
Определить, какие из слов, поданных на вход программы, невозможно записать в байтовом типе.
Для проверки правильности работы кода используйте значения: «attribute», «класс», «функция», «type»
"""


def bite_verify(words):
    for word in words:
        try:
            wordb = eval(f"b'{word}'")
            print(f'Слово {word} представленное в байтовом типе - {wordb}')
        except SyntaxError:
            print(f'Слово {word} не может быть представленно в байтовом типе')


if __name__ == '__main__':
    words = ['attribute', 'класс', 'функция', 'type']
    bite_verify(words)
