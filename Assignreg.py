# -*- coding: utf-8 -*-
"""
Created on Wed Apr 10 12:34:58 2019

@author: Manmeet Kaur
"""
import re
file=open("assign.txt",'r')
for line in file:
    print(line,end='')
    Email=re.compile(r'[a-z A-Z 0-9.+]+@[a-z A-Z 0-9.+]+[^\.]')
    print(Email.findall(line))
    