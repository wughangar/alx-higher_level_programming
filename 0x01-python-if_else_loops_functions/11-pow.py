#!/usr/bin/python3
pow = __import__('11-pow').pow
def pow(a, b):
    result = 1
    for i in range(0, b):
        result *= a
        return result
