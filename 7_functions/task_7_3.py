# -*- coding: utf-8 -*-
"""
Задание 7.3

Создать функцию get_int_vlan_map, которая обрабатывает конфигурационный файл коммутатора
и возвращает два объекта:
* словарь портов в режиме access, где ключи номера портов, а значения access VLAN:
{"FastEthernet0/12":10,
 "FastEthernet0/14":11,
 "FastEthernet0/16":17}

* словарь портов в режиме trunk, где ключи номера портов, а значения список разрешенных VLAN:
{"FastEthernet0/1":[10,20],
 "FastEthernet0/2":[11,30],
 "FastEthernet0/4":[17]}

Функция ожидает в качестве аргумента имя конфигурационного файла.

Проверить работу функции на примере файла config_sw1.txt
"""

from sys import argv

def get_int_vlan_map(config):
    """
    config - имя конфигурационного файла коммутатора

    Возвращает кортеж словарей:
    - первый словарь: порты в режиме access
      { "FastEthernet0/12": 10,
        "FastEthernet0/14": 11,
        "FastEthernet0/16": 17  }
    - второй словарь: порты в режиме trunk
      { "FastEthernet0/1":[10, 20],
        "FastEthernet0/2":[11, 30],
        "FastEthernet0/4":[17] }

    """
    access_port_dict = {}
    trunk_port_dict = {}

    with open(config, "r") as f:

        conf = (f.read()).split("!")

        for block in conf:
            block = block.strip()

            if block.startswith("interface FastEthernet"):
                intf = block.split()[1]
               
                for line in block.split("\n"):

                    if "switchport mode access" in line:
                        access_port_dict[intf] = []
                    
                    elif "switchport mode trunk" in line:
                        trunk_port_dict[intf] = []
                    

    print access_port_dict
    print trunk_port_dict
                


config_file = argv[1]

get_int_vlan_map(config_file)