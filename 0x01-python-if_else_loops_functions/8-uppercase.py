#!/usr/bin/python3
def uppercase(str):
    str_bank = ""
    for char in str:
        if ord(char) >= 97 and ord(char) < 122:
            str_bank += chr(ord(char) - 32)
        else:
            str_bank += char
    print(f"{str_bank}".format())
