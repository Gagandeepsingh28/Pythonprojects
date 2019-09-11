# -*- coding: utf-8 -*-
"""
Created on Sun Apr  7 22:34:49 2019

@author: Manmeet Kaur
"""

class Overload:
    def sum(self,datatype,*args):
        if datatype == 'int':
            answer=0
        elif datatype=='str':
            answer=''
        for x in args:
            answer=answer+x
        return answer
    
over=Overload()
print(over.sum('int',2,3,6,9))
print(over.sum('str',"Hi","This","is"))
