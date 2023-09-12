#!usr/bin/python3
def inherits_from(obj, a_class):
	"""Function that defines whether object is an instance of a class that inherited
	
	Args:
		obj: object
		a_class:  a class
	Return:
		True if the object is an instance of a class otherwise false
	"""
	return isinstance(obj, a_class)
