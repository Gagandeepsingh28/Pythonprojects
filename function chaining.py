# -*- coding: utf-8 -*-
"""
Created on Wed Apr  3 12:13:12 2019

@author: Manmeet Kaur
"""
def f1(a):
    def f2(b):
        return a*b
    return f2
c=f1(6)
print(c(5))