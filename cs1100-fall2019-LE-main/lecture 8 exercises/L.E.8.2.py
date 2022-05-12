# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

values = [ 14, 10, 8, 19, 7, 13 ]

number_one = input("Enter a value: ")
print(number_one)
number_one = int(number_one)
values.append(number_one)
number_two = input("Enter another value: ")
print(number_two)
number_two = int(number_two)
values.insert(2, number_two)
print(values[3], values[-1])
difference = (max(values) - min(values))
print("Difference:", difference)
average = (sum(values) / len(values))
print("Average:", format(average, '.1f'))
values.sort() 
upper = (len(values) // 2)
lower = (len(values) // 2 -1)
median = (values[4] + values[3]) / 2
print("Median:", median)
