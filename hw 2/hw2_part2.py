#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Oct  1 10:32:40 2019

This programs takes a user input, which is a string, and encrypts it to a 
secret message. It then prints the change in length from the original string
to the encrypted one. After this, the program will decipher the message,
using the function decrypt(word). 
Sometimes it will decipher completely, sometimes not. As a result, the last 
line prints whether it can be fully deciphered back to the original string
or not. 

@author: kaitlin
"""

message = input("Enter a string to encode ==> ")
print(message)
message = str(message)
print() 
#Takes a string and encrypts it to a secret code
def encrypt(word):
    final = message.replace(" a", "%4%")
    final = final.replace("he", "7!")
    final = final.replace("e", "9(*9(")
    final = final.replace("y", "*%$")
    final = final.replace("u", "@@@")
    final = final.replace("an", "-?")
    final = final.replace("th", "!@+3")
    final = final.replace("o", "7654")
    final = final.replace("9", "2")
    final = final.replace("ck", "%4")
    return final

"""
Function encrypt takes a string as a parameter. It then takes that string and 
replaces key letters and/or characters with the "secret symbols" to create
a string that is then encoded. This string is returned. 
"""

#Takes the string that is encrypted and decrypts it to original if possible
def decrypt(word):
    begin = secret.replace("%4", "ck")
    begin = begin.replace("2", "9")
    begin = begin.replace("7654", "o")
    begin = begin.replace("!@+3", "th")
    begin = begin.replace("-?", "an")
    begin = begin.replace("@@@", "u")
    begin = begin.replace("*%$", "y")
    begin = begin.replace("9(*9(", "e")
    begin = begin.replace("7!", "he")
    begin = begin.replace("%4%", " a")
    return begin

'''
Function decrypt takes a string as a parameter. It takes the string from the 
previous function, encrypt. It then takes the "secret symbols" and replaces 
them with their coresponding standard english characters to decipher the code.
The function then returns this decoded string. 
'''

#reassignment variable
secret = encrypt(message) 

#Finds the difference of the length between the original and encrypted message
difference_length = abs(len(message) - len(secret)) 

#reassignment variable
original = decrypt(message)
print("Encrypted as ==>", secret)
print("Difference in length ==>", difference_length)
print("Deciphered as ==>", original)

if message == decrypt(message):
    print("Operation is reversible on the string.")
else:
    print("Operation is not reversible on the string.")
