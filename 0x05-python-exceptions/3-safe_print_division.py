#!/usr/bin/python3


def safe_print_division(a, b):
    ans = None
    try:
        ans = a / b
        print("Inside result: {ans}".format(ans))
    except (ZeroDivisionError):
        print("Inside reult: {ans}".format(ans))
    finally:
        return ans
