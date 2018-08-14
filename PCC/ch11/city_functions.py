#Module
#Write a function that accepts two parameters: a city name and a country name.
def get_city_country(city, country):
 """return a single string of the form City, Country"""
 location = city + ' ' + country
 return location.title()
