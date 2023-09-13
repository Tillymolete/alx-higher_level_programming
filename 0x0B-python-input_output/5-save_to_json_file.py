#!/usr/bin/python3
"""A function that writes object save"""

import json

def save_to_json_file(my_obj, filename):
	"""function that writes an Object to a text file, using a JSON representation

	Args:
		my_obj: the object representation
		filename: the file 
	Return: the object for json
	"""
	
	with open(filename, "w", encoding="uft-8") as file:
		json.dump(my_obj, f)
