#!/usr/bin/python3


def safe_print_list(my_list=[], x=0):
    count = 0
    for item in my_list:
        count += 1

    try:
        if x <= count:
            for item in my_list[:x]:
                print(item, end=' ')
                print()
                return count
    except Exception:
        print("Error:")
        return 0
