# -*- coding: utf-8 -*-
'''
Задание 6.2c

Переделать скрипт из задания 6.2b:
* передавать как аргументы:
 * имя исходного файла конфигурации
 * имя итогового файла конфигурации

Внутри, скрипт должен отфильтровать те строки, в исходном файле конфигурации,
в которых содержатся слова из списка ignore.
И затем записать оставшиеся строки в итоговый файл.

Проверить работу скрипта на примере файла config_sw1.txt.

'''

from sys import argv

ignore = ['duplex', 'alias', 'Current configuration']

src_file, dst_file = argv[1:]
#dst_file = "config_sw1_cleared.txt"
save_to_file = []

with open(src_file, "r") as f:
	for line in f:
		if [elem for elem in ignore if elem in line]:
			continue
		else:
			save_to_file.append(line.strip())

cfg_lines = "\n".join(save_to_file)

with open(dst_file, "w") as f:
	f.write(cfg_lines)