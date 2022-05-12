#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Sep 16 22:49:59 2019

This program takes in four user inputs (minutes, seconds, miles, target miles),
and calculates the pace using modulo arithmetic and the speed along with the 
time that it will take to run the target miles that were given by the user. 

@author: kaitlin
"""
minutes = str(input("Minutes ==> "))
print(minutes)
minutes = int(minutes)

seconds = str(input("Seconds ==> "))
print(seconds)
seconds = int(seconds)

miles = str(input("Miles ==> "))
print(miles)
miles = float(miles)

target_miles = str(input("Target Miles ==> "))
print(target_miles, "\n")
target_miles = float(target_miles)

total_seconds = ((minutes*60) + seconds)
pace = (total_seconds / miles)
pace_minutes = int(pace / 60)
pace_seconds = int(pace % 60) 

speed = (60 / (pace/60))

target_time = ((target_miles * 60))
target_minutes = int(target_time / speed)
target_calculate = ((target_time / speed) - int(target_minutes))
target_seconds = int((60 * target_calculate))
miles = format(miles, '.2f')
target_miles = format(target_miles, '.2f')

print("Pace is", pace_minutes, "minutes and", pace_seconds, "seconds per mile.")
print("Speed is", format(speed, '.2f'), "miles per hour.")
print("Time to run the target distance of", target_miles, "miles is", target_minutes, "minutes and", target_seconds, "seconds.")
