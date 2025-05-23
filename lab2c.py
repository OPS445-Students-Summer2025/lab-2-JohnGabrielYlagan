#!/usr/bin/env python3
# Author: John Gabriel Ylagan
# Script: lab2c.py
# Use sys.argv for command line arguments

#name = 'Jon'
#age = 20
# print('Hi ' + name + ', you are ' + str(age) + ' years old.')

#colour = input("Type in a colour and press enter: ")
#print('The colour I typed in is: ' + colour)

#name = input("Name: ")
#age = input("Age: ")

#print("Hi " + name + ", you are " + age + " years old.")

import sys

#print("Python version:")
#print(sys.version)

#print("\nPlatform:")
#print(sys.platform)

#print("\nCommand-line arguments list (sys.argv):")
#print(sys.argv)

#print("\nNumber of arguments (len(sys.argv)):")
#print(len(sys.argv))

#sys.exit()  # Exit before running anything else
#print("This line will not be shown because sys.exit() ends the script")

if len(sys.argv) != 3:
    print("Usage: " + sys.argv[0] + " NAME AGE")
    sys.exit()

# Assign the input arguments
name = sys.argv[1]
age = int(sys.argv[2])  
# Must input string for name and integer for age, so 2 inputs

print("Hi " + name + ", you are " + str(age) + " years old.")

# Hi John, you are 24 years old.
