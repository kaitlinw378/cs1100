#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Oct 30 20:44:47 2019

This program simulates a pokemon trainer moving around a board and catching 
pokemon. It prints a table of values of the likelihood of catching it based 
on the number of simulations that is input by the user. It then prints out
the average number of turns per simulation, max and min of the number of 
turns and the highest and lowest amount of misses by the trainer. 

@author: kaitlin
"""
import random

def move_trainer(): 
    directions = ['N', 'E', 'S', 'W']
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
    
def boundaries(x, y): 
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
    
def run_one_simulation(grid, prob):
    start_pos = [grid_size//2, grid_size//2]
    y = start_pos[0]
    x = start_pos[1] 
    num_false = 3
    num_true = 1
    
    
    missed = 0
    encount = 0
    caught = 0
    turns = 0    
    while __name__ == "__main__":    
        if boundaries(x,y) is True:        
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
                if throw_pokeball(num_false, num_true) is True:     
                    num_true += 1
                    caught += 1              
                    count_grid[x][y] +=1 
                else:
                    missed +=1
                    count_grid[x][y] -=1                  
            turns += 1   
    return turns 
'''
Function run_one_simulation takes two parameters which are the grid size and
the probability. It runs through the simulation one time, collecting and 
storing the values of caught, turns, missed, encountered. 
'''

if __name__ == '__main__':  
    grid_size = int(input("Enter the integer grid size => ")) 
    print(grid_size) 
    probability = input("Enter a probability (0.0 - 1.0) => ")
    print(probability) 
    probability = float(probability)
    sim_num = int(input("Enter the number of simulations to run => "))
    print(sim_num)
    print()
    
    count_grid = []
    for i in range(grid_size):
        count_grid.append([0] * grid_size ) 
    
    random.seed(11 * grid_size)
    
    start_pos = [grid_size//2, grid_size//2]
    y = start_pos[0]
    x = start_pos[1] 
    num_false = 3
    num_true = 1

    avg_list =  []
    for i in range(sim_num):             
        turns = run_one_simulation(count_grid, probability) 
        avg_list.append(turns) 
        
    for line in count_grid:
        for l in line:
            print('{:5d}'.format(l), end = '')
        print()
               
    total = sum(avg_list) 
    avg = total / sim_num
    
    min_turns = min(avg_list)
    max_turns = max(avg_list) 
    
    min_index = avg_list.index(min(avg_list)) + 1
    max_index = avg_list.index(max(avg_list)) + 1
    
    max_like = max(count_grid)
    min_like = min(count_grid)
    
    nets = []
    for line in count_grid:
        for integer in range(grid_size):
            nets.append(line[integer])
    
    print("Average number of turns in a simulation was {:.2f}".format(avg))
    print("Maximum number of turns was {} in simulation {}".format(max_turns, max_index))
    print("Minimum number of turns was {} in simulation {}".format(min_turns,min_index))
    print("Best net missed pokemon versus caught pokemon is {}".format(max(nets)))
    print("Worst net missed pokemon versus caught pokemon is {}".format(min(nets)))
      