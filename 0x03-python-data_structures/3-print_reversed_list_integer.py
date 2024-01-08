#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):
    i, length, count = -1, len(my_list), 0
    while count < length:
        print(my_list[i])
        i -= 1
        count += 1
