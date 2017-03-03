# -*- coding: utf-8 -*-
"""
Задание 7.1a

Сделать копию скрипта задания 7.1.

Дополнить скрипт:
* ввести дополнительный параметр, который контролирует будет ли настроен port-security
 * имя параметра "psecurity"
 * по умолчанию значение False

Проверить работу функции на примере словаря access_dict,
с генерацией конфигурации port-security и без.
"""

from pprint import pprint

def generate_access_config(access, psecurity=False):
    """
    access - словарь access-портов,
    для которых необходимо сгенерировать конфигурацию, вида:
        { "FastEthernet0/12":10,
          "FastEthernet0/14":11,
          "FastEthernet0/16":17 }

    psecurity - контролирует нужна ли настройка Port Security. По умолчанию значение False
        - если значение True, то настройка выполняется с добавлением шаблона port_security
        - если значение False, то настройка не выполняется

    Возвращает список всех команд, которые были сгенерированы на основе шаблона
    """

    access_template = ["switchport mode access",
                       "switchport access vlan",
                       "switchport nonegotiate",
                       "spanning-tree portfast",
                       "spanning-tree bpduguard enable"]

    port_security = ["switchport port-security maximum 2",
                     "switchport port-security violation restrict",
                     "switchport port-security"]

    result = []
    
    for intf in access:
        result.append("interface {}".format(intf))
        for command in access_template:
            if command.endswith("access vlan"):
                result.append(" {} {}".format(command, access[intf]))
            else:
                 result.append(" {}".format(command))
        if psecurity == True:
            for command in port_security:
                result.append(" {}".format(command))
    return result

access_dict = { "FastEthernet0/12":10,
                "FastEthernet0/14":11,
                "FastEthernet0/16":17,
                "FastEthernet0/17":150 }

access_command_list = generate_access_config(access_dict, True)

pprint(access_command_list)
