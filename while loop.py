# -*- coding: utf-8 -*-
"""
Created on Tue Apr  2 22:46:45 2019

@author: Manmeet Kaur
"""
n=0
while n<=10:
    print(n)
    n+=1
    if n==6:
        continue
    if n==8:
        break
    print(n)
e=type(n) is int
print(e)
