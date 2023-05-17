#!/usr/bin/python3


def square_matrix_simple(matrix=[]):
    mmatrix = []
    for row in matrix:
        mrow = [value ** 2 for value in row]
        mmatrix.append(mrow)
    return mmatrix
