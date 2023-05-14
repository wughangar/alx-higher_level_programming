#!/usr/bin/python3


def max_integer(my_list=[]):
    candidate = None

    for elem in my_list:
        if candidate is None or elem > candidate:
            candidate = elem

    return candidate
