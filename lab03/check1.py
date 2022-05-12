#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Sep 23 23:48:34 2019
@author: kaitlin
"""
from PIL import Image
im = Image.new('RGB', (512, 512), 'white')

image_1_file = '/Users/kaitlin/Dropbox/cs1100/lab/lab03/lab03files/ca.jpg'
image_1 = Image.open(image_1_file)
image_1 = image_1.resize((256,256))
im.paste(image_1, (0,0))

image_2_file = '/Users/kaitlin/Dropbox/cs1100/lab/lab03/lab03files/im.jpg'
image_2 = Image.open(image_2_file)
image_2 = image_2.resize((256,256))
im.paste(image_2, (256,0))

image_3_file = '/Users/kaitlin/Dropbox/cs1100/lab/lab03/lab03files/hk.jpg'
image_3 = Image.open(image_3_file)
image_3 = image_3.resize((256,256))
im.paste(image_3, (0,256))

image_4_file = '/Users/kaitlin/Dropbox/cs1100/lab/lab03/lab03files/bw.jpg' 
image_4 = Image.open(image_4_file)
image_4 = image_4.resize((256,256))
im.paste(image_4, (256,256))

im.show()
