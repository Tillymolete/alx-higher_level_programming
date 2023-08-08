#!/usr/bin/python3
for ch in range(97, 122):
    if ch != 101 and ch != 113:
        print("{:c}".format(ch), end='')
