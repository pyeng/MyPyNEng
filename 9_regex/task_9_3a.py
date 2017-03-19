# -*- coding: utf-8 -*-

'''
Задание 9.3a

Переделать функцию parse_cfg из задания 9.3 таким образом, чтобы она возвращала словарь:
* ключ: имя интерфейса
* значение: кортеж с двумя строками:
  * IP-адрес
  * маска

Например (взяты произвольные адреса):
{'FastEthernet0/1':('10.0.1.1', '255.255.255.0'),
 'FastEthernet0/2':('10.0.2.1', '255.255.255.0')}

Для получения такого результата, используйте регулярные выражения.

Проверить работу функции на примере файла config_r1.txt.
'''

from sys import argv
from re import compile
from pprint import pprint


def parse_cfg(file, exp):
	#open file
	with open(file, "r") as f:
		# and read file
		line = f.read()
		#split by "!"
		for section in (line.strip()).split("!"):
			#leave only interface section with configured ip addr
			if ((section.strip()).startswith("interface") and "ip addr" in section) \
				and "no ip addr" not in section:

				for i in (section.strip()).split("\n"):
					#find interface name
					if "interface " in i:
						intf = i.split("interface")[1]
						ip_addr[intf] = ()
					#find ip addr and mask with regexp
					if "ip addr" in i:
						match = exp.search(i)
						ip = match.group("ip")
						mask = match.group("mask")
						ip_addr[intf] = (ip, mask)

	return ip_addr


filename = argv[1]
regexp = compile("(?P<ip>[\d+\.]+)\s+(?P<mask>[\d+\.]+)")

ip_addr = {}

parse_cfg(filename, regexp)

pprint(ip_addr)
