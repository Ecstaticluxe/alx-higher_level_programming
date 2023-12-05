#!/usr/bin/python3
"""Contains the matrix_mul function"""



def matrix_mul(m_a, m_b):
    """Multiply two matrices (lists of lists of integers/floats)"""

    if not isinstance(m_a, list):
        raise TypeError("m_a must be a list")

    if not m_a:
        raise ValueError("m_a can't be empty")

    row_length_a = len(m_a[0])
    for row in m_a:
        if not isinstance(row, list):
            raise TypeError("m_a must be a list of lists")
        if len(row) != row_length_a:
            raise ValueError("Each row of m_a must have the same size")

        for element in row:
            if not isinstance(element, (int, float)):
                raise TypeError("m_a should contain only integers or floats")

    if not isinstance(m_b, list):
        raise TypeError("m_b must be a list")

    if not m_b:
        raise ValueError("m_b can't be empty")

    row_length_b = len(m_b[0])
    for row in m_b:
        if not isinstance(row, list):
            raise TypeError("m_b must be a list of lists")
        if len(row) != row_length_b:
            raise ValueError("Each row of m_b must have the same size")

        for element in row:
            if not isinstance(element, (int, float)):
                raise TypeError("m_b should contain only integers or floats")

    if row_length_a != len(m_b):
        raise ValueError("m_a and m_b can't be multiplied")

    result_matrix = []
    for i in range(len(m_a)):
        row_result = []
        for j in range(row_length_b):
            element_sum = 0
            for k in range(len(m_b)):
                element_sum += m_a[i][k] * m_b[k][j]
            row_result.append(element_sum)
        result_matrix.append(row_result)

    return result_matrix
