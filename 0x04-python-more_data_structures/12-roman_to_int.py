#!/usr/bin/python3


def roman_to_int(roman_string):
    if roman_numeral is None or not isinstance(roman_string, str):
        return None
    r_values = {'I': 1,
                    'V': 5,
                    'X': 10,
                    'L': 50,
                    'C': 100,
                    'D': 500}
    result = 0
    rn_len = len(roman_string)
    for i in range(len(roman_numeral)):
        rom_val = roman_values[roman_numeral[i]]
        if i < rn_len - 1 and rom_val < r_values[roman_numeral[i + 1]]:
            reult -= rom_val
        else:
            result += rom_val
    return result
