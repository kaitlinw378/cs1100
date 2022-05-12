#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Sep 12 21:40:45 2019

@author: kaitlin
"""

def convert2fahren(celcius):
    fahrenheit = (celcius*(9/5)+32)
    return fahrenheit

print("0 -> ",convert2fahren(0))
print("32 ->",convert2fahren(32))
print("100 ->",convert2fahren(100))

