# -*- coding: utf-8 -*-

"""
Задание 8.2a

С помощью функции parse_cdp_neighbors из задания 8.2
и функции draw_topology из файла draw_network_graph.py
сгенерировать топологию, которая соответствует выводу
команды sh cdp neighbor в файле sw1_sh_cdp_neighbors.txt

Не копировать код функций parse_cdp_neighbors и draw_topology.

В итоге, должен быть сгенерировано изображение топологии.
Результат должен выглядеть так же, как схема в файле task_8_2a_topology.svg

> Для выполнения этого задания, должен быть установлен graphviz:
> pip install graphviz

"""

from task_8_2 import parse_cdp_neighbors
from draw_network_graph import draw_topology

if __name__ == "__main__":

	from sys import argv
	from pprint import pprint

	cdp_file = argv[1]

	with open(cdp_file, "r") as f:
		cdp_data = f.read()
		result = parse_cdp_neighbors(cdp_data)

	draw_topology(result)
