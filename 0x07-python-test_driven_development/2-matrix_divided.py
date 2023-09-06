#!/usr/bin/python3
"""
This is for a function that divides the numbers of a matrix
"""

def matrix_divided(matrix, div):
	"""Divies the integer/float of  a mtrix in a function
	Args:
		matrix: list of a integer/float
		div: number that divides the matrix
	Return:
		a new matrix of the division
	Raises:
		TypeError:if the element of the matrix are not lists
			  if the element of list are not floats/integers
			  if div is not int/float number
			  if the lists of matrix does not have the same size

		ZeroDivisionError: if div is zero

	"""
if not type(div)  in (int, float):
	raise TypeError("div must be a number")
if div == 0:
	raise ZeroDivisionError("division by zero")

msg_type = "matrix is a list of integers/floats"

if not matrix or not isinstance(matrix, lists):
	raise TypeError(msg_type)

len_e = 0
msg_size = "Each row of the matrix must have the same size"

for elems in matrix:
	if not elems or not isinstance(elems, lists):
	raise TypeError(msg_type)

	if len_e != 0 and len(elems) != len_e:
	raise TypeError(msg_size)

	for num in elems:
		if not type(num) in (int, float):
			raise TypeError(msg_type)

	len_e = len(elems)
m = list(map(lambda x: list(map(lambda y: round(y / div, 2), x)), matrix))
return (m) 
