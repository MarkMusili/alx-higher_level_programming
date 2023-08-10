#!/usr/bin/python3
for i in range(0, 9):
    for n in range(1, 10):
        if i < n and i != n:
            if n != 9 and i != 8:
                print("{}{}, ".format(i, n), end="")
            elif i == 8 and n == 9:
                print("{}{}".format(i, n))
        else:
            pass
