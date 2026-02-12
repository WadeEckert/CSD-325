"""
===================================================================================
Title: Module 8.2 JSON Practice
Original Author: Wade Eckert
Date Modified: 11 February 2026
Description: This program demonstrates how to read from and write to a .json file in Python.
It loads a list of students from a .json file, allows the user to add a new student, 
and then updates the .json file with the new information.
===================================================================================
"""

import json # Import the json module to work with .json files in Python.
import os # Import the os module to work with file paths.


filename = 'Student.json' # This is the name of the .json file that will be loaded and updated.
filepath = os.path.join(os.getcwd(), filename) # Create the full file path to the .json file using the current working directory and the filename.


""" Define a function that loops through the .json class list and prints out each value. """
def print_students(student_list):
    for student in student_list: # Loop through each student in the student_list and print their information in a formatted way.
        print(f"{student['L_Name']}, {student['F_Name']}: ID = {student['Student_ID']} , Email = {student['Email']}")

""" Define a function that adds a new student to the class list. """
def add_student(student_list, first_name, last_name, student_id, email): # Adds a new student to the student_list using the provided information.
    new_student = {
        "F_Name": first_name,
        "L_Name": last_name,
        "Student_ID": student_id,
        "Email": email
    }
    student_list.append(new_student) # Append the new student to the student_list.


if __name__ == "__main__":

    """ Load the Student.json file into a Python class list. """
    with open(filepath, 'r') as infile:
        student_list = json.load(infile) # Load the contents of the .json file into a Python list called student_list.

    print("-- Original Student List --\n") 
    print_students(student_list) # Call the print function to display the original student list.

    """ Prompt user to input new student information. """
    print("\n-- Add New Student --\n")
    first_name = input("Enter student's first name: ")
    last_name = input("Enter student's last name: ")
    student_id = int(input("Enter student's ID: ")) # Convert the input string to an integer.
    email = input("Enter student's email: ")
    add_student(student_list, first_name, last_name, student_id, email) # Add the new student input to the student_list using the add_student function.

    print("\n-- Updated Student List --\n")
    print_students(student_list) # Call the print function to display the updated student list.

    """ Use the JSON dump() function to append the new data to the .json file. """
    with open(filepath, 'w') as outfile:
        json.dump(student_list, outfile, indent=4) # Write the updated student_list back to the .json file with indentation for readability.

    print("\nThe .json file was updated with the new student information.")