#!/usr/bin/python3
"""Creating a class Mylist that inherits from list"""


class Mylist(list):
    """Mylist class that inherits from list"""
    def is_same_class(obj, a_class):
        """print_sorted method for sorting Mylist instances"""
        if type(obj) == a_class:
            return (True)
        else:
            return (False)
    
    a = 1
    if is_same_class(a, int):
        print("{} is an instance of the class {}".format(a, int.__name__))
    if is_same_class(a, float):
        print("{} is an instance of the class {}".format(a, float.__name__))
    if is_same_class(a, object):
        print("{} is an instance of the class {}".format(a, object.__name__))