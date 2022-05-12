#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Nov 30 15:26:45 2019

@author: kaitlin
"""
import json

class BerryField(object):
    
    def __init__(self, other):
        self.vals = other["berry_field"]
    
    def __str__(self):
        totals = 0 
        for i in self.vals:         
            totals += sum(i)
        print('Field has {} berries.'.format(totals))
        
        line = ''
        for i in self.vals:
            for j in i:        
                line = line + '{:>4}'.format(j)
            line = line + '\n'
        
        return line
        
    def grow():
        
        
        pass
    
    

if __name__ == '__main__':
    with open('bears_and_berries_1.json') as i :
       i = json.load(i) 
    
    berryf = BerryField(i) 
    
    
    print(berryf)
    
    