#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Nov  6 21:31:23 2019

@author: kaitlin
"""

#check if the word is present in the set having words in dictionary file
def found(set1,word):
    if(word in set1):#if present then return word
        return word;
    return None;#otherwise return None

#find if a word after dropping any character is present in set
def drop(set1,word):
    word1=""
    for i in range(len(word)):
        word1=word[0:i]#substring of word from 0->i-1
        word1=word1+word[i+1:]#substring of word from i+1->end
        if(word1 in set1):#if after dropping ith character the word is present in set then return word1
            return word1;
    return None;

#swap two adjacent letters and try to check of it is present in the dictionary
def swap(set1,word):
    for i in range(len(word)-1):
        word1="";
        if(i-1>=0):#if i-1>0 then assign substring from 0->i-1 to word1
            word1=word[0:i]
            word1=word1+word[i+1]#put the character i+1 before i character
            word1=word1+word[i]
        if(i+2<len(word)):#if i+2 is with in length of string then assign that remaining string part to word1
            word1=word1+word[i+2:];
        if(word1 in set1):#if word1 is present then return it
            return word1;
    return None;

#check if after replacing any index character with any of the alphabet is present in the set then return it
def replace(set1,word):
    word1=""
    letters = [ 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w','x', 'y', 'z' ]
    for i in range(len(word)):
        for j in range(26):
            word1=word[0:i];#get substring from 0->i-1
            word1=word1+letters[j];#replace ith to jth index letter alphabet
            word1=word1+word[i+1:];#add remaining string into word1
            if word1 in set1:
                return word1;
    return None;

print ("Dictionary file => ")
dictFile=input();#take input
set1=set();#create set
dictObject=open(dictFile, "r")#open file
#for each line in dictObject
for line in dictObject:
    listt=line.split(" ");#split the line by space
    set1.update(listt)#update set1 by listt elements
dictObject.close();#close file

#create file inputObject
print ("Input file => ");
inputFile=input();
set2=set();
inputObject =open(inputFile,"r")
for line in inputObject:
    listt=line.split(" ");
    set2.update(listt)
inputObject.close()

#traverse each word in set2 to check
for word in set2:
    actualWord=word.split()[0]#to remove \n from the word if present(because of file \n)
    if(found(set1,word) is not None):
        print (actualWord," -> ",found(set1,word)," :FOUND");
    elif (drop(set1,word) is not None):
        print (actualWord," -> ",drop(set1,word)," :DROP");
    elif (swap(set1,word) is not None):
        print (actualWord," -> ",swap(set1,word)," :SWAP");
    elif (replace(set1,word) is not None):
        print (actualWord," -> ",replace(set1,word)," :REPLACE");
    else:
        print (actualWord," -> ",actualWord ," :NO MATCH"); 