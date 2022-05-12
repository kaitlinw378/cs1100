#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Sep 16 19:26:11 2019

@author: kaitlin
"""

number1 = input("Enter the first number: ")
print(number1)
number1 = float(number1)
number2 = input("Enter the second number: ")
print(number2)
number2=float(number2)
average = ((number1 + number2)/2)


if number1 > 10 and number2 > 10:
    print("Both are above 10.")
elif number1 < 10 and number2 < 10:
    print("Both are below 10.")
    
print("Average is {:.2f}".format(average))
