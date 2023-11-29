#!/usr/bin/python3
'''Prints a square with the character #'''


def print_square(size):
    '''Define print_square
    Raises:
    TypeError: size must be an integer.
    '''
    if not isinstance(size, int):
        raise TypeError("size m ust be an integer")

        if size < 0:
            '''
            Raises:
            ValueError: size must be less than ot equal to 0.
            '''
        raise ValueError("size must be >= 0")

    if isinstance(size, float) and size < 0:
        raise TypeError("size must be an integer")

        for _ in range(size):
        print("#" *size)
