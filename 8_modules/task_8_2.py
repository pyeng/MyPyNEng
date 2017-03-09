# -*- coding: utf-8 -*-

"""
Задание 8.2

Создать функцию parse_cdp_neighbors, которая обрабатывает
вывод команды show cdp neighbors.

Функция ожидает, как аргумент, вывод команды одной строкой.

Функция должна возвращать словарь, который описывает соединения между устройствами.

Например, если как аргумент был передан такой вывод:
R4>show cdp neighbors

Device ID    Local Intrfce   Holdtme     Capability       Platform    Port ID
R5           Fa 0/1          122           R S I           2811       Fa 0/1
R6           Fa 0/2          143           R S I           2811       Fa 0/0

Функция должна вернуть такой словарь:

    {('R4', 'Fa0/1'): ('R5', 'Fa0/1'),
     ('R4', 'Fa0/2'): ('R6', 'Fa0/0')}


Проверить работу функции на содержимом файла sw1_sh_cdp_neighbors.txt

"""



def parse_cdp_neighbors(cdp_neigh):

	interconnection = {}
	
	# iterate over each line in cdp
	for line in cdp_neigh.split("\n"):
		
		#find local hostname
		if ">" in line:
			local_host = line.split(">")[0]
		
		# discard useless line	
		elif line.startswith("Capability") or "Repeater" in line or "Capability" in line:
			pass

		# find other info (remote hostname, local and remote interfaces)	
		elif len(line.split()) >= 9:
			remote_host = line.split()[0]
			local_int = "".join(line.split()[1:3])
			remote_int = "".join(line.split()[-2:])
			interconnection[local_host, local_int] = (remote_host, remote_int)

	return interconnection


if __name__ == "__main__":

	from sys import argv
	from pprint import pprint

	cdp_file = argv[1]

	with open(cdp_file, "r") as f:
		cdp_data = f.read()
		result = parse_cdp_neighbors(cdp_data)

	print
	pprint(result)
	print