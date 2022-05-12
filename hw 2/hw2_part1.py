#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Sep 30 13:57:26 2019

This programs simulates a gumball machine and how much gumballs are needed to 
last for one week without refilling the machine. This requires calculating
dimensions and target sales to optimize the machine to achieve a lattice. 
It takes two user inputs, a radius and a weekly sale number.
The program then calculates the volume of the gumballs, the volume of the cube 
and how to fit the gumballs in the cube. The results are then printed.

@author: kaitlin
"""
import math as m

#Function finds the volume of a sphere based on a given radius
def find_volume_sphere(radius):
    vs = (4/3) * m.pi * (radius ** 3)
    return vs
    
'''
Function find_volume_sphere takes radius as a parameter. It then uses the 
formula for calculating the volume of a sphere with the givern radius. 
This volume is returned. 
'''

#Function finds the volume of a cube with the parameter "side"
def find_volume_cube(side):
    vc = side * side * side
    return vc

'''
Function find_volume_cube takes a side as a parameter. It then calculates 
the volume of a cube with the given side. This final volume is returned. 
'''

rad_data = input("Enter the gum ball radius (in.) => ")
print(rad_data)
rad_data = float(rad_data)

sales = int(input("Enter the weekly sales => "))
print(sales) 
print()
t_gum = m.ceil((sales * 1.25) ** (1/3)) # total gum per side

if rad_data == 0:
    fit = 0
else:
    fit = m.floor((find_volume_cube(t_gum * (rad_data)*2)) / 
              find_volume_sphere((rad_data))) 
#how much gum will fit in the machine

per_edge = m.floor(fit ** (1/3)) #how much gum will fit per edge of machine

edge_length = float(t_gum * (2*  rad_data)) #finding the length of one row of gum

v_gum = find_volume_sphere(rad_data) * (t_gum **3) #find the volume of gum one side 

t_g_b = m.ceil((sales * 1.25)) #total gum ball target sales

wasted_space_2 = find_volume_cube(edge_length) - (find_volume_sphere(rad_data) * (t_gum ** 3))
#wasted space with gumballs if machine is filled

wasted_space = find_volume_cube(t_gum* ((rad_data)*2)) - (find_volume_sphere(rad_data) * t_g_b)
#wasted space with gumballs

print("The machine needs to hold {} gum balls along each edge.".format(t_gum, '.2f' ))
print("Total edge length is {:.2f} inches.".format(edge_length))
print("Target sales were {}, but the machine will hold {} extra gum balls.".format(t_g_b, (t_gum**3 - t_g_b)))
print("Wasted space is {:.2f} cubic inches with the target number of gum balls,\nor {:.2f} cubic inches if you fill up the machine."
      .format(wasted_space, wasted_space_2))
