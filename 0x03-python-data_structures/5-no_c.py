#!/usr/bin/python3
def no_c(my_string):
    result_str = ''
    for ch in my_string:
        if ch.lower() != 'c' or 'C':
            result_str += ch
            return result_str
