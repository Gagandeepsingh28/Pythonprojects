# -*- coding: utf-8 -*-
"""
Created on Fri Apr  5 12:49:31 2019

@author: Manmeet Kaur
"""
class Abstract:
    def __init__(self,a,b):
        self.a=a
        self.b=b
    def  add(self,a,b):
        return NotImplementedError
        
    def sun(self,a,b):
        return NotImplementedError
    
    def mul(self,a,b):
        m=a*b
        return m
    def dsi():
        pass
a=Abstract(4,6)
er=a.add(5,3)
print(er)
print(a.sun(9,2))
print(a.mul(4,2))

