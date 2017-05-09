# -*- coding: utf-8 -*-
'''
Задание 2

Создать функции:
- generate_access_config - генерирует конфигурацию для access-портов,
                           на основе словарей access и psecurity из файла sw_templates.yaml
- generate_trunk_config - генерирует конфигурацию для trunk-портов,
                           на основе словаря trunk из файла sw_templates.yaml
- generate_ospf_config - генерирует конфигурацию ospf, на основе словаря ospf из файла templates.yaml
- generate_mngmt_config - генерирует конфигурацию менеджмент настроек, 
                         на основе словаря mngmt из файла templates.yaml
- generate_alias_config - генерирует конфигурацию alias, на основе словаря alias из файла templates.yaml
- generate_switch_config - генерирует конфигурацию коммутатора, в зависимости от переданных параметров,
                           использует для этого оставильные функции
'''
import yaml
import pprint


access_dict = { 'FastEthernet0/12':10,
                'FastEthernet0/14':11,
                'FastEthernet0/16':17,
                'FastEthernet0/17':150 }

trunk_dict = { 'FastEthernet0/1':[10,20,30],
               'FastEthernet0/2':[11,30],
               'FastEthernet0/4':[17] }


def generate_access_config(access, psecurity=False):
    """
    access - словарь access-портов,
    для которых необходимо сгенерировать конфигурацию, вида:
        { 'FastEthernet0/12':10,
          'FastEthernet0/14':11,
          'FastEthernet0/16':17}
    psecurity - контролирует нужна ли настройка Port Security. По умолчанию значение False
        - если значение True, то настройка выполняется с добавлением шаблона port_security
        - если значение False, то настройка не выполняется

    Возвращает список всех команд, которые были сгенерированы на основе шаблона
    """

    with open('sw_templates.yaml') as f:
        templates = yaml.load(f)
    
    access_conf = []

    for intf in access_dict:
        
        access_conf.append("interface {}".format(intf))
        
        for line in templates["access"]:
        
            if line.startswith("switchport access"):
                access_conf.append(" switchport access vlan {}".format(access_dict[intf]))
        
            else:
                access_conf.append(" " + line)
        
        if psecurity == True:
        
            for line in templates["psecurity"]:
                access_conf.append(" " + line)

    data = "\n".join([line for line in access_conf])
    print data



def generate_trunk_config(trunk):
    """
    trunk - словарь trunk-портов,
    для которых необходимо сгенерировать конфигурацию, вида:
        { 'FastEthernet0/1':[10,20],
          'FastEthernet0/2':[11,30],
          'FastEthernet0/4':[17] }

    Возвращает список всех команд, которые были сгенерированы на основе шаблона
    """
    with open('sw_templates.yaml') as f:
        templates = yaml.load(f)

    trunk_conf = []

    for intf in trunk_dict:
    
        trunk_conf.append("interface {}".format(intf))
    
        for line in templates["trunk"]:
    
            if line.endswith("allowed vlan"):
                vlans = ",".join([str(vid) for vid in trunk_dict[intf]])
                trunk_conf.append(" switchport trunk allowed vlan {}".format(vlans))

            else:
                trunk_conf.append(" " + line)

    data = "\n".join([line for line in trunk_conf])
    print data
    
def generate_ospf_config(filename):
    """
    filename - имя файла в формате YAML, в котором находится шаблон ospf.

    Возвращает список всех команд, которые были сгенерированы на основе шаблона
    """
    templates = yaml.load(open(filename))



def generate_mngmt_config(filename):
    """
    filename - имя файла в формате YAML, в котором находится шаблон mngmt.

    Возвращает список всех команд, которые были сгенерированы на основе шаблона
    """
    pass

def generate_alias_config(filename):
    """
    filename - имя файла в формате YAML, в котором находится шаблон alias.

    Возвращает список всех команд, которые были сгенерированы на основе шаблона
    """
    pass

def generate_switch_config(access=True, psecurity=False, trunk=True,
                           ospf=True, mngmt=True, alias=False):
    """
    Аргументы контролирует какие настройки надо выполнить.
    По умолчанию, будет настроено все, кроме psecurity и alias.

    Возвращает список всех команд, которые были сгенерированы на основе шаблона
    """
    pass

# Сгенерировать конфигурации для разных коммутаторов:

sw1 = generate_switch_config()
sw2 = generate_switch_config(psecurity=True, alias=True)
sw3 = generate_switch_config(ospf=False)

#generate_access_config(access_dict, psecurity=True)
#generate_trunk_config(trunk_dict)