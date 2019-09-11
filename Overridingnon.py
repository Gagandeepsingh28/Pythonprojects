# -*- coding: utf-8 -*-
"""
Created on Tue Apr 16 23:00:51 2019

@author: Manmeet Kaur
"""
class Over:
    @staticmethod
    def sum1(a,b):
        c=a+b
        print(c)
#o=Over(3,4)
        
class Load:
    @staticmethod
    def sum1(d,f):
        s=d+f
        print(s)
#p=Load(2,3)

class Loading(Over,Load):
    def __init__(self,a,b):
        self.a=a
        self.b=b
    def sum1(self):
        print("this is class")
        Over.sum1(self.a,self.b)
        Load.sum1(self.a,self.b)
y=Loading(4,5)
y.sum1()

        