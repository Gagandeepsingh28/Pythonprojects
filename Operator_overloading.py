# -*- coding: utf-8 -*-
"""
Created on Wed Apr 17 12:51:05 2019

@author: Manmeet Kaur
"""
class Vector:
    def __init__(self,num):
        self.num=num
    def add(self,other):
        if not isinstance(other,Vector):
            return NotImplemented
        return  Vector([a+b for a,b in zip(self.num,other.num)])
    
    def __str__(self):
        return ','.join(map(str,self.num))
a=Vector([1,2,3,4])
b=Vector([5,6])

print(a.add(b))

