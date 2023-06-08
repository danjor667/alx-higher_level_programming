#!/usr/bin/python3
import sys
from calculator_1 import add, mul, div, sub


def operation(*args):
    if len(args) != 3:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        exit(1)
    else:
        a = args[0]
        b = args[2]
        s = args[1]
        #s is the operator
        if s == "+":
            print(f"{a} + {b} = {add(int(a), int(b))}")
            exit(0)
        elif s == "-":
            print(f"{a} - {b} = {sub(int(a), int(b))}")
            exit(0)
        elif s == "*":
            print(f"{a} * {b} = {mul(int(a), int(b))}")
            exit(0)
        elif s == "/":
            print(f"{a} / {b} = {div(int(a), int(b))}")
            exit(0)
        else:
            print("Unknown operator. Available operators: +, -, * and /")
            exit(1)


if __name__ == "__main__":
    operation(*sys.argv[1:])
