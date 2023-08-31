#!/usr/bin/python3
"""
function to find peak in a list on unsorted integers
"""


def find_peak(list_of_integers):
    """
    peak function covering all edge cases
    """
    n = len(list_of_integers)
    if n == 0:
        return None
    if n == 1:
        return list_of_integers[0]
    if list_of_integers[0] >= list_of_integers[1]:
        return list_of_integers[0]
    if list_of_integers[n - 1] >= list_of_integers[n - 2]:
        return list_of_integers[n - 1]
    for x in range(1, n - 1):
        if list_of_integers[x - 1] <= list_of_integers[x] and \
                list_of_integers[x + 1] <= list_of_integers[x]:
            return list_of_integers[x]
    return None
