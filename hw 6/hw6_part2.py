#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Nov  8 15:34:13 2019

This program sorts through sets of Harry Potter movie data and prints out
the name of the title that relates to what a user inputs and then shows the
beasts that appear in that movie. It also prints the other movies that have
similar beasts in common. 

@author: kaitlin
"""
import textwrap 

while True: 
    title = input('Enter a title (stop to end) => ')
    print(title) 
    print() 
    
    if title == 'stop':
        break 
    
        
    else: 
        word = []
        words = []
    
        for line in open('titles.txt'):
            line = line.strip('\n') 
            word.append(line)
        for l in word: 
            w = l.split('|')     
            words.append(w)
            
        allwords = {d[0]:d[1:] for d in words} 
        
        x = None
        for lists in words: 
            for j in lists: 
                if title.lower() in j.lower(): 
                    
                    x = lists[0] 
                    lists.pop(0) 
                    print("Found the following title: " + (x))
                    new = sorted(lists) 
                    if x in new:
                        new.remove(x) 
                    fstring = ', '.join(new) 
                    fstring = ('Beasts in this title: ' + fstring) 
                    fs = textwrap.wrap(fstring)
                    for char in fs:
                        print(char)
                        
                    
                    
        if x is None:
            print('This title is not found!') 
            
        else:
            print()
            
            allwords.pop(x)
            movietitles = []
            for key in allwords: 
                if any(i in new for i in allwords[key]):
                    movietitles.append(key)
            movietitles = sorted(movietitles) 
            
            nstring = ', '.join(movietitles)
            nstring = ("Other titles containing beats in common: " + nstring )
            ns = textwrap.wrap(nstring)
            for char in ns:
                print(char)
    
            print()
                    
            onlytitle = set(new) 
            
            nobeasts = set() 
            for key in allwords:
                for i in allwords[key]:
                    nobeasts.add(i) 
                    
            diffmovies = onlytitle.difference(nobeasts) 
            diffmovies = list(diffmovies)
            diffmovies = sorted(diffmovies)
            
            tstring = ', '.join(diffmovies)
            tstring = ('Beasts appearing only in this title: ' + tstring)
            ts = textwrap.wrap(tstring)
            for char in ts:
                print(char)        
            