#!/usr/bin/python3
def fizzbuzz():
    for i in range(1, 101):
        if i%3 == False and i%5 == False:
            s = "FizzBuzz"
        elif i%3 == False:
            s = "Fizz"
        elif i%5 == False:
            s = "Buzz"
        else:
            s = str(i)
        print("{}".format(s), end=" ")
    print("")

