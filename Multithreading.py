# -*- coding: utf-8 -*-
"""
Created on Thu Apr 11 12:28:25 2019

@author: Manmeet Kaur
"""
import threading
import time
def thr(n,name):
    print("i am thread %s, gone for sleep%s\n"%(name,n))
    #print("i am thread{},gone for sleep{}"format(name))
    time.sleep(n)
    print("i woke up after %s seconds" %(n))
def sleep(a,naming):
    print("i am the game %s, going to sleep %s\n"%(naming,a))
    time.sleep(a)
    print("i am waking after %s  seconds "%(a))
def learn(c,namirt):
    print("i am the game %s, going to sleep %s\n"%(namirt,c))
    time.sleep(c)
    print("i am waking after %s  seconds "%(c))
k=threading.Thread(target=learn ,name="for loop",args=(14,"for loop"))
j=threading.Thread(target=sleep ,name="triple",args=(8,"triple"))
t=threading.Thread(target= thr ,name="thread1",args=(5,"thread1"))
t.start()
j.start()
k.start()
t.join()
j.join()
print("hi thread")
print("please wake up")
