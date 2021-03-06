# -*- coding: utf-8 -*-

'''
Задание 9.1

Создать скрипт, который будет ожидать два аргумента:
    1. имя файла, в котором находится вывод команды show
    2. регулярное выражение

В результате выполнения скрипта, на стандартный поток вывода должны быть
выведены те строки из файла с выводом команды show,
в которых было найдено совпадение с регулярным выражением.

Проверить работу скрипта на примере вывода команды sh ip int br (файл sh_ip_int_br.txt).
Например, попробуйте вывести информацию только по интерфейсу FastEthernet0/1.
'''

from sys import argv
from pprint import pprint
from re import compile

filename, regexp = argv[1:3]

exp = compile(regexp)

result =  []

with open(filename, "r") as f:
	for line in f:
		if exp.search(line):
			result.append(line.strip())

print
pprint(result)
print 
