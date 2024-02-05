#!/usr/bin/python3
"""class that inherits from list"""


class MyList(list):
    """
    MyList inherits from lists

    Methods:
        print_sorted (self): sorts the the built-in list
    """
    def print_sorted(self):
        """would print the list in ascending order"""
        print(sorted(self))
