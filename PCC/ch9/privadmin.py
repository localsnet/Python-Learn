#!/usr/bin/python3
from user import User
#T:Instances as Attributes
class Privileges():
 def __init__(self, privileges=[]): #Note! Need set a list here, else got error:"TypeError: __init__() missing 1 required positional argument: 'privileges'"
  self.privileges = privileges

 def show_privileges(self):
  print("Privileges:")
  for i in self.privileges:
   print('- ' + i.title())
# 9-7
class Admin (User):
 def __init__(self, first_name, last_name):
  super().__init__(first_name, last_name)
  self.privileg = Privileges()
 


