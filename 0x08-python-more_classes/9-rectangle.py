#!/usr/bin/python3
"""Defines a class Rectangle"""


class Rectangle:
    """Represents a rectangle
    Attributes:
    number_of_instance (int): The number of Rectangle instances.
    print_symbol (any): the symbol for representation
    """

    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        """Initializes a rectangle with a given width and height.
        Args:
        width (int): The width of the new rectangle
        height (int): The height of teh new rectangle
        """
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

    @property
    def width(self):
        """Gets the width of the rectangle."""
        return self.__width

    @width.setter
    def width(self, value):
        """Sets the width of the rectangle.
        Args:
        Value (int): the value or size of the neww Rectangle
        Raises:
        TypeError: width must be an integer.
        ValueError: width must be >= 0.
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        else:
            self.__width = value

    @property
    def height(self):
        """Gets the height of the rectangle."""
        return self.__height

    @height.setter
    def height(self, value):
        """Sets the height of the rectangle."""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        else:
            self.__height = value

    def area(self):
        """Returns the area of the rectangle."""
        return self.width * self.height

    def perimeter(self):
        """Returns the perimeter of the rectangle."""
        return 2 * (self.width + self.height)
    if self.width != 0 and self.height != 0 else 0

    def __str__(self):
        """Returns a string representation of the rectangle."""
        if self.width == 0 or self.height == 0:
            return ""
        return ((str(self.print_symbol) * self.width + "\n")
                * self.height).strip()

    def __repr__(self):
        """Returns a string representation of the rectangle for recreation."""
        return f"Rectangle({self.width}, {self.height})"

    def __del__(self):
        """Prints a message when an instance of Rectangle is deleted."""
        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """Returns the bigger rectangle based on the area."""
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        if not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")

        area_1 = rect_1.width * rect_1.height
        area_2 = rect_2.width * rect_2.height

        if area_1 >= area_2:
            return rect_1
        else:
            return rect_2

    @classmethod
    def square(cls, size=0):
        """Returns a new Rectangle instance with width == height == size."""
        return cls(size, size)
