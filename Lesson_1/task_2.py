"""
Каждое из слов «class», «function», «method» записать в байтовом типе. Сделать это небходимо в автоматическом,
а не ручном режиме с помощью добавления литеры b к текстовому значению,
(т.е. ни в коем случае не используя методы encode и decode) и
определить тип, содержимое и длину соответствующих переменных.
"""


def convert_to_bite(words):
    for el in words:
        item = eval(f"b'{el}'")
        print(
            f'Слово {el}\n пердставленно в байтовом виде - {item}\n '
            f'имеет тип -{type(item)}\n '
            f'имеет длину {len(item)}')


if __name__ == '__main__':
    lst = ['class', 'function', 'method']
    convert_to_bite(lst)
