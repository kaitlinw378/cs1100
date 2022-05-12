#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Oct 31 01:53:16 2019

@author: kaitlin
"""

import random
num_trials = 2500
counts = [0] * 10
for i in range(num_trials):
    digit = random.randint(0, 9)
    counts[digit] += 1
    
print('Occurrences and percentages:') 
for i in range(10):
    print("{:1d}: {:4d} {:4.1f}".format(i, counts[i], 100.0 * counts[i] / num_trials))