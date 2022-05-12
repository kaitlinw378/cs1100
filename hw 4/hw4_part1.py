#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Oct 15 14:59:09 2019

This program simulates a password checker. It takes as input from a user a
password that is a string. It then goes through 5 rules to see if the password
is valid. If it is not, then it suggests a new one that the user may want to 
use instead. 

@author: kaitlin
"""
def check_rule1(password):
    length = len(password)
    first = password[0]
    if 10 <= length <= 25 and (first.isupper() or first.islower()):
        print("Rule 1 is satisfied")
    else:
        print("Rule 1 is not satisfied")
        return False
'''
Function check_rule1 checks if the password is between 10 and 25 characters 
long and then checks if the first character is a letter. Will return True if
conditions are met.
'''     

def check_rule2(password):
    if ("@" in password or "$" in password) and ("%" not in password):
        print("Rule 2 is satisfied") 
        return True
    else:
        print("Rule 2 is not satisfied")
        return False  
'''
Function check_rule2 checks if there is either the @ symbol or the $ symbol 
in the password and if there is no % symbol. If these are all met, function
returns True. 
'''

def check_rule3(password):
    if (password.isupper() == False and password.islower() == False) or ("1" in password or "2" in password\
       or "3" in password or "4" in password):
        print("Rule 3 is satisfied")
        return True
    else:
        print("Rule 3 is not satisfied")
        return False
'''        
Function check_rule3 checks if there are any upper and lower case letters in 
the password. If not, it checks if there are only numbers between 1 to 4 as a 
substitute instead. If satisfied it returns True. 
'''

def check_rule4(password):
     for i in range(len(password)):
        letter = password[i] 
        if letter.isupper() == True: 
            if i == (len(password) -1):
                print("Rule 4 is not satisfied")
                return False
            next_letter = password[i + 1] 
            if next_letter != "_":
                print("Rule 4 is not satisfied")
                return False
     print("Rule 4 is satisfied")
     return True
        
'''
Function check_rule4 checks if there is underscore immediately following any 
uppercase letters in the password. If there are no uppercase letters, this rule
returns true. 
'''
        
def check_rule5(password):
    for i in range(len(password)):
        character = password[i]
        if character.isdigit() and (1 > int(character) or int(character) > 4): 
            print("Rule 5 is not satisfied")
            return False
    print("Rule 5 is satisfied")
    return True
'''
Function check_rule5 checks if there are only numbers in the range of 1 to 4 in
the password. If there are any numbers outside of this range, the function will
return False. 
'''

def suggested(password):
    suggest = password[:8] + "42" + password[len(password)-8:len(password)]
    return suggest
'''
Function suggested appends the numbers 42 between the first 8 and last 
characters in the password if the last 4 rule checks are not satisfied. It 
returns the password despite if the new one is valid or not. 
'''

def check_pass(password):
    rule1 = check_rule1(password)
    rule2 = check_rule2(password)
    rule3 = check_rule3(password)
    rule4 = check_rule4(password)
    rule5 = check_rule5(password)
    
    # Suggest a password if any rule except rule 1 is broken.
    
    if rule1 == False:
        print ('The password is not valid')
    elif (rule2 == False or rule3 == False \
        or rule4 == False or rule5 == False):
        print("A suggested password is: " + str(suggested(password)))
    else:
        print("The password is valid")
        
#    if (rule2 == False or rule3 == False \
#        or rule4 == False or rule5 == False):
#        print("A suggested password is: " + str(suggested(password)))
#    elif rule1 == False:
#        print("The password is not valid")
#    else:
#        print("The password is valid")
'''
Function check_pass finalizes the program and calls all the other definitions 
at once and prints out the results of each. If it is needed, it will call
the function suggested and print a new password. If not, it will print that
the password is valid.
'''

if __name__ == "__main__":
    password = input("Enter a password => ")
    print(password)
    
    check_pass(password)
