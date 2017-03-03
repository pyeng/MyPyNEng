# -*- coding: utf-8 -*-

#task_7_1a.py
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


#task_7_2.py
def generate_trunk_config(trunk):
    """
    trunk - словарь trunk-портов, для которых необходимо сгенерировать конфигурацию

    Возвращает список всех команд, которые были сгенерированы на основе шаблона
    """
    trunk_template = ["switchport trunk encapsulation dot1q",
                      "switchport mode trunk",
                      "switchport trunk native vlan 999",
                      "switchport trunk allowed vlan"]

    result = []

    for intf in trunk:
        result.append("interface {}".format(intf))
        for command in trunk_template:
            if command.endswith("allowed vlan"):
                result.append(" {} {}".format(command, ",".join([str(vlan) for vlan in trunk[intf]])))
            else:
                result.append(" {}".format(command))
    return result

#task_7_3.py
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
        for conf_section in (f.read()).split("!"):
            if "interface FastEthernet" in conf_section:
                if "switchport access" in conf_section:
                    for line in conf_section.split("\n"):
                        if line.startswith("interface FastEtherne"):
                            intf = (line.strip()).split()[1]
                            access_port_dict[intf] = []
                        if "switchport access vlan" in line:
                            vlan = (line.split()[-1])
                            access_port_dict[intf] = vlan                        
                    
                elif "switchport trunk" in conf_section:
                    for line in conf_section.split("\n"):
                        if line.startswith("interface FastEtherne"):
                            intf = (line.strip()).split()[1]
                            trunk_port_dict[intf] = []
                        if "switchport trunk allowed vlan" in line:
                            vlan = (line.split()[-1]).split()
                            trunk_port_dict[intf] = vlan

    return (access_port_dict, trunk_port_dict)
