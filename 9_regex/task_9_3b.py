# -*- coding: utf-8 -*-

'''
Задание 9.3b

Проверить работу функции parse_cfg из задания 9.3a на конфигурации config_r2.txt.

Обратите внимание, что на интерфейсе e0/1 назначены два IP-адреса:
interface Ethernet0/1
 ip address 10.255.2.2 255.255.255.0
 ip address 10.254.2.2 255.255.255.0 secondary

А в словаре, который возвращает функция parse_cfg, интерфейсу Ethernet0/1
соответствует только один из них (второй).

Переделайте функцию parse_cfg из задания 9.3a таким образом,
чтобы она возвращала список кортежей для каждого интерфейса.
Если на интерфейсе назначен только один адрес, в списке будет один кортеж.
Если же на интерфейсе настроены несколько IP-адресов, то в списке будет несколько кортежей.

Проверьте функцию на конфигурации config_r2.txt и убедитесь, что интерфейсу
Ethernet0/1 соответствует список из двух кортежей.
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
				#list with ip address 
				ip_intf = []
				
				for i in (section.strip()).split("\n"):
					#find interface name
					if "interface " in i:
						intf = (i.split("interface")[1]).strip()
						ip_addr[intf] = ()
					#find ip addr and mask with regexp
					if "ip addr" in i:
						match = exp.search(i)
						ip = match.group("ip")
						mask = match.group("mask")
						ip_intf.append((ip, mask))
				#filled list with ip addr
				ip_addr[intf] = ip_intf

	return ip_addr


filename = argv[1]
regexp = compile("(?P<ip>[\d+\.]+)\s+(?P<mask>[\d+\.]+)")

ip_addr = {}

parse_cfg(filename, regexp)

pprint(ip_addr)
