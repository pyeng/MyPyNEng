# -*- coding: utf-8 -*-
'''
Задание 3.4

Из строк command1 и command2 получить список VLAN, 
которые есть и в команде command1 и в команде command1. 
Не использовать для решения задачи циклы, оператор if.
'''

command1 = "switchport trunk allowed vlan 1,3,10,20,30,100"
command2 = "switchport trunk allowed vlan 1,3,100,200,300"

vlans1 = (command1.split()[-1]).split(",")
vlans2 = (command2.split()[-1]).split(",")

set1 = set(vlans1)
set2 = set(vlans2)

both_vlans = str(set1 & set2)

print both_vlans