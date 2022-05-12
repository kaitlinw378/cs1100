#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Sep 12 00:08:38 2019

@author: kaitlin
"""

phrase = '"Things you wish you knew as a freshman"'
print('The phrase',phrase)
print('becomes the hashtag',phrase.title().replace(" ", "").replace("Th", "#Th"))