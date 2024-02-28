#!/usr/bin/python3
"""Defines a class Student."""


class Student:
    """Represent a student."""

    def __init__(self, first_name, last_name, age):
        """Initialize a new Student.

        Args:
            first_name (str): The first name of the student.
            last_name (str): The last name of the student.
            age (int): The age of the student.
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """Get a dictionary representation of the Student.

        If attrs is a list of strings, represents only those attributes
        included in the list.

        Args:
            attrs (list): (Optional) The attributes to represent.
        """
        if attrs is None:
            return self.__dict__

        if not isinstance(attrs, list):
            raise TypeError("attrs must be a list of strings")

        return {k: v for k, v in self.__dict__.items() if k in attrs}

    def reload_from_json(self, json):
        """Replace all attributes of the Student.

        Args:
            json (dict): The key/value pairs to replace attributes with.
        """
        if not isinstance(json, dict):
            raise TypeError("json must be a dictionary")

        for k, v in json.items():
            setattr(self, k, v)

