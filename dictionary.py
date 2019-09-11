# -*- coding: utf-8 -*-
"""
Created on Wed Mar 27 12:21:58 2019

@author: Manmeet Kaur
"""
di={}                                          
di["name"]="gagan"
print(di)
d={}
l1=[1,2,3,4]
d["list"]=l1
print(d)
print(di.keys())
print(di.values())
print(di.get("age"))
print(di.get("name"))
di.setdefault("age",20)
print(di)
d2=di.copy()
print(d2)
dic={"name":"gagan","age":20,"club":{"name":"anu","age":8}}
dic.get("club")["name"]
print(dic)
print(di.fromkeys(di))
print(di.items())
print(di.pop("name"))
print(di.pop("class","this key is not available"))
#di.update({"pidleath":"not"})
#print(di)
