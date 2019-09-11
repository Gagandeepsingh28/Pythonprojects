# -*- coding: utf-8 -*-
"""
Created on Sun Apr 21 23:27:44 2019

@author: Manmeet Kaur
"""

class Overload:
    def __init__(self,a):
        self.a=a
    def __add__(self,b):
        return self.a+b.a
    def __mul__(self,c):
        return self.a*b.a
    def __gt__(self,d):
        if(self.a>d.a):
            return True
        else:
            return False
    def __lt__(self,d):
        if(self.a<d.a):
            return True
        else:
            return False
    def __eq__(self,d):
        if(self.a==d.a):
            return True
        else:
            return False


        
a=Overload(4)
b=Overload(6)
d=Overload(7)
print(a+b)
print(a*b)
print(a>d)
print(a<d)
print(a==d)

class ComplexOverload:
    def __init__(self,a,b):
        self.a=a
        self.b=b
    def __add__(self,b):
        return self.a+b.a+self.b+b.b
    def __mul__(self,c):
        return self.a*c.a*self.b*c.b
    def __gt__(self,d):
        if(self.a>d.a):
            return True
        else:
            return False

a=ComplexOverload(4,6)
b=ComplexOverload(6,10)
print("Complex",a+b)
print(a*b)