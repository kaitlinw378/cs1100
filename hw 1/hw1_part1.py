#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Sep 16 20:45:41 2019

This program takes user inputs and creates a madlib which is a story based on 
words the user chooses. The program takes these inputs and places them into
pre-selected locations throughout the story. 

@author: kaitlin
"""
print("Let's play Mad Libs for Homework 1")
print("Type one word responses to the following:\n")

proper_name = input("proper_name ==> ")
print(proper_name)

adjective = input("adjective ==> ")
print(adjective)

noun = input("noun ==> ")
print(noun)

verb = input("verb ==> ")
print(verb)

verb2 = input("verb ==> ")
print(verb2)

noun2 = input("noun ==> ")
print(noun2)

emotion = input("emotion ==> ")
print(emotion)

verb3 = input("verb ==> ")
print(verb3)

noun3 = input("noun ==> ")
print(noun3)

season = input("season ==> ")
print(season)

adjective2 = input("adjective ==> ")
print(adjective2)

emotion2 = input("emotion ==> ")
print(emotion2)

team_name = input("team-name ==> ")
print(team_name)

noun4 = input("noun ==> ")
print(noun4)

adjective3 = input("adjective ==> ")
print(adjective3, "\n")

print("Here is your Mad Lib...\n")

print("Good morning ", proper_name,"!", sep = "", end = "\n"*2)
print(" ", "This will be a/an" , adjective , noun +"!", "Are you", verb, "forward to it?")
print(" ", "You will", verb2, "a lot of", noun2, "and feel", emotion, "when you do.")
print(" ", "If you do not, you will", verb3, "this", noun3 + ".", end = "\n"*2)
print(" ","This", season, "was", adjective2 +".", "Were you", emotion2,
      "when", team_name, "won\n" + " ", "the", noun4+"?", end = "\n"*2)
print(" ", "Have a/an" , adjective3 , "day!")
