#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Oct  9 10:14:28 2019

This program simulates the changes in population of an area occupied by bears.
The number of bears, number of tourists, and area of berry fields are all 
affected by one another. This program takes in user inputs of an initial amount
of bears and berries, calculates the outputs for the next 9 years (after the
first year) and prints it as a table. 
@author: kaitlin
"""
import math

def tourists(bears):
    if (bears < 4) or (bears> 15): 
        return 0
    elif 4 <= bears <= 10: 
        return 10000 * bears                 
    else: 
        return (100000) + ((20000 * (bears - 10)))
'''
Function tourists takes as an input the number of bears and calculates the
number of tourists that will come to the area based on that number. 
'''

def find_next(bears, berries, tourists):
    bears_next = berries/(50*(bears+1)) + bears*0.60 - (math.log(1+tourists,10)*0.1) 

    berries_next = (berries*1.5) - (bears+1)*(berries/14) - \
         (math.log(1+tourists,10)*0.05)

    if bears_next < 0: 
        bears_next = 0
    
    if berries_next < 0: 
        berries_next = 0 
    
    bears_next = int(bears_next)
    berries_next = float(berries_next)
    
    nxt = ((bears_next, berries_next))
    return nxt
'''
Function find_next takes as the current number of bears, berries, and 
tourists as an argument and calculates the number of bears for the next 
year and the number of berries for the next year. These values are stored
as a tuple. 
'''

def totals(bears_next, berries_next, people):
    m_bears = []
    m_berries = []
    m_people = []
    column1 = "Year" + " "*6
    column2 = "Bears" + " "*5
    column3 = "Berry" + " "*5
    column4 = "Tourists" + " "*2
    year = 1 
    print(column1 + column2 + column3 + column4)
    print("{:<10}{:<10}{:<10}{:<10}".format(year, bears, round(berries, 1), tourists(bears)))
    
    m_bears.append(bears)
    m_berries.append(berries)
    m_people.append(tourists(bears))
    
    year = 2
    while year <= 10:
        total = find_next(bears_next, berries_next, people) 
        bears_next = total[0] 
        people = tourists(bears_next) 
        berries_next = total[1]
        m_bears.append(bears_next)
        m_berries.append(berries_next)                     
        m_people.append(people)
        print("{:<10}{:<10}{:<10}{:<10}".format(year, bears_next, round(berries_next, 1), people))
        year += 1   
    print()
    print("{:<10}{:<10}{:<10}{:<10}".format("Min:", min(m_bears), format(min(m_berries), '.1f'), min(m_people)))
    print("{:<10}{:<10}{:<10}{:<10}".format("Max:", max(m_bears), format(max(m_berries), '.1f'), max(m_people)))
    
"""
Function totals takes the number of bears_next, berries_next and current
number of tourists as an argument and prints it as a table. It uses a 
while loop to print out the following years after the first one. 
"""
    
if __name__ == "__main__" :  
    bears = int(input("Number of bears => "))
    print(bears) 

    berries = input("Size of berry area => ")
    print(berries) 
    berries = float(berries)

    totals(bears, berries, tourists(bears))
