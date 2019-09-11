# -*- coding: utf-8 -*-
"""
Created on Wed Apr 17 12:23:22 2019

@author: Manmeet Kaur
"""
class Overload:
    def __init__(self,a):
        self.a=a
    def __add__(self,b):
        return self.a+b.a

a=Overload(4)
b=Overload(6)
print(a+b)

l=[1,2,3,4]
l1=[6,7,8,9] 
r=zip(l,l1)
print(list(r))
