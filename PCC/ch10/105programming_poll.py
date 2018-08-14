#!/usr/bin/python3
filename = 'poll_responds.txt'
name = ''
respond = ''
with open(filename, 'a') as file_object:
 while not (name and respond):
  name = input('What is your name? \n Answer: ')
  respond = input('Why you like programming? \n Answer: ')
  if not (name and respond):
   print('you must provide all requested informtaion')
   continue
  print('Thank you ' + name)
 file_object.write(name + ': ' + respond + '\n')
  

