#!/usr/bin/python3


def divisible_by_2(my_list=[]):
    result = []

    for elem in my_list:
        result += [elem % 2 == 0]

    return result
