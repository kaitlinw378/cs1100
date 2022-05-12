#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Nov  4 18:06:17 2019

@author: kaitlin
"""

file = input("Enter the name of the IMDB file ==> ")
print(file) 

actors = dict()
for line in open(file, encoding = "ISO-8859-1"):
    words = line.strip().split('|')
    name = words[0].strip()
    movie = words[1].strip()
    
    if movie in actors:
        actors[movie].add(name)
    else:
        actors[movie] = set()
        actors[movie].add(name)
        
count = 0        
unique = 0
for movie in actors: 
    
    if len(actors[movie]) == 1:
        count += 1
    
for movie in actors: 
    if len(actors[movie]) > 1:
        unique += 1
        x = movie
    
lf = []
for value in actors: 
    lf.append([len(actors[value]), value])
lf.sort()
for value in lf:
    if value[0] == 1: 
        unique += 1
 
print(lf[-1][0])       
print(lf[-1][1])
print(count)
