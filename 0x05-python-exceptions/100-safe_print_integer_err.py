#!/usr/bin/python3

def safe_print_integer_err(value):
    try:
        int_value = int(value)
    except Exception as e:
        open(2, 'w').write("Exception: Unknown format code ")
        open(2, 'w').write("'d' for object of type 'str'\n",)
    else:
        print("{:d}".format(int_value))
        return (True)
