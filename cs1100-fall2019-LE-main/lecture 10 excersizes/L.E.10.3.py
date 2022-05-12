#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Oct  3 14:24:09 2019

@author: kaitlin
"""

co2_levels = [ 320.03, 322.16, 328.07, 333.91, 341.47, \
               348.92, 357.29, 363.77, 371.51, 382.47, 392.95 ]

average_nums = []

avg = ((sum(co2_levels)) / (len(co2_levels)))

for co2_level in co2_levels:
    if co2_level > avg:
        average_nums.append(co2_level)

print("Average: " + str(format(avg, '.2f')))
print("Num above average: " + str(len(average_nums)))
