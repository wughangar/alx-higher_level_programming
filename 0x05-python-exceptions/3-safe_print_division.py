#!/usr/bin/python3


def safe_print_division(a, b):
    ans = None
    try:
        ans = a / b
        return ans
    except Exception:
        return None
    finally:
        print("Inside result: {}".format(ans))
