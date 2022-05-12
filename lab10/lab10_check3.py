#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Nov 12 12:56:27 2019

@author: kaitlin
"""

from Date import Date

birthdays = []
for line in open('birthdays.txt'): 
    line = line.strip('\n')
    line = line.split(' ')  
    birthdays.append(line) 
    
dates = [] 
months = 13 *[0]
for line in birthdays: 
    d = Date(line[0],line[1],line[2]) 
    months[int(line[1])] += 1
    d = str(d)
    dates.append(d) 
    
dates = sorted(dates)
 
print()
print('earliest birthday:', dates[0]) 
print('latest birthday:', dates[-1]) 

most = max(months) 
for i in range(len(months)): 
    if months[i] == most: 
        print('month that has most birthdays', month_names[i]) 
        
        