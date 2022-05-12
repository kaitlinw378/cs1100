#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Oct 29 00:12:48 2019

This program simulates a pokemon trainer moving a random direction. It has 3
user inputs which are the size of the baord, a number of trues and a number
of falses. The program then simulates which direction was randomly selected
along with which random number was chosen to be the value. It then prints out
the function 5 times and shows when the trues and falses were selected. 

@author: kaitlin
"""
import random

def move_trainer(): 
    directions = ['N', 'E', 'S', 'W']
    print("Directions: " + str(directions))
    print("Selected " + str(random.choice(directions)) + ", value " +\
          str(format(random.random(), '.2f')))
'''
Function move_trainer assigns four directions to a list and then randomly 
selects a direction and a value. It prints the results as a string. 
'''

def throw_pokeball(num_false, num_true):
    boolean_list = []
    i = 0 
    while i < num_false:
        boolean_list.append("False")  
        i += 1
    j = 0 
    while j < num_true:
        boolean_list.append("True")
        j += 1     
    k = 0 
    while k < 5:
        print("Booleans: [{}]".format(', '.join(map(str, boolean_list))))
        print("Selected " + random.choice(boolean_list))
        k += 1
'''
Function throw_pokeball takes two inputs which are the number of falses and 
the number of trues. It stores these in a list that is then printed out 
followed by the randomly selected True or False choice. This continues until 
the number input by the user has been reached. 
'''
        
if __name__ == "__main__":
    grid_size = int(input("Enter the integer grid size => "))
    print(grid_size)
    falses = int(input("Enter the integer number of Falses => "))
    print(falses)
    trues = int(input("Enter the integer number of Trues => "))
    print(trues) 
    
    seed = 11 * grid_size 
    print("Setting seed to " + str(seed))
    seed = random.seed(seed) 
    
    move_trainer()
    move_trainer()
    move_trainer()
    move_trainer()
    move_trainer()
    throw_pokeball(falses, trues) 
    