#!/bin/bash/python3
def safe_print_list(my_list=[], x=0):
	try:
		count = 0
		for i in range(x):
			print(my_list[i], end='')
			count = count + 1
		print('')
		return (count)
	except IndexError:
		print('')
	return (count)
