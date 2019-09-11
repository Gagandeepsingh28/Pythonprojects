# -*- coding: utf-8 -*-
"""
Created on Wed Apr 17 11:18:54 2019

@author: Manmeet Kaur
"""
#1.
class Createtupple:
    def create(self,a,b,c,d,e):
        t=(a,b,c,d,e)
        return t
t1=Createtupple().create(5,6,4,8,7)
print(t1)
#3.
class Pri(Createtupple):
    def pri(self):
        p=t1.index(8)
        print(p)
l=Pri()
l.pri()

class Sli(Createtupple):
    def sli(self):
        s=t1[0:3]
        print(s)
r=Sli()
r.sli()
#5.
class Add:
    def add(self):
        a=[t1]
        a.append(2)
        l1=tuple(a)
        print(l1)
k=Add()
k.add()





