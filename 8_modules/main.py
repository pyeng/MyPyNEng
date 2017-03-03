from sys import argv
from pprint import pprint
from my_func import *

config_file = argv[1]
out_file = "result.txt"

sw_int = get_int_vlan_map(config_file)

access_config = generate_access_config(sw_int[0], True)

trunk_config = generate_trunk_config(sw_int[1])

with open(out_file, 'w') as f:
	f.writelines([line + '\n' for line in access_config])
	f.writelines([line + '\n' for line in trunk_config])