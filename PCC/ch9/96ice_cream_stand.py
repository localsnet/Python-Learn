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

#End of 9-1

class IceCreamStand(Restaurant):
 """Class inheritance"""
 def __init__(self,restaurant_name, restaurant_cuisine='ice cream'):
  """Initialize attributes of the parent class"""
  super().__init__(restaurant_name,restaurant_cuisine)
  """Initialize attributes specific to a child class"""
  self.flavors = ['orange','banana','apple']
  
 def show_flavors(self):
  print("Now we offer icecream with this flavors:")
  for flavor in self.flavors:
   print('- ' + flavor.title())  

restaurant = IceCreamStand('frost')

print("Restaurant's name "+ restaurant.restaurant_name.title())
print("Restaurant's quisine "+ restaurant.restaurant_cuisine.title())

restaurant.describe_restaurant()
restaurant.show_flavors()
