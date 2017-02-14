# -*- coding: utf-8 -*-

"""
Задание 4.3a

В этой задаче нельзя использовать условие if.

Дополнить скрипт из задания 4.3 таким образом, чтобы, в зависимости от выбранного режима,
задавались разные вопросы в запросе о номере VLANа или списка VLANов:
* для access: 'Enter VLAN number:'
* для trunk: 'Enter allowed VLANs:'

"""

access_template = ['switchport mode access',
                   'switchport access vlan {}',
                   'switchport nonegotiate',
                   'spanning-tree portfast',
                   'spanning-tree bpduguard enable']

trunk_template = ['switchport trunk encapsulation dot1q',
                  'switchport mode trunk',
                  'switchport trunk allowed vlan {}']

template = {"access": access_template, "trunk": trunk_template }
vlan_prompt = {"access": "Enter VLAN number: ", "trunk": "Enter allowed VLANs: "}

mode = raw_input("\nEnter interface mode (access/trunk): ")
int_num = raw_input("Enter interface type and number: ")
vlan = raw_input(vlan_prompt[mode])

print "\ninterface {}".format(int_num)
print "\n".join(template[mode]).format(vlan)
print