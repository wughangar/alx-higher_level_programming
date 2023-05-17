#!/usr/bin/python3


def square_matrix_simple(matrix=[]):
    m_matric = []
    for row in matrix:
        m_row = [value ** 2 for value in row]
        m_matrix.append(m_row)
    return m_matrix
