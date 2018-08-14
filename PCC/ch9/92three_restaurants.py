#!/usr/bin/python3
class Restaurant():
 """A simple attempt to model a restaurant."""
 def __init__(self,restaurant_name,restaurant_cuisine):
  """Initialize name and cuisine attributes."""
  self.restaurant_name = restaurant_name
  self.restaurant_cuisine = restaurant_cuisine

 def describe_restaurant(self):
  """Describe"""
  print(self.restaurant_name.title()+" is healthy food, from wild places")
  print(self.restaurant_cuisine.title()+" just taste it!")
 def open_restaurant(self):
  """Schedule"""
  print("We are open from 8:00 till 21:00")



#1
restaurant1 = Restaurant('forest town','wild game')
restaurant1.describe_restaurant()

#2
restaurant2 = Restaurant('solitary','wolf menu')
restaurant2.describe_restaurant()

#3
restaurant3 = Restaurant('joy','bread of life')
restaurant3.describe_restaurant()
