#!/usr/bin/python3
"""
This module writes a json text to a file
"""
import json


def save_to_json_file(my_obj, filename):
    """
    Args:
        my_obj (string): object to be converted
        filename (string): path of the file
    Return:
        Nothing
    """
    with open(filename, 'w') as f:
        json.dump(my_obj, f)
