# -*- coding: utf-8 -*-
'''
Задание 6.3a

Сделать копию скрипта задания 6.3.

Дополнить скрипт:
  Отсортировать вывод по номеру VLAN
'''

from sys import argv

file = argv[1]

table = []

with open(file, "r") as f:
	for line in f:
		if len((line.strip()).split()) == 4 and "-" not in line:
			entry = []
			vid, mac, junk, port = (line.strip()).split()
			entry = [vid, mac, port]
			table.append(entry)

table.sort()




for item in table:
	print "{:6} {:16} {:8}".format(item[0], item[1], item[2])

#print table