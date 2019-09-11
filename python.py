# -*- coding: utf-8 -*-

#Spyder Editor

#This is a temporaname
a="Helloworldhowareyou2"
print(len(a))
print("world" in a)
print("how are" not in a )
print(a.lower())
print(a.upper())
print(a.upper().isupper())
print(a.lower().isupper())
print(a.istitle())
print(a.isalpha())
print(a.isdigit())
print(a.isalnum())
print(a.isspace())
b="   true  "
c=" hello"
print(b.isspace())
print(a.startswith("a"))
print(a.endswith("2"))
strcopy= a.join([b,c])
print(strcopy)
d="tttttttrueppppppp"
print(d.rjust(10,"w"))
print(d.ljust(10,"w"))
e="      hello this is learning     "
print(e.rjust(50,"r"))
print(e.center(50,"t"))
print(d.strip())
print(d.lstrip())
print(d.rstrip())
print(d.strip("t"))
print(d.lstrip("t").rstrip("p"))
print("hello",end="")
print("hey")
print("age "," name "," location",sep="hi")
name="gagan"
age=20
location="delhi"
print("my name is %s and i am %s years old located in %s" %(name,age,location))





















    


