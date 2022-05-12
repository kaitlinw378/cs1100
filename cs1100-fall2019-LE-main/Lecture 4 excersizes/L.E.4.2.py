#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Sep 12 20:44:21 2019

@author: kaitlin
"""
r_1 = 5 
r_2 = 32 
pi = 3.14159
area_circle_1 = pi * r_1**2
area_circle_2 = pi * pow(r_2, 2)
area1 = "Area 1 = {:.2f}".format(area_circle_1)
print(area1)
print("Area 2 =", round(area_circle_2, 2))