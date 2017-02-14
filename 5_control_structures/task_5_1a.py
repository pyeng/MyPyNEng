# -*- coding: utf-8 -*-
'''
Задание 5.1a

Сделать копию скрипта задания 5.1.

Дополнить скрипт:
- Добавить проверку введенного IP-адреса.
- Адрес считается корректно заданным, если он:
   - состоит из 4 чисел разделенных точкой,
   - каждое число в диапазоне от 0 до 255.

Если адрес задан неправильно, выводить сообщение:
'Incorrect IPv4 address'
'''

ip_addr = raw_input("\nEnter IP address in dotted decimal notation: ")

first_byte = int(ip_addr.split(".")[0])

if len(ip_addr.split(".")) == 4:
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
else:
	print "\nIncorrect IPv4 address\n"