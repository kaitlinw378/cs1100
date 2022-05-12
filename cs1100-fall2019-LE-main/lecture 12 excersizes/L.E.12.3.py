#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Oct 10 16:21:09 2019

@author: kaitlin
"""

def find_min(lists):
    absolute_min = min(lists[0])
    for one_list in lists: 
        one_min = min(one_list)
        if one_min < absolute_min:
            absolute_min = one_min
        
    return absolute_min
    
if __name__ == "__main__":
    v = [ [ 11,12,3], [6, 8, 4], [ 17, 2, 18, 14] ]
    print("Min of list v: {}".format(find_min(v)) )
    u = [ [ 'car', 'tailor', 'ball' ], ['dress'], ['can', 'cheese', 'ring' ], \
              [ 'rain', 'snow', 'sun' ] ]
    print("Min of list u: {}".format(find_min(u)) )
    