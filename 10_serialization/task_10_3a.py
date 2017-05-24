# -*- coding: utf-8 -*-

'''
Задание 10.3a

С помощью функции parse_sh_cdp_neighbors из задания 10.3,
обработать вывод команды sh cdp neighbor из файлов:
* sh_cdp_n_sw1.txt
* sh_cdp_n_r1.txt
* sh_cdp_n_r2.txt
* sh_cdp_n_r3.txt
* sh_cdp_n_r4.txt
* sh_cdp_n_r5.txt
* sh_cdp_n_r6.txt

Объединить все словари, которые возвращает функция parse_sh_cdp_neighbors,
в один словарь topology и записать его содержимое в файл topology.yaml.

Структура словаря topology должна быть такой:
{'R4': {'Fa0/1': {'R5': 'Fa0/1'},
        'Fa0/2': {'R6': 'Fa0/0'}},
 'R5': {'Fa0/1': {'R4': 'Fa0/1'}},
 'R6': {'Fa0/0': {'R4': 'Fa0/2'}}}

Не копировать код функции parse_sh_cdp_neighbors
'''
import re
import glob
import yaml
from task_10_3 import parse_sh_cdp_neighbors

if __name__ == '__main__':
    
    sh_cdp_files = glob.glob("sh_cdp_n_*")

    # Dict that contain output of sh cdp neigh
    topology = {}

    # Filename to that write topology
    file_for_write = "topology.yaml"

    for file in sh_cdp_files:

        # Get content from file sh_cdp_n__*
        with open(file, "r") as f:
            output = (f.read()).strip()

            # Merge output from different dict
            for key, values in parse_sh_cdp_neighbors(output).items():
                topology[key] = values

    # Write dict topology to file
    with open(file_for_write, 'w') as f:
        f.write(yaml.dump(topology))