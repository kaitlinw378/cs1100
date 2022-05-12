#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Oct  8 14:37:13 2019

This program simulates a pokemon moving across a board and interacting with
other pokemons. It takes in multiple user inputs which are the number of turns
that the user wants to play, the name of the pokemon, how often the pokemon
runs into others, and the directions that the pokemon travels in. The number of
wins, losses, no interactins are stored in a list and printed along with the 
coordinates of the pokemon. 

@author: kaitlin
"""

def move_pokemon(coordinates, direction, steps): 
    row = coordinates[0]
    column = coordinates[1]
    direction = direction.lower()
    if direction == "w": 
        new_col = column - steps 
        if new_col < 0:
            new_col = 0
        return (row, new_col)
    elif direction == "e":
        new_col = column + steps
        if  new_col > 150:
            new_col = 150
        return (row, new_col)
    elif direction == "n":
        new_row = row - steps
        if new_row < 0:
            new_row = 0
        return (new_row, column)
    elif direction == "s":
        new_row = row + steps
        if new_row > 150:
            new_row = 150
        return (new_row, column)
    else: 
        return (row,column)
'''
Function move_pokemon takes coordinates, direction and steps as input. The 
coordinates are stored as a tuple. It then calculates where the pokemon will
moved based on a user input of north, south, east, or west. 
'''

if __name__ == "__main__":
    num_turns = int(input("How many turns? => "))
    print(num_turns)
    
    name = input("What is the name of your pikachu? => ")
    print(name)
    
    see_other = int(input("How often do we see a Pokemon (turns)? => "))
    print(see_other)
    print()
    
    i = 1 
    current_x = 75
    current_y = 75
    turns = 1
    variable = see_other
    print("Starting simulation, turn 0 {} at ({}, {})".format(name, str(current_x), str(current_y)))
    record = []
    while i <= num_turns: 
        direction = input("What direction does {} walk? => ".format(name))
        print(direction)
        new_cord = move_pokemon((current_x, current_y), direction, 5) 
        current_x = new_cord[0]
        current_y = new_cord[1] 
        current_turn = str(i)  
        if turns == see_other : 
            see_other = see_other + variable
            print("Turn", current_turn + ", " +str(name), "at","("+ str(current_x) + ", " + str(current_y) + ")")
            battle = input("What type of pokemon do you meet (W)ater, (G)round? => " )
            print(battle)
            battle = battle.upper()         
            if battle == "G":  
                record.append('Lose')
                direction = direction.lower()
                if direction == "e": 
                    current_y -= 10
                    if current_y > 150:
                        current_y = 150
                elif direction == "w" :
                    current_y +=10 
                    if current_y < 0:
                        current_y = 0
                elif direction == "n":
                    current_x += 10 
                    if current_x > 150: 
                        current_x = 150
                elif direction == "s": 
                    current_x -= 10    
                    if current_x < 0:
                        current_x = 0
                print("{} runs away to ({}, {})".format(name, current_x, current_y))         
            elif battle == "W":
                record.append('Win')
                direction = direction.lower()
                if direction == "e": 
                    current_y += 1
                    if current_y < 0:
                        current_y = 0
                if direction == "w":
                    current_y -= 1
                    if current_y > 150:
                        current_y = 150
                if direction == "n":
                    current_x -= 1
                    if current_x < 0:
                        current_x = 0
                if direction == "s":
                    current_x += 1  
                    if current_x > 150:
                        current_x = 150
                print("{} wins and moves to ({}, {})".format(name, current_x, current_y))
            else:
                record.append("No Pokemon") 
        i += 1
        turns += 1
        
    print("{} ends up at ({}, {}), Record: {}".format(name, str(current_x), str(current_y), record))
