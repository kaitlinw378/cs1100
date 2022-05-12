#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Oct  1 12:09:28 2019

@author: kaitlin
"""

bpop = int(input("Number of bunnies ==> "))
print(bpop)

fpop = int(input("Number of foxes ==> "))
print(fpop)

def get_bpop(bpop, fpop):
    bpop_next = int((10*bpop)/(1+0.1*bpop) - 0.05*bpop*fpop)
    return bpop_next

def get_fpop(bpop, fpop):
    fpop_next = int(0.4 * fpop + 0.02 * fpop * bpop)
    return fpop_next

print("Year 1:", str(bpop), str(fpop))
print("Year 2:", get_bpop(bpop,fpop), get_fpop(bpop, fpop))

