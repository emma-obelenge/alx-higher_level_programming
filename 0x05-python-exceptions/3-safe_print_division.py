#!/usr/bin/python3

def safe_print_division(a, b):
    result = None
    try:
        result = a / b
    except ZeroDivisionError:
        pass
    finally:
        if result is None:
            print("Inside result: None")
            return (None)
        else:
            print("Inside result: {}".format(result))
            return (result)
