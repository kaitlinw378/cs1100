#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Sep 19 17:46:13 2019

@author: kaitlin
"""

def add_tuples(x,y,z):
    x_values = ((x[0] + y[0] + z[0]))
    y_values = ((x[1] + y[1] + z[1]))
    return(x_values, y_values)
    print((x_values, y_values))
    
print(add_tuples( (1,4), (8,3), (14,0) ))
print(add_tuples( (3,2), (11,1), (-2,6) ))
