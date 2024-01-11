#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Dec 17 11:08:19 2023

@author: Ben
"""

import re
import numpy as np

#%% Read in File

text = open('Day-2/Cubes.txt' , 'r') # Read the file in

#%% Part 1
total = 0
gameNum = 1
for line in text:
    splitLine = line.split(': ',1)
    rounds = splitLine[1].split('; ')
    possible = np.zeros((len(rounds),))
    for subset in range(len(rounds)):
        red = np.array(re.findall(r'(\d+) red', rounds[subset])).astype(int)
        green = np.array(re.findall(r'(\d+) green', rounds[subset])).astype(int)
        blue = np.array(re.findall(r'(\d+) blue', rounds[subset])).astype(int)
        if ((len(red) == 0 or red[0]<13) and (len(green) == 0 or
            green[0]<14) and (len(blue) == 0 or blue[0]<15)):
            possible[subset] = 1
    if np.sum(possible) == len(possible):
        total += gameNum
    gameNum += 1

print(total)


#%% Part 2

text.seek(0)
power = 0

for line in text:
    splitLine = line.split(': ',1)
    rounds = splitLine[1].split('; ')
    redMin = 0
    greenMin = 0
    blueMin = 0
    for subset in range(len(rounds)):
        red = np.array(re.findall(r'(\d+) red', rounds[subset])).astype(int)
        if red.size > 0 and red[0] > redMin: redMin = red[0]
        green = np.array(re.findall(r'(\d+) green', rounds[subset])).astype(int)
        if green.size > 0 and green[0] > greenMin: greenMin = green[0]
        blue = np.array(re.findall(r'(\d+) blue', rounds[subset])).astype(int)
        if blue.size > 0 and blue[0] > blueMin: blueMin = blue[0]
    power += redMin * greenMin * blueMin
    

print(power)