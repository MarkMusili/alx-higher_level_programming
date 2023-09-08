#!/usr/bin/python3
"""
This mudule prints:
    My name is <first name> <last name>
Takes user input for the names
Without importing any module
"""


def say_my_name(first_name, last_name=""):
    """
    Args:
        first_name (str): first name of person
        last_name (str): last name of person
    Return:
        My name is <first name> <last name>
    """
    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")
    if not isinstance(last_name, str):
        raise TypeError("last_name must be a string")
    print(f"My name is {first_name} {last_name}")
