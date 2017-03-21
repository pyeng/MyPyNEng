# -*- coding: utf-8 -*-

'''
Задание 9.4

Создать функцию parse_show, которая ожидает два аргумента:
* имя файла, в котором находится вывод команды show
* регулярное выражение

Функция должна обрабатывать вывод команды show ip int br и возвращать такие поля:
* Interface
* IP-Address
* Status
* Protocol

Информация должна возвращаться в виде списка кортежей:
[('FastEthernet0/0', '10.0.1.1', 'up', 'up'),
 ('FastEthernet0/1', '10.0.2.1', 'up', 'up'),
 ('FastEthernet0/2', 'unassigned', 'up', 'up')]

Для получения такого результата, используйте регулярные выражения.

Проверить работу функции на примере файла sh_ip_int_br_2.txt.
'''
#import modules 
from sys import argv
from re import compile
from pprint import pprint

#func expect filename and regexp, than return -- intf, ip_addr, status, protocol
def parse_show(file, exp):
	#dict for data
	ip_int = []
	#open file
	with open(filename, "r") as f:
		#read file by line
		for line in f:
			#leave only line that start with "F", "G", "T", "L" (FastEthernet, 
			#	GigaEthernet, TenEthernet, Loopback)
			if line[0] in ["F", "G", "T", "L"]:
				#find: Interface, IP-Address, Status, Protocol
				match = (exp.search(line)).groups()
				ip_int.append(match)

	return ip_int

filename = argv[1]
regexp = compile("""(?P<intf>\S+)\s+(?P<address>\S+)\s+[\w\s]+\
(?P<status>up|down|administratively down)\s+(?P<protocol>up|down)""")

result = parse_show(filename, regexp)

pprint(result)