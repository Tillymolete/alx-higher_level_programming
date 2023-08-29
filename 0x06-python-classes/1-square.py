#!/usr/bin/python3
"""``defination of class 'Square' with private instance attribute"""

class Square:
	"""Class Square that defines a square."""
	def __init__(self, size=0):
		"""Inits Square with private intsance attribute 'size'
		Args:
			size: Size of the square with integer value"""
		self.__size = size
