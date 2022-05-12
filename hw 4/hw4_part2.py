#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Oct 16 10:18:20 2019

This program takes three user inputs which are the name of a university,
a number(index) that will be compared and a second number(index) that will
be compared. It then reads this data and prints it out in the form of a table.

@author: kaitlin
"""
import hw4_util

def right_justify(pad_amt, the_str):
    padding_string = "{0:>" + str(pad_amt) + "}"
    return padding_string.format(the_str)
'''
Function right_justify takes two parameters which are a padding amount and a 
string to print out the string with the certain numbre of spaces before it is 
printed. It returns the string. 
'''

def find_university(university_name, data):
    for d in range(len(data)):
        if data[d][0] == university_name:
            return d 
    return -1
'''
Function get_index finds the index of the university name that was input by the
user. If the name is not found, it returns -1.
'''
            
def print_data(yours_rank, first_rank, second_rank, data): 
    yours = data[yours_rank]
    first = data[int(first_rank)]
    second = data[int(second_rank)]
    
    print("First university: " + first[0])
    print("Second university: " +second[0])
    print()
    the_string = right_justify(25, '') + right_justify(12, "First") + \
        right_justify(12, "Second") + right_justify(12, "Yours")
    print(the_string)
    
    for i in range(1, len(data[0])):
        the_string = right_justify(25, data[0][i]) + right_justify(12, first[i]) + \
            right_justify(12, second[i]) + right_justify(12, yours[i])
        print(the_string)
'''
Function print-stats takes in four inputs. The first three are the user inputs
from the beginning of the function. The last one is the data that is read from 
the imported module. It prints out the header string and then loops over the 
data list to print out the coresponding information based off the index of the
data provided by the user. 
'''

if __name__ == "__main__":
    data = hw4_util.read_university_file("university_data.csv")
    
    uname = input("University name => ")
    print(uname)
    
    first_name = input("Line number for first university to compare (1-1000) => ")
    print(first_name)
    
    second_name = input("Line number for second university to compare (1-1000) => ")
    print(second_name)
    
    index = find_university(uname, data)
    
    if index == -1:
        print("University not found")
    else: 
        print_data(index, first_name, second_name, data)
