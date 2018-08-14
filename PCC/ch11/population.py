#Module
#Modify your function so it requires a third parameter, population.
#Modify the function so the population parameter is optional.
def get_city_country(city, country, population=''):
 """return a single string of the form City, Country, population"""
 if population:
  location = city + ' ' + country + ' ' + str(population)
  return location.title()

 else:
  location = city + ' ' + country
  return location.title()
