# -*- coding: utf-8 -*-
"""
Created on Mon Apr 15 23:31:12 2019

@author: Manmeet Kaur
"""
class Over:
    def __init__(self,a,b):
        self.a=a
        self.b=b
    
    def sum1(self):
        c=self.a+self.b
        print(c)
#o=Over(5,6)
class Load:
    def __init__(self,d,f):
        self.d=d
        self.f=f
    
    def sum1(self):
        s=self.d+self.f
        print(s)
#p=Load(3,7)
class Loading(Over,Load):
    def __init__(self,a,b):
        self.a=a
        self.b=b
    def sum1(self):
        print("this is class")
        o=Over(self.a,self.b)
        o.sum1()
        l=Load(self.a,self.b)
        l.sum1()
y=Loading(5,6)
y.sum1()

