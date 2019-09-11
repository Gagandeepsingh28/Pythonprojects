# -*- coding: utf-8 -*-
"""
Created on Mon Apr  1 23:35:43 2019

@author: Manmeet Kaur
"""
n =int(input())
flag=0
for i in range(2,n+1):
    k=2
    
    try:
        while k<=i-1:
            
            if i%k==0:
                flag=0
                break
            elif i%k!=0:
                flag=1
            k+=1
        if flag==1:
           print("The prime number is "+str(i))
    except ZeroDivisionError:
        print("The prime number is "+str(i))
        

    