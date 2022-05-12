#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Oct 28 19:57:53 2019

@author: kaitlin
"""

def get_words(description): 
    description = ''.join(description)
    description = description.replace('|', ' ').replace(',', ' ').replace('.', ' ').replace('(', ' ').replace(')', ' ').replace('"', ' ') 
    description = description.lower()
    words = description.split(' ')
    
    list1 = []
    for word in words:
        if word.isalpha() and (len(word) >= 4):    
            list1.append(word)     
    list1.pop(0)        
    return list1
  
filename = input("Enter filename: ")
with open(filename) as f:
    description = f.readlines()
    print(get_words(description))
    
print(len(get_words(description)))