# -*- coding: utf-8 -*-
"""
Created on Wed Apr 10 11:45:12 2019

@author: Manmeet Kaur
"""
import re
#greedy
regexAnything=re.compile(r'<(.*)>')
#print(regexAnything.search("<this is dinner> for you>").group())

#non greedy
reg=re.compile(r'<(.*?)>')
#print(reg.search("<this is dinner> for you>").group())

s="hello this\n how are\t you doing" 
he=re.compile(r'(.*)')
#print(he.search(s).group())
#print(he.findall(s))

Dot=re.compile(r'(.*)',re.DOTALL)
#print(Dot.search(s).group())

st="Agent John gives secret codes to Agent Cathy"
t=re.compile(r'Agent \w+')
#print(t.findall(st))
y=re.compile(r'(Agent) \w*')
#print(y.findall(st))

#print(t.sub("Replace",st))

repl=re.compile(r'Agent (\w)(\w)\w*')
#print(repl.findall(st))
#print(repl.sub(r'Agent \1***',st))
#print(repl.sub(r'Agent \2***',st))
