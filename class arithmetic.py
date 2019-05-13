# -*- coding: utf-8 -*-
"""
Created on Wed Apr  3 23:18:03 2019

@author: Manmeet Kaur
"""
class Arith:
    def __init__(self,a,b):
        self.a=a
        self.b=b
    def addition(self):
        c=self.a+self.b
        print("the sum is",(c))
    def subtr(self):
        d=self.a-self.b
        print("the subt is",(d))
    def multi(self):
        m=self.a*self.b
        print("the multi is",(m))
    def division(self):
        p=self.a/self.b
        print("the divi is",(p))
a=Arith(16,4)
a.addition()
a.subtr()
a.multi()
a.division()


