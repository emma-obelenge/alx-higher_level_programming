#!/usr/bin/python3
"""Here we would be checking if an object is an instance of \
a class or class that inherits from another class"""


def is_kind_of_class(obj, a_class):
    """Checks if obj is an instance of a_class, or of class of class
        Args:
            obj (any): The object to be checked
            a_class (type): The class for check comparism
        Returns:
            True if obj is an instance of a_class
            and False if the reverse is the case
    """
    if (isinstance(obj, a_class)):
        return (True)
    else:
        return (False)
