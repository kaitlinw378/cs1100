#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Oct 28 19:56:57 2019

@author: kaitlin
"""
def get_line(fname, parno, lineno):
    text = open(fname, encoding = 'utf8').read()   
    linelist = text.strip().split('\n')
    paralist = []
    startpt = 0
    tmp = ''
    for i in range(len(linelist)):
        if linelist[i] == '' and linelist[i-1] != '\n':
            endpt = i-1
            for j in range(startpt, endpt):
                tmp = tmp + str(linelist[i] + '\n')
            paralist.append(tmp.split('\n'))
            startpt = i+1
            tmp = ''
    return paralist[parno-1][lineno-1].rstrip()
    

def parse_line(sentence):
    new_sent = sentence.split("/")
    if len(new_sent) < 4:
        return None
    else:
        if (new_sent[-1]).isdigit() and (new_sent[-2]).isdigit() and (new_sent[-3]).isdigit():           
            news = "/".join(new_sent[0: len(new_sent) -3])
            news_later = [int(new_sent[-3]), int(new_sent[-2]), int(new_sent[-1]), news]
            return news_later
        else:
            return None


fname = input("Please enter a file number ==> ")
print(fname)
fname = fname + ".txt"

parno = int(input("Please enter a paragraph number ==> "))
print(parno)

lineno = int(input("Please enter a line number ==> "))
print(lineno)

print(get_line(fname, parno, lineno)) 
data = parse_line(get_line(fname,parno,lineno))
f = open('program.py','w')
clue = get_line(fname, parno, lineno)

while data[0] != 0 and data[1] != 0 and data[2] != 0: 
    if parse_line(clue) == "[0,0,0,'END']":
        break
    fname = data[0]
    parno = data[1]
    lineno = data[2]
    f.write(data[3]+'\n')
    clue = get_line(fname,parno,lineno)
    data = parse_line(clue)

f.close()
   