# -*- coding: utf-8 -*-
"""
Created on Wed Apr  3 12:44:37 2019

@author: Manmeet Kaur
"""
class Nonstatic():
    @staticmethod  # self keyword is not required. 
    def sum():
        print("without self")
Nonstatic.sum()

