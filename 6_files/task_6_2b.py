# -*- coding: utf-8 -*-
'''
Задание 6.2b

Дополнить скрипт из задания 6.2a:
* вместо вывода на стандартный поток вывода, скрипт должен записать полученные строки в 
файл config_sw1_cleared.txt

При этом, должны быть отфильтрованы строки, которые содержатся в списке ignore.

Строки, которые начинаются на '!' отфильтровывать не нужно.
'''

from sys import argv

ignore = ['duplex', 'alias', 'Current configuration']

cfg_cleared = "config_sw1_cleared.txt"

file = argv[1]

save_to_file = []

with open(file, "r") as f:
	for line in f:
		if [elem for elem in ignore if elem in line]:
			continue
		else:
			save_to_file.append(line.strip())

cfg_lines = "\n".join(save_to_file)

with open(cfg_cleared, "w") as f:
	f.write(cfg_lines)