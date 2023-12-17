#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Dec 16 22:53:17 2023

@author: Ben
"""

import re

#%% Read in File

cali = open('CalibrationDocument.txt' , 'r') # Read the file in

#%% Loop through file

code = 0 # Create the counter for the final answer
for line in cali: # Loop through the file line by line
    num = ''.join(re.findall(r'\d+', line)) # Find the number and collate into single string
    finalNumber = int(num[0]+num[len(num)-1]) # Keep only the first and last number
    code += finalNumber # Add this to the running total

print(code)