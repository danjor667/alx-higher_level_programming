from calculator_1 import add, sub, mul, div
if __name__ == "__main__":
    a = 10
    b = 5
    print("{a:d} + {b:d} = {:d}".format(a=a, b=b, add(a, b)))
    print("{a:d} - {b:d} = {:d}".format(a=a, b=b, sub(a, b)))
    print("{a:d} * {b:d} = {:d}".format(a=a, b=b, mul(a, b)))
    print("{a:d} / {b:d} = {:d}".format(a=a, b=b, div(a, b)))
