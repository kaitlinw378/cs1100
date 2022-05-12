#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Nov 19 12:23:09 2019

@author: kaitlin
"""

class Ball(object):
    def __init__(self, x, y, dx, dy, radius, color):
        self.x = x
        self.y = y
        self.dx = dx
        self.dy = dy
        self.radius = radius
        self.color = color

    def position(self):
        return((self.x, self.y))

    def move(self):
        self.x = int(self.x) + int(self.dx)
        self.y = int(self.y) + int(self.dy)

    def bounding_box(self):
        x0 = int(self.x) - int(self.radius)
        x1 = int(self.x) + int(self.radius)

        y0 = int(self.y) - int(self.radius)
        y1 = int(self.y) + int(self.radius)

        return((x0, y0, x1, y1))

    def get_color(self):
        return(self.color)

    def some_inside(self, a, b):
        x0 = int(self.x) - int(self.radius)
        x1 = int(self.x) + int(self.radius)

        y0 = int(self.y) - int(self.radius)
        y1 = int(self.y) + int(self.radius)

        return ((0 <= self.x + self.radius) and (self.x - self.radius <= a) and (0 <= self.y + self.radius) and (self.y - self.radius <= b))

    def check_and_reverse(self, maxx, maxy):
        if (self.x - self.radius - 3 <= 0) or (self.x + self.radius + 3 >= maxx):
            self.dx = int(-1) * int(self.dx)
            
            return(True)
        if (self.y - self.radius - 3 <= 0) or (self.y + self.radius + 3 >= maxy):
            self.dy = int(-1) * int(self.dy)
            return(True)
        return False