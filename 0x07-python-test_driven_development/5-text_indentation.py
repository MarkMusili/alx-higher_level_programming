#!/usr/bin/python3
"""
This module prints a text with 2 new line after
each special character
Without importing any module
"""


def text_indentation(text):
    """
    Args:
        text (str): Text to be used
    Return:
        lines with 2 new lines after the special characters
    """

    if not isinstance(text, str):
        raise TypeError("text must be a string")

    space_char = True
    for char in text:
        if char in ".?:":
            print(char, end="\n\n")
            space_char = True
        elif char == ' ' and space_char:
            continue
        else:
            print(char, end="")
            space_char = False
