#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Oct  3 14:33:52 2019

@author: kaitlin
"""

co2_levels = [ 320.03, 322.16, 328.07, 333.91, 341.47, \
               348.92, 357.29, 363.77, 371.51, 382.47, 392.95 ]

p = float(input("Enter the fraction: "))
print(p)

def increase(co2_levels):
    for i in range(len(co2_levels)):
        co2_levels[i] = (co2_levels[i] * (1 + p))
        #co2_levels[i] = co2_levels
        
increase(co2_levels)

print('First: {:.2f}'.format(co2_levels[0]))
print('Last: {:.2f}'.format(co2_levels[-1]))
