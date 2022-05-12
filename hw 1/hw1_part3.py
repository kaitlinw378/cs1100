#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Sep 17 21:00:33 2019

This programs takes three user inputs(a character, a height, a width) and creates
a box with the box dimensions centered perfectly inside if it is odd, 
and in the middle(+ or -) 1 if it is even. 

@author: kaitlin
"""
character = input("Enter frame character ==> ")
print(character)

height = int(input("Height of box ==> "))
print(height)

width = int(input("Width of box ==> "))
print(width)
print()

first = int(width)

top_space = ((int(width) - 2)* " ")

vertical = int((int(height-2) // 2))
vertical_remainder = int((int(height-2) % 2))

statement = str((str(width)+"x"+str(height)))

horizontal = int((width-2) - len(statement))
horizontal_remainder = int(horizontal // 2)
spaces_left = (horizontal - horizontal_remainder)
final_statement = (character +horizontal_remainder*" " + statement + spaces_left*" " + character)

print("Box:")
print(character * first) 
print((((character +top_space + character+"\n")*(vertical + vertical_remainder -1) ) + (final_statement+"\n"))+((character+top_space+ character+"\n")*(vertical_remainder-1)), end = "")
print((character +top_space + character +"\n")*vertical, end = ""  ) 
print(character * first)
