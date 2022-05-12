#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Sep 17 12:51:18 2019

@author: kaitlin
"""

first= input("Please enter your first name: ")
print(first)
last = input("Please enter your last name: ")
print(last)

greeting = "Hello,"

number = max(len(first), len(last) + 1, len(greeting)) 
#total = number + 6
total = number + 6
print("*" * (total))
second = total - 5 - len(greeting)
third = total - 5 - len(first)
fourth = total - 5 - len(last)-1
print("*"*2 + " "+ greeting + " " * second + "*"*2)
#print("*"*2,greeting," " * (number - len(greeting) - 1), "*"*2)
print("*"*2 + " " + first + " " * third + "*"*2 )
#print("*"*2,first," " * (number - len(first) -1),"*"*2)
print("*"*2 + " " + last + "!" + " " * fourth + "*"*2)
#print("*"*2,last +"!", " "* (number - len(last) -2),"*"*2)
print("*"+len(greeting)*"*" +"*"*6)
