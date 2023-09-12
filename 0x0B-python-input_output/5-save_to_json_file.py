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
	try:
		with open(filename, "w", encoding="uft-8") as file:
			jason.dump(my_obj, file, ensure_ascii=False, indent=4)
	expect Expection as e:
		print(f"An error occurred: {e}")
