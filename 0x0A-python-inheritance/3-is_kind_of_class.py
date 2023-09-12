#!/usr/bin/python3
"""function that returns True/False if the object is an instance"""

def is_kind_of_class(obj, a_class):
	"""Function checks an object is instance of a class
	Args:
		obj: object
		a_class: class
	Return:
		True if the object is an instance of class
		False otherwise
	"""
	return isinstance(obj, a_class)
