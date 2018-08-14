#!/usr/bin/python3
class User():
 def __init__(self, first_name, last_name):
  """Initialize name and age attributes."""
  self.first_name = first_name
  self.last_name = last_name
  self.age = 0
  self.gender = ""

#Describe user method
 def describe_user(self):
  """Describe and summarize all attributes in one place"""
  print("first name: " + self.first_name.title() + "\nlast name: " + self.last_name.title() + "\nage:" + str(self.age) + "\ngender: " + str(self.gender) +"\n")

#Greet user method
 def greet_user(self):
  """Personalized greeting to the user """
  print("Your file here, dear user: "+ self.first_name)

#Specify opt params method:
 def specify_opt(self, age, gender):
  """Optionals params"""
  self.age = age
  self.gender = gender 
#End of 9-3


