#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Sep 25 17:16:14 2019

@author: kaitlin
"""
a = input("Please select operation -\n1. Add\n2. subtract\n3. Multiply\n4. Divide\nSelect operations from 1, 2, 3, 4 : ")

print(a)

num1 = int(input('Enter first number: '))
num2 = int(input('Enter second number: '))

if a == 1:
    number_final_1 = (num1 + num2)
    print('You chose to add numbers', num1, 'and', num2)
    print('The sum is:', number_final_1)
    
elif a == 2:
    number_final_2 = (num1 - num2)
    print('You chose to subtract the numbers', num1, 'and', num2)
    print('The difference is:', number_final_2)
    
elif a == 3:
    number_final_3 = (num1 * num2)
    print('You chose to multiply the numbers', num1, 'and', num2)
    print('The product is:', number_final_3)
    
elif a == 4: 
    number_final_4 = (num1 / num2)
    print('You chose to divide the numbers', num1, 'and', num2)
    print('The quotient is:', number_final_4)
    
else:
    print('Number out of range')


#removes all invisible characters l.strip() from left and right side of string
#\n is one character
#sum(a,b,c) - min(a,b,c)-max(a,b,c) find middle value of three numbers
#format statements: {} - default representation 
    #{:.2f} - floating point number with two decimal spaces 
    #{:3d} - integer format, 3 spaces total 
    #{:s} - string format, not used often

