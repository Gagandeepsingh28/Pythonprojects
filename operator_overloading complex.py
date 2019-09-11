# -*- coding: utf-8 -*-
"""
Created on Tue Apr 16 17:31:25 2019

@author: My Pc
"""
#l=[1,2,3]
#l1=["Hello","Hi","Bye"]
#result=zip()
#print(list(result))
#result=zip(l,l1)
#print(list(result))
class Vector:
    def __init__(self,num):
        self.num=num
    def add(self,other):
        if not isinstance(other,Vector):
            return NotImplemented
        return Vector([a+b for a,b in zip(self.num,other.num)])
            
    def __str__(self):
        return ','.join(map(str,self.num))
a=Vector([1,2,3])
b=Vector([9,10,11])

print(a.add(b))


class Vector:
    def __init__(self,num):
        self.num=num
    def __add__(self,other):
        if not isinstance(other,Vector):
            return NotImplemented
        return Vector([a+b for a,b in zip(self.num,other.num)])
    def __mul__(self,other):
        if not isinstance(other,Vector):
            return NotImplemented
        return Vector([a*b for a,b in zip(self.num,other.num)])
            
    def __str__(self):
        return ','.join(map(str,self.num))
a=Vector([1,2,3])
b=Vector([9,10,11])

print(a+b)
print(a*b)

class MulVector:
     def __init__(self,num):
        self.num=num
     def __mul__(self,other):
        if not isinstance(other,int) and not  isinstance(other,float):
            return NotImplemented
        return MulVector([a * other for a in self.num])
            
     def __str__(self):
        return ','.join(map(str,self.num))
a=MulVector([1,2,3])
print(a * 2) 