# -*- coding: utf-8 -*-
"""
Created on Wed Apr  3 12:19:21 2019

@author: Manmeet Kaur
"""
class Cons:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def dispname(self):
        print("my name is"+str(self.name))
    def dispage(self):
        print("my age is"+str(self.age))
c=Cons("gagan",20)
print(c.name)
print(c.age)
c.dispage()
c.dispname()
class Grand():
    def address(self):
        print("inside the class")
class Child(Cons,Grand):
    pass
ch=Child("gagan",21)
ch.dispname()
ch.dispage()
ch.address()
