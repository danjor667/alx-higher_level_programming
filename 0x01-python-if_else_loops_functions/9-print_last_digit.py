#!/usr/bin/python3
def print_last_digit(number):
    if number < 0:
        n = -1 * number
        rem = n % 10
        rem = -1 * rem
        print("{}".format(rem), end="")
        return rem
    else:
        print("{}".format(number % 10), end="")
        return (number % 10)
