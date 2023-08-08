#!/usr/bin/python3
def uppercase(str):
    for char in str:
        if ord(char) >= 'a' and ord(char) <= 'z':
            uppercase_char = chr(ord(char) - ord('a') + ord('A'))
        else:
            uppercase_char = char
            print(uppercase_char, end="")
        print()
