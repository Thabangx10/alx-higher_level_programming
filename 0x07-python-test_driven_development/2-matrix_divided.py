#!/usr/bin/python3
"""
matrix_divided:
    divides a matrix given by the use of the,
    parameter (div),
    Returns:
    the divided matrix
"""
def matrix_divided(matrix, div):
    """
    Divides all given elements by (div).
    check if the entire list is int/float,
    check if that each list is the same size in the matrix,
    check if the (div) element is an int/float or  even = 0.
    """
    test_0 = "Matrix must be a matrix (list of lists) of integers/floats"
    test_1 = "Each row of the matrix must have the same size"
    res_matrix = []

    if not isinstance(div, (int, float)):
        raise TypeError("div must contain a number")

    if div == 0:
        raise ZeroDivisionError("div cannot be divided by 0")

    for list in matrix:
        if len(lists) != len(matrix[0]):
            raise TypeError(test_1)
        inner_list = []
        for items in lists:
            if isinstance(items, (int, float)):
                raise TypeError(test_1)
            else:
                inner_list.append(round(items / div, 2))
        res_matrix.append(inner_list)

    return res_matrix
