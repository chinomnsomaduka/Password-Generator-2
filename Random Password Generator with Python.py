# Random Password Generator with Python
# 1. Import Modules
# Import the in-built random modules, which is used to generate random numbers.
import random

# 2. Declare Variable
# Global Variables

# Create a variable called chars that reads in a string of letters and symbols.
chars = 'abcdefghijklmnopqrstuvwxyz1234567890ABCDEFGHIJKLMNOPQRSTUVWXYZ!@#$%^&*'

# Create a variable called number that reads in a user's input of type integer.
number = input('Enter the number of passwords:')
number = int(number)

# Create a variable called length that reads in a user's input of type integer.
length = input('Enter the length of your password:')
length = int(length)

# This for loop reads in the number of passwords provided by the user and prints a string for each number.
# The range() function returns a sequence of numbers, starting from 0 by default, and increments by 1 (by default), and stops before a specified number.
for p in range(number):
    password = ''
    # For loop reads in the length of password provided by the user and uses the random module to randomize the chars variable.
    for c in range(length):
        # The choice() method returns a randomly selected element from the specified sequence.
        # The += symbol is used to add the new character to the password string each time.
        password += random.choice(chars)
    print(password)
