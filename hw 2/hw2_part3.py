#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Oct  1 11:36:52 2019

This program simulates an AI that is trying to interpret if a sentence is 
happy, sad or neutral. A user inputs a sentence that is then scanned for
select "happy" and "sad" words. If it is detected that there are more happy
than sad words, the machine prints out the sentiment with the number of 
happy words and vice versa. Otherwise, it will print out a neutral statement. 
The sentiment in this case, represents the tone of voice of the user.

@author: kaitlin
"""

phrase = str(input("Enter a sentence => ")).strip()
print(phrase)
phrase = phrase.lower()

#Counts the number of happy words in a sentence, adds them, stores them a list.
def number_happy(sentence):
    phrase.lower()
    phrasesH = []
    phrasesH.append(phrase.count("laugh"))
    phrasesH.append(phrase.count("happiness"))
    phrasesH.append(phrase.count("love"))
    phrasesH.append(phrase.count("excellent"))
    phrasesH.append(phrase.count("good"))
    phrasesH.append(phrase.count("smile"))  
    total = sum(phrasesH)
    return total

'''
Function number_happy takes a string as a parameter, counts the number of times
each of the key happy words appear in that string and store those numbers in 
a list. The function then takes the sum of the numbers stored in the list and 
returns that number.
'''

#Counts number of sad words in a sentence, adds them, stores them in a list.
def number_sad(sentence):
    phrase.lower()
    phraseS = []
    phraseS.append(phrase.count("bad"))
    phraseS.append(phrase.count("sad"))
    phraseS.append(phrase.count("terrible"))
    phraseS.append(phrase.count("horrible"))
    phraseS.append(phrase.count("problem"))
    phraseS.append(phrase.count("hate"))
    total2 = sum(phraseS)
    return total2   

'''
Function number_sad takes a string as a parameter, counts the number of times 
that the key sad words appear in that string and stores that in a list. 
The function then takes the sum of those numbers and returns the total sum.
'''

#creates the sentiment output
happy = (number_happy(phrase)) * "+"
sad = (number_sad(phrase)) * "-"

if number_happy(phrase) > number_sad(phrase):
    print("Sentiment: " + (happy) + sad)
    print("This is a happy sentence.")
elif number_sad(phrase) > number_happy(phrase):
    print("Sentiment: " + happy + (sad))
    print("This is a sad sentence.")
else:
    print("Sentiment: " + (happy) + (sad))
    print("This is a neutral sentence.")
