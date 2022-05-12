#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Oct  7 16:05:46 2019

This program takes in a user input of a paragraph. It then calculates the 
number of syllables, number of "hard words" which is defined by words with 3
or more syllables, and readability indexes. Then the function calculates 
percentage of hard words, the average sentence length and the average number of 
syllables. The output is printed. 

@author: kaitlin
"""
import syllables

def PHW(words):
    computation = []
    words = paragraph.split()
    count = 0 
    for word in words: 
        if syllables.find_num_syllables(word) >= 3:           
            if word.endswith("es"): 
                count += 0
            elif word.endswith("ed"):
                count +=0 
            elif "-" in word: 
                count += 0
            else: 
                computation.append(word)
                count += 1
    return computation
'''
function PHW takes words as an argument. It then splits the argument (in this
case a paragraph) and finds the words that have 3 or more syllables. It does
not count words that end with "es" or "ed". These are stored in a list.
'''

def ASL(paragraph):
    sentences = paragraph.split(".")
    count = 0
    for sentence in sentences: 
        length_current = len(sentence.split())
        count += length_current
    avg = count / (len(sentences) - 1)
    return avg      
'''
Function ASL takes as an argument a paragraph. The argument is split and a for
loop is used to calculate the average sentence length. This is done by finding
the number of words total of the list that paragraph is stored in divided by 
the len of the list.
'''

def ASYL(paragraph): 
    num_words = paragraph.split()
    total_words = len(num_words)    
    syl_count = 0
    for i in num_words:
        syl_count += syllables.find_num_syllables(i)       
    total_syllables = syl_count / total_words
    return total_syllables
'''
Function ASYL takes as an argument a paragraph. The argument is split and a 
for loop is used to calculate the total number of syllables in the input 
divided by the total number of words that are input. 
'''

if __name__ == "__main__" :
    paragraph = input("Enter a paragraph => ")
    print(paragraph)

    computation = PHW(paragraph)

    words = paragraph.split()

    total = (len(computation) / len(words)) * 100

    percent_hw = (len(PHW(paragraph)) / len(words)) *100

    asl = ASL(paragraph)
    asyl = ASYL(paragraph)

    GFRI = 0.4*(asl + percent_hw) 

    FKRI = 206.835-1.015*asl-86.4*asyl 

    print("Here are the hard words in this paragraph:")
    print(computation)
    print("Statistics: ASL:{:.2f} PHW:{:.2f}% ASYL:{:.2f}".format(ASL(paragraph), percent_hw , ASYL(paragraph)))
    print("Readability index (GFRI): {:.2f}".format(GFRI))
    print("Readability index (FKRI): {:.2f}".format(FKRI))

