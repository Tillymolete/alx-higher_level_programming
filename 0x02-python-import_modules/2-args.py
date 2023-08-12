#!/usr/bin/python3
import sys
if __name__ == "__main__":
	argv = sys.argv[1:]
	num_args = len(argv)
	
	if num_args == 1:
		print("Number of arguments: 1:", end=" ")
	else:
		print("Number of arguments: {}:".format(num_args), end=" ")
	
	for i, arg in enumerate(argv, start=1):
		print("{}: {}".format(i, arg))
	
	if num_args == 0:
		print(".", end=" ")
	else:
		print("")
