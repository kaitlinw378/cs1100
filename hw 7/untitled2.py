#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Nov 14 16:03:19 2019

@author: kaitlin
"""

letters = [ 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

dictfile = open('words_10percent.txt').readlines() 
dictfile = [i.strip().split(',') for i in dictfile]
namedict = {yolo[0]:yolo[1] for yolo in dictfile}

keyfile = open('keyboard.txt').readlines() 
keyfile = [i.strip() for i in keyfile]
letterdict = {letter[0]:letter[1:] for letter in keyfile}

input_file = 'input_words.txt'
input_file = open(input_file).read().strip().split('\n') 

word = 'agew'

for letter in range(len(word)): 
    for i in letterdict[word[letter]]: 
        words = word[0:letter] + i + word[letter+1:]
        if words in namedict:
            print('{:<15} -> {:<15} :REPLACE'.format(word, words))
    
    
    
    
    
#    wordlist = list(word) 
#    let = word[letter+1]  
#    wordlist[letter +1] = wordlist[letter] 
#    wordlist[letter] = let 
#    dropword = ''.join(wordlist)
#    if dropword in namedict:
#        print(dropword) 
#       
        
    