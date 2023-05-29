#!/usr/bin/python3


def safe_print_list(my_list=[], x=0):
    try:
        if x >= 0:
            for i in range(x):
                print(my_list[i], end='')
            print()
        return x
    except Exception:
        print()
    return 0
