#!/usr/bin/python3
"""This module defines a function that reads a text file
and prints it to stdout
"""


def read_file(filename=""):
    """
    Args:
        filename = path of the file to be opened
    Return:
        Prints the contents to the stdout
    """
    with open(filename) as f:
        file_contents = f.read()
        print(file_contents, end="")
