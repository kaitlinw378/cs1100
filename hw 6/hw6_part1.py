#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Nov  6 19:45:32 2019

This program simulates an autocorrect. It takes a list of words and compares 
the words to a dictionary of common and correctly spelled english words. It 
also makes minor changes to a word in order to see if that is what was meant
as the correct spelling. The dictionary words, input words and results are 
printed out in grid format. 

@author: kaitlin
"""

def found(dictionary, inputfile):         
    if inputfile in dictionary:
        return inputfile
    else:
        return None
'''
Function found takes a dictionary of words as a set and a file as the parameters.
It then checks if each word in the file matches any of the words in the 
dictionary. 
'''
 
def drop(dictionary, inputfile): 
    word = []
    for l in range(len(inputfile)):
        new_word1 = inputfile[0:l] + inputfile[l+1:]
        if new_word1 in dictionary: 
            word.append(new_word1)    
    word = sorted(word)
    if len(word) > 0:
        return word[0]
    else:
        return None
'''
Function drop takes two parameters, the dictionary of words as a set and the 
file. It then removes a letter each time it iterates through a word to see if 
that word is in the dictionary and is the proper spelling of it.
'''
       
def swap(dictionary, inputfile): 
    words = [] 
    new = ''
    for l in range(len(inputfile) - 1):
        new = inputfile[0:l] + inputfile[l+1] + inputfile[l] + inputfile[l + 2:]        
        if new in dictionary: 
            words.append(new)
    words = sorted(words)
    if len(words) > 0:
        return words[0] 
    else:
        return None
'''
Function swap takes a dictionary (as a set) and a file as the parameters. It then
checks to see if a word from the file exists in the dictionary by switching the
position of two letters at a time in order to check if the altered word is correct.
'''
                     
def replace(dictionary, inputfile):
    letters = [ 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    replace_words = [] 
    for l in range(len(inputfile)): 
        for i in range(len(letters)): 
            new_word = inputfile[0:l] + letters[i] + inputfile[l+1:] 
            if new_word in dictionary: 
                replace_words.append(new_word)    
    replace_words = sorted(replace_words)
    if len(replace_words) > 0: 
        return replace_words[0] 
    else:
        return None
'''
Function replace takes a dictionary (as a set) and a file as parameters. It 
then checks to see if a word from the file matches any of the words from the 
dictionary by replacing a letter each time it iterates through the word with 
a different letter from the standard english alphabet. 
'''

def allwords(dictionary, inputfile):
    for l in fset:
        if(found(dset,l) != None):
            print ('{:<15} -> {:<15} {:}'.format(l, found(dset,l), ':FOUND'))
        elif (drop(dset,l) != None):
            print ('{:<15} -> {:<15} {:}'.format(l, drop(dset,l), ":DROP"))
        elif (swap(dset,l) != None):
            print ('{:<15} -> {:<15} {:}'.format(l, swap(dset, l), ':SWAP'))
        elif (replace(dset,l) != None):
            print ('{:<15} -> {:<15} {:}'.format(l, replace(dset, l), ':REPLACE'))
        else:
            print ('{:<15} -> {:<15} {:}'.format(l, l, ':NO MATCH'))
'''
Function allwords takes in the dictionary as a set and the input file as the 
parameters. It then iterates through all the previous functions and prints
out the word, the input word, and the result formated as a grid-type output. 
'''
    
if __name__ == '__main__':       
    dictionary_file = input("Dictionary file => ")
    print(dictionary_file) 
    #dictionary_file = dictionary_file + '.txt'
    
    input_file = input("Input file => ")
    print(input_file) 
    #input_file = input_file + '.txt'
    
    dset = set() 
    dfile = open(dictionary_file, 'r').readlines()
    for line in dfile: 
        line = line.rstrip('\n')
        dset.add(line) 
        
    dset = sorted(dset)
    
    fset = list()
    ifile = open(input_file, 'r').readlines() 
    for line2 in ifile:
        line2 = line2.rstrip('\n')
        fset.append(line2)
    
    allwords(dset, ifile)
