#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Sep 19 14:17:02 2019

@author: kaitlin
"""

"""
tuple can contain any data type including other tuples
strings can only hold characters
example of a tuple is (1,2)

if s is a string that equals 'abc'
and x is a tuple that is (4,5,10)
we can fin the first element of both by asing for 0 element of each
x[0] = 4
s[0] = 'a' 

arrays, lists, tuples, strings first element is always at position 0

tuples are different from arrays. numpy has arrays but python does not

tuple once it is set cannot be changed
cannot do x[1] = 2 because it is not a legal opperation 

can d0 x = x[0], 2, x[2]
it is not changing just one of the elements 

strings and tuples are immutable. you can throw away a value and replace it
with a new value as shown above

cant just change one element, you must restate the entire tuple/string to 
change one element 

tuples are good for things where you have to return multiple values. 
example is a coordinate system such as (x,y)

2,3 is a tuple
in: 2,3
out: (2,3)

a, b = 4, 5 
assigns a to 4 and b to 5

if x = (2,3)
a, b = x gives a = 2 and b = 3
if you have a tuple of length of (number) you can make assignment as long as the number 
matches the amount of values you have in a tuple 

a, b, c = ('x', 'y', 'z')
d = a, b, c

in: d
out: ('x', 'y', 'z')


def split(n):
    tens = n // 10
    ones = n % 10
    return tens, ones
    

x = 83

a, b = split(x) 

print("Tens =", a, "Ones =", b)
Tens = 8 Ones = 3

can import other python programs to ne as long as it is saved 

ex" import hw1_part3

rgb values are tuples. 

im.crop(100,100,200,400)
is the same as (xstart, ystart, xend, yend) colums vs rows

im.paste does not return anything only modifies the image


"""

