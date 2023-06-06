#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
if number < 0:
    number = -1 * number
    last = -1 * (number % 10)
    number = -1 * number
else:
    last = number % 10
st1 = "and is zero"
st2 = "and is greater than 5"
st3 = "and is less than 6 and not 0"
if last == 0:
    st = st1
elif last >= 6:
    st = st2
else:
    st = st3
print(f"Last digit of {number:d} is {last:d}" + " " + st)
