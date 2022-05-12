#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Dec  2 21:29:08 2019

@author: kaitlin
"""

def add(m,n):
    if n == 0:
        return m
    else:
        return add(m,n-1) + 1
    
def mult(m,n):
    if n == 1: 
        return m
    else: 
        return add(mult(m,n-1), m) 

def power(x,n):
    if n == 0:
        return 1
    else: 
        return mult(power(x,n-1), x)
    
print(add(5,3))
print(mult(8,3))
print(power(6,3))

'''
THX
'''
