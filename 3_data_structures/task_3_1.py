# -*- coding: utf-8 -*-
'''
Задание 3.1
Обработать строку ospf_route и вывести информацию в виде:
Protocol:				OSPF
Prefix:					10.0.24.0/24
AD/Metric:				110/41
Next-Hop:				10.0.13.3
Last update:			3d18h
Outbound Interface:		FastEthernet0/0

'''

ospf_route = "O        10.0.24.0/24 [110/41] via 10.0.13.3, 3d18h, FastEthernet0/0"

(protocol, prefix, metric, junk, next_hop, last_update, out_int) = ospf_route.split() 
if protocol == "O":
	protocol = "OSPF"
metric = metric.strip("[")
metric = metric.strip("]")
next_hop = next_hop.strip(",")
last_update = last_update.strip(",")

print """
Protocol:             {}
Prefix:               {}
AD/Metric:            {}
Next-Hop:             {}
Last update:          {}
Outbound Interface:   {}
""".format(protocol, prefix, metric, next_hop, last_update, out_int)