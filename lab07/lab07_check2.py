#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Oct 22 12:28:48 2019

@author: kaitlin
"""
def parse_line(sentence):
    new_sent = sentence.split("/")
    if len(new_sent) < 4:
        return None
    else:
        if (new_sent[-1]).isdigit() and (new_sent[-2]).isdigit() and (new_sent[-3]).isdigit():           
            news = "/".join(new_sent[0: len(new_sent) -3])
            news_later = [int(new_sent[-3]), int(new_sent[-2]), int(new_sent[-1]), news]
            return news_later
        else:
            return None
        
'''
print(parse_line("Here is some random text, like 5/4=3./12/3/4"))
print(parse_line("Here is some random text, like 5/4=3./12/3/4as"))
print(parse_line("Here is some random text, like 5/4=3./12/412/a/3/4"))
print(parse_line("     Here is some spaces 12/32/4"))
print(parse_line("    Again some spaces\n/12/12/12"))
'''

def get_line(fname, parno, lineno):
    fname = open(fname, 'r')   
    paragraphs = []
    lines = []    
    for line in fname.read().rsplit("\n\n"):
        paragraphs.append(line)   
    lines = paragraphs[parno].split("\n")
    return lines[lineno-1]


fname = input("Please enter a file number ==> ")
print(fname)
fname = fname + ".txt"

parno = int(input("Pleas enter a paragraph number ==> "))
print(parno)

lineno = int(input("Please enter a line number ==> "))
print(lineno)

print(get_line(fname, parno, lineno)) 
