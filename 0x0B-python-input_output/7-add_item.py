#/usr/bin/python3
"""Add all arguments to a Python list and save them to a file."""
import sys
save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = \
    __import__('6-load_from_json_file').load_from_json_file
arg_list = []
arg_list.extend(sys.argv[1:])
print(arg_list)

with open("add_item.json", "a") as the_file:
    save_to_json_file(arg_list, the_file)