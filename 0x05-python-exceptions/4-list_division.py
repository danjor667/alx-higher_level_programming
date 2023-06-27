#!/usr/bin/python3


def list_division(my_list_1, my_list_2, list_length):
    res = []
    ans = 0
    for i in range(list_length):
        try:
            ans = my_list_1[i] / my_list_2[i]
            res.append(ans)
        except TypeError:
            print("wrong type")
            ans = 0
            res.append(ans)
        except IndexError:
            print("out of range")
            ans = 0
            res.append(ans)
        except ZeroDivisionError:
            ans = 0
            res.append(ans)
            print("division by 0")
        finally:
            pass
    return res
