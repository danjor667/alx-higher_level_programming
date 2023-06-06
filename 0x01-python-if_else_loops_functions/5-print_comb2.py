#!/usr/bin/python3
for i in range(10):
    for j in range(10):
        if i == 9 and j == 9:
            break
        else:
            print("{}{}".format(i, j), end=", ")
print("{}{}".format(i, j))
