#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    result = sorted(a_dictionary.items())
    for key, value in result:
        print("{}: {}".format(key, value))
