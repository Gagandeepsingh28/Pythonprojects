# -*- coding: utf-8 -*-
"""
Created on Tue Apr 16 12:47:41 2019

@author: Manmeet Kaur
"""
import queue
q=queue.Queue()
q.put(5)
print(q.get())
print(q.empty())

for n in range(5):
    print("inserting values",n)
    q.put(n)

while not  q.empty():
    print("popping elements", end=" ")
    print(q.get())