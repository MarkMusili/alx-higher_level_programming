#!/usr/bin/python3
"""
This module writes a string to a text file
and returns the number of characters written
"""


def write_file(filename="", text=""):
    """
    Args:
        filename (str): file path
        text (str): text to be written
    Return:
        count(int) number of chars written
    """
    with open(filename, 'w') as f:
        count = f.write(text)
        return count
