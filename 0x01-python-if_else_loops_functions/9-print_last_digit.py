#!/usr/bin/python3
def print_last_digit(number):
    ldigit = number % (10 if number >= 10 else -10)
    ldigit *= -1 if number < 0 else 1
    print(ldigit, end='')
    return ldigit
