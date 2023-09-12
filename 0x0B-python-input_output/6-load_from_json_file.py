#!/usr/bin/python3
"""
This module reads a json text from a file
"""
import json


def load_from_json_file(filename):
    """
    Args:
        my_obj (string): object to be converted
        filename (string): path of the file
    Return:
        Return: the python object
    """
    with open(filename, 'r') as f:
        return json.load(f)
