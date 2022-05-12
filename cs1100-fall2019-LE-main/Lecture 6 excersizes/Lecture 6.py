# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
chris_height = float(input("Enter Chris's height (in cm): "))
sandy_height = float(input("Enter Sandy's height (in cm): "))
if chris_height > sandy_height:
    print("Chris is taller")
else:
    print("Sandy is taller")

"""
ways to convert integers, floats and strings to booleans: 
"""

x = 5<3
#will output false on the variable 

if x == False: 
    print("f")
    
if not x: 
    print("f")

x = 17 
y = 15.1 

x < y 
#returns false 

x<=y 
#returns false

y< y 
#return false

y<=y
#returns true

s1 = "art"
s2 = "Art"
s3 = "Music"
s4 = "music" 

s1<s2
#Out[8]: False

s1<=s2
#Out[9]: False

s1
#Out[10]: 'art'

s2
#Out[11]: 'Art'

s1>s2
#Out[12]: True

"""
using ASCII table, capitals comee first so lower case a is larger than upper
case A. 
"""

s1.lower()<= s2.lower()

#lexicographical ordering(?) 

s4 != s2 
#is not not equal (they are equal). Returns true if the two things are different

name1 = "Dale"
print("Enter the height of", name1, "in cm ==> ", end='')
height1 = int(input())

name2 = "Erin"
print("Enter the height of", name2, "in cm ==> ", end='')
height2 = int(input())

if height1 < height2:
    print(name2, "is taller")
    max_height = height2

if height1 >= height2:
    print(name1, "is taller")
    max_height = height1

print("The max height is", max_height)

 