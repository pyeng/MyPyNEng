# -*- coding: utf-8 -*-

'''
Задание 10.3

Создать функцию parse_sh_cdp_neighbors, которая обрабатывает
вывод команды show cdp neighbors.

Функция ожидает, как аргумент, вывод команды одной строкой.

Функция должна возвращать словарь, который описывает соединения между устройствами.

Например, если как аргумент был передан такой вывод:
R4>show cdp neighbors

Device ID    Local Intrfce   Holdtme     Capability       Platform    Port ID
R5           Fa 0/1          122           R S I           2811       Fa 0/1
R6           Fa 0/2          143           R S I           2811       Fa 0/0

Функция должна вернуть такой словарь:

{'R4': {'Fa0/1': {'R5': 'Fa0/1'},
        'Fa0/2': {'R6': 'Fa0/0'}}}


Проверить работу функции на содержимом файла sh_cdp_n_sw1.txt
'''

import re
from pprint import pprint

def parse_sh_cdp_neighbors(filename):
    """ Function return dictionary with data from filename with CDP data"""

    cdp_data = {}

    # RegExp for matching hostname 
    reg_host = ".+[>#]"
    # Hostname of device on which running "show cdp neigh"
    hostname = (re.search(reg_host, filename)).group()[:-1]

    # RegExp for matching neighbor, local interface, remote interface
    regexp = re.compile("""(?P<neigh>\w+) +(?P<lcl_int>\w+\s\d+/\d+).+?\
    (?P<rmt_int>\w+\s\d+/\d+)""")

    cdp_data[hostname] = {}

    for line in filename.split("\n"):

        match = regexp.search(line)

        if match != None:
            (neigh, local, remote) = match.groups()
            cdp_data[hostname][local] = {neigh:remote}

    return cdp_data


# File with CDP data
file = "sh_cdp_n_sw1.txt"

# Opening and reading file to the var
with open(file, "r") as f:
    output = (f.read()).strip()

    # Passing output of the file to func
    result = parse_sh_cdp_neighbors(output)

    # Result of execution func
    pprint(result)