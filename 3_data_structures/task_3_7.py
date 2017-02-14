# -*- coding: utf-8 -*-
'''
Задание 3.7

Преобразовать MAC-адрес в двоичную строку (без двоеточий).
'''

MAC = "AAAA:BBBB:CCCC"
MAC = MAC.split(":")
MAC = "".join(MAC)

bin_mac = []

for i in MAC:
	bin_i =  bin(ord(i))
	bin_mac.append(bin_i)
	
print bin_mac


