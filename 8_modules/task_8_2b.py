# -*- coding: utf-8 -*-

"""
Задание 8.2b

С помощью функции parse_cdp_neighbors из задания 8.2
и функции draw_topology из файла draw_network_graph.py
сгенерировать топологию, которая соответствует выводу
команды sh cdp neighbor из файлов:
* sh_cdp_n_sw1.txt
* sh_cdp_n_r1.txt
* sh_cdp_n_r2.txt
* sh_cdp_n_r3.txt


Не копировать код функций parse_cdp_neighbors и draw_topology.

В итоге, должен быть сгенерировано изображение топологии.
Результат должен выглядеть так же, как схема в файле task_8_2b_topology.svg

> Для выполнения этого задания, должен быть установлен graphviz:
> pip install graphviz
"""

from task_8_2 import parse_cdp_neighbors
from draw_network_graph import draw_topology

if __name__ == "__main__":

	from sys import argv

	cdp_file = argv[1:]

	full_topology = {}

	for file in cdp_file:
		
		#parsing CDP tables		
		with open(file, "r") as f:
			cdp_data = f.read()
			partial_topology = parse_cdp_neighbors(cdp_data)
			full_topology.update(partial_topology)

			#delete duplicate connections
			for i in full_topology.keys():
				if i in full_topology.values():
					del(full_topology[i])

	#generate graph
	draw_topology(full_topology)
