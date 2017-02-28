# -*- coding: utf-8 -*-
"""
Задание 7.4

Создать функцию, которая обрабатывает конфигурационный файл коммутатора
и возвращает словарь:
* Все команды верхнего уровня (глобального режима конфигурации), будут ключами.
* Если у команды верхнего уровня есть подкоманды, они должны быть в значении у 
  соответствующего ключа, в виде списка (пробелы вначале можно оставлять).
* Если у команды верхнего уровня нет подкоманд, то значение будет пустым списком

Функция ожидает в качестве аргумента имя конфигурационного файла.

Проверить работу функции на примере файла config_sw1.txt

При обработке конфигурационного файла, надо игнорировать строки, которые начинаются с "!",
а также строки в которых содержатся слова из списка ignore.

Для проверки надо ли игнорировать строку, использовать функцию ignore_command.

"""

from sys import argv
from pprint import pprint

ignore = ["duplex", "alias", "Current configuration"]

def ignore_command(command, ignore):
    """
    Функция проверяет содержится ли в команде слово из списка ignore.

    command - строка. Команда, которую надо проверить
    ignore - список. Список слов

    Возвращает True, если в команде содержится слово из списка ignore, False - если нет
    """
    ignore_command = False

    for word in ignore:
        if word in command:
            return True
    return ignore_command


def config_to_dict(config):
    """
    config - имя конфигурационного файла

    Возвращает словарь:
    - Все команды верхнего уровня (глобального режима конфигурации), будут ключами.
    - Если у команды верхнего уровня есть подкоманды,
      они должны быть в значении у соответствующего ключа, в виде списка (пробелы вначале 
      можно оставлять).
    - Если у команды верхнего уровня нет подкоманд, то значение будет пустым списком
    """
    config_dict = {}
    with open(config, "r") as f:
        for line in f:
            check_ignore = ignore_command(line, ignore)
            if not line.startswith("!") and not check_ignore:
                line = line.strip("\r")
                if not line.startswith(" "):
                    top_command = line.strip()
                    config_dict[top_command] = []     
                elif line.startswith(" "):
                    config_dict[top_command].append(line.strip())
    return config_dict
               
    
config_file = argv[1]


result = config_to_dict(config_file)
pprint(result)

