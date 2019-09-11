# -*- coding: utf-8 -*-
"""
Created on Mon Apr 15 23:07:42 2019

@author: Manmeet Kaur
"""


import threading
import time

class MyThread(threading.Thread):
    def __init__(self, number,style,*args,**kwargs):
       super(MyThread,self).__init__(*args,**kwargs) # can retain all methods and attributes from origianl Thread class init method
       self.number=number
       self.style=style
    def run(self,*args,**kwargs):
       print("Thread starting")
       super(MyThread,self).run(*args,**kwargs)
       print("Thread has finished")
def sleeper(num,style):
    print("we are sleeping for {} seconds as {}".format(num,style))
    time.sleep(num)


t=MyThread(number=3,style='yello',target=sleeper,args=(3,'yellow'))
t.start()