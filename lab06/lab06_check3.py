#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#"""
#Created on Tue Oct 15 13:38:08 2019
#
#@author: kaitlin
#"""

import lab06_util

bd = [ [ '1', '.', '.', '.', '2', '.', '.', '3', '7'],
       [ '.', '6', '.', '.', '.', '5', '1', '4', '.'],
       [ '.', '5', '.', '.', '.', '.', '.', '2', '9'],
       [ '.', '.', '.', '9', '.', '.', '4', '.', '.'],
       [ '.', '.', '4', '1', '.', '3', '7', '.', '.'],
       [ '.', '.', '1', '.', '.', '4', '.', '.', '.'],
       [ '.', '1', '7', '5', '.', '.', '.', '8', '.'],
       [ '2', '8', '.', '.', '4', '.', '.', '.', '6'] ]

#print(len(bd))
#print(len(bd[0]))
#print(bd[0][0])
#print(bd[8][8])

def print_board(board):
    line = " ".lstrip()
    i = 0
    for i in range(len(board)): 
        if 0 == (i % 3):
                line = line + ("-" * 25) + "\n"
        line = line + "| " 
        for j in range(len(board[i])):   
            line = line + board[i][j] + " "
            if (j + 1)%3 ==0:
                line = line + "| "
        if i != len(board)-1:
            line = line + "\n"
        
    print(line)
    print("-" * 25)

 

# if the number is already located at the exact spot, then this also will return true
def ok_to_add(row, column, number, board):
    if row < 0 or row > 8:
        print('Not a valid number') 
        return False
    elif column < 0 or column > 8:
        print("Not a valid number")
        return False
    elif number < 1 or number >9:
        print("Not a valid number")
        return False
    original_number=board[row][column]
    board[row][column]="."
#    if board[row][column] == str(number): 
#        return True
    
    #look at spaces in row
    for i in range(9):
        #if the space is a '.', then ignore it
        if board[row][i] == ".":
            continue 
        #if the space is not a '.', then we need to make sure that it's not already somewhere in the row
        elif int(board[row][i]) == number:
            print(i,row," False")
            board[row][column]=original_number
            return False
    
    #look at spaces in column
    for i in range(9):
        #if the space is a '.', then ignore it
        if board[i][column] == ".":
            continue
        
        #if the space is not a '.', then we need to make sure that it's not already somewhere in the column
        elif int(board[i][column]) == number:
            print("False")
            board[row][column]=original_number
            return False
    
    l1 = []  
    for i in range(3):
        for j in range(3):
            l1.append(board[row//3*3 + i][column//3*3 + j])
            
    for i in range(3):
        l1.append(board[row//3*3][column//3*3 + i])
        l1.append(board[row//3*3 + 1][column//3*3 + i])
        l1.append(board[row//3*3 + 2][column//3*3 + i])
    if str(number) in l1:
        print("False")
        board[row][column]=original_number
        return False
    
    board[row][column]=original_number
    return True

def verify_board(ptl_sol):
    #verify that there are no empty spaces on the board
    for i in range(9):
        for j in range(9):
            if ptl_sol[i][j] == '.':
                return False
    
    #verify each number in potential solution
    for i in range(9):
        for j in range(9):
            if not ok_to_add(i, j, int(ptl_sol[i][j]), ptl_sol):
#                print("It was not OK to add: row:%d  col:%d  number:%d"%(i,j, int(ptl_sol[i][j])))
                return False
    return True 
    

filename = input("What file do you want to open?")
path = "lab6Files/" + filename

potential_sol = lab06_util.read_sudoku(path)

print_board(potential_sol) 

while verify_board(potential_sol) != True:
    row = int(input("Enter a row "))
    print(row)

    column = int(input("Enter a column "))
    print(column)

    number = int(input("Enter a number "))
    print(number)

    if ok_to_add(row, column, number, potential_sol):
        potential_sol[row][column] = str(number) 
    print_board(potential_sol) 
       

##is potential_sol a valid board?
#is_valid_sol = verify_board(potential_sol)  
#
#if is_valid_sol:
#    print("Yay it's valid!")
#else:
#    print(":( it's not valid.")
##
#row = int(input("Enter a row "))board.txt
    
#print(row)
#
#column = int(input("Enter a column "))
#print(column)
#
#number = int(input("Enter a number "))
#print(number)
#
#is_ok_to_add = ok_to_add(row, column, number)
#
#if (is_ok_to_add):
#    print("It's valid!")
#else:
#    print("It's not valid!")

print("Done!")
'''
file = input("Enter a file name: ")
print(file)

lab06_util.read_sudoku(file)
'''