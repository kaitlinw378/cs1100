#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Nov  5 12:37:41 2019

@author: kaitlin
"""
import time
import random

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

if __name__ == '__main__':
    L1 = [] 
    for i in range(0, 10000): 
        L1.append(random.uniform(0.0, 1000.0))
    start = time.time()
    closest1(L1) 
    end = time.time() 
    
    total = end - start
    print(total) 
    
    start1 = time.time()
    closest2(L1)
    end1 = time.time()
    total2 = end1 - start1 
    print(total2)