#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Oct  7 20:03:24 2019

@author: kaitlin
"""
hd = int(input("Enter Dale's height: "))
print(hd)

he = int(input("Enter Erin's height: "))
print(he)

hs = int(input("Enter Sam's height: "))
print(hs)

if (hd > he) and (hd > hs): 
        print("Dale") 
        if he > hs:
            print("Erin")
            print("Sam")
        else: 
            print("Sam")
            print("Erin")
elif (he > hd) and (he > hs): 
        print("Erin")
        if hd > hs:
            print("Dale")
            print("Sam")
        else: 
            print("Sam")
            print("Dale")
elif (hs > hd) and (hs > he): 
        print("Sam")
        if he > hd: 
            print("Erin")
            print("Dale")
        else: 
            print("Dale")
            print("Erin")
