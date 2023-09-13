#!/usr/bin/python3
"""A class that defines the student class"""
class Student:
	def __init__(self, first_name, last_name, age):
	"""A function that initialises arguments

	Args:
		first_name: the first name
		last_name: the last name
		age: the age of the student
	"""
	self.first_name = first_name
	self.last_name = last_name
	self.age = age

	def to_json(self):
	""" a function that retrieves a dictionary representation of student

	"""
	def to_json(self):
	result = {}
	for key, value in self.__dict__.item():
		if isinstance(value, (str, int)):
			result[key] = value
	return result
