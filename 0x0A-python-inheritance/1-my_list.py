#!/usr/bin/python3
"""class that inherits from list"""
class MyList(list):
    """MyList inherits from lists

        Methods:
            print_sorted (self): sorts the list
    """
    def print_sorted(self):
        """would sort the list"""
        print(sorted(self))