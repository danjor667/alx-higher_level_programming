#!/usr/bin/python3
import hidden_4
if __name__ == "__main__":
    names = dir(hidden_4)
    names.sort()
    for name in names:
        if name[0:2] == "__":
            continue
        print(name)
