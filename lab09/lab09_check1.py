#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Nov  5 11:55:53 2019

@author: kaitlin
"""

L1 = [ 15.1, -12.1, 5.4, 11.8, 17.4, 4.3, 6.9 ]
#L1 = [ 15, -12, 5, 11, 17, 4, 6 ]


def closest1(flist):
    distance = abs(flist[0] - flist[1]) 
    minval1 = 0
    minval2 = 1
    for i in range(len(flist)): 
        for j in range(len(flist)): 
            if i < j: 
                if abs(flist[i] - flist[j]) < distance:
                    distance = abs(flist[i] - flist[j]) 
                    minval1 = i 
                    minval2 = j
    print(flist[minval1], flist[minval2]) 
    
closest1(L1) 
