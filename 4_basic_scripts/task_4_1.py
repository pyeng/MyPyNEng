# -*- coding: utf-8 -*-
"""
Задание 4.1

Запросить у пользователя ввод IP-сети в формате: 10.1.1.0/24

Затем вывести информацию о сети и маске в таком формате:

Network:
10        1         1         0
00001010  00000001  00000001  00000000

Mask:
/24
255       255       255       0
11111111  11111111  11111111  00000000

Проверить работу скрипта на разных комбинациях сеть/маска.
"""
import ipaddress

prompt = unicode(raw_input("\nEnter IP addr in format 'X.X.X.X/24' : "))

prompt_net = ipaddress.ip_network(prompt, strict=False)

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