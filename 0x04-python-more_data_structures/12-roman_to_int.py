#!/usr/bin/python3


def roman_to_int(roman_string):
    if roman_string is None or not isinstance(roman_string, str):
        return None

    r_values = {'I': 1,
                'V': 5,
                'X': 10,
                'L': 50,
                'C': 100,
                'D': 500}
    result = 0
    rn_len = len(roman_string)
    for i in range(len(roman_string)):
        rom_val = r_values[roman_string[i]]
        if i < rn_len - 1 and rom_val < r_values[roman_string[i + 1]]:
            result -= rom_val
        else:
            result += rom_val
    return result
