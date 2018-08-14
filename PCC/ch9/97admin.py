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

# 9-7
class Admin (User):
 def __init__(self, first_name, last_name):
  super().__init__(first_name, last_name)
  self.privileges = []
 
 def show_privileges(self):
  print("Privileges:")
  for i in self.privileges:
   print('- ' + i.title())
#Instance1
user1 = Admin('John', 'Doe')

user1.specify_opt(33,'male')
user1.privileges = [
    'can reset passwords',
    'can moderate discussions',
    'can suspend accounts',
    ]  
user1.greet_user()
user1.describe_user()
user1.show_privileges()
