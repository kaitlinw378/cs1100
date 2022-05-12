#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Sep 24 00:25:31 2019

@author: kaitlin
"""
from PIL import Image

def make_square(im):
    print(im.size[0])
    print(im.size[1])
    square = min(im.size[0], im.size[1])
    print(square) 
    im = im.crop((0,0,square,square)) 
    return im

im = Image.open('/Users/kaitlin/Dropbox/cs1100/lab/lab03/lab03files/ca.jpg')
im = make_square(im)
#im.show()
 