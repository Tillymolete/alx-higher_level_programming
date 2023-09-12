#!/usr/bin/python3
""" A module containing definition for reed_file function"""

def read_file(filename=""):
	"""Function to read data from a file
	Args:
		filename (str: name of the file to read
	"""
	with open(filename, "r", encoding="utf-8") as f:
		read_data =  f.read()
		print(read_data, end=""
