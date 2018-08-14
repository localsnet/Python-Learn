#!/usr/bin/python3\
from restaurant import Restaurant
restaurant = Restaurant('forest town','wild game')

print("Restaurant's name "+ restaurant.restaurant_name.title())
print("Restaurant's quisine "+ restaurant.restaurant_cuisine.title())

restaurant.describe_restaurant()
restaurant.open_restaurant()

