#!/usr/bin/python3
"""A class module called student"""

class Student:
	""" A constractor method for the Student class

        Args:
            first_name: the first name of a person instance
            last_name: the last_name of a person instance
            age: the age of a person instance
        """
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
	""" A method that retrieves a dictionary representation
            of a Student instance
        Returns:
            the dictionary representation of a Student instance
        """
        result = {}
        if attrs is None:
            return self.__dict__
        for attr in attrs:
            if hasattr(self, attr):
                result[attr] = getattr(self, attr)
        return result
