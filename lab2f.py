#!/usr/bin/env python3
# Author: John Gabriel Ylagan
# Author ID: 101563237
# Date Created: 2025/02/23
# lab2f.py
# Use while loop with arguments

import sys 

#count down from
# make timer the commandline argument as int
timer = int(sys.argv[1])

while timer > 0:
    print(timer)
    # print if timer is still greater than 0
    timer = timer - 1 
    # will print each instance of timer minus 1 until its 0
    
print("blast off!") 