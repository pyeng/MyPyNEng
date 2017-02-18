# -*- coding: utf-8 -*-
'''
Задание 6.2a

Сделать копию скрипта задания 6.2.

Дополнить скрипт:
  Скрипт не должен выводить команды, в которых содержатся слова,
  которые указаны в списке ignore.
'''

from sys import argv

ignore = ['duplex', 'alias', 'Current configuration']

file = argv[1]

with open(file, "r") as f:
	for line in f:
		if line.startswith("!"):
			continue
		elif [elem for elem in ignore if elem in line]:
			continue
		else:
			print line.strip()