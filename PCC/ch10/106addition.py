#!/usr/bin/python3

a = input('Enter first number')
b = input('Enter second number')
try:
 c =int(a) + int(b)
except ValueError:
 print("Can't calculate, you must enter numerical data only")

else:
 print(c)

