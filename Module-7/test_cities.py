"""
===================================================================================
Title: Module 7.2 Test Cases
Original Author: Wade Eckert
Modified By: Wade Eckert
Date Modified: 5 February 2026
Description: This module contains test cases for the city_country function defined in
'city_functions.py'. It verifies that the function correctly formats city and country
names without optional parameters for population and language. It uses the unittest
framework to structure the tests.
===================================================================================
"""

import unittest # Import the unittest module for testing.
from city_functions import city_country # Import the function to be tested.

"""Class for testing the city_country function in 'city_functions.py'."""
class CityCountryTestCase(unittest.TestCase):

    """Test that city_country function returns the correct formatted string under different parameter combinations."""
    def test_city_country(self):

        formatted_string = city_country("Santiago", "Chile") # Call the function with only city and country.
        self.assertEqual(formatted_string, "Santiago, Chile") # Use assertEqual to check the output equals the expected value.

        formatted_string = city_country("Tokyo", "Japan", 13929286) # Call the function with population parameter and no language.
        self.assertEqual(formatted_string, "Tokyo, Japan - population 13929286") 

        formatted_string = city_country("Berlin", "Germany", language="German") # Call the function with language parameter and no population.
        self.assertEqual(formatted_string, "Berlin, Germany, German")

        formatted_string = city_country("Paris", "France", 2161000, "French") # Call the function with both population and language parameters.
        self.assertEqual(formatted_string, "Paris, France - population 2161000, French") 

        formatted_string = city_country("Madrid", "Spain", None, None) # Call the function with both optional parameters set to None.
        self.assertEqual(formatted_string, "Madrid, Spain")

"""Run the test case only if this file is executed directly."""
if __name__ == '__main__':
    unittest.main() # This runs the main function in the unittest module, which runs all test methods in the file.
