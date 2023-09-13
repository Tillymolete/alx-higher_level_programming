#!/usr/bin/python3
"""A python module defining function called class_to_json"""
def class_to_json(obj):
	"""A function that returns the dictionary description with simple data structure
	
	Args:
		obj: the object
	Return:
		A dictionary description
	"""
	return obj.__dict__
