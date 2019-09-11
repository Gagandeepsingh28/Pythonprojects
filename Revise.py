# -*- coding: utf-8 -*-
"""
Created on Tue Apr 16 12:19:21 2019

@author: Manmeet Kaur
"""
class Parent:
    def __init__(self):
        print("inside the class")
o=Parent()
class Child:
    pass
class Ch(Parent,Child):
    def __init__(self):
        print("we are")
c=Ch()

