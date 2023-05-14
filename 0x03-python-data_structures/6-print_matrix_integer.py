#!/usr/bin/python3


def print_matrix_integer(matrix=[[]]):
    for row in matrix:
        for idx in range(0, len(row)):
            col = row[idx]
            print("{:d}".format(col), end=' ' if idx < len(row)-1 else '')
        print("$")
