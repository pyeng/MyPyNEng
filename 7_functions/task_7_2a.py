# -*- coding: utf-8 -*-

"""
Задание 7.2a

Сделать копию скрипта задания 7.2

Изменить скрипт таким образом, чтобы функция возвращала не список команд, а словарь:
    - ключи: имена интерфейсов, вида "FastEthernet0/1"
    - значения: список команд, который надо выполнить на этом интерфейсе

Проверить работу функции на примере словаря trunk_dict.
"""

import pprint

def generate_trunk_config(trunk):
    """
    trunk - словарь trunk-портов,
    для которых необходимо сгенерировать конфигурацию, вида:
        { "FastEthernet0/1":[10,20],
          "FastEthernet0/2":[11,30],
          "FastEthernet0/4":[17] }

    Возвращает словарь:
    - ключи: имена интерфейсов, вида "FastEthernet0/1"
    - значения: список команд, который надо выполнить на этом интерфейсе
    """
    trunk_template = ["switchport trunk encapsulation dot1q",
                      "switchport mode trunk",
                      "switchport trunk native vlan 999",
                      "switchport trunk allowed vlan"]

    command_dict = {}

    for intf in trunk:
        command_dict[intf] = []
        for command in trunk_template:
            if command.endswith("allowed vlan"):
                command_dict[intf].append("{} {}".format(command, ",".join([str(vlan) for vlan in trunk[intf]])))
            else:
                command_dict[intf].append(command)

    return command_dict


trunk_dict = { "FastEthernet0/1":[10,20,30],
               "FastEthernet0/2":[11,30],
               "FastEthernet0/4":[17] }


result = generate_trunk_config(trunk_dict)

pprint.pprint(result)