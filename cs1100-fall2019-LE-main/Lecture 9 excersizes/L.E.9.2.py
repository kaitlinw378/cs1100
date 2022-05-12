#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Sep 30 15:54:22 2019

@author: kaitlin
"""

census = [ 340, 589, 959, 1372, 1918, 2428, 3097, 3880, 4382, 5082, \
            5997, 7268, 9113, 10385, 12588, 13479, 14830, 16782, \
            8236, 17558, 17990, 18976, 19378 ]

i = 1
added_numbers = 0
while i < len(census):
    pc = (((census[i] - census[i-1])/(census[i-1]))*100)
    i += 1
    added_numbers = added_numbers + pc
    
    #print(added_numbers) #temporary only to see if working program

average = (added_numbers / 22) 
average = format(average, '.1f') 
print("Average = "+ str(average) + "%")
