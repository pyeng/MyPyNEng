# -*- coding: utf-8 -*-
'''
Задание 5.1

1. Запросить у пользователя ввод IP-адреса в десятично-точечном формате.
2. Определить какому классу принадлежит IP-адрес.
3. В зависимости от класса адреса, вывести на стандартный поток вывода:
   'unicast' - если IP-адрес принадлежит классу A, B или C
   'multicast' - если IP-адрес принадлежит классу D
   'local broadcast' - если IP-адрес равен 255.255.255.255
   'unassigned' - если IP-адрес равен 0.0.0.0
   'unused' - во всех остальных случаях

Подсказка по классам (диапазон значений первого байта в десятичном формате):
A: 1-127
B: 128-191
C: 192-223
D: 224-239
'''
ip_addr = raw_input("\nEnter IP address in dotted decimal notation: ")

first_byte = int(ip_addr.split(".")[0])

if first_byte in range(0, 224):
	print "\nunicast\n"
elif first_byte in range(224, 240):
	print "\nmulticast\n"
elif ip_addr == "255.255.255.255":
	print "\nlocal broadcast\n"
elif ip_addr == "0.0.0.0":
	print "\nunassigned\n"
else:
	print "\nunused\n"