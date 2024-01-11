#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jan  2 21:20:40 2024

@author: Ben
"""

import sys
sys.path.append('Day-1/')
from AdventOfCodeDay1 import extractFirstLast

def test_extractFirstLast():
    lines = ["gjsga5hjsbdvf6hssjdb7hd", "dgja5ssvdhd7sbavdd5"]
    answers = [0,0]
    for x in range(2):
        answers[x] = extractFirstLast(lines[x])
    assert answers == [57, 55]
# def test_extract_numbers():
    # lines = ["gjsga5hjsbdvf6hssjdb7hd", "dgja5ssvdhd7sbavdd5"]
    
    # assert extract_numbers(lines) == ["567", "575"]