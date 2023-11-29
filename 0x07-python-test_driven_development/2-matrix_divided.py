#!/usr/bin/python3
'''Define a matrix division'''


def matrix_divided(matrix, div):
    '''Divide elements of the matrix.

    Args:
    matrix (list): a list of all integer and flost.
    div (int): The divider
    Raises:
    TypeError: if the matrix is non int.
    '''

    if not all(isinstance(row, list) and all(isinstance(x, (int, float))
        for x in row) for row in matrix):
        raise TypeError("matrix must be a matrix (list of lists)
                of integers/floats")


    if any(len(row) != len(matrix[0]) for row in matrix):
        raise TypeError("Each row of the matrix must have the same size")

    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")


    if div == 0:
        raise ZeroDivisionError("division by zero")


    new_matrix = [[round(x / div, 2) for x in row] for row in matrix]

    return new_matrix
