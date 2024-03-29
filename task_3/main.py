"""
3. Задание на закрепление знаний по модулю yaml.
 Написать скрипт, автоматизирующий сохранение данных
 в файле YAML-формата.
Для этого:

Подготовить данные для записи в виде словаря, в котором
первому ключу соответствует список, второму — целое число,
третьему — вложенный словарь, где значение каждого ключа —
это целое число с юникод-символом, отсутствующим в кодировке
ASCII(например, €);

Реализовать сохранение данных в файл формата YAML — например,
в файл file.yaml. При этом обеспечить стилизацию файла с помощью
параметра default_flow_style, а также установить возможность работы
с юникодом: allow_unicode = True;

Реализовать считывание данных из созданного файла и проверить,
совпадают ли они с исходными.
"""

import yaml

data = {'компьютер': ['материнская плата', 'процессор', 'блок питания', 'оперативная память', 'видеокарта'],
        'количество позиций': 5,
        'цена': {'материнская плата': '10000₽', 'процессор': '15000₽', 'блок питания': '3000₽',
                 'оперативная память': '2500₽', 'видеокарта': '30000₽'}}

with open('file.yaml', 'w', encoding="utf-8") as f_n:
    yaml.dump(data, f_n, default_flow_style=False, allow_unicode=True)


with open('file.yaml') as f_n:
    print(f_n.read())