"""
===================================================================================
Title: Module 9.2 API Tutorial
Original Author: Charlie Custer
Modified By: Wade Eckert
Date Modified: 21 February 2026
Description:  This tutorial program demonstrates how to use the requests library to 
access a public API and print the results in a formatted way.
===================================================================================
"""

import requests
import json

""" Main function to call the API and print the results """
def main():
    response = requests.get('http://api.open-notify.org/astros.json') # This API endpoint returns the number of people currently in space and their names.
    print("\n" + str(response.status_code)) # Print the status code of the response to check if the request was successful (200 means OK).
    print("\n" + str(response.json())) # Print the JSON response from the API. This will be a Python dictionary. 

    jprint(response.json()) # Use the jprint function to print the JSON response in a more readable format.

""" Create a formatted string of the Python JSON object """
def jprint(obj):
    text = json.dumps(obj, sort_keys=True, indent=4) # Convert the Python dictionary (obj) into a JSON-formatted string with sorted keys and indentation for readability.
    print(text)

""" Call the main function when the script is executed directly """
if __name__ == "__main__":
    main()