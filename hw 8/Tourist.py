#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Dec 11 20:49:38 2019

@author: kaitlin
"""

import json

class Tourist(object):
    
    def __init__(self,other):
        for i in self: 
            for j in i: 
                x = j.x 
                y = j.y 
        return (x, y)
    
    def __str__(self):
        
        
        
        pass
    
if __name__ == '__main__':
    with open('bears_and_berries_1.json') as i :
       i = json.load(i) 
    
    b = Tourist(i)
    
    print(b)
    