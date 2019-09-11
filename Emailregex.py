# -*- coding: utf-8 -*-
"""
Created on Wed Apr 10 12:53:49 2019

@author: Manmeet Kaur
"""
import re
ema="gagandeep280898@gmail.com"
Email=re.compile(r'[a-z A-Z 0-9.+]+@[a-z A-Z 0-9.+]+[^\.]')
print(Email.search(ema).group())
