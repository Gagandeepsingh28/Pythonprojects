from flask import Flask, request,jsonify
from flask_mysqldb import MySQL


app = Flask(__name__)
app.config['MYSQL_HOST']="localhost"
app.config['MYSQL_USER']="root"
app.config['MYSQL_PASSWORD']="realmadrid@1902"
app.config['MYSQL_DB']="learn1"
mysql=MySQL(app)

import json
class Object:
    def toJSON(self):
        return json.dumps(self,default=lambda o:o.__dict__,sort_keys=True,indent=4)
cur=None
@app.route("/learn1",methods =["POST"])
def add_user():
    request.get_json(force=True)
    global cur
    username = request.json['username']
    email = request.json['email']
    cur= mysql.connection.cursor()
    query="insert into t1 values (null,%s,%s)"
    data=[username,email]
    cur.execute(query,data)
    cur.connection.commit()
    cur.close()

    me=Object()
    me.name= username
    me.email= email
    return jsonify(me.toJSON())
#end point to show all users
@app.route("/")
def hello():
    return  "hello world"
if __name__ == '__main__':
    app.run(debug=True)
