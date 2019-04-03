# -*- coding: utf-8 -*-
"""
Created on Wed Mar 27 00:04:35 2019

@author: Manmeet Kaur
"""
n=input()
len=len(n)
k=int(n)
rem=0
arm=0
while k>0:
    rem=int(k%10)
    arm=arm+(rem**len)
    k=int(k/10)
if arm==int(n):
    print("armstrong " +str(n))
else:
    print("not armstrong")



    
