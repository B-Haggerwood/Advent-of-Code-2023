#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Dec 16 22:53:17 2023

@author: Ben
"""

import re

#%% Read in File

cali = open('CalibrationDocument.txt' , 'r') # Read the file in

#%% Part 1

code = 0 # Create the counter for the final answer
for line in cali: # Loop through the file line by line
    num = ''.join(re.findall(r'\d+', line)) # Find the number and collate into single string
    finalNumber = int(num[0]+num[len(num)-1]) # Keep only the first and last number
    code += finalNumber # Add this to the running total

print('Code to part 1 is ' + str(code))

#%% Part 2

cali.seek(0)
digits = ['one', 'two', 'three', 'four', 'five', 'six', 
                    'seven', 'eight', 'nine', '0', '1', '2', '3', '4', '5', 
                    '6', '7', '8', '9']

code2 = 0 # Create the counter for the final answer
for line2 in cali: # Loop through the file line by line
    print(line2)
    characters = []
    positions = []
    for word in digits:
        for m in re.finditer(word, line2):
            if m.start() != -1:
                positions.append(m.start())
                characters.append(word)
    orderChar = [characters for (positions, characters) in sorted(zip(positions, characters))]
    print(orderChar)
    for index in [0,len(orderChar)-1]:
        if orderChar[index] == 'one':
            orderChar[index] = 1
        elif orderChar[index] == 'two':
            orderChar[index] = 2
        elif orderChar[index] == 'three':
            orderChar[index] = 3
        elif orderChar[index] == 'four':
            orderChar[index] = 4
        elif orderChar[index] == 'five':
            orderChar[index] = 5
        elif orderChar[index] == 'six':
            orderChar[index] = 6
        elif orderChar[index] == 'seven':
            orderChar[index] = 7
        elif orderChar[index] == 'eight':
            orderChar[index] = 8
        elif orderChar[index] == 'nine':
            orderChar[index] = 9
        else: 
            orderChar[index] = int(orderChar[index])
    lineCode = int(''.join([str(orderChar[0]), str(orderChar[len(orderChar)-1])]))
    print(lineCode)
    code2 += lineCode
print('Code to part 2 is ' + str(code2))