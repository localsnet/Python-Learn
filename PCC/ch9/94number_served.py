#!/usr/bin/python3
class Restaurant():
 """A simple attempt to model a restaurant."""
 def __init__(self,restaurant_name,restaurant_cuisine):
  """Initialize name and cuisine attributes."""
  self.restaurant_name = restaurant_name
  self.restaurant_cuisine = restaurant_cuisine
  self.number_served = 0
 def describe_restaurant(self):
  """Describe and summarize all attributes in one place"""
  print(self.restaurant_name.title()+" is healthy food, from wild places "+ self.restaurant_cuisine.title()+"- our cuisine | Were served in bussines day overall:"+ str(self.number_served))
 def open_restaurant(self):
  """Schedule"""
  print("We are open from 8:00 till 21:00")
 def set_number_served(self,customers):
  """set the number of customers that have been served"""
  self.number_served = customers
 def increment_number_served(self,customers_add):
  """ increment the number of customers who’ve been served"""
  self.number_served += customers_add 
  

restaurant = Restaurant('forest town','wild game')
# Verifying that self.number_served = 0
restaurant.describe_restaurant()
#Modifying an attribute’s Value Directly
restaurant.number_served = 2
restaurant.describe_restaurant()
#Increment it on 2
restaurant.increment_number_served(2)
restaurant.describe_restaurant()
#Call this method with a new number and print the value again
restaurant.set_number_served(3)
restaurant.describe_restaurant()
