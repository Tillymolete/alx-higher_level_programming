#!/usr/bin/python3
"""Defines inheritance list class mylist"""

class MyList(list):
	"""Implement printing built-in list class"""
	
	def print_sorted(self):
	"""print a list in ascending order"""
	print(sorted(self))
