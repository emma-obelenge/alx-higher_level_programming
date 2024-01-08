#!/usr/bin/env python3
def no_c(my_string):
    remove = "cC"
    for char in remove:
        my_string = my_string.replace(char, "")
    return (my_string)
