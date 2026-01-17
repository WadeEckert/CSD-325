#===================================================================
# Title: Module 3.2 Assignment - Brownsfield Chohan Game
# Original Author: Al Sweigart
# Modified By: Wade M. Eckert
# Date Modified: 16 January 2026
# Description: A simple brownsfield implementation of the traditional 
# Japanese dice game Cho-Han.
# This version includes a house fee of 12% on winnings and a bonus for 
# rolling a total of 2 or 7.
#===================================================================

"""Cho-Han, by Al Sweigart al@inventwithpython.com
The traditional Japanese dice game of even-odd.
View this code athttps://nostarch.com/big-book-small-python-projects
Tags: short, beginner, game"""

import random, sys

JAPANESE_NUMBERS = {1: 'ICHI', 2: 'NI', 3: 'SAN',
                    4: 'SHI', 5: 'GO', 6: 'ROKU'}

print('''Cho-Han, by Al Sweigart al@inventwithpython.com

In this traditional Japanese dice game, two dice are rolled in a bamboo
cup by the dealer sitting on the floor. The player must guess if the
dice total to an even (cho) or odd (han) number.

BONUS: If the dice roll totals 2 or 7, you get a 10 mon bonus!
''')

purse = 5000 # Initialize the player's purse with 5000 mon.
while True:  # Main game loop.
    # Place your bet:
    print('You have', purse, 'mon. How much do you bet? (or QUIT)')
    print()
    while True:
        pot = input('wme: ') # Changed prompt to my initals.
        if pot.upper() == 'QUIT':
            print()
            print('Thanks for playing!')
            print()
            sys.exit()
        elif not pot.isdecimal():
            print()
            print('Please enter a number.')
            print()
        elif int(pot) > purse:
            print()
            print('You do not have enough to make that bet.')
            print()
        else:
            # This is a valid bet.
            pot = int(pot)  # Convert pot to an integer.
            break  # Exit the loop once a valid bet is placed.

    # Roll the dice.
    dice1 = random.randint(1, 6)
    dice2 = random.randint(1, 6)

    # Output the dealer's actions:
    print()
    print('The dealer swirls the cup and you hear the rattle of dice.')
    print('The dealer slams the cup on the floor, still covering the')
    print('dice and asks for your bet.')
    print()
    print('    CHO (even) or HAN (odd)?')

    # Let the player bet cho or han:
    while True:
        bet = input('wme: ').upper() # Changed prompt to my initals.
        if bet != 'CHO' and bet != 'HAN':
            print()
            print('Please enter either "CHO" or "HAN".')
            print()
            continue
        else:
            break

    # Reveal the dice results:
    print()
    print('The dealer lifts the cup to reveal:')
    print('  ', JAPANESE_NUMBERS[dice1], '-', JAPANESE_NUMBERS[dice2])
    print('    ', dice1, '-', dice2)
    print()

    # Check for bonus if dice total is 2 or 7:
    diceTotal = dice1 + dice2
    if diceTotal == 2 or diceTotal == 7:
        print('The dice total is', diceTotal, '! You get a 10 mon bonus!')
        print()
        purse = purse + 10

    # Determine if the player won:
    rollIsEven = (dice1 + dice2) % 2 == 0
    if rollIsEven:
        correctBet = 'CHO'
    else:
        correctBet = 'HAN'

    playerWon = bet == correctBet

    # Display the bet results:
    if playerWon:
        print('You won! You take', pot, 'mon.')
        print()
        purse = purse + pot  # Add the pot from player's purse.
        fee = round(pot * 0.12)  # Calculate the house fee at 12% and round up to nearest integer.
        print('The house collects a', fee, 'mon fee.')
        print()
        purse = purse - fee # Subtract the fee from player's purse.
    else:
        purse = purse - pot  # Subtract the pot from player's purse.
        print('You lost!')
        print()

    # Check if the player has run out of money:
    if purse == 0:
        print('You have run out of money!')
        print('Thanks for playing!')
        sys.exit()
