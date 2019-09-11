# -*- coding: utf-8 -*-
"""
Created on Tue Mar 26 11:41:38 2019

@author: Manmeet Kaur
"""
a=[]
print (len(a))
a.append("hello world")
print (a)
a.insert(0,2)
print(a)
a[0]=5
print(a)
b,c=a
print(b)
print(c)
a.append("how")
a.append("are")
a.append("you")
a.append(28)
a.append(14)
print(a)
val=a.index("how")
#print(val)
d=[1,2,3,4]
#e=["hi","how","you"]
#f=d+e
#print(f)
#m=f*2
#print(m)
#s=[14,2,35,4,9]
#s.sort()
#print(s)
#t=["hi","and","tuple"]
#t.sort()
#print(t)
#t.sort(reverse=True)
#print(t)
#s.sort(reverse=True)
#print(s)
#c1=["Bob","Is","And","age","is"]
#c1.sort()
#print(c1)
#c1.sort(key=str.lower)
#print(c1)
l7=list(range(10))
[0,1,2,3,4,5,6,7,8,9]
print(l7)
#l8=list("tuples")
#print(l8)
#l9=[l7,s]
#print(l9)
#l9[0][7]
#print(l9[1][2])
print(a.pop)
for n in l7:
    print(n)
for m in  range(len(d)):
    print(m)
d.extend([5,8,9])
print(d)
r=["how","hi","how","to"]
print(r.count("how"))
r.reverse()
print(r)
r.clear()
print(r)
sli=[1,2,3,4,5,6]
k=sli[:2]
print(k)
