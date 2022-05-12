#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Oct 29 15:28:40 2019

This program simulates a pokemon trainer moving around a board. It takes two 
user inputs which are the grid size and a probability. It uses these values to 
show if the trainer catches any pokemons on the journey around the board. The 
function prints out the location that it saw a pokemon and which turn it was. 
It also prints if the pokemon was caught or missed and states the totals at the 
end.

@author: kaitlin
"""
import random

def move_trainer(): 
    directions = ['N', 'E', 'S', 'W']
#    print("Directions: " + str(directions))
#    print("Selected " + str(random.choice(directions)) + ", value " +\
#          str(round(random.random(),2)))
    direction = random.choice(directions)
    probability = random.random()
    return (direction, probability)
'''
Function move_trainer assigns four possible directions in a list. It chooses 
a random direction and a random number for the probability and returns a tuple.
'''

def throw_pokeball(num_false, num_true):
    outputs = [False] * num_false + [True] * num_true 
    return random.choice(outputs)
'''
Function throw_pokeball takes two inputs which are a number of falses and a 
number of trues. It stores these in a list and returns a random selection 
from the list. 
'''
    
def boundaries(): 
    if y == 0 or x == 0:
        return True 
    elif y == grid_size -1 or x == grid_size -1:
        return True
    else:
        return False
'''
Function boundaries checks if the trainer is staying within the dimensions of 
the board. It only returns true or false values. 
'''

if __name__ == "__main__":
    grid_size = int(input("Enter the integer grid size => ")) 
    print(grid_size) 
    probability = (input("Enter a probability (0.0 - 1.0) => "))
    print(probability) 
    probability = float(probability)
    
    random.seed(11 * grid_size)
    
    start_pos = [grid_size//2, grid_size//2]
    y = start_pos[0]
    x = start_pos[1] 
    num_false = 3
    num_true = 1 
    
    caught = 0
    encount = 0
    turns = 1    
    while __name__ == "__main__":      
        if boundaries() is True: 
            print("Trainer left the field at turn " + str(turns-1)  + \
                  ", location " + str((x, y)) +'.')
            print(str(encount) + " pokemon were seen, " + str(caught) + " of which were captured.")
            break
        else:
            movement = move_trainer() 
            direction = movement[0] 
            if direction == "N":
                x -=1
            elif direction == "E": 
                y +=1 
            elif direction == "S": 
                x += 1
            elif direction == "W":
                y -=1        
            prob = movement[1] 
            if prob <= probability: 
                encount += 1 
                print("Saw a pokemon at turn " + str(turns) + ", location " + str((x,y)))
                if throw_pokeball(num_false, num_true) is True:             
                    print("Caught it!") 
                    num_true += 1
                    caught += 1                  
                else: 
                    print("Missed ...")
        turns += 1        
                 