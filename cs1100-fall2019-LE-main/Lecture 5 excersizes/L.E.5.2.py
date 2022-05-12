#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Sep 12 21:44:45 2019

@author: kaitlin
"""

def frame_string(words):
    print(len(words)*"*" + "*"*6)
    print("*"*2, words, "*"*2)
    print(len(words)*"*" + "*"*6)
    
frame_string("Spanish Inquisition")
print(" ")
frame_string("Ni")