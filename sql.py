# -*- coding: utf-8 -*-
"""
Created on Fri Apr 19 11:24:45 2019

@author: Manmeet Kaur
"""

import mysql.connector
mydb=mysql.connector.connect(user="root",password="realmadrid@1902",host="localhost")
print(mydb)
cursor=mydb.cursor()
#cursor.execute("CREATE DATABASE learn1")
cursor.execute("SHOW DATABASES")
for db in cursor:
    print(db)
cursor.execute("use learn1")
#cursor.execute("CREATE TABLE mystudents (name varchar(20), age varchar(20), address varchar(20))")
cursor.execute("show tables")

for tb in cursor:
    print(tb)
insert_query="INSERT INTO mystudents values(%s,%s,%s)"
students_info=("Vansh",35,"Delhi")
cursor.execute(insert_query,students_info)
#to add multiple values
students_info=[("Abhi",24,"Gurgaon"),
               ("Kamal",23,"Delhi"),
               ("data",68,"Kolkata")]

cursor.executemany(insert_query,students_info)

#to save database

mydb.commit()

cursor.execute("select * from mystudents")
real=cursor.fetchall()

for line in real:
    print(line)

