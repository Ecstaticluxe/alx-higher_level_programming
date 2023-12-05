#!/usr/bin/python3
'Defines a matrix multiplication by NumPy.'''

import NumPy as np

def lazy_matrix_mul(m_a, m_b):
    '''Retrun the result of the multiplication.
    Args:
    m_a (list of lists of ints/floats): The first matrix.
    m_b (list of lists of ints/floats): The second matrix.
    '''

    result = np.matmul(m_a, m_b)
