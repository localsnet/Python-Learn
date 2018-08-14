#!/usr/bin/python3
class User():
 def __init__(self, first_name, last_name):
  """Initialize name and age attributes."""
  self.first_name = first_name
  self.last_name = last_name
  self.age = 0
  self.gender = ""
  self.login_attempts = 0

##Increment method
 def increment_login(self):
  """ Method increments the value of login_attempts by 1"""
  self.login_attempts += 1

##Reset method
 def reset_login_attempts(self):
  """Method resets the value of login_attempts to 0"""
  self.login_attempts = 0

#Describe user method
 def describe_user(self):
  """Describe and summarize all attributes in one place"""
  print("first name: " + self.first_name.title() + "\nlast name: " + self.last_name.title() + "\nage:" + str(self.age) + "\ngender: " + str(self.gender) + "Logged attempts: " + str(self.login_attempts) + "\n")

#Greet user method
 def greet_user(self):
  """Personalized greeting to the user """
  print("Your file here, dear user: "+ self.first_name)

#Specify opt params method:
 def specify_opt(self, age, gender):
  """Optionals params"""
  self.age = age
  self.gender = gender 

#Instance1
user1 = User('John', 'Doe')

user1.specify_opt(25,'male')  
user1.greet_user()
user1.describe_user()
user1.increment_login()
user1.increment_login()
user1.describe_user()
user1.reset_login_attempts()
user1.describe_user()



  
 
