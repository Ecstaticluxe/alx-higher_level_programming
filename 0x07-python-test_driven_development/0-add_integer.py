#!/usr/bin/python3
"""Define integer addition."""


def add_integer(a, b=98):
    """Return integer addition of a and b.
    a and b must be integers or floats.
    Raises:
    TypeError: if a and b is non integer or float.
    """

    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")

    a = int(a)
    b = int(b)

    return a + b
