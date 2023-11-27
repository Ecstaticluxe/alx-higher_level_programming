#!/usr/bin/python3
'''Define a class Rectangle.'''


class Rectangle:
    '''Represent a Rectangle.'''

    def __init__(self, width=0, height=0):
        '''Initialize a Rectangle.
        Args:
        size (int): size of the rectangle.
        width (int): width of the rectangle, default 0.
        height (int): height of the rectangle, default 0.
        '''
        self.width = width
        self.height = height

    @property
    def width(self):
        '''Define the width of the rectangle'''

        return self.__width

    @width.setter
    def width(self, value):
        '''Set the width of the rectangle.
        Args:
        value (int): The value of the width of the rectangle.

        Raises:
        TypeError: width must be an int.
        ValueError: width must be less than or equal to 0
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
        return 2 * (self.width + self.height)

    def __str__(self):
        if self.width == 0 or self.height == 0:
            return ""
        else:
            rectangle_str = ""
            for i in range(self.height):
                rectangle_str += "#" * self.width + "\n"
            return rectangle_str[:-1]
