#!/usr/bin/env python3
def no_c(my_string):
    str_cpy = ""
    for char in my_string:
        if char == "c" or char == "C":
            char = ""
        str_cpy += char
    return(str_cpy)
