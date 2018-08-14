#!/usr/bin/python3
filename = 'guest_book.txt'
name = ''
with open(filename, 'a') as file_object:
 while not name:
  name = input('Apply your name: ')
  if not name:
   continue
  print('Thank you ' + name)
 file_object.write(name + '\n')
  

