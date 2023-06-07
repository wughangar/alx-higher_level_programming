#!/usr/bin/python3
"""
1. Divide a matrix
"""
def matrix_divided(matrix, div):
    """
    divides the matrix 

    Args:
        matrix: to be divided 
        div: value to divide the matrix with

    Raises:
        
        TypeError: if matrix is not list or or row is not list 
        TypeError: is numbers gives are not ints or floats
        ZeroDivisionError: if matrix is divded by zero
    """
    if not isinstance(matrix, list):
        raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
    if not all(isinstance(row, list) for row in matrix):
        raise TypeError("matrix must be a matrix (list of lists) of integers/floats")

    rlen = len(matrix[0])
    x = len(row)
    if not all(x) == rlen for row in matrix):
        raise TypeError("Each row of the matrix must have the same size")

    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")

    nmatrix = [[round(element / div, 2) for element in row] for row in matrix]
    return nmatrix
