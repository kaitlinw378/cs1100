#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Oct  8 12:16:31 2019

@author: kaitlin
"""

import lab05_util

restaurants = lab05_util.read_yelp('yelp.txt')

id_tag = int(input("Enter a restaurant ID starting from 1: "))
print(id_tag)
id_tag = id_tag - 1

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

if id_tag > len(restaurants):
    print("Warning: ID is out of range of restaurant list.")
else:
    print_info(restaurants[id_tag])
#print_info(restaurants[0])
#print_info(restaurants[1])
#print_info(restaurants[26])

