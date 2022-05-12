#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Oct 28 20:40:01 2019

@author: kaitlin
"""
#def get_words(description): 
#    description = ''.join(description)
#    description = description.replace('|', ' ').replace(',', ' ').replace('.', ' ').replace('(', ' ').replace(')', ' ').replace('"', ' ') 
#    description = description.lower()
#    words = description.split(' ')
#    
#    list1 = []
#    for word in words:
#        if word.isalpha() and (len(word) >= 4):    
#            list1.append(word)     
#    list1.pop(0)        
#    return list1 

def club_description_finder(user_input):
	temp = []
	new_list = []
	description = ""

	for x in open(user_input):
		temp.append(x.split("|"))

	new_list.append(temp[0][1])

	description = new_list[0]

	return(description)

def club_name_finder(user_input):
	temp = []
	new_list = []
	
	
	for x in open(user_input):
		temp.append(x.split())
	
	temp_number_finder = 0

	for x in range(len(temp[0])):
		if (temp[0][x].find("|") != -1):
			temp_number_finder = x
		new_list.append(temp[0][x])

	temp_string = ""
	for x in range(temp_number_finder + 1):
		temp_string += str(new_list[x]) + " "

	club_names_finally = temp_string[0:temp_string.find("|")]

	return(club_names_finally)

filename = input("Enter filename: ")
file2 = input("Enter another file: ")
#with open(filename) as f:
#    description = f.readlines()
#    file2 = f.readlines()
#    print(get_words(description))
#    print(two_clubs(description, file2)) 

club_1_description = club_description_finder(filename).lower().split()
club_2_description = club_description_finder(file2).lower().split()
 
description_new_1 = []
description_new_2 = []

for x in club_1_description:
	a = x
	a = a.replace(".", "")
	a = a.replace(",", "")
	a = a.replace("(", "")
	a = a.replace(")", "")
	a = a.replace("\"", "")
	a = a.lower()
	if ((len(a) >= 4) and (a.isalpha() == True)):
		description_new_1.append(a)

for x in club_2_description:
	a = x
	a = a.replace(".", "")
	a = a.replace(",", "")
	a = a.replace("(", "")
	a = a.replace(")", "")
	a = a.replace("\"", "")
	a = a.lower()
	if ((len(a) >= 4) and (a.isalpha() == True)):
		description_new_2.append(a)

list_1 = set(description_new_1)
list_2 = set(description_new_2)

same_words = list_1.intersection(list_2)
unique_to_1 = list_1.difference(list_2)
unique_to_2 = list_2.difference(list_1)

print("Comparing clubs", club_name_finder(filename), "and", club_name_finder(file2))
print()
print("Same words:", same_words)
print()
print("Unique to", club_name_finder(filename), unique_to_1)
print()
print("Unique to", club_name_finder(file2), unique_to_2)