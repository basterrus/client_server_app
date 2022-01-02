"""
2. Задание на закрепление знаний по модулю json. Есть файл orders в формате JSON с информацией о заказах.
Написать скрипт, автоматизирующий его заполнение данными. Для этого:
Создать функцию write_order_to_json(), в которую передается 5 параметров — товар (item), количество (quantity),
цена (price), покупатель (buyer), дата (date). В это словаре параметров обязательно должны присутствовать юникод-символы,
отсутствующие в кодировке ASCII. Функция должна предусматривать запись данных в виде словаря в файл orders.json.
При записи данных указать величину отступа в 4 пробельных символа;
Необходимо также установить возможность отображения символов юникода: ensure_ascii=False;
Проверить работу программы через вызов функции write_order_to_json() с передачей в нее значений каждого параметра."""

import json


def write_order_to_json(item, quantity, price, buyer, date):

    data = {}

    with open("Lesson_2/orders.json", 'r', encoding="utf-8") as f:
        data = json.loads(f.read())

    data["orders"].append(
        {
            "item": item,
            "quantity": quantity,
            "price": price,
            "buyer": buyer,
            "date": date,
        }
    )

    with open("Lesson_2/orders.json", "w+", encoding="utf-8") as f:
        json.dump(data, f, indent=4, ensure_ascii=False, separators=(",", ": "))


if __name__ == '__main__':
    write_order_to_json("носки", 2, 20, "АО ФЕДЕРАЛЬНАЯ НОСКОВАЯ КОМПАНИЯ", "12.05.21.")
