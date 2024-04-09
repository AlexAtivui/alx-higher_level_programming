#!/usr/bin/python3
"""
Module matrix_divided
Divides each element of a matrix of numbers by a number
"""


def matrix_divided(matrix, div):
    """
    Divide all elements of a matrix by a given number.

    Args:
        matrix (list of lists): The input matrix containing integers or floats.
        div (int or float): The number to divide by (must not be 0).

    Returns:
        list of lists: A new matrix with elements rounded to 2 decimal places.

    Raises:
        TypeError: If the matrix is not a list of lists of integers or floats,
                   if rows have different sizes, or if div is not a number.
        ZeroDivisionError: If div is equal to 0.
    """

    if not isinstance(matrix, list) or len(matrix) == 0 or not matrix[0]:
        raise TypeError("matrix must be a matrix (list of lists) " +
                        "of integers/floats")

    for row in matrix:
        if len(row) == 0:
            raise TypeError("matrix must be a matrix (list of lists) " +
                            "of integers/floats")
        for x in row:
            if type(x) is not int and type(x) is not float:
                raise TypeError("matrix must be a matrix (list of lists) " +
                                "of integers/floats")

    len_rows = []
    for row in matrix:
        len_rows.append(len(row))
    if not all(elem == len_rows[0] for elem in len_rows):
        raise TypeError("Each row of the matrix must have the same size")

    if type(div) is not int and type(div) is not float:
        raise TypeError("div must be a number")

    if div == 0:
        raise ZeroDivisionError("division by zero")

    new_matrix = [[round(x / div, 2) for x in row] for row in matrix]

    return new_matrix