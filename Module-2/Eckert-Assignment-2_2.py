#===================================================================
#Title: Module 2.2 Assignment - String Manipulation Program
#Original Author: Wade Eckert
#Date Modified: 14 December 2025
#Description: This program acquires a string from the user containing 
#a person's first, middle, and last names, and then display their 
#first, middle, and last initials.
#===================================================================

#Define the main function
def main():
  #Acquire a string from the user containing a person's first, middle, and last name.
  #Validate the input for only letters and spaces and all three names.
  while True:
    name = input("Enter your first, middle, and last name: ")
    name_list = name.split()
    if len(name_list) == 3 and name.strip() and name.replace(" ", "").isalpha():
      break
    else:
      print("\nInvalid input. Please enter your first, middle, and last name using only letters and spaces.\n")

  #Call the get_initials function and pass the name variable as an argument.
  initials = get_initials(name_list)

  #Display the initials.
  print(f"\nYour initials are: {initials}")

#Define a function to get the initials from the inputed name.
def get_initials(name_list):
  #Get the first letter of each word in name_list, capitalize it, and store in new list.
  initials = [word[0].upper() for word in name_list]
  #Join the initials with a period and a space and add a final period and return the result.
  return ". ".join(initials) + "."

# Call the main function to execute the program.
if __name__ == "__main__":
    main()