# -*- coding: utf-8 -*-
"""
Created on Tue Apr  9 23:48:18 2019

@author: Manmeet Kaur
"""
def isPhoneNumber(text):
    if len(text)!=12:
        return False
    for i in range (0,3):
        if not text[i].isdecimal():
            return False
    if text[3]!='-':
        return False
    for i  in range(4,7):
        if not text[i].isdecimal():
            return False
    if text[7]!='-':
        return False
    for i in range(8,12):
        if not text[i].isdecimal():
            return False
    return True
message="Call  me  415-555-2222 tomorrow , or at 415-555-1111"
foundNumber=False
for i in range(len(message)):
    chunk=message[i:i+12]
    if isPhoneNumber(chunk):
        print("Phone number exists",chunk)
        foundNumber=True
if not foundNumber:
        print("Could not find any number")

import re
phoneNumRegex=re.compile(r'\d\d\d-\d\d\d-\d\d\d\d')
mo=phoneNumRegex.search(message)
print(mo.group())
print(phoneNumRegex.findall(message))

phoneNumRegex=re.compile(r'(\d\d\d)-(\d\d\d-\d\d\d\d)')
mo=phoneNumRegex.search(message)
print(mo.group())
print(mo.group(1))
print(mo.group(2))
print(phoneNumRegex.findall(message))

message="Call  me  (415)-555-2222 tomorrow , or at (415)-555-1111"

phoneNumRegex=re.compile(r'(\(\d\d\d\))-(\d\d\d-\d\d\d\d)')
mo=phoneNumRegex.search(message)
print(mo.group())
print(mo.group(1))
print(mo.group(2))
print(phoneNumRegex.findall(message))

sampleText="Batmobile is used for calling pirpose"
pipRegEx=re.compile(r'(man|mo|woma)')
print(pipRegEx.search(sampleText).group())

sample="Adventures of Batwoman"

batRegex=re.compile(r'Bat(wo)?man')
print(batRegex.search(sample).group())

sample="Adventures of Batman"

batRegex=re.compile(r'Bat(wo)*man')
print(batRegex.search(sample).group())

sample="Adventures of Batwowowowoman"

batRegex=re.compile(r'Bat(wo)+man')
print(batRegex.search(sample).group())

HelloText="Hello"
startswithRegex=re.compile(r'^He')
print(startswithRegex.search(HelloText).group())

HelloText="Hello World!"
endswithRegex=re.compile(r'World!$')
print(endswithRegex.search(HelloText).group())
onlyNumRegex=re.compile(r'^(\d+)$')
num="123454897"
print(onlyNumRegex.search(num).group())
SampleAlNum="This is sample string 12345678 with num "
samalnum=re.compile(r'(\d)')
print(samalnum.findall(SampleAlNum))

x = re.search("\s", "The rain in Spain")
print(x.start())

x = re.split("\s", "The rain in Spain")
print(x)



x = re.search(r"\bS\w+","The rain 123 in Spain Singapore")

'''span() used to find out the start and end index of resultant value from regex'''
print("Span= ",x.span())
print(x.group())

print("String =",x.string)

characterEscape="We learn handling of ?+*"

handling=re.compile(r'(\?\+\*)+')
print(handling.findall(characterEscape))

occurenceRegex=re.compile(r'(HA){3,5}?')
print(occurenceRegex.search("HAHAHAHAHAHHAHAHAHA").group())
vowelsRegex=re.compile(r'[aeiou]',re.I)
print(vowelsRegex.findall("This is sample for testing vowels India"))
dotRegex=re.compile(r'.at')
print(dotRegex.findall("The cat is sat om flat mat"))

dotRegex=re.compile(r'.{,2}at')
print(dotRegex.findall("The cat is sat om flat mat"))


IntCharRegex=re.compile(r'(\d\s\w+)')
lyrics='''On the third day of Christmas
my true love sent to me:
3 French Hens
2 Turtle Doves
and a Partridge in a Pear Tree

On the fourth day of Christmas
my true love sent to me:
4 Calling Birds
3 French Hens
2 Turtle Doves
and a Partridge in a Pear Tree

On the fifth day of Christmas
my true love sent to me:
5 Golden Rings
4 Calling Birds
3 French Hens
2 Turtle Doves
and a Partridge in a Pear Tree

On the sixth day of Christmas
my true love sent to me:
6 Geese a Laying
5 Golden Rings
4 Calling Birds
3 French Hens
2 Turtle Doves
and a Partridge in a Pear Tree


 

On the seventh day of Christmas
my true love sent to me:
7 Swans a Swimming
6 Geese a Laying
5 Golden Rings
4 Calling Birds
3 French Hens
2 Turtle Doves
and a Partridge in a Pear Tree

On the eighth day of Christmas
my true love sent to me:
8 Maids a Milking
7 Swans a Swimming
6 Geese a Laying
5 Golden Rings
4 Calling Birds
3 French Hens
2 Turtle Doves
and a Partridge in a Pear Tree

On the ninth day of Christmas
my true love sent to me:
9 Ladies Dancing
8 Maids a Milking
7 Swans a Swimming
6 Geese a Laying
5 Golden Rings
4 Calling Birds
3 French Hens
2 Turtle Doves
and a Partridge in a Pear Tree

On the tenth day of Christmas
my true love sent to me:
10 Lords a Leaping
9 Ladies Dancing
8 Maids a Milking
7 Swans a Swimming
6 Geese a Laying
5 Golden Rings
4 Calling Birds
3 French Hens
2 Turtle Doves
and a Partridge in a Pear Tree'''
print(IntCharRegex.findall(lyrics))


regexAnything=re.compile('r<(.*)>')
print(regexAnything.search("this is dinner> for you>").group())
