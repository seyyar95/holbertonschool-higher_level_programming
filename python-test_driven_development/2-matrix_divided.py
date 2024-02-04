#!/usr/bin/python3

"""This module contains matrix_divided function"""


def matrix_divided(matrix, div):
    """Divides each element of a matrix by a number.

     Args:
        matrix: A list of lists of integers or floats
        representing the matrix to be divided.
        div: The number (int or float) to divide each element of the matrix by.

    Returns:
        A new matrix (list of lists) with the same dimensions
        as the input matrix, containing the results of the division
        rounded to 2 decimal places.

    Raises:
        TypeError: If the matrix is not a list of lists of integers or floats,
                   if any row of the matrix has a different length,
                   or if the divisor is not a number.
        ZeroDivisionError: If the divisor is zero.
    """
    error = 'matrix must be a matrix (list of lists) of integers/floats'
    if not all(isinstance(el, (int, float)) for row in matrix for el in row):
        raise TypeError(error)
    length = len(matrix[0])
    if any(len(row) != length for row in matrix):
        raise TypeError('Each row of the matrix must have the same size')
    if not isinstance(div, (int, float)):
        raise TypeError('div must be a number')
    if div == 0:
        raise ZeroDivisionError('division by zero')

    return ([list(map(lambda x: round(x / div, 2), row)) for row in matrix])
