#======================================================================================================
# Author:      Wade Eckert
# Date:        12/06/2025
# Assignment:  Module 1 Assignment 1.3
# Description: This program demonstrates the use of functions, loops, and conditionals
#              by printing the lyrics to the "99 Bottles of Beer" song, starting from a user-defined,
#              positive, non-zero integer number of bottles.
#======================================================================================================

# Define the main function of the program to orchestrate the logic and program flow.
def main():
    bottles = get_positive_integer("How many bottles of beer are on the wall? ") # Call the input function to get user input.
    print()  
    beer_countdown(bottles)    # Call the countdown function with the stored user input.
    print("No more bottles of beer on the wall! Time to go buy more bottles of beer!") 

# Get user input for the number of bottles to start with and validate it for only positive, non-zero integers.
def get_positive_integer(prompt):
    while True:
        try:
            bottles = int(input(prompt))
            if bottles > 0:
                return bottles
            else:
                print("\nInvalid input. Please enter a positive non-zero integer.\n")
        except ValueError:
            print("\nInvalid input. Please enter a positive non-zero integer.\n")

# Define the countdown function for the song lyrics. 
# Iterate from the starting number down to 1, adjusting the lyrics for singular and plural amounts as needed.
def beer_countdown(bottles):
    while bottles > 0:
        if bottles == 1:
            print(f"{bottles} bottle of beer on the wall, {bottles} bottle of beer.")   
            print("Take one down and pass it around, no more bottles of beer on the wall.\n")
        else:
            print(f"{bottles} bottles of beer on the wall, {bottles} bottles of beer.")
            next_bottle = bottles - 1 
            if next_bottle == 1:
                print(f"Take one down and pass it around, 1 bottle of beer on the wall.\n")
            else:
                print(f"Take one down and pass it around, {next_bottle} bottles of beer on the wall.\n")
        bottles -= 1 # Decrement the bottle count by 1 each iteration.

# Call the main function to start the program.
if __name__ == "__main__":
    main()