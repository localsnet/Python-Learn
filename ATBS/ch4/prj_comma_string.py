#!/usr/bin/env python3
spam = ['apples', 'bananas', 'tofu', 'cats']
def comma(listName):
 for i in range(len(listName)):
  if (len(listName)-i)!=1: 
   print(listName[i]+',', end=' ')
  else:
   print ('and '+listName[-1])

comma(spam)
