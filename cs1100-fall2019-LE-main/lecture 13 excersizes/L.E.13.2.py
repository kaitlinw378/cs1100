#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Oct 18 11:45:07 2019

@author: kaitlin
"""




scores = input("Enter the scores file: ")
print(scores)

output = input("Enter the output file: ")
print(output)

s = open(scores)
s1 = s.read()

sl = s1.split() 
for i in range(len(sl)):
    sl[i] = int(sl[i])
    
new_scores = sorted(sl) 
new_file = open(output, 'w')

for i in range(len(new_scores)):
    new_file.write("{0:>2d}: {1:>3d}\n".format(i, new_scores[i]))

new_file.close() 

