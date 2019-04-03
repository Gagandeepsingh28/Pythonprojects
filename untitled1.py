# -*- coding: utf-8 -*-
"""
Created on Thu Mar 28 12:20:15 2019

@author: Manmeet Kaur
"""
import os
#print(os.getcwd())
import sys
file=sys.argv[0]
#print(file)
#print(os.listdir
#(os.getcwd()))
p=(os.path.abspath("test.txt"))
print(os.path.isabs("F:\python\test.txt"))
r=os.path.relpath("F:\python\"","test.txt")
print(r)
 

