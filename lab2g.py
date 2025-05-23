#!/usr/bin/env python3
# Author: John Gabriel Ylagan
# Author ID: 101563237
# Date Created: 2025/02/23
# lab2g.py
# Use if statement and sys.argv condition

import sys 

# Set default timer value
if len(sys.argv) == 2:
    timer = int(sys.argv[1])  
    # Use the user-provided argument number in the command line
else:
    timer = 3  # Default to start at number 3 if no argument is given

while timer > 0:
    print(timer)
    # print if timer is still greater than 0
    timer = timer - 1 
    # will print each instance of timer minus 1 until its 0
    
print("blast off!") 