#!/usr/bin/python3
import sys

result = 0
args = sys.argv
argc = len(sys.argv)

if __name__ == "__main__":
    if argc == 1:
        print("0")
    else:
        for i in range(1, argc):
            result += int(args[i])
        print("{}".format(result))
