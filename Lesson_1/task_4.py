"""
Преобразовать слова «разработка», «администрирование», «protocol», «standard» из строкового представления в
байтовое и выполнить обратное преобразование (используя методы encode и decode).
"""


def encode_decode(words):
    for word in words:
        print(f'Слово {word}')
        word_b = word.encode('utf-8')
        print(f' В байтовом типе - {word_b}')
        word_str = word_b.decode('utf-8')
        print(f'Декодировано - {word_str}')


if __name__ == '__main__':
    words = ['разработка', 'администрирование', 'protocol', 'standard']
    encode_decode(words)
