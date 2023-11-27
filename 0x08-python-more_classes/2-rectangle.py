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
        '''Set the width of the rectangle.
        Args:
        '''
        return self.__width

    @width.setter
    def width(self, value):
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
        return 2 * (self.width + self.height)
