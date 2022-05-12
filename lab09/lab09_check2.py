#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Nov  5 12:27:23 2019

@author: kaitlin
"""

def closest2(flist):
    new_list = flist.copy()
    new_list.sort() 
    distance = abs(new_list[0] - new_list[1]) 
    minval1 = 0
    minval2 = 1
    for i in range(len(new_list) - 1): 
        if abs(new_list[i] - new_list[i + 1]) < distance:
                    distance = abs(new_list[i] - new_list[1]) 
                    minval1 = i 
                    minval2 = i + 1
    
    print(new_list[minval1], new_list[minval2])
    
L1 = [ 15.1, -12.1, 5.4, 11.8, 17.4, 4.3, 6.9 ]
closest2(L1)
