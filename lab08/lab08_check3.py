#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Lab 8, Checkpoint 3
Created on Tue Oct 29 09:59:25 2019

@author: psquared
"""

import string

primary_club_name = input("Enter club  name => ")
allclubs_f = open('allclubs.txt').readlines()
primary_club_f = open('{}.txt'.format(primary_club_name)).read()
print('\n')


# Returns big words in description as a set
def get_words(text):
    text = text.split('|')
    text.pop(0)
    text = str(text).strip("[]'")
    text = text.split('\\')
    text.pop(-1)
    text = str(text).strip("[]'")
    text = text.translate(str.maketrans('', '', string.punctuation))
    text = text.split(' ')
    text = [word.lower() for word in text if (word.isalpha() is True)
                                                  and (len(word) > 3)]
    out = set(text)
    return(out)


primary_club_words = get_words(primary_club_f)
similars = []
for club in allclubs_f:
    x_club = len(primary_club_words.intersection(get_words(club)))
    name = club.split('|')[0]
    similars.append([x_club, name])


similars = sorted(similars)
the_sims = [similars[x][1] for x in range(-1, -7, -1)]


print("Most similar clubs to {}:".format(the_sims[0]))
for sims in the_sims[1:]:
    print("{}.{}".format(the_sims.index(sims), sims))

 