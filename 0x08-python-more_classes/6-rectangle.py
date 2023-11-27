#!/usr/bin/python3
'''Define a Clas Rectangle.'''


class Rectangle:
    '''Represent a Rectangle class'''
    number_of_instances = 0

    def __init__(self, width=0, height=0):
        '''Initialize a rectangle instance.
        Args:
        size (int): The size of the rectangle.
        width (int): The width hof the rectangle.
        height (int): The height of the rectangle
        '''
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

    @property
    def width(self):
        '''Define the width of the rectangle'''
        return self.__width

    @width.setter
    def width(self, value):
        '''set the value of the rectangle.

        Args:
        value: The value of the rectangle.

        Raises:
        TypeError: width must be onteger
        ValueError: idth must be less greater than or equal to 0
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
            return rectangle_str[:-1]  # Remove the trailing newline for the last row

    def __repr__(self):
        return f"Rectangle({self.width}, {self.height})"

    def __del__(self):
        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1
