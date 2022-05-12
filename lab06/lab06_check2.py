#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Oct 15 12:39:35 2019

@author: kaitlin
"""

bd = [ [ '1', '.', '.', '.', '2', '.', '.', '3', '7'],
       [ '.', '6', '.', '.', '.', '5', '1', '4', '.'],
       [ '.', '5', '.', '.', '.', '.', '.', '2', '9'],
       [ '.', '.', '.', '9', '.', '.', '4', '.', '.'],
       [ '.', '.', '4', '1', '.', '3', '7', '.', '.'],
       [ '.', '.', '1', '.', '.', '4', '.', '.', '.'],
       [ '4', '3', '.', '.', '.', '.', '.', '1', '.'],
       [ '.', '1', '7', '5', '.', '.', '.', '8', '.'],
       [ '2', '8', '.', '.', '4', '.', '.', '.', '6'] ]

print(len(bd))
print(len(bd[0]))
print(bd[0][0])
print(bd[8][8])


line = " ".lstrip()
i = 0
for i in range(len(bd)):     
    if 0 == (i % 3):
            line = line + ("-" * 25) + "\n"
    line = line + "| " 
    for j in range(len(bd[i])):   
        line = line + bd[i][j] + " "
        if (j + 1)%3 ==0:
            line = line + "| "
    if i != len(bd)-1:
        line = line + "\n"
    
print(line)
print("-" * 25)

l1 = []   
def ok_to_add(row, column, number):
    if row < 0 or row > 9:
        print('Not a valid number')
    elif column < 0 or column > 9:
        print("Not a valid number")
    elif number < 0 or number >9:
        print("Not a valid number")
    for i in range(9):
        if bd[row][i] == number:
            print("False")
        if bd[i][column] == number:
            print("False")
    for i in range(3):
        l1.append(bd[row//3*3][column//3*3 + i])
        l1.append(bd[row//3*3 + 1][column//3*3 + i])
        l1.append(bd[row//3*3 + 2][column//3*3 + i])
    if str(number) in l1:
        print("False")
    else:
        print("True")



row = int(input("Enter a row "))
print(row)

column = int(input("Enter a column "))
print(column)

number = int(input("Enter a number "))
print(number)

ok_to_add(row, column, number)