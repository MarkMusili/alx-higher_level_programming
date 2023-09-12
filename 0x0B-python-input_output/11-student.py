#!/usr/bin/python3
"""
This module defines a class
"""


class Student:
    """
    Stores data of a student
    """
    def __init__(self, first_name, last_name, age):
        """
        Attributes:
            first_name (str): first name of student
            last_name (str) last name of student
            age (int) age of student
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """
        Convert data into json format
        Args:
            attrs: list of attributes
        """
        data = {}
        if attrs is None:
            attrs = ["first_name", "last_name", "age"]

        for name in attrs:
            if hasattr(self, name):
                value = getattr(self, name)
                data[name] = value
        return data

    def reload_from_json(self, json):
        """
        Replaces all attributes of the Student instance
        Args:
            json: dictionary
        """
        for key, value in json.items():
            setattr(self, key, value)
