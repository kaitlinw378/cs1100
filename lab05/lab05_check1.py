#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Oct  8 11:29:10 2019

@author: kaitlin
"""

import lab05_util

restaurants = lab05_util.read_yelp('yelp.txt')

print(restaurants[0])

def print_info(restaurant):
    print(restaurant[0], "({})".format(restaurant[5]))
    address = restaurant[3].split("+")
    i = 0
    while i < len(address): 
        print("\t" + str(address[i]))
        i += 1 
    avg = sum(restaurant[6]) / len(restaurant[6])
    print("Average score:", format(avg, '.2f'))
    print()
####### main code starts here
restaurants = lab05_util.read_yelp('yelp.txt') 
print_info(restaurants[0])
print_info(restaurants[1])
print_info(restaurants[26])