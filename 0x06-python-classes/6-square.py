#!/usr/bin/python3
"""Define a class Square."""


class Square:
    """A Square class, for handling values needed for computation."""
    def __init__(self, size=0, position=(0, 0)):
        """__init__ method handles instantiation with size

        Args:
        size (int): size of the square as required
        """
        self.__size = size
        self.__position = position

    @property
    def size(self):
        """retrieves the size of the class instance

        Returns:
            returns the size on validated conditions
        """
        return (self.__size)

    @size.setter
    def size(self, value):
        """sets the size of the square instance via encapsulation"""
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    def area(self):
        """area method handles computation of area using size attribute passed

        Args:
            self: instance of the square class passed in

        Returns:
            returns the square of the size attribute
        """
        return (self.__size ** 2)

    def my_print(self):
        """my_print method prints the square '#' to stdou"""
        if (self.__size == 0):
            print()
        else:
            for _ in range(self.__size):
                print("#" * self.__size)

    @property
    def position(self):
        """retrieves the position of the class instance

        Returns:
            returns the position upon request
        """
        return (self.__size)

    @position.setter
    def position(self, value):
        """sets the size of the position instance via setter property"""
        display = "position must be a tuple of 2 positive integers"
        if (isinstance(value, tuple) and len(value) == 2):
            status = 0
            for i in len(value):
                if value[i] > 0:
                    status = 1
                else:
                    status = 0
            if (status == 0):
                raise TypeError(display)
            else:
                self.__position = value
        else:
            raise TypeError(display)
