#!/usr/bin/python3
'''Define a class Rectangle.'''


class Rectangle:
    '''Represent a rectangle.'''

    def __init__(self, width=0, height=0):
        '''Initialize a Rectangle instance.
        Args:
        size (int): The size of the rectangle.
        '''
        self.width = width
        self.height = height

    @property
    def width(self):
        '''Define the width of the rectangle.'''
        return self.__width

    @width.setter
    def width(self, value):
        '''Set the value of the Rectangle.
        Args:
        value (int): The value of teh rectangle
        .
        Raises:
        ValError: must be less than or equal to 0.
        TypeError: must be an integer.
        '''
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        else:
            self.__width = value

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        else:
            self.__height = value

    def area(self):
        return self.width * self.height

    def perimeter(self):
        '''Calculate and return the perimeter of the Rectangle'''
        return 2 * (self.width + self.height)
