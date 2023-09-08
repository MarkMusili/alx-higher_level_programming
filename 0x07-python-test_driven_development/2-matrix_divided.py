#!/usr/bin/python3
"""
This module divides the elements of a matix by a number
Without importing any module
"""


def matrix_divided(matrix, div):
    """
    Args:
        matrix (list of list): The matrix we interact with
        div (int or float): number to be used for dividing
    Return:
        new natrix with divided elements
    """
    new_matrix = []
    if not isinstance(matrix, list):
        raise TypeError("matrix must be a matrix(list of lists) \
                of integers/floats")
    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")
    for row in matrix:
        new_row = []
        size = len(matrix[0])
        if len(row) != size:
            raise TypeError("Each row of the matrix must have the same size")
        for element in row:
            if not isinstance(element, (float, int)):
                raise TypeError("matrix must be a matrix(list of lists) \
                        of integers/floats")
            res = round(element / div, 2)
            new_row.append(res)
        new_matrix.append(new_row)

    return new_matrix
