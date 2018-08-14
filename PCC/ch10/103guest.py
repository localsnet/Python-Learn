#!/usr/bin/python3
filename = 'guest.txt'
with open(filename, 'w') as file_object:
 file_object.write(input('Apply your name:'))
