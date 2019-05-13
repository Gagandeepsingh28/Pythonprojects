from flask import Flask, request, jsonify
from flask import MySQL


app = Flask(__name__)
app.config['MYSQL_HOST']="localhost"
app.config['MYSQL_USER']="root"
app.config["MYSQL_PASSWORD"]="realmadrid@1902"
app.config["MYSQL_DB"]="user"
mysql=MySQL(app)

cur=mysql.connection.cursor()
query="insert into user_de values (null,%s,%s)"
data=[username,email]
cur.execute(query,data)
cur.connection.commit()
cur.close()
