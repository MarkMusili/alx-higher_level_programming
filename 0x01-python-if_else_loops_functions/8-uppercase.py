#!/usr/bin/python3
def uppercase(str):
    string = ""
    for i in str:
        if 'a' <= i <= 'z':
            string += chr(ord(i) - 32)
        else:
            string += i
    print(string)
    return string
