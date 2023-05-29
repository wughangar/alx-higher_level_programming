#!/usr/bin/python3


def safe_print_division(a, b):
    try:
        ans = a / b
        return ans
    except Execprion:
        return None
    finally:
        print("Inside result: {}".format(ans))
