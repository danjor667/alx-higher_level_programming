#!/usr/bin/python3
"""
function, roman_to_int
"""


def roman_to_int(roman_string):
    """
    convert roman numerals to int
    Args:
        roman_string: str representing roman num
    Return:
        int equivilent of roman_string
    """

    dic = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
    value = 0
    if roman_string is None or type(roman_string) != str:
        return value
    for i in range(len(roman_string) - 1):
        if dic.get(roman_string[i]) < dic.get(roman_string[i + 1]):
            value -= dic.get(roman_string[i])
        else:
            value += dic.get(roman_string[i])
    value += dic.get(roman_string[len(roman_string)-1])
    return value
