#!/usr/bin/python3

"""
12. Pascal's Triangle
"""


def pascal_triangle(n):
    """
    function that returns a list on its pascas traingle of n

    Args:
        n: list with integers

    Returns:
        a list of lists of integers representing the pascas triangle of n
    """
    if n <= 0:
        return []
    r = []
    for i in range(n):
        row = [1]

        if i > 0:
            prow = r[i-1]
            for j in range(len(prow) - 1):
                row.append(prow[j] + prow[j + 1])
            row.append(1)
        r.append(row)
    return r
