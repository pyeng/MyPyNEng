# -*- coding: utf-8 -*-
'''
Задание 6.1

Аналогично заданию 3.1 обработать строки из файла ospf.txt
и вывести информацию по каждой в таком виде:
Protocol:				OSPF
Prefix:					10.0.24.0/24
AD/Metric:				110/41
Next-Hop:				10.0.13.3
Last update:			3d18h
Outbound Interface:		FastEthernet0/0

Так как это первое задание с открытием файла, заготовка для открытия файла уже сделана.
'''

with open('ospf.txt', 'r') as f:
    for line in f:
        line = (line.strip()).split()
        if line[0] == "O":
        	protocol = "OSPF"
        prefix = line[1]
        metric = line[2]
        next_hop = line[4].strip(",")
        update = line[5].strip(",")
        out_int = line[6]
        print """
Protocol:             {}
Prefix:               {}
AD/Metric:            {}
Next-Hop:             {}
Last update:          {}
Outbound Interface:   {}
			""".format(protocol, prefix, metric, next_hop, update, out_int)