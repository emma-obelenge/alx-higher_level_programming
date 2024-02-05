#!/usr/bin/python3
"""a function that returns True if the object is exactly\
    n instance of the specified class ; otherwise False"""


def is_same_class(obj, a_class):
    """Checks if obj is an instance of a_class
        Args:
            obj (any): The object to be checked
            a_class (type): The class for check comparism
        Returns:
            True if obj is an instance of a_class
            and False if the reverse is the case
    """
    return (type(obj) is a_class)
