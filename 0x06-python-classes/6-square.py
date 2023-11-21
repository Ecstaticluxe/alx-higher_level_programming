#!/usr/bin/python3

"""Define a class square."""

class Square:
    """Represent a square."""

    def __init__(self, size=0, position=(0, 0)):
        """Initialize a Square instance.

        Args:
            size (int): The size of the square. Default is 0.
            position (tuple): The position of the square. Default is (0, 0).

        Raises:
            ValueError: If size or position is invalid.
            TypeError: If size is not an integer or position is not a tuple of 2 positive integers.
        """
        self.size = size
        self.position = position

    @property
    def size(self):
        """Retrieve the size of the square."""
        return self.__size

    @size.setter
    def size(self, value):
        """Set the size of the square.

        Args:
            value (int): The size to set.

        Raises:
            ValueError: If size is less than 0.
            TypeError: If size is not an integer.
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    @property
    def position(self):
        """Retrieve the position of the square."""
        return self.__position

    @position.setter
    def position(self, value):
        """Set the position of the square.

        Args:
            value (tuple): The position to set.

        Raises:
            ValueError: If position is not a tuple of 2 positive integers.
            TypeError: If position is not a tuple.
        """
        if not isinstance(value, tuple) or len(value) != 2 or \
                not all(isinstance(coord, int) and coord >= 0 for coord in value):
            raise TypeError("position must be a tuple of 2 positive integers")
        else:
            self.__position = value

    def area(self):
        """Calculate and return the area of the square."""
        return self.__size ** 2

    def my_print(self):
        """Print the square with the character # and respect the position."""
        if self.__size == 0:
            print()
        else:
            for _ in range(self.__position[1]):
                print()
            for _ in range(self.__size):
                print(" " * self.__position[0] + "#" * self.__size)
