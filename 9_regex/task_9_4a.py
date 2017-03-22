# -*- coding: utf-8 -*-

'''
Задание 9.4a

Создать функцию convert_to_dict, которая ожидает два аргумента:
* список с названиями полей
* список кортежей с результатами отработки функции parse_show из задания 9.4

Функция возвращает результат в виде списка словарей (порядок полей может быть другой):
[{'interface': 'FastEthernet0/0', 'status': 'up', 'protocol': 'up', 'address': '10.0.1.1'},
 {'interface': 'FastEthernet0/1', 'status': 'up', 'protocol': 'up', 'address': '10.0.2.1'}]

Проверить работу функции на примере файла sh_ip_int_br_2.txt:
* первый аргумент - список headers
* второй аргумент - результат, который возвращает функции parse_show из прошлого задания.

Функцию parse_show не нужно копировать.
Надо импортировать или саму функцию, и использовать то же регулярное выражение,
что и в задании 9.4, или импортировать результат выполнения функции parse_show.

'''

import task_9_4
from pprint import pprint

def convert_to_dict(fields, ip_int):
	#list for dict with int, addr. status, protocol
	int_list = []
	#obtain tuple from task_9_4
	for line in ip_int:
		#dict for data
		int_dict = {}
		#iterator
		for position, i in enumerate(line, 0):
			#add key/value to dict
			int_dict[fields[position]] = i
		#append dict to list
		int_list.append(int_dict)
	#return final result
	return int_list
	

headers = ['interface', 'address', 'status', 'protocol']

parse_show = task_9_4.result

result = convert_to_dict(headers, parse_show)

pprint(result)
