#!/usr/bin/python3


def safe_print_division(a, b):
    ans = None
    try:
        ans = a / b
        print("Inside result: {}".format(ans))
    except (ZeroDivisionError):
        print("Inside result: {}".format(ans))
    finally:
        return ans
