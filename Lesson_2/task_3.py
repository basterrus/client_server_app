"""
3. Задание на закрепление знаний по модулю yaml.
Написать скрипт, автоматизирующий сохранение данных в файле YAML-формата. Для этого:
Подготовить данные для записи в виде словаря, в котором первому ключу соответствует список, второму — целое число,
третьему — вложенный словарь, где значение каждого ключа — это целое число с юникод-символом,
отсутствующим в кодировке ASCII (например, €);
Реализовать сохранение данных в файл формата YAML — например, в файл file.yaml.
При этом обеспечить стилизацию файла с помощью параметра default_flow_style, а также установить
возможность работы с юникодом: allow_unicode = True;
Реализовать считывание данных из созданного файла и проверить, совпадают ли они с исходными.
"""

import yaml

data = {
    "info": ["some", "information", "we", "have_to", "proceed"],
    "number": 25,
    "dict": {"num_1": "10€", "num_2": "15€", "num_3": "20€"},
}

with open("Lesson_2/write_to_yaml.yaml", "w") as file:
    yaml.dump(data, file, default_flow_style=False, allow_unicode=True)

with open("Lesson_2/write_to_yaml.yaml", encoding="utf-8") as file:
    print(file.read())
