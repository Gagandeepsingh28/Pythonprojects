# -*- coding: utf-8 -*-
"""
Created on Thu Apr 11 13:08:58 2019

@author: Manmeet Kaur
"""
import threading
import time
def sleeper (n,name):
    print("hi i am %s, gonna sleep for 5 seconds \n"%(name))
    time.sleep(n)
    print("is woke up after %s seconds sleep \n" %(n))
t=threading.Thread(target=sleeper, name="thread1",args=(5,"thread1"))
l=[]
start=time.time()
for n in range(5):
    t=threading.Thread(target=sleeper, name="Thread"+str(n),args=(5,"Thread"+str(n)))
    l.append(t)
    t.start()
    #print("%s start and ends here"%(t.name()))

for m in l:
    print("%s has started"%(m.name))
    m.join()
    
end=time.time()
print("Thread executes within "+str(end-start))
t.join()