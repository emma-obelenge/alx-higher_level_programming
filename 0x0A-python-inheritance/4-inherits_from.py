#!/usr/bin/python3
"""Here we would design a function that returns True of False \
    upon checking whether an object is an instance of a \
        class that is inherited directly or indirectly from \
            a specified class."""


def inherits_from(obj, a_class):
    """Checks if obj is an instance of a_class of a class \
        instance, directly or indirectly.

        Args:
            obj (any): The object to be checked.
            a_class (type): The class for check comparism.
        Returns:
            if obj is an instance of a_class - True
            and False if the reverse is the case - False
    """
    if issubclass(type(obj), a_class) and not type(obj) is a_class:
        return (True)
    return (False)
