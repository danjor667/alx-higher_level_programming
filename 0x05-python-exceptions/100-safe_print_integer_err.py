#!/usr/bin/python3


from sys import stderr


def safe_print_integer_err(value):
    new_line = "\n"
    try:
        print("{:d}".format(value))
    except (TypeError, ValueError) as te:
        stderr.write("Exception: {}".format(te) + new_line)
        return False
    return True
