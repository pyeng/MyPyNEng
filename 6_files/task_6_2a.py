# -*- coding: utf-8 -*-
'''
Задание 6.2a

Сделать копию скрипта задания 6.2.

Дополнить скрипт:
  Скрипт не должен выводить команды, в которых содержатся слова,
  которые указаны в списке ignore.
'''

ignore = ['duplex', 'alias', 'Current configuration']

from sys import argv

file = argv[1]

with open(file, "r") as f:
	for line in f:
		 line.startswitch("!") not in line:
			print line.strip()