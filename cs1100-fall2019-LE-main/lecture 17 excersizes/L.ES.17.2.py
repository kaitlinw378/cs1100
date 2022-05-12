#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Nov  5 15:22:28 2019

@author: kaitlin
"""

def file_look(file):
    l1 = []
    l2 = []
    s1 = set() 
    for l in open(file):
        l1.append(l.strip())
    for l in l1:
        t = l.split("|")
        for i in range(0, len(t)):
            t[i] = t[i].strip()
        t.pop(2)
        l2.append(t)
        s1.add(t[1]) 
    return [l2, s1] 

file = input("Enter the name of the IMDB file ==> ")
print(file) 
m = file_look(file)
movies = sorted(list(m[1]))
ms = dict()
for movie in movies: 
    ms[movie] = set() 
for actor in m[0]:
    ms[actor[1]].add(actor[0])
sp = 0
lf = []
for value in ms: 
    lf.append([len(ms[value]), value])
lf.sort()
for value in lf:
    if value[0] == 1: 
        sp += 1
        
print(lf[-1][0], lf[-1][1], sp, sep = '\n') 
