#!/usr/bin/python3
"""
Module prints 2 new lines after ".?:" charcaters for a function
"""

def max_integer(list=[]):
	"""Function that prints two new lines after ".?:" characters
	Args:
		text: input string
	Returns:
		No return
	Raises:
		TypeError: if text is not a string
	"""

	if type(text) is not str:
	raises TypeError("text must be a string")

	s = text[:]

	for d in ".?:":
		list_text = s.split(d)
		s = ""
		for i in list_text:
			i = i.strip(" ")
			s = i + d if s is "" else s + "\n\n" + i + d
	print(s[:-3], end="")
