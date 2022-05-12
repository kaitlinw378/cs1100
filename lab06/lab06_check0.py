#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Oct 14 15:16:56 2019

@author: kaitlin
"""
line = " ".lstrip()
x = 0
y = 0
for x in range(0,9):
    for y in range(0,9):
        line = line + str(x) + "," + str(y) + " "
        if y == (2) or y == 5:
            line = line + " "
        if y == 8:
            line = line + " \n"
    if x == (2) or (x == 5):
        line = line + " \n"
 
print(line)
      
row = int(input("row: "))
print(row)

row_line = " ".lstrip()

for x in range(row):
    for y in range(0,9):
        row_line = row_line + str(row) + "," + str(y) + " "
    if y == 8:
        break
    
print(row_line)
    
column = int(input("column: "))
print(column)

column_line = " ".lstrip()

for y in range(column):
    for x in range(0,9):
        column_line = column_line + str(x) + "," + str(column) + " "
    if x == 8:
        break
    
print(column_line)
print()

tbt = " ".lstrip()

for x in range(0,3):
    for y in range(0,3):
        tbt = tbt + str(x) + "," + str(y) + " "
        if y == 2:
            tbt = tbt + "\n"
        if x == 3:
            break

print(tbt)