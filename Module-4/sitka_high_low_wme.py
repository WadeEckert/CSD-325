#===================================================================
# Title: Module 4.2 Assignment - High/Low Temperatures Visualization
# Original Author: Ed Parks
# Modified By: Wade M. Eckert
# Date Modified: 17 January 2026
# Description: This program reads daily high and low temperature data
# from a CSV file for Sitka, Alaska in 2018. It provides a menu for the
# user to choose whether to view high temperatures, low temperatures,
# or exit the program. Based on the user's choice, it generates and
# displays the corresponding temperature plot using Matplotlib.
#===================================================================

import csv
import sys
from datetime import datetime
from matplotlib import pyplot as plt

# Get weather data from file.
filename = 'sitka_weather_2018_simple.csv'
with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)

    # Get dates, high temperatures, and low temperatures from this file.
    dates, highs, lows = [], [], []
    for row in reader:
        current_date = datetime.strptime(row[2], '%Y-%m-%d')
        dates.append(current_date)
        high = int(row[5])
        highs.append(high)
        low = int(row[6])
        lows.append(low)

# Display menu and get user input
while True:
    print("\n" + "="*50) # Decorative line for clarity using "=" characters.
    print("SITKA WEATHER DATA VISUALIZATION")
    print("="*50)
    print("Menu Options:")
    print("\n[H] - View Daily High Temperatures")
    print("[L] - View Daily Low Temperatures")
    print("[E] - Exit Program")
    print("="*50)
    
    # Get user choice, ensuring it's uppercase and stripped of whitespace.
    choice = input("\nEnter your choice (H/L/E): ").upper().strip()
    
    # If user chooses Highs or Lows, plot the respective data.
    if choice == 'H':
        # Plot the high temperatures.
        fig, ax = plt.subplots()
        ax.plot(dates, highs, c='red') # Plot highs in red.
        
        # Format plot.
        plt.title("Daily high temperatures - 2018", fontsize=24)
        plt.xlabel('', fontsize=16)
        fig.autofmt_xdate()
        plt.ylabel("Temperature (F)", fontsize=16)
        plt.tick_params(axis='both', which='major', labelsize=16)
        plt.show()
        
    elif choice == 'L':
        # Plot the low temperatures.
        fig, ax = plt.subplots()
        ax.plot(dates, lows, c='blue') # Plot lows in blue.
        
        # Format plot.
        plt.title("Daily low temperatures - 2018", fontsize=24)
        plt.xlabel('', fontsize=16)
        fig.autofmt_xdate()
        plt.ylabel("Temperature (F)", fontsize=16)
        plt.tick_params(axis='both', which='major', labelsize=16)
        plt.show()

    # If user chooses Exit, terminate the program.   
    elif choice == 'E':
        print("\n" + "="*50)
        print("Thank you for using the Weather Visualization program!")
        print("Goodbye!")
        print("="*50 + "\n")
        sys.exit()

    # Handle invalid input.
    else:
        print("\nInvalid choice. Please enter H, L, or E.")