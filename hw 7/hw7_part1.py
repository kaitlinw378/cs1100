#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Nov 14 15:39:22 2019

This program simulates an improved autocorrect that has a new function to 
suggest words based off of nearby characters. It prints out a list of words 
that have been corrected or not found based on the original ones. 

@author: kaitlin
"""

letters = [ 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

dictfile = input("Dictionary file => ") 
print(dictfile)
dictfile = open(dictfile).readlines()
dictfile = [i.strip().split(',') for i in dictfile]
namedict = {yolo[0]:yolo[1] for yolo in dictfile} 
names = dict()

inputf = input('Input file => ')
print(inputf)
input_file = open(inputf).read().strip().split('\n') 

keyfile = input('Keyboard file => ')
print(keyfile)
#keyfile = open(keyfile).readlines() 
keydict = dict() 
for line in open(keyfile):
    keyline = line.split(' ') 
    l1 = [] 
    for j in range(len(keyline) - 1): 
        l1.append(keyline[j+1].strip() )
        
    keydict[keyline[0]] = l1
    
    

def drop(word):
    for letter in range(len(word.strip())): 
        dropword = ''
        dropword = word[0:letter] + word[letter + 1:]
        if dropword.strip() in namedict: 
            wordlist.append([namedict[dropword.strip()], dropword.strip()])
'''
Function drop suggests words based on removing a letter to see if any matches 
occure
'''

def insert(word):
    word = word + ' '
    for letter in range(len(word)):    
        for i in letters:   
            dropword = ''
            dropword = word[0:letter] + i + word[letter:]
            if dropword.strip() in namedict: 
                wordlist.append([namedict[dropword.strip()], dropword.strip()])
'''
Function insert suggests words based on adding a letter from the alphabet 
inside of the word to find matches.
'''                
            
def swap(word):
    for letter in range(len(word)-1): 
        new = word[0:letter] + word[letter + 1] + word[letter] + word[letter + 2:]
        if new in namedict:
            wordlist.append([namedict[new], new])      
'''
Function swap switches the position of two letters in the wrod to see if there 
are any matches in the english dictionary
'''
            
def replace(word):        
    for letter in range(len(word.strip())): 
        for i in keydict[word.strip()[letter]]: 
            words = word[0:letter] + i + word[letter+1:]
            if words.strip() in namedict:
                wordlist.append([namedict[words.strip()], words.strip()])  
'''
Function replace takes from a list of nearby characters to see if there are 
any mistakes that have been made by accidently clicking a letter nearby
'''


if __name__ == '__main__':
    for word in input_file: 
        wordlist = []
        
        if word in namedict: 
            print('{:<15} -> {:<15} :FOUND'.format(word, word))
            
        else: 
            drop(word)
            insert(word)
            swap(word)
            replace(word)
            
            lol = [] 
            for i in wordlist: 
                if i not in lol: 
                    lol.append(i) 
            wordlist = lol
            
            count = 1 
            
            wordlist = sorted(wordlist, reverse = True) 
            if len(wordlist) > 0:
                for i in wordlist[:3]: 
                    print('{:<15} -> {:<15} :MATCH {}'.format(word, i[1], count)) 
                    count +=1
            else:
                
                print('{:<15} -> {:<15} :NO MATCH'.format(word, word)) 
            
            