# -*- coding: utf-8 -*-
"""
Created on Thu Mar 28 12:20:15 2019

@author: Manmeet Kaur
"""
import os
print(os.getcwd())
import sys
file=sys.argv[0]
print(file)
print(os.listdir)
print(os.getcwd())
p=(os.path.abspath("test.txt"))
#print(os.path.isabs("F:\python\test.txt"))
r=os.path.relpath("E:\python\"","test.txt")
#print(os.path.dirname("file"))
#print(os.path.basename("file"))
#print(os.path.exists("exception handling.py"))
#print(os.path.exists("treat"))
#print(os.path.isdir("file"))
#print(os.path.isdir(os.getcwd()))
#print(os.path.isfile("file"))
#print(os.path.getsize(os.getcwd()))
#print(dir(os))
#cwd=os.getcwd()+"\\testing123"
#os.mkdir(cwd)
#print(os.stat(file).st_size)
#print(os.stat(file).st_mtime)
#import datetime
date=os.stat(file).st_mtime
#print(datetime.datetime.fromtimestamp(date)) #modified time and current time stamp
#print(os.walk("E:\movies:")) #walk in the directory 
#for dirpath,dirname,filepath in os.walk("E:\movies"):
    #print(dirpath)
    #print(dirname)
   # print(filepath)
#print(os.environ.get("Path"))
#print(os.path.join(os.getcwd(),"test.txt"))
#print(os.path.exists("F:\python"))
#print(os.path.exists("E:\""))
#file=open(sys.argv[0],'r')
#print(file.name)
#print(file.readline())
#print(file.mode)
#print(file.readline())
#for line in file:
#    print(line,end="")
#file.close()
f=open("E:\python\\test.13456.txt",'w')
f.write("hello") #only string can be passed
f.writelines("\n new line") #list of strings can be passed
l=[1,2,3,4,5]
f.writelines(str(l))
ls="hello world"
f.writelines(ls)
f.close()
fa=open("E:\python\\test.13456.txt",'a')
fa.writelines("this is append file")
fa.close()
#help("sys")

