#!/usr/bin/python3
"""Class Rectangle that inherits from Base"""

from base import Base
"""importing the Base clase from the the base.py file"""

class Rectangle(Base):
    """the Rectangle class inherits from the Base class
    
    Args:
        
    """
    def __init__(self, width, height, x=0, y=0, id=None):
        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y

        super().__init__(id)
    def area(self):
        return (self.__width * self.__height)
    
    def display(self):
        for i in range(self.__width):
            for j in range(self.__height):
                print("#", end='')
            print()

    #setting up the getter methods as required.
    @property
    def width(self):
        return (self.__width)
    @width.setter
    def width(self, value):
        if type(value) != int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        return (self.__height)
    @height.setter
    def height(self, value):
        if type(value) != int:
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value
    
    @property
    def x(self):
        return (self.__x)
    @x.setter
    def x(self, value):
        if type(value) != int:
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("x must be > 0")
        self.__x = value
    
    @property
    def y(self):
        return (self.__y)
    @y.setter
    def y(self, value):
        if type(value) != int:
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("x must be > 0")
        self.__y = value
    

    
    @y.setter
    def y(self, value):
        if type(value) != int:
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("y must be > 0")
        self.__y = value

    def __str__(self):
        result = "[Rectangle] ({}) {}/{}".format(self.id, self.__x, self.y)
        result += " - {}/{}".format(self.__width, self.__height)
        return (result)

r1 = Rectangle(4, 6, 2, 1, 12)
print(r1)

r2 = Rectangle(5, 5, 1)
print(r2)