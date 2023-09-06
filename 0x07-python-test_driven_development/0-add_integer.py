#!/usr/bin/python3
"""
This module is  for a function that adds two numbers
"""

def add_integer(a, b=98):
	"""A function that adds two numbers
	Args:
		a: the firat number
		b: the second number
	return: the sum of  two numbers
	raises:
		TypeError: if a or b is not an integer or a float number
"""
if not isinstance(a, int) and not isinstance(a, float):
	raise TypeError("a must be an integer")
if not isinstance(b, int) and not isinstance(b, float):
	raise TypeError("b must be an integer")
a = int(a)
b = int(b)
return (a + b)
