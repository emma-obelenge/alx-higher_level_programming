#!/usr/bin/python3
"""Creating a class that will serve as base for other class"""


class Base:
    """The base class for managing the id attribute

    Args:
        id(int): receives the id passed upon instantiation

    Methods:
        __init__: the class constructor
    """
    __nb_objects = 0

    def __init__(self, id=None):
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            id = Base.__nb_objects
            self.id = id
