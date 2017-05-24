# -*- coding: utf-8 -*-

'''
Задание 10.3b

Переделать функциональность скрипта из задания 10.3a,
в функцию generate_topology_from_cdp.

Функция generate_topology_from_cdp должна быть создана с параметрами:
* list_of_files - список файлов из которых надо считать вывод команды sh cdp neighbor
* save_to_file - этот параметр управляет тем, будет ли записан в файл, итоговый словарь
 * значение по умолчанию - True
* topology_filename - имя файла, в который сохранится топология.
 * по умолчанию, должно использоваться имя topology.yaml.
 * топология сохраняется только, если аргумент save_to_file указан равным True

Функция возвращает словарь, который описывает топологию.
Словарь должен быть в том же формате, что и в задании 10.3a.

Проверить работу функции generate_topology_from_cdp на файлах:
* sh_cdp_n_sw1.txt
* sh_cdp_n_r1.txt
* sh_cdp_n_r2.txt
* sh_cdp_n_r3.txt
* sh_cdp_n_r4.txt
* sh_cdp_n_r5.txt
* sh_cdp_n_r6.txt

Записать полученный словарь в файл topology.yaml.

Не копировать код функции parse_sh_cdp_neighbors
'''

import glob
import yaml
from task_10_3 import parse_sh_cdp_neighbors


def generate_topology_from_cdp(list_of_files, save_to_file=True, 
                                topology_filename="topology.yaml"):

    # Dict that contain output of sh cdp neigh
    topology = {}

    # For loop that walk by file in list_of_files
    for file in list_of_files:

        # Get content from file sh_cdp_n__*
        with open(file, "r") as f:
            output = (f.read()).strip()

            # Merge output from different dict
            for key, values in parse_sh_cdp_neighbors(output).items():
                topology[key] = values

    # If topology_filename is True -> write dict to file
    if save_to_file:
        with open(topology_filename, 'w') as f:
            f.write(yaml.dump(topology))


if __name__ == '__main__':

    sh_cdp_files = glob.glob("sh_cdp_n_*")

    generate_topology_from_cdp(sh_cdp_files)