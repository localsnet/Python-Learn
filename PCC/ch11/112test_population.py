#Change name function on population
#Write a second test called test_city_country_population() that verifies you can call your function with the values 'santiago' , 'chile' , and 'population=5000000'
import unittest
from population import get_city_country
class CityTestCase(unittest.TestCase):
	"""Tests for 111city_functions.py ."""
	def test_city_country(self):
		"""Do names like Santiago, Chile work?"""
		city_country = get_city_country('Santiago', 'Chile')
		self.assertEqual(city_country, 'Santiago Chile')

	def test_city_country_population(self):
                """Do names like Santiago, Chile with population work?"""
                city_country = get_city_country('santiago', 'chile', 5000000)
                self.assertEqual(city_country, 'Santiago Chile 5000000')
unittest.main()
 
