#!/usr/bin/python3
"""This module defines the function is_same_class"""

def is_same_class(obj, a_class):
	"""Function checks whether object is exactly an instance of the specified class

	Args:
		obj: object
		a_class: a class
	Returns:
		True if the object is exactly an instance of the specified class and False otherwise
	"""
	return type(obj) == a_class
