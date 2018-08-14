#!/usr/bin/python3
#a = ''
#b = ''
#while not a and not b:
while True:
	try:
	 a = input('Enter first number')
	 b = input('Enter second number')
	 c =int(a) + int(b)
	except (ValueError, NameError):
	 print("Can't calculate, you must enter numerical data only")

	else:
	 print(c)
#Break it if user want get the data
	if not a or not b:
	 print ('No data, no results, bye')
	 break
#Make a wipe data
#	a = ''
#	b = ''
#	continue