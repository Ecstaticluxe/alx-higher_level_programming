#!/usr/bin/python3
"""Contains the Rectangle class inherited from BaseGeometry"""


BaseGeometry = __import__('7-base_geometry').BaseGeometry



class Rectangle(BaseGeometry):
    """A subclass of Basegeometry"""
    def __init__(self, width, height):
        """Instantiation with width and height"""

        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height
