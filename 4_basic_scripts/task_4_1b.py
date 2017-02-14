# -*- coding: utf-8 -*-
"""
Задание 4.1b

Преобразовать скрипт из задания 4.1a таким образом, чтобы сеть/маска не запрашивались у пользователя,
а передавались как аргумент скрипту.
"""
import ipaddress
from sys import argv

data = unicode(argv[1])
prompt_net = ipaddress.ip_network(data, strict=False)
#print prompt_net

net_mask = (str(prompt_net.network_address) + "." + str(prompt_net.netmask)).split(".")

binx = []
for i in net_mask:
	i = bin(int(i))
	i = i.split("0b")[1]
	while len(i) != 8:
		i = "0" + i 
		if len(i) == 8:
			binx.append(i)
			break
	else:
		binx.append(i)

print "\nNetwork:"
print "{:10} {:10} {:10} {:10}".format(net_mask[0], net_mask[1], net_mask[2], net_mask[3])
print "{:10} {:10} {:10} {:10}".format(binx[0], binx[1], binx[2], binx[3])

print "\nMask:"
print "{:10} {:10} {:10} {:10}".format(net_mask[4], net_mask[5], net_mask[6], net_mask[7])
print "{:10} {:10} {:10} {:10}".format(binx[4], binx[5], binx[6], binx[7])
