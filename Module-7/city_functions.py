"""
===================================================================================
Title: Module 7.2 Test Cases
Original Author: Wade Eckert
Modified By: Wade Eckert
Date Modified: 5 February 2026
Description: This module contains a function to format city and country names,
with optional parameters for population and language. It also includes test cases
to verify the function works correctly if the file is executed directly.
===================================================================================
"""

"""Function to format city and country names, with an optional population parameter."""
def city_country(city, country, population=None, language=None): # Define the function with optional parameters for population and language set to None by default.
    if population is not None and language is not None: # Check if both optional parameters are provided.
        return f"{city}, {country} - population {population}, {language}"
    elif population is not None and language is None: # Check if only population is provided.
        return f"{city}, {country} - population {population}"
    elif language is not None and population is None: # Check if only language is provided.
        return f"{city}, {country}, {language}"
    else:
        return f"{city}, {country}" # Return formatted string with just city and country when no optional parameters are provided.
    
"""Print the city, country, population, and language names only if this file is executed directly."""
if __name__ == '__main__':
    print(city_country("Santiago", "Chile"))
    print(city_country("Tokyo", "Japan", 13929286))
    print(city_country("Paris", "France", 2161000, "French"))