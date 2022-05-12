#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Oct  8 12:30:26 2019

@author: kaitlin
"""

import lab05_util
import webbrowser

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

print("What would you like to do next? \n1. Visit the homepage \n2.Show on Google Maps \n3.Show directions to this restaurant")
choice = int(input("Your choice (1-3)? ==> "))
print(choice)

if choice == 1:
    webbrowser.open(restaurants[id_tag][4]) 
elif choice == 2: 
    webbrowser.open('http://www.google.com/maps/place/{}'.format(restaurants[id_tag][3]))
else:
    webbrowser.open('http://www.google.com/maps/dir/110 8th Street Troy/{}'.format(restaurants[id_tag][3]))
