#!/usr/bin/python3


def safe_print_list_integers(my_list=[], x=0):
    try:
        num = 0
        for i in my_list:
            if isinstance(i, int):
                print("{:d}".format(i), end='')
                num += 1
            if num == x:
                break
        print()
        return num
    except IndexError:
        print("IndexError: list index out of range")
        return 0
