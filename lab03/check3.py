#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Sep 24 12:54:04 2019

@author: kaitlin
"""
from PIL import Image
import check2_helper

im = Image.new('RGB', (1000, 360), 'white')

image_1_file = '/Users/kaitlin/Dropbox/cs1100/lab/lab03/lab03files/1.jpg'
image_1 = Image.open(image_1_file)
#image_1 = check2_helper.make_square(image_1)
image_1 = image_1.resize((128,256))
im.paste(image_1, (31,20))


image_2_file = '/Users/kaitlin/Dropbox/cs1100/lab/lab03/lab03files/2.jpg'
image_2 = Image.open(image_2_file)
#image_2 = check2_helper.make_square(image_2)
image_2 = image_2.resize((128,256))
im.paste(image_2, (169,60))

image_3_file = '/Users/kaitlin/Dropbox/cs1100/lab/lab03/lab03files/3.jpg'
image_3 = Image.open(image_3_file)
#image_3 = check2_helper.make_square(image_3)
image_3 = image_3.resize((128,256))
im.paste(image_3, (307,20))

image_4_file = '/Users/kaitlin/Dropbox/cs1100/lab/lab03/lab03files/4.jpg' 
image_4 = Image.open(image_4_file)
#image_4 = check2_helper.make_square(image_4)
image_4 = image_4.resize((128,256))
im.paste(image_4, (445,60))

image_5_file = '/Users/kaitlin/Dropbox/cs1100/lab/lab03/lab03files/5.jpg'
image_5 = Image.open(image_5_file)
#image_5 = check2_helper.make_square(image_5)
image_5 = image_5.resize((128,256))
im.paste(image_5, (583,20))

image_6_file = '/Users/kaitlin/Dropbox/cs1100/lab/lab03/lab03files/6.jpg'
image_6 = Image.open(image_6_file)
#image_6 = check2_helper.make_square(image_6)
image_6 = image_6.resize((128,256))
im.paste(image_6, (721,60))

im.show()
