import mysql.connector
db=mysql.connector.connect(user="root",password="realmadrid@1902",host="localhost")
print(db)

cursor=db.cursor(buffered=True)
#cursor.execute("CREATE DATABASE studen")
cursor.execute("SHOW DATABASES")
for tb in cursor:
    print(tb)
cursor.execute("use studen")
#cursor.execute("CREATE TABLE stdata (name varchar(20) , age varchar(10) , id varchar(10) , marks varchar(10))")
#cursor.execute("CREATE TABLE employee (name varchar(20) , age varchar(10) , id varchar(10) , salary varchar(20))")
#cursor.execute("CREATE TABLE local (name varchar(20) , housenum varchar(10) , locality varchar(20))")
#cursor.execute("SHOW TABLES")

#ins_to="INSERT INTO stdata values (%s,%s,%s,%s)"
#info_of=[("gagan",21,1,89),
      #("rohan",23,2,94),
      #("vansh",22,4,91),
      #("sohan",26,3,81)]
#cursor.executemany(ins_to,info_of)

#db.commit()

#cursor.execute("select * from stdata")
#real=cursor.fetchall()

#for line in real:
    #print(line)

inp="INSERT INTO employee values (%s,%s,%s,%s)"
val=[("sachin",35,5688,25000),
     ("saurabh",47,2976,35000),
     ("austin",58,8722,65000)]
cursor.executemany(inp,val)
db.commit()

ins="INSERT INTO local values (%s,%s,%s)"
vl=[("gagan",45,"Delhi"),
    ("anon",74,"gurugram"),
    ("honey",3,"mumbai")]
cursor.executemany(ins,vl)
db.commit()

cursor.execute("select age from stdata order by age")
for x in cursor:
    print(x)
cursor.execute("select count(name),name from stdata group by name")
for i in cursor:
    print(i)
