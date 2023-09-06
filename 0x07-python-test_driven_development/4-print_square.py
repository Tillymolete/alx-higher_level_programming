#!/usr/bin/python3
"""
This will print the square with the # character
"""

def print_square(size):
	"""Function that prints a square with # character

	Args:
		size: size of the square printed
	Returns:
		No return
	Raises:
		TypeError: if size not an integer number
	"""

if not isinstance(size, int):
	raise TypeError("Size must be an integer")
if size < 0:
	raises ValueError("size must be >= 0")

for i in range(size):
	print("#" * size)
