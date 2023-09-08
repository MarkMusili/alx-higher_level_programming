#!/usr/bin/python3
"""
This module prints:
    My name is <first name> <last name>
Depends on the input from the user
Without importing any module
"""
def say_my_name(first_name, last_name=""):
    """
    Args:
        first_name (str): represents the first name of the person
        last_name (str): represents the last name of the person
    Return:
        string: My name is <first name> <last name>
    """
    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")
    if not isinstance(first_name, str):
        raise TypeError("last_name must be a string ")
    print(f"My name is {first_name} {last_name}")
