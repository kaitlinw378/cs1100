#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Oct 31 17:27:18 2019

@author: kaitlin
"""
imdb_file = input("Enter the name of the IMDB file ==> ").strip()
print(imdb_file)
counts = dict()

for line in open(imdb_file, encoding = "ISO-8859-1"):
    words = line.strip().split('|')
    name = words[0].strip()
    if name in counts:
        counts[name] += 1
    else:
        counts[name] = 1
 
nums = list(counts.values())

def find_name(dictionary, value):
    names = list()
    items = dictionary.items()
    for item in items: 
        if item[1] == value:
            names.append(item[0])
    return names

val = find_name(counts, max(nums)) 
for key in val: 
    print(str(key) + " appears most often: " + str(max(nums)) + " times") 

counter = 0
for i in counts: 
    if counts[i] == 1:
        counter += 1
        
print(str(counter) + " people appear once")
