# -*- coding: utf-8 -*-
"""
Created on Tue Apr  2 11:54:23 2019

@author: Manmeet Kaur
"""
class Pract:
    "this is python"
    d={"name":"age"}
p=Pract()  # instance is created to get all the methods of class and creates default constructor
print(p.__doc__)
print(Pract.__dict__)
print(p.__module__)
print(__name__)
class P:
    def dis(self): #self  
        print("inside dis")
pc=P()
pc.dis()
class C:
    pass
c=C()
c.x=12
