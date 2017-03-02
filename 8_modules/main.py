from sys import argv
from my_func import get_int_vlan_map

config_file = argv[1]

if __name__ == "__main__":
	result = get_int_vlan_map(config_file)
	print result
