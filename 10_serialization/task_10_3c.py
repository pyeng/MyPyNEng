# -*- coding: utf-8 -*-

'''
Задание 10.3c

С помощью функции draw_topology из файла draw_network_graph.py
сгенерировать топологию, которая соответствует описанию в файле topology.yaml

Обратите внимание на то, какой формат данных ожидает функция draw_topology.
Описание топологии из файла topology.yaml нужно преобразовать соответствующим образом,
чтобы использовать функцию draw_topology.

Для решения задания можно создать любые вспомогательные функции.

В итоге, должно быть сгенерировано изображение топологии.
Результат должен выглядеть так же, как схема в файле task_10_3c_topology.svg

Не копировать код функции draw_topology.

> Для выполнения этого задания, должен быть установлен graphviz:
> pip install graphviz

'''

import yaml
from draw_network_graph import draw_topology


topology_file = "topology.yaml"

# Get topology info from yaml file
with open(topology_file, "r") as f:
    topology = yaml.load(f)

    # Lists for stroring keys and values from topology file
    keys = []
    values = []

    # Fillinf lists "keys" and "values"
    for k, v in topology.items():

        for i in v.keys():
            keys.append((k, i))

        for i in v.values():
            values.append(i.items()[0])

    # Delete duplicate connections
    topo = dict(zip(keys, values))
    for i in topo.keys():
        if i in topo.values():
            del(topo[i])
           
    # Create topology graph.svg file
    draw_topology(topo, out_filename="graph")