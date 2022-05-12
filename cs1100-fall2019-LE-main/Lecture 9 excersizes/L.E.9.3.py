#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Sep 30 17:48:39 2019

@author: kaitlin
"""

#value = int(input("Enter a value (0 to end): "))
#print(value)

list1 = []

i = 1
while i > 0: 
    i = int(input("Enter a value (0 to end): "))
    print(i)
    #print(i)
    if i != 0:
        list1.append(i)
    
print("Min: " + str(min(list1)))
print("Max: " + str(max(list1)))
average = sum(list1)/len(list1)
print("Avg: " + str(format(average, '.1f')))
