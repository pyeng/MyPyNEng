# -*- coding: utf-8 -*-
'''
Задание 6.3b

Сделать копию скрипта задания 6.3a.

Дополнить скрипт:
  Запросить у пользователя ввод номера VLAN.
  Выводить информацию только по указанному VLAN.

'''
from sys import argv

file = argv[1]

vlan = raw_input("Enter VLAN ID: ")

table = []

with open(file, "r") as f:
	for line in f:
		if len((line.strip()).split()) == 4 and "-" not in line:
			entry = []
			vid, mac, junk, port = (line.strip()).split()

			if vid == vlan:
				entry = [vid, mac, port]
				table.append(entry)

table.sort()

for item in table:
	print "{:6} {:16} {:8}".format(item[0], item[1], item[2])