#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Nov  7 16:58:58 2019

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
                    if x in lists:
                        lists.remove(x)
                    fstring = ', '.join(new) 
                    fstring = ('Beasts in this title: ' + fstring) 
                    fs = textwrap.wrap(fstring)
                    for char in fs:
                        print(char)
                    
        if x is None:
            print('This title is not found!') 
        if x is not None:  
              
            beasts = [] 
            allwords.pop(x)
            for key in allwords: 
                if any(i in new for i in allwords[key]):
                    beasts.append(key)  
            
            beasts = sorted(beasts)
                       
            notbeasts = set() 
            for key in allwords: 
                for i in allwords[key]:
                    notbeasts.add(i)
                       
            inmovie = set(new)
            imov = inmovie.difference(notbeasts)
            imov = sorted(imov)
            
            print()
            
            #beasts.pop(0)
            nstring = ', '.join(beasts)
            nstring = ("Other titles containing beats in common: " + nstring )
            ns = textwrap.wrap(nstring)
            for char in ns:
                print(char)
    
            print()
    
            tstring = ', '.join(imov)
            tstring = ('Beasts appearing only in this title: ' + tstring)
            ts = textwrap.wrap(tstring)
            for char in ts:
               print(char)
            tstring
            