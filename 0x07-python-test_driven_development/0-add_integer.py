#!/usr/bin/python3
"""custom function that adds two integers."""


def add_integer(a, b=98):
    """Returns the addition of a and b integers.

    Float args are typecasted to ints before any addition.

    Raises:
        TypeError: when a or b is a non-int or non-float.
    """
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")
    return (int(a) + int(b))
