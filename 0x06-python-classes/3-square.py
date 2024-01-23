#!/usr/bin/python3
"""Define a class Square."""


class Square:
    """A Square class, for handling values needed for computation."""
    def __init__(self, size=0):
        """__init__ method handles instantiation with size

        Args:
        size (int): size of the square as required
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size

    def area(self):
        """area method handles computation of area using size attribute passed

        Args:
            self: instance of the square class passed in

        Returns:
            returns the square of the size attribute
        """
        return (self.__size ** 2)
