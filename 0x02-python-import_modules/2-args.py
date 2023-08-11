#!/usr/bin/python3
import sys

argc = len(sys.argv)
args = sys.argv

if __name__ == "__main__":
    if argc == 1:
        print("0 arguments.")
    elif argc == 2:
        print("{} argument:".format(argc - 1))
    else:
        print("{} arguments:".format(argc - 1))

    for i in range(1, argc):
        if argc >= 2:
            print("{}: {}".format(i, args[i]))
