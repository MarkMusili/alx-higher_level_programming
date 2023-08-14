#!/usr/bin/python3
def no_c(my_string):
    new_string = [char for char in my_string if char != 'c' and char != 'C']
    string = "".join(new_string)
    return string
