#!/usr/bin/python3
exceptions = ['q','e']
for i in range(ord('a'),ord('z') + 1):
    if chr(i) not in exceptions:
        print(chr(i), end = '')
