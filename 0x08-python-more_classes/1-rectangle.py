#!/usr/bin/python3
'''Define Class Rectangle'''


class Rectangle:
    '''Represent a Rectangle.'''

    def __init__(self, width=0, height=0):
        '''Initialize a Rectangle instance.
        Args:
        size (int): The new size of the rectangle
        width (int): the width of the rectangle, default 0.
        Height (int): the new heigtr of the rectangle default 0.
        '''
        self._width = 0
        self._height = 0
        self.width = width
        self.height = height

    @property
    def width(self):
        '''Define the width of the Rectangle'''
        return self._width

    @width.setter
    def width(self, value):
        '''Set the value of the Rectangle
        Args:
        value (int): the value of the Rectangle
        Raises:
        TypeError: must be an integer.
        ValueError: must be less than or equal to 0.
        '''
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self._width = value

    @property
    def height(self):
        return self._height

    @height.setter
    def height(self, value):
         '''Set the value of the Rectangle
         Args:
         value (int): the value of the Rectangle
         TypeError: must be an integer.
         ValueError: must be less than or equal to 0
         '''
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self._height = value
