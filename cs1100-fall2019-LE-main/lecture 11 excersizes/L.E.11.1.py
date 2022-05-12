#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Oct  7 14:20:06 2019

@author: kaitlin
"""


def earlier_semester(tuple1, tuple2):
    if tuple1[1] < tuple2[1]:
        return True
    elif tuple1[1] > tuple2[1]:
        return False
    else: 
        if tuple1[0] == "Spring" and tuple2[0] == "Fall":
            return True
        else: 
            return False
    
   
w1 = ('Spring',2015)
w2 = ('Spring',2014)
w3 = ('Fall', 2014)
w4 = ('Fall', 2015)
print( "{} earlier than {}? {}".format( w1, w2, earlier_semester(w1,w2)))
print( "{} earlier than {}? {}".format( w1, w1, earlier_semester(w1,w1)))
print( "{} earlier than {}? {}".format( w1, w4, earlier_semester(w1,w4)))
print( "{} earlier than {}? {}".format( w4, w1, earlier_semester(w4,w1)))
print( "{} earlier than {}? {}".format( w3, w4, earlier_semester(w3,w4)))
print( "{} earlier than {}? {}".format( w1, w3, earlier_semester(w1,w3)))
