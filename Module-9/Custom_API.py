"""
===================================================================================
Title: Module 9.2 Custom API
Original Author: Charlie Custer
Modified By: Wade Eckert
Date Modified: 21 February 2026
Description: This program demonstrates how to use the requests library to access a 
public API (JSONPlaceholder) and print the results in a formatted way. JSONPlaceholder 
is a free online REST API that you can use whenever you need some fake data. 
===================================================================================
"""

import requests
import json

""" Main function to call JSONPlaceholder and print the first 10 posts """
def main():
    response = requests.get('https://jsonplaceholder.typicode.com/posts?_limit=10') # Request the first 10 posts from JSONPlaceholder (no auth required)
    print("\n" + str(response.status_code)) # Print the status code (200 means OK).
    print("\n" + str(response.json()) + "\n") # Print the raw JSON response.

    jprint(response.json()) # Use the jprint function to print the JSON response in a more readable format.

""" Create a formatted string of the Python JSON object """
def jprint(obj):
    text = json.dumps(obj, sort_keys=True, indent=4) # Convert the Python dictionary (obj) into a JSON-formatted string with sorted keys and indentation for readability.
    print(text)

""" Call the main function when the script is executed directly """
if __name__ == "__main__":
    main()