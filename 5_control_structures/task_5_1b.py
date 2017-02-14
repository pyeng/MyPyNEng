# -*- coding: utf-8 -*-
'''
Задание 5.1b

Сделать копию скрипта задания 5.1a.

Дополнить скрипт:
Если адрес был введен неправильно, запросить адрес снова.
'''
ip_addr = raw_input("\nEnter IP address in dotted decimal notation: ")

first_byte = int(ip_addr.split(".")[0])

pass_OK = False

while not pass_OK:
	if len(ip_addr.split(".")) != 4:
		print "\nIncorrect IPv4 address"
		ip_addr = raw_input("\nEnter IP address in dotted decimal notation: ")
		first_byte = int(ip_addr.split(".")[0])
	else:
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
		pass_OK = True